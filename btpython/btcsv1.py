#!/usr/bin/env python3
import csv
with open('data/nhansu.csv', 'w') as f:
 new_file = csv.writer(f)
 new_file.writerow(['An', '25', 'IT Manager', 'HCM'])
 new_file.writerow(['Thành', '30', 'Developer', 'HCM'])

