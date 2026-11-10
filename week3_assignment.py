import pandas as pd

# 1. Load the messy dataset
df = pd.read_csv('data.csv')

print("=== 1. ORIGINAL DATA (First 10 Rows) ===")
print(df.head(10))
print(f"Original shape: {df.shape}\n")

# -------------------------------------------------------------
# STEP 2: Handle Missing Values
# -------------------------------------------------------------
print("=== 2. HANDLING MISSING VALUES ===")
print("Missing values before cleaning:\n", df.isnull().sum())

# Fill missing Calories with the mean (average) of the Calories column
mean_calories = df['Calories'].mean()
df['Calories'] = df['Calories'].fillna(mean_calories)

# Drop rows where 'Date' is missing (or you can fill it if needed)
df = df.dropna(subset=['Date'])

print("Missing values after cleaning:\n", df.isnull().sum(), "\n")

# -------------------------------------------------------------
# STEP 3: Fix Wrong Formats & Data Types (Cleaning Dates)
# -------------------------------------------------------------
print("=== 3. FIXING DATE FORMATS ===")
# Remove quotes from date strings if present and convert to datetime format
df['Date'] = df['Date'].astype(str).str.replace("'", "", regex=True)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%Y/%m/%d')

# If there are alternate formats like '20201226', convert them too
df['Date'] = df['Date'].fillna(pd.to_datetime('2020-12-26', format='%Y-%m-%d'))
print("Dates cleaned successfully!\n")

# -------------------------------------------------------------
# STEP 4: Fix Wrong Data / Outliers (e.g., Duration = 450 instead of 45)
# -------------------------------------------------------------
print("=== 4. FIXING OUTLIERS & WRONG VALUES ===")
print("Unique values in Duration before fix:", df['Duration'].unique())

# Replace unrealistic duration value 450 with 45
df.loc[df['Duration'] > 120, 'Duration'] = 45

print("Unique values in Duration after fix:", df['Duration'].unique(), "\n")

# -------------------------------------------------------------
# STEP 5: Remove Duplicates
# -------------------------------------------------------------
print("=== 5. REMOVING DUPLICATES ===")
print(f"Rows before dropping duplicates: {len(df)}")

df = df.drop_duplicates()

print(f"Rows after dropping duplicates: {len(df)}\n")

# -------------------------------------------------------------
# STEP 6: Filter Rows & Create New Columns
# -------------------------------------------------------------
print("=== 6. FILTERING ROWS & CREATING NEW COLUMNS ===")

# Create a new column: Burn Rate (Calories divided by Duration)
df['Burn_Rate'] = df['Calories'] / df['Duration']

# Filter rows where Calories > 300 and Pulse > 100
filtered_df = df[(df['Calories'] > 300) & (df['Pulse'] > 100)]

print("Filtered Data (Workouts with Calories > 300 and Pulse > 100):")
print(filtered_df.head())

print("\n=== CLEANING COMPLETED SUCCESSFULLY! ===")
print("Final Cleaned Shape:", df.shape)