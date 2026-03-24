import pandas as pd
import os

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Step 1: Load raw data
input_file = "output/aapl_stock_data.csv"
df = pd.read_csv(input_file)

print("Loaded data:")
print(df.head())

# Step 2: Clean column names
df.columns = [col.replace("_aapl", "") for col in df.columns]

# Step 3: Convert datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Step 4: Sort by time
df = df.sort_values(by='datetime')

# Step 5: Handle missing values
df = df.dropna()

# Step 6: Remove duplicates
df = df.drop_duplicates()

# Step 7: Feature Engineering (VERY IMPORTANT 🔥)

# Price change
df['price_change'] = df['close'] - df['open']

# Percentage change
df['percent_change'] = (df['price_change'] / df['open']) * 100

# Moving average (window = 3)
df['moving_avg_3'] = df['close'].rolling(window=3).mean()

# Step 8: Add simple sentiment (mock)
import random
sentiments = ["positive", "negative", "neutral"]
df['sentiment'] = [random.choice(sentiments) for _ in range(len(df))]

# Step 9: Save processed data
output_file = "output/aapl_processed.csv"
df.to_csv(output_file, index=False)

print("\nProcessed data saved:", output_file)
print("\nFinal preview:")
print(df.head())

print("\nFinal shape:", df.shape)