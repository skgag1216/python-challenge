import os
import csv

budget_data_csv = ("Resources\\budget_data.csv")

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 
    print(f"Header: {csv_header}")
    # for row in csv_reader:
    #     line_count = 0
    # if line_count == 0:
    #     print(f'Column names are {(row[0])}')
    #     line_count += 1
    