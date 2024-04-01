import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
performance_data = pd.read_csv('Student_Performance_Data.csv')

def checkPerformance(performance_data):
    # Check for missing values in all columns
    missing_values = performance_data[performance_data.isnull().any(axis=1)]

    # Check for values outside the range 0 to 100 in the 'Marks' column
    invalid_marks = performance_data[(performance_data['Marks'] < 0) | (performance_data['Marks'] > 100)]

    # Check for values less than 0 or non-integer values in the 'Effort_Hours' column
    invalid_hours = performance_data[performance_data['Effort_Hours'] < 0]

    # Check for multiple marks per Paper_ID for each Student_ID
    multiple_marks = performance_data[performance_data.duplicated(['Student_ID', 'Paper_ID'], keep=False)]

    # Report exceptions
    if not missing_values.empty:
        print("Missing values found:")
        print(missing_values)
        print()

    if not invalid_marks.empty:
        print("Invalid marks (outside the range 0-100) found:")
        print(invalid_marks)
        print()

    if not invalid_hours.empty:
        print("Invalid effort hours (less than 0 or non-integer) found:")
        print(invalid_hours)
        print()

    if not multiple_marks.empty:
        print("Multiple marks per Paper_ID for a Student_ID found:")
        print(multiple_marks)
        print()

    # Remove entries with issues
    clean_data = performance_data.drop(index=missing_values.index)
    clean_data = clean_data.drop(index=invalid_marks.index)
    clean_data = clean_data.drop(index=invalid_hours.index)
    clean_data = clean_data.drop(index=multiple_marks.index)


    # If no exceptions found, print a success message
    if missing_values.empty and invalid_marks.empty and invalid_hours.empty and multiple_marks.empty:
        print("No exceptions found. Data is clean!")



    return clean_data
