import os 
import csv 
election_csv = ("Resources\election_data.csv")
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 

    total_votes = 0
    candidates = []
    votes_per_cand = []
    for row in csv_reader:
        total_votes += 1
        candidate = str(row[2])
        #candidates.sort()
        if candidate in candidates:
            i = candidates.index(candidate)
            votes_per_cand[i] += 1 
        else:
            candidates.append(candidate)
            votes_per_cand.append(1)

L0 = "Election Results"
L1 = "-----------------------"       
L2 = ("Total Votes:" + str(total_votes))
print(L2)