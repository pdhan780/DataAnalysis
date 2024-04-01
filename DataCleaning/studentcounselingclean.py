import pandas as pd

def checkStudent(student_data):
    # Check for missing values in Department_Admission
    missing_values_admission = student_data[student_data['Department_Admission'].isnull()]

    # Report exceptions
    if not missing_values_admission.empty:
        print("Missing values in Department_Admission found:")
        print(missing_values_admission)
        print()

    if missing_values_admission.empty:
        print("data is clean")
    
    return student_data