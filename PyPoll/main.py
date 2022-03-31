import os
import csv 

election_csv = ("PyPoll\Resources\election_data.csv")
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file) 

    total_votes = 0
    for row in csv_reader:
        total_votes += 1

print("Total Votes:" + str(total_votes))
