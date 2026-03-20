import pandas as pd
import sys
import os

def prepare_data(filename):
    print(f"Reading data from {filename}...")
    df = pd.read_parquet(filename)
    print("Cleaning data...")
    df = df[(df["trip_distance"] <= 100) & (df["trip_distance"] > 0)].copy()
    df = df[df["fare_amount"] > 0].copy()
    df.drop([
    "VendorID", "store_and_fwd_flag", "payment_type", "trip_type", 
    "extra", "mta_tax", "tolls_amount", "improvement_surcharge",
    "congestion_surcharge", "ehail_fee", "passenger_count", "RatecodeID"
    ], axis=1, inplace=True)
    df = df[(df["trip_distance"] <= 20)].copy()
    df['pickup_hour'] = df['lpep_pickup_datetime'].dt.hour
    df['pickup_day_of_week'] = df['lpep_pickup_datetime'].dt.dayofweek
    df['pickup_month'] = df['lpep_pickup_datetime'].dt.month
    df['trip_duration'] = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']).dt.total_seconds() / 60 

    return df

def save_clean_data(df, clean_filename):
    print("Saving clean data...")
    df.to_parquet(clean_filename, index=False)

def main():
    if len(sys.argv) != 3:
        print("Provide datafile and output filenames")
        sys.exit(1)

    filename = sys.argv[1]
    clean_filename = sys.argv[2]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, f"../data/{filename}")
    clean_filename = os.path.join(script_dir, f"../data/{clean_filename}")

    df = prepare_data(filename)
    save_clean_data(df, clean_filename)

if __name__ == "__main__":
    main()
    