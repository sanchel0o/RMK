import csv
from datetime import datetime


# reading data from csv files / returns list of dictionaries
def read_csv(path: str) -> list:
    with open(path, 'r', newline='') as csvfile:
        return list(csv.DictReader(csvfile))


# sorting first file by Date / returns sorted list of dictionaries
def sorting(file: list) -> list:
    return sorted(file, key=lambda x: datetime.strptime(x['Дата'], '%d/%m/%Y'), reverse=True)


# merge 2 lists of dictionaries by Date / returns list1 merged with list2
def merge(list1, list2: list) -> list:
    for i in list1:
        for j in list2:
            if i.get('Дата') == j.get('Дата'):
                i.update(j)
    return list1
