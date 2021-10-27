import csv

with open('buritizeiro.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        credor = row[1]
        empenhado = row[2]
        print(credor, empenhado)
