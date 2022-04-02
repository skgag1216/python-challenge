import os
import csv
from numpy import maximum

from sympy import Max 

bd_csv = ("Resources\\budget_data.csv")
with open(bd_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 
     # print(f"Header: {csv_header}")

    month = 0
    net_budget = 0
    overall_change = []
    greatest_inc = 0
    greatest_dec = 0 

    for row in csv_reader:
        if month > 0:
            current_pl = int(row[1])-previous_pl 
            overall_change.append(current_pl)
            if current_pl > greatest_inc:
                greatest_inc = current_pl
                greatest_inc_date = str(row[0]) 
            if current_pl < greatest_dec:
                greatest_dec = current_pl
                greatest_dec_date = str(row[0])
                
        month += 1
        #print(type(row[1])) reading data type 
        net_budget += int(row[1])
        previous_pl = int(row[1])
average_change = sum(overall_change)/len(overall_change)
#print(sum(overall_change)/len(overall_change))

print("Financial Analysis")
print("-----------------------")
print("Total months: " + str(month))
print("Total net of Profits/Losses: " + "$" + str(net_budget))
print("Average change: " +"$" + str(round(average_change, 2)))
print("Greatest increase in profits: " + greatest_inc_date + " $" + str(greatest_inc))
print("Greatest decrease in profits: " + greatest_dec_date + " $" + str(greatest_dec))