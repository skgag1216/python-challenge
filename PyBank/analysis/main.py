import os
import csv

wrtxtfl = open("pybank_final_analysis.txt", "w")

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

L1 = "Financial Analysis"
L2 = "-----------------------"
L3 = "Total months: " + str(month)
L4 = "Total net of Profits/Losses: " + "$" + str(net_budget)
L5 = "Average change: " +"$" + str(round(average_change, 2))
L6 = "Greatest increase in profits: " + greatest_inc_date + " $" + str(greatest_inc)
L7 = "Greatest decrease in profits: " + greatest_dec_date + " $" + str(greatest_dec)
L8 = '\n'+L1+'\n'+L2+'\n'+L3+'\n'+L4+'\n'+L5+'\n'+L6+'\n'+L7+'\n'

print(L8)
wrtxtfl.write(L8)
