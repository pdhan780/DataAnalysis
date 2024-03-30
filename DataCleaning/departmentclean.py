#department relation simply has all errors reported, nothing is actually removed

import pandas as pd

# Load the data
data = pd.read_csv('Department_Information.csv')

# Convert 'DOE' column to string and replace NaN values with empty strings
data['DOE'] = data['DOE'].astype(str)

# Check for duplicates in Department_ID and Department_Name
duplicate_ids = data[data.duplicated('Department_ID', keep=False)]
duplicate_names = data[data.duplicated('Department_Name', keep=False)]

# Check for valid years in DOE
invalid_doe = data[~data['DOE'].str.contains(r'\d{1,2}/\d{1,2}/19\d{2}|20\d{2}')]

# Check for missing values
missing_values = data[data.isnull().any(axis=1)]

# Report exceptions
if not duplicate_ids.empty:
    print("Duplicate Department IDs found:")
    print(duplicate_ids)
    print()

if not duplicate_names.empty:
    print("Duplicate Department Names found:")
    print(duplicate_names)
    print()

if not invalid_doe.empty:
    print("Invalid DOE values (not >= 1900):")
    print(invalid_doe)
    print()

if not missing_values.empty:
    print("Missing values found:")
    print(missing_values)
    print()

# If no exceptions found, print a success message
if duplicate_ids.empty and duplicate_names.empty and invalid_doe.empty and missing_values.empty:
    print("No exceptions found. Data is clean!")
