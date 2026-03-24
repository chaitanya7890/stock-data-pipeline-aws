import os
import pandas as pd

file_path = "output/aapl_processed.csv"

# Step 1: Check file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Processed file not found: {file_path}")

# Step 2: Load file
df = pd.read_csv(file_path)

print("Loaded processed dataset successfully.")
print("Shape:", df.shape)

# Step 3: Required columns
required_columns = [
    "datetime",
    "adj_close",
    "close",
    "high",
    "low",
    "open",
    "volume",
    "price_change",
    "percent_change",
    "moving_avg_3",
    "sentiment"
]

missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing required columns: {missing_cols}")

# Step 4: Check duplicate timestamps
duplicate_count = df["datetime"].duplicated().sum()
if duplicate_count > 0:
    raise ValueError(f"Duplicate datetime values found: {duplicate_count}")

# Step 5: Numeric checks
numeric_columns = [
    "adj_close", "close", "high", "low",
    "open", "volume", "price_change",
    "percent_change"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

if df[numeric_columns].isnull().sum().sum() > 0:
    raise ValueError("Numeric conversion failed for one or more columns.")

# Step 6: Volume check
if (df["volume"] < 0).any():
    raise ValueError("Invalid negative volume detected.")

# Step 7: Sentiment check
valid_sentiments = {"positive", "negative", "neutral"}
invalid_sentiments = set(df["sentiment"].dropna().unique()) - valid_sentiments
if invalid_sentiments:
    raise ValueError(f"Invalid sentiment values found: {invalid_sentiments}")

# Step 8: Moving average nulls check
null_ma = df["moving_avg_3"].isnull().sum()
print(f"moving_avg_3 null count: {null_ma}")

# This is expected for first 2 rows with rolling window=3
if null_ma > 2:
    raise ValueError("Unexpected null values in moving_avg_3.")

print("\nData validation passed successfully.")
print("\nColumn summary:")
print(df.dtypes)