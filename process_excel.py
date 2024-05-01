import pandas as pd

def readContents(name):
    data = []
    course_codes = []
    df = pd.read_excel(name)
    unique_values = df.drop_duplicates(subset=["COURSE CODE"], keep='first')

    query = f"INSERT INTO Courses (courseId, courseName, courseYear, courseType, courseUnits) VALUES "

    for index, row in unique_values.iterrows():
        if (type(row['COURSE CODE']) == float 
        and type(row['COURSE NAME']) == float
        and type(row['YEAR LEVEL']) == float
        and type(row['COURSE TYPE']) == float
        and type(row['UNITS']) == float):
            continue

        # Append all the values as a single tuple
        data.append((row['COURSE CODE'], row['COURSE NAME'], row['YEAR LEVEL'], row['COURSE TYPE'], int(row['UNITS'])))

    # Construct the query string
    for i, x in enumerate(data):
        query += str(x)
        if i != len(data) - 1:
            query += ", "
            
    return query
