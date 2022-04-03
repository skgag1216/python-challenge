import os 
import csv 
election_csv = ("Resources\election_data.csv")
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 

    total_votes = 0
    candidates = []
    for row in csv_reader:
        total_votes += 1
        #candidate = str(row[2])
        #candidates.append(candidate)
        #candidates.sort()

L0 = "Election Results"
L1 = "-----------------------"       
L2 = ("Total Votes:" + str(total_votes))
print(L2)