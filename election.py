import os
import csv

total_votes = 0

candidates = []
num_votes = []
result = {}
percent_votes = []
with open('election_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader)

    for row in reader:
        total_votes += 1
        
        if row[2] not in candidates:
            candidates.append(row[2])

            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    for votes in num_votes:
        percentage = (votes/total_votes) *100
        percentage = round(percentage)
        percentage = "%.2f%%" % percentage
        percent_votes.append(percentage)

    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

    print('Election Results')
    print('----------------')
    print(f"Total Votes: {total_votes}")
    print('-----------------')
    for i in range(len(candidates)):
        print(f"{candidates[i]} : {percent_votes[i]} {num_votes[i]}")
    print('-----------------')
    print(f"winner: {winning_candidate}")
