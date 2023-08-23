from googleapiclient.discovery import build
import csv, time
from authors_names_list import authors3

api_key='API_KEY'
resource = build("customsearch", 'v1', developerKey=api_key).cse()
twitters=[]
for name in authors3:
    query = f'{name} twitter'
    # print(query)
    try:
        result = resource.list(q=query, cx='738614f36fb84493d').execute()
        link = result['items'][0]['link']
        title = result['items'][0]['title']
        descr = result['items'][0]['snippet']
        print([link, title, descr])
        if title.find('@'):
            twitters.append([link, title, descr])
        time.sleep(1)
    except:
        pass

# print(twitters)
with open('twitter_authors1.csv', 'w', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerows(twitters)