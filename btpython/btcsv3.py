#!/usr/bin/env python3
import csv
with open('data/nhansu.txt', 'r', encoding='UTF-8') as txt_file:
    with open('data/ns.csv', 'r+') as csv_file:
        reader = csv.reader(txt_file, delimiter='\t')
        writer = csv.writer(csv_file)
        for row in reader:
            writer.writerow(row)
        csv_file.seek(0)
        reader = csv.reader(csv_file)
        print(next(reader))
with open('data/nhansu.txt', 'r') as txt_file:
    content = txt_file.readlines()
    for i in range(1,len(content)):
        print(content[i].strip())
        
