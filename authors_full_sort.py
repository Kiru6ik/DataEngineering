# Import the necessary module for CSV file operations
import csv

# Define the path of the CSV file that contains twitter authors' information
path = r'/Users/kirillevseev/PycharmProjects/readocracy /twitter_authors2.csv'
with open(path, 'r') as file:
    # next(file)  # This line is commented out; if active, it would skip the header row of the CSV
    reader = csv.reader(file)
    data = list(reader)  # Read the CSV file and convert it to a list of lists

# Define the path of the second CSV file that contains information about authors' articles
path2 = r'/Users/kirillevseev/Downloads/authors_readocracy2.csv'
with open(path2, 'r') as file:
    # next(file)  # Again, this line is commented out; if active, it would skip the header row of the CSV
    reader = csv.reader(file)
    articles_data = list(reader)  # Read the CSV file and convert it to a list of lists

# This list will store names of authors and their corresponding articles
name_article = []
for row in articles_data:
    for i, name in enumerate(row):
        if i > 1:  # Start from the third element of each row
            # print(name)  # This line is commented out; if active, it would print the name
            if name:  # Check if the name is not empty
                name_article.append([name, row[0]])  # Add the name and the article (from the first column) to the list

# Loop through the twitter authors' data
for row in data:
    name1 = row[1].lower().strip()  # Extract, lowercase and trim whitespace from the name from the twitter data

    # Loop through the list of names and articles
    for line in name_article:
        name2 = line[0].lower().strip()  # Lowercase and trim whitespace for the name from the articles data
        if name2 in name1:  # Check if the name from articles data is a substring of the name from the twitter data
            row.append(line[1])  # If so, append the article to the corresponding row in the twitter data

# Write the modified twitter authors' data to a new CSV file
with open('full_authors_list1.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
