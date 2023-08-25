# Import required libraries/modules
import time  # To pause execution between API calls
from googleapiclient.discovery import build  # To access Google API services
import csv  # For CSV file operations
from authors_names_list import authors  # Import a list named 'authors' from the module 'authors_names_list'

# Initialize the Google Custom Search API with your API key
api_key = 'API_KEY'
resource = build("customsearch", 'v1', developerKey=api_key).cse()

# Open and read data from a CSV file named 'full_authors_list1.csv'
with open(r'/Users/kirillevseev/PycharmProjects/readocracy /full_authors_list1.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Iterate through each row of the CSV data
for row in data:
    # Extract the author's name from the row (assuming it's the second element in each row)
    name = row[1]

    # Build a search query to look for the author's profile on the 'muckrack.com' website
    query = f'site:https://muckrack.com/ AND {name}'
    print(query)  # Print each query (for debugging purposes)

    try:
        # Execute the search query using Google Custom Search
        result = resource.list(q=query, cx='cx_key').execute()

        # Extract the link of the top search result
        link = result['items'][0]['link']

        # Insert the link to the row's fourth position
        row.insert(3, link)

        # Pause for half a second to prevent overwhelming the server or getting rate-limited
        time.sleep(0.5)

    # If any error occurs during the search or data extraction, insert an empty string and print the error
    except Exception as e:
        print(e)
        row.insert(3, "")

# Save the modified data to a new CSV file named 'muckrack_authors1.csv'
with open('muckrack_authors1.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
