# helper function to extract a specific column from a csv file

"""
    Extract a specific column's data from a CSV file.
    
    Parameters:
    - csv_path (str): Path to the input CSV file.
    - column_name (str): Name of the column to be extracted.
    
    Returns:
    - list: A list of values from the specified column.
    
    Extracts and returns all values from the specified column in the provided CSV file.
    """
import csv
def Fetch_column_from_csv(filename, column_name):
    ids = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile) # create a reader object by calling the reader function from the csv module
        headers = next(reader) # get the first row of the csv file (the headers)
        col_index = headers.index(column_name) # get the index of the column name by calling the index function on the headers list 
        for row in reader:
            ids.append(row[col_index]) # append the values matching the column name to the ids list
    return ids
