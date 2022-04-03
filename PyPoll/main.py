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

#percent_of_vote = ((votes_per_cand/total_votes)*100)

L0 = "Election Results"
L1 = "-----------------------"       
L2 = ("Total Votes:" + str(total_votes))
L2n = "-----------------------"
L3 = (str(candidates[0]) + ": " + str(votes_per_cand[0]) + " " + str(((votes_per_cand[0])/total_votes)*100))
L4 = (str(candidates[1]) + ": " + str(votes_per_cand[1]) + " " + str(((votes_per_cand[1])/total_votes)*100))
L5 = (str(candidates[2]) + ": " + str(votes_per_cand[2]) + " " + str(((votes_per_cand[2])/total_votes)*100))
lastL = "\n"+L0+"\n"+L1+"\n"+L2+"\n"+L2n+"\n"+L3+"\n"+L4+"\n"+L5+"\n"
print(lastL)