#  find total number of votes cast
# list of candidates who received votes
# percentage of votes each candidate won
# total number of votes each candidate won
# # winner of the election based on popular vote

import os
import csv

azElectioncsv = os.path.join('..', "election_data.csv")


mydict = {}
candidate = []
votes = 0


# open csv file
with open(azElectioncsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:

        # find unique candidates
        if row[2] in mydict:
            mydict[row[2]] += 1
        else:
            mydict[row[2]] = 1



total_votes = sum(mydict.values())
winner = max(mydict, key = mydict.get)


        # parse votes

print("ElectionResults")
print("_______________")
print("Total Votes: ", {total_votes})
print("_______________")
for candidate in mydict:
    vote_share = 100*(mydict[candidate]/total_votes)
    print(f'{candidate}: {vote_share:2.2f}% ({mydict[candidate]})')
print("_______________")
print(f"Winner: {winner}")