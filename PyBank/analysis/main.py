import os
import csv

bd_csv = ("PyBank\\Resources\\budget_data.csv")
with open(bd_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 
     # print(f"Header: {csv_header}")

count = 0
with open(bd_csv) as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        count += 1
    months = count - 1 #subtract 1 for the header row
   # print(months)




print("Financial Analysis")
print("-----------------------")
print("Total number of months: " + str(months))
