import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error, r2_score
import pickle
import sys
import os

def read_parquet(filename):
   print(f"Reading data from {filename}...")
   return pd.read_parquet(filename)

def make_model(df):
    print("Creating model...")
    X = df[["trip_distance", "pickup_hour", "trip_duration", "pickup_day_of_week"]]
    y = df["total_amount"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)
    model = RandomForestRegressor(n_estimators=100, random_state=11)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = root_mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return model, mse, r2

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

    df = read_parquet(filename)
    model, mse, r2 = make_model(df)
    print(f"RMSE - {mse}\nR2 score - {r2}")

    save_model(model, model_name)

if __name__ == "__main__":
    main()