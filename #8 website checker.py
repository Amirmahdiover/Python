import csv

with open('websites.csv', 'r') as r:
    data_web = csv.reader(r)
    website=[]
    for item in data_web:
        print(item[1])
        website.append(item)
print(website)
# print(data_web)
