import os
import pandas as pd
import yfinance as yf

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Choose stock ticker
ticker = "AAPL"

# Download recent stock data
df = yf.download(ticker, period="5d", interval="1h", auto_adjust=False)

# Reset index so Datetime becomes a normal column
df = df.reset_index()

# Flatten columns if needed
if isinstance(df.columns, pd.MultiIndex):
    df.columns = ['_'.join([str(c) for c in col if c]).strip('_') for col in df.columns]

# Standardize column names
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Save raw dataset
output_file = f"output/{ticker.lower()}_stock_data.csv"
df.to_csv(output_file, index=False)

print(f"Dataset saved successfully: {output_file}")
print("\nPreview:")
print(df.head())
print("\nShape:")
print(df.shape)
print("\nColumns:")
print(df.columns.tolist())