import csv
from collections import Counter
path=r'/Users/kirillevseev/PycharmProjects/readocracy /twitter_authors1.csv'
with open(path, 'r') as file:
    # next(file)
    reader = csv.reader(file)
    data = list(reader)
for row in data:
    title=row[1]
    # print(title)
    name=title[:title.find('(')]
    row[1]=name
    curdle=title[title.find('(')+1:title.find(')')]
    row[2]=curdle
    # print(row)
with open('twitter_authors2.csv', 'w', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerows(data)