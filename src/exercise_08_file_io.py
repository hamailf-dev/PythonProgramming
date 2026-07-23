# 08 · Working with files — reading a CSV
import csv

print("\n--- Exercise 8: File I/O with CSV ---")

# 8.1 — Read and print the rows
print("8.1 Reading rows with csv.reader:")
with open("data/sample_data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 8.2 — Read as dictionaries
print("\n8.2 Reading with csv.DictReader:")
with open("data/sample_data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is a {row['age']}-year-old {row['role']} from {row['city']}")

# 8.3 — Answer questions about the data
print("\n8.3 Answering questions:")
engineer_count = 0
total_age = 0
person_count = 0

with open("data/sample_data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["role"] == "Engineer":
            engineer_count += 1
        total_age += int(row["age"])  # convert text to int
        person_count += 1

avg_age = total_age / person_count if person_count > 0 else 0
print(f"a) Number of Engineers: {engineer_count}")
print(f"b) Average age: {avg_age:.1f}")

# 8.4 — Stretch with Pandas
print("\n8.4 Stretch with Pandas:")
try:
    import pandas as pd
    df = pd.read_csv("data/sample_data.csv")
    print(df.head())          # first few rows
    print(f"\nAverage age with pandas: {df['age'].mean():.1f}")
except ImportError:
    print("Pandas not installed. Run: pip install pandas")

print("\n--- Exercise 8 Complete ---")