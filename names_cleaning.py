# Import required libraries/modules
import csv  # For CSV file operations
from collections import Counter  # To count occurrences of list items

# Specify the path of the CSV file to read data from
path = r'/Users/kirillevseev/Downloads/authors_readocracy2.csv'

# Open and read data from the CSV file specified in 'path'
with open(path, 'r') as file:
    next(file)  # Skip the first row (typically the header row)
    reader = csv.reader(file)
    data = list(reader)

# Initialize an empty list to store authors' names
authors_names = []

# Iterate through each row of the CSV data
for row in data:
    # Iterate through each name in the row, keeping track of its position using enumerate
    for i, name in enumerate(row):
        # Check if the current name is not in the first two columns (index 0 and 1)
        if i > 1:
            # Check if the name is not an empty string
            if name:
                # Append the name to the authors_names list
                authors_names.append(name)

# Print a frequency count of each author's name using the Counter object
print(Counter(authors_names))

# Remove duplicates from the authors_names list using set and convert it back to a list
res = [*set(authors_names)]

# Print the list of unique author names
print(res)
