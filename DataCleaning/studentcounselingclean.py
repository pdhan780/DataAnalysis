import pandas as pd

# Load the data
data = pd.read_csv('Student_Counceling_Information.csv')

# Check for missing values in Department_Admission
missing_values_admission = data[data['Department_Admission'].isnull()]

# Report exceptions
if not missing_values_admission.empty:
    print("Missing values in Department_Admission found:")
    print(missing_values_admission)
    print()

if missing_values_admission.empty:
    print("data is clean")