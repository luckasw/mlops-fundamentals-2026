import logging
import os
import pickle
import sys
import time

import pandas as pd
import yaml
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

from dvclive import Live

logger = logging.getLogger(__name__)


def read_parquet(filename):
    print(f"Reading data from {filename}...")
    return pd.read_parquet(filename)


def load_params(params_path: str) -> dict:
    """Load parameters from a YAML file."""
    try:
        with open(params_path, "r") as file:
            params = yaml.safe_load(file)
            logger.debug("Parameters retrieved from %s", params_path)
            return params
    except FileNotFoundError:
        logger.error("File not found: %s", params_path)
        raise
    except yaml.YAMLError as e:
        logger.error("YAML error: %s", e)
        raise
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        raise


def make_model(df, params):
    print("Creating model...")

    num_features = params["feature_engineering"]["num_features"]

    selected_features = df.columns[:num_features].tolist()
    X = df[selected_features]
    y = df["total_amount"]

    test_size = params["data_ingestion"]["test_size"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=params["model_building"]["random_state"]
    )

    model = RandomForestRegressor(
        n_estimators=params["model_building"]["n_estimators"],
        random_state=params["model_building"]["random_state"],
        max_features=params["model_building"]["max_features"],
    )
    start1 = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start1
    start2 = time.time()
    y_pred = model.predict(X_test)
    pred_time = time.time() - start2

    mse = root_mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return model, mse, r2, training_time, pred_time


def save_model(model, model_name):
    print(f"Saving model as {model_name}")
    with open(model_name, "wb") as f:
        pickle.dump(model, f)


def main():
    if len(sys.argv) != 3:
        print("Provide datafile name and output model name")
        sys.exit(1)

    filename = sys.argv[1]
    model_name = sys.argv[2]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, f"../data/{filename}")
    model_name = os.path.join(script_dir, f"../models/{model_name}")

    params = load_params(os.path.join(script_dir, "../params.yaml"))

    df = read_parquet(filename)
    model, mse, r2, training_time, pred_time = make_model(df, params)
    print(
        f"RMSE - {mse}\nR2 score - {r2}\nTraining time - {training_time}\nPred time - {pred_time}"
    )

    with Live(save_dvc_exp=True) as live:
        live.log_metric("rmse", mse)
        live.log_metric("r2", r2)
        live.log_metric("training_time", training_time)
        live.log_metric("pred_time", pred_time)
        live.log_params(params)

    save_model(model, model_name)


if __name__ == "__main__":
    main()
