import time

from googleapiclient.discovery import build
import csv
from authors_names_list import authors


api_key='API_KEY'
resource = build("customsearch", 'v1', developerKey=api_key).cse()
with open(r'/Users/kirillevseev/PycharmProjects/readocracy /full_authors_list1.csv', 'r') as file:
    # next(file)
    reader = csv.reader(file)
    data = list(reader)
i=0
for row in data:
    name=row[1]
    query=f'site:https://muckrack.com/ AND {name}'
    print(query)
    try:
        result = resource.list(q=query, cx='cx_key').execute()
        # print(result)
        link = result['items'][0]['link']
        row.insert(3, link)
        # print(row)
        time.sleep(0.5)
    except Exception as e:
        print(e)
        row.insert(3, "")
        # print(row)
    # i+=1
    # if i>2:
    #     break
with open('muckrack_authors1.csv', 'w', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerows(data)