import csv

path=r'/Users/kirillevseev/PycharmProjects/readocracy /twitter_authors2.csv'
with open(path, 'r') as file:
    # next(file)
    reader = csv.reader(file)
    data = list(reader)
path2=r'/Users/kirillevseev/Downloads/authors_readocracy2.csv'
with open(path2, 'r') as file:
    # next(file)
    reader = csv.reader(file)
    articles_data = list(reader)
name_article=[]
for row in articles_data:
    for i, name in enumerate(row):
        if i>1:
            # print(name)
            if name:
                name_article.append([name, row[0]])
for row in data:
    name1=row[1].lower().strip()
    for line in name_article:
        name2 = line[0].lower().strip()
        if name2 in name1:
            row.append(line[1])
with open('full_authors_list1.csv', 'w', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerows(data)
