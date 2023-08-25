# Importing necessary modules and libraries
from googleapiclient.discovery import build  # Google API client library
import csv  # For CSV file operations
from newspaper import Article, Config  # For scraping and extracting article details
from topics_list import topic_list  # An external file that provides a list of topics
import time  # Not used in the current program, but generally useful for timing functions

# Configuration for the 'newspaper' library
config = Config()
config.memoize_articles = False  # This means articles won't be cached after download

# Your Google API key (should be replaced by your actual key)
api_key = 'API_KEY'
resource = build("customsearch", 'v1', developerKey=api_key).cse()  # Creating a search resource for Google's Custom Search Engine

# Lists to store data we'll collect:
authors_list = []  # For storing articles with authors
broken_links = []  # For storing links that fail to open or parse
no_authors_list = []  # For storing articles with no authors

# Looping through each topic from the topics_list
for i, topic in enumerate(topic_list):
    # Creating a query to search for articles on the current topic
    query = f'article {topic}'
    # Making 3 separate searches (up to 30 results) for the same topic
    result = resource.list(q=query, cx='cx').execute()
    result2 = resource.list(q=query, cx='cx', start=10).execute()
    result3 = resource.list(q=query, cx='cx', start=20).execute()
    
    # Combining the results from the 3 searches
    if result3:
        all_results = result['items'] + result2['items'] + result3['items']
    elif result2:
        all_results = result['items'] + result2['items']
    else:
        all_results = result['items']
    
    # Looping through each search result
    for r in all_results:
        url = r['link']  # Extracting the link from the result
        
        # Attempt to process the article from the link
        try:
            # Extracting article details using the 'newspaper' library
            article = Article(url, config=config)
            article.download()
            article.parse()
            authors = article.authors
            print(authors)  # Printing the authors of the article
            
            # If there are authors, add the topic, URL, and authors to the authors_list
            if authors:
                auth = [topic, url]
                auth.extend(authors)
                authors_list.append(auth)
            # If there are no authors, add the topic and URL to the no_authors_list
            else:
                non_auth = [topic, url]
                no_authors_list.append(non_auth)
        # If an error occurs, consider it a 'broken link' and store it
        except:
            broken_links.append([topic, url])
            print('broken link: ', url)

# Saving our collected data to CSV files
with open('authors_list.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(authors_list)

with open('broken_links.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(broken_links)

with open('no_authors_list.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(no_authors_list)
