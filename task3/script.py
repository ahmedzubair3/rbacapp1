import pandas as pd

# Read CSV file
df = pd.read_csv('./task3/data.csv')

# Calculate price per square foot
df['price_per_sqft'] = df['price'] / df['sq__ft']

# Calculate average price per sqft
avg_price_per_sqft = df['price_per_sqft'].mean()
print(f"Average price per square foot: {avg_price_per_sqft:.2f}")

# Filter properties where price per sqft is less than average
filtered_df = df[df['price_per_sqft'] < avg_price_per_sqft]

# Drop the helper column if you want
filtered_df = filtered_df.drop(columns=['price_per_sqft'])

# Save to new CSV
filtered_df.to_csv('./data/filtered_sales.csv', index=False)

print("Filtered data saved to ./data/filtered_sales.csv")
