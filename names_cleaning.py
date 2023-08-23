import csv
from collections import Counter
path=r'/Users/kirillevseev/Downloads/authors_readocracy2.csv'
with open(path, 'r') as file:
    next(file)
    reader = csv.reader(file)
    data = list(reader)
authors_names=[]
for row in data:
    for i, name in enumerate(row):
        if i>1:
            # print(name)
            if name:
                authors_names.append(name)
# print(Counter(authors_names))
res=[*set(authors_names)]
print(res)