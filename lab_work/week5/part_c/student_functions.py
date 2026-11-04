import pandas as pd


def read_csv(filename):
    """Read the CSV file into a DataFrame. Returns None if it can't be read."""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: '{filename}' is empty.")
    return None


def display_total_records(df):
    print(f"\nTotal number of student records: {len(df)}")


def display_headings(df):
    print("\nColumn headings:")
    for i, col in enumerate(df.columns, start=1):
        print(f"  {i}. {col}")


def display_all_records(df):
    print("\nAll student records:")
    print(df.to_string(index=False))


def display_first_rows(df, n=5):
    print(f"\nFirst {n} records:")
    print(df.head(n).to_string(index=False))


def display_summary(df):
    print("\nSummary of numeric columns:")
    print(df.describe())


def display_average(df, column):
    if column not in df.columns:
        print(f"\nNo column called '{column}' in this dataset.")
        return
    print(f"\nAverage {column}: {df[column].mean():.2f}")


def display_counts(df, column):
    if column not in df.columns:
        print(f"\nNo column called '{column}' in this dataset.")
        return
    print(f"\nNumber of students by {column}:")
    print(df[column].value_counts())
