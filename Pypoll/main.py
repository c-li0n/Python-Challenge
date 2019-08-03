#import election_data.csv
import os
import csv

#declare file path
csvpath = os.path.join("..", "..", "Python Datasets", "Python Homework", "election_data.csv")

#define lists and values
candidates = []
candidate_votes = []
vote_amounts = 0

#open file and skip header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    #define vote amounts and indicate list
    for row in csvreader:
        vote_amounts= (vote_amounts)+1
        candidate= (row[2])
        
        #create an if/else statement for candidates and create index
        if candidate in candidates:
            candidate_index= candidates.index(candidate)
            candidate_votes[candidate_index]= candidate_votes[candidate_index]+1
        else:
            candidates.append(candidate)
            candidate_votes.append(1)

#create a list for percentage of votes for candidates and index
percentages= []
max_votes= candidate_votes[0]
max_index= 0

#create a loop for candidate votes/vote percentage and round percentages
for count in range(len(candidates)):
    vote_percentage= (candidate_votes[count])/vote_amounts*100
    percentages.append(vote_percentage)
    percentages= [round(i,2)for i in percentages]

    #create index for max votes to declare winner
    if candidate_votes[count]>max_votes:
        max_votes= candidate_votes[count]
        max_index= count

#define winner
winner= candidates[max_index]

#Print Results
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {vote_amounts}")
print("--------------------------------")

#Print Candidates and vote percentages/amounts using a for loop and previously stated variables
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({candidate_votes[count]})")

#Print Winner Results    
print("--------------------------------")
print(f"Winner: {winner}")
print("--------------------------------") 
  
#Create text file for presentation of results
file= open("Election Results", mode= 'w')

file.write("Election Results\n")
file.write("--------------------------------\n")
file.write(f"Total Votes: {vote_amounts}\n")
file.write("--------------------------------\n") 
for count in range(len(candidates)):
    file.write(f"{candidates[count]}: {percentages[count]}% ({candidate_votes[count]})\n")
file.write("--------------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("--------------------------------\n")

file.close()

