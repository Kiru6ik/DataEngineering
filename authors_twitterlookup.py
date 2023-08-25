# Import necessary libraries and modules
from googleapiclient.discovery import build  # Google API client
import csv  # CSV file operations
import time  # For time-related functions
from authors_names_list import authors  # Import a list named 'authors3' from a module 'authors_names_list'

# Initialize the Google Custom Search API with your API key
api_key = 'API_KEY'
resource = build("customsearch", 'v1', developerKey=api_key).cse()

# Create an empty list to store twitter-related results for authors
twitters = []

# Loop through each author's name in the 'authors3' list
for name in authors:
    # Build the search query to look for the author's Twitter profile
    query = f'{name} twitter'
    # print(query)  # This line, if uncommented, will print each search query

    try:
        # Execute the search query using Google Custom Search
        result = resource.list(q=query, cx='738614f36fb84493d').execute()

        # Extract link, title, and description/snippet of the top search result
        link = result['items'][0]['link']
        title = result['items'][0]['title']
        descr = result['items'][0]['snippet']

        # Print these details to the console
        print([link, title, descr])

        # Check if the title contains an '@' symbol (usually indicative of a Twitter handle)
        if title.find('@'):
            twitters.append([link, title, descr])  # Append these details to the 'twitters' list

        # Pause for 1 second to avoid overwhelming the server or getting rate-limited
        time.sleep(1)

    # If any error occurs during the search or data extraction, just skip and continue with the next author
    except:
        pass

# Once all authors have been processed, write the collected Twitter details to a CSV file
with open('twitter_authors1.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(twitters)
