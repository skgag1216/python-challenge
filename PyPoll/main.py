import os 
import csv 

f = open("final_analysis_pypoll.txt", "w")

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
    percent = []
    votes = []
    max_vote = 0
    for count in range(len(candidates)): 
        name = candidate[count]
        #votes.append(candidates.count[name])
        totalrows = total_votes
        percofvote = round(votes_per_cand[count]/totalrows*100, 3)
        percent.append(percofvote)
        f.write(str(print(f'{candidates[count]}:{percent[count]}% ({votes_per_cand[count]})')))
        if votes_per_cand[count] > max_vote:
            max_vote = votes_per_cand[count]
            maxcountindex = count
            winner = candidates[maxcountindex]
    f.write(str((print("Winner: " + winner))))

