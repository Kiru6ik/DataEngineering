# Import required libraries/modules
import csv  # For reading/writing CSV files

# Specify the path of the CSV file to read data from
path = r'/Users/kirillevseev/PycharmProjects/readocracy /twitter_authors1.csv'

# Open and read data from the CSV file specified in 'path'
with open(path, 'r') as file:
    reader = csv.reader(file)  # Create a CSV reader object
    data = list(reader)  # Convert the CSV content into a list of rows

# Iterate through each row of the CSV data
for row in data:
    title = row[1]  # Get the title from the second column of the row
    
    # Extract the author's name from the title by taking the substring before the first '(' character
    name = title[:title.find('(')]
    row[1] = name  # Update the name in the row
    
    # Extract the handle (or any content between '(' and ')') from the title
    handle = title[title.find('(') + 1:title.find(')')]
    row[2] = handle  # Update the handle in the row

# Specify the path of the new CSV file to save the modified data
output_path = 'twitter_authors2.csv'

# Open and write the modified data to the new CSV file
with open(output_path, 'w', encoding='utf-8') as file:
    writer = csv.writer(file)  # Create a CSV writer object
    writer.writerows(data)  # Write all rows to the CSV file
