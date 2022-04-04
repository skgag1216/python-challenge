import os 
import csv 

f = open("final_analysis_pypoll.txt", "w")

election_csv = ("Resources\election_data.csv")
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 

    total_votes = 0
    candidates = [] #create empty lists to append/add candidates names to
    votes_per_cand = [] #create empty list to append/add the tally of votes per each cadidate to
    for row in csv_reader:
        total_votes += 1
        candidate = str(row[2]) #establish row where candidates' names are found, only row we will be working with
        if candidate in candidates:
            i = candidates.index(candidate) #this establishes a number or vote associated with candidate
            votes_per_cand[i] += 1 #adds the vote to the new list (votes_per_cand) and keeps tally of votes per each candidate
        else:
            candidates.append(candidate) #this adds the name to the candidates list the first time a candidate appears in data
            votes_per_cand.append(1) #adds one 'vote' for this candidate to the votes_per_cand list
    f.write("Election Results: " + '\n' + '\n')            
    f.write("Total Votes: " + str(total_votes) + '\n' + '\n')
    percentvote = [] #establish an empty list to start holding values for percent of the vote per candidate
    max_vote = 0
    for count in range(len(candidates)): # or can use range (0, 3)
        totalrows = total_votes
        percofvotecalc = round(votes_per_cand[count]/totalrows*100, 3) #calculation used to find percent of the vote per candidate
        percentvote.append(percofvotecalc) #adds to the empty lits percentvote 
        f.write((f"{candidates[count]}:{percentvote[count]}% ({votes_per_cand[count]})")+'\n') #using an f string to print results since there are diff data types
        if votes_per_cand[count] > max_vote: #max vote starts at 0 (above start of for loop)
            max_vote = votes_per_cand[count] #stores the new value of max vote or highest value
            maxcountindex = count #on the current row as it runs thru saved into new variable associated with where the max value was found
            winner = candidates[maxcountindex]
            LL = "Winner: " + winner
f.write('\n')            
f.write(LL)

