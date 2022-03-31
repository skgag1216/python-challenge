import os
import csv

bd_csv = ("PyBank\\Resources\\budget_data.csv")
with open(bd_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 
     # print(f"Header: {csv_header}")

    count = 0
    net_budget = 0
    overall_change = []
    greatest_inc = 0
    greatest_dec = 0 
# with open(bd_csv) as count_file:
#     csv_reader = csv.reader(count_file)
    for row in csv_reader:
        if count > 0:
            current_pl = int(row[1])-previous_pl
            overall_change.append(current_pl)
            if current_pl > greatest_inc:
                greatest_inc = current_pl
            if current_pl < greatest_dec:
                greatest_dec = current_pl
        count += 1
        #print(type(row[1])) reading data type 
        net_budget += int(row[1])
        previous_pl = int(row[1])


    months = count #subtract 1 for the header row
    #print(months)
   # print(net_budget)
average_change = sum(overall_change)/len(overall_change)
#print(sum(overall_change)/len(overall_change))


print("Financial Analysis")
print("-----------------------")
print("Total number of months: " + str(months))
print("Total net amount of Profits/Losses: " + str(net_budget))
print("Average change: " + str(round(average_change, 2)))

print(greatest_inc)
print(greatest_dec)