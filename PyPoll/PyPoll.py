# This code should be used for the PyPoll homework for the Rice Bootcamp, May 2020.
# Requires a set of finanical data called election_data.csv in the Resources sub folder.
# The dataset should compose of three columns, Voter ID, County, Candidate
# Tried a method which doesn't require knowing number of candidates (or candidate names) in advance.

#1 Import modules
#2 Create dictionary to hold the data
#3 find file path
#4 Upload and read the CSV file
#5 Populate the dictionary by looping through all the data.
#6 Calculate total votes by summing the dictionary
#7 Find the winner by reversing the dictionary and finding the index of the maximum result
#8 Print results (including loop for all candidates)
#9 Save the analysis to a text file.

#1 Import modules
import os
import csv

#2 Create dictionary to hold the data
Candidate_Dict = {}

#3 find file path
csvpath = os.path.join('Resources', 'election_data.csv')

#4 Upload and read the CSV file
with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header
    csv_header = next(csvreader)
#5 Populate the dictionary by looping through all the data.
    for row in csvreader:
        if row[2] in Candidate_Dict:
            Candidate_Dict[row[2]] += int(1)
        else:
            Candidate_Dict[row[2]] = int(1)
#6 Calculate total votes by summing the dictionary
Total_Votes = sum(Candidate_Dict.values())
#7 Find the winner by reversing the dictionary and finding the index of the maximum result (yes, I googled this)
Winner = (dict((v,k) for k,v in Candidate_Dict.items()).get(max(Candidate_Dict.values())))

#8 Print results (including loop for all candidates)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------")
for key, value in Candidate_Dict.items() :
    print(f'{key}: {round(value/Total_Votes*100,2)}% ({value})')
print("-------------------------")
print(f'Winner: {Winner}')
print("-------------------------")

#9 Save the analysis to a text file.
output_path = os.path.join("Analysis", "PyPoll_Output.txt")
text_file = open(output_path, 'w')
text_file.write("Election Results\n")
text_file.write("-------------------------\n")
text_file.write(f"Total Votes: {Total_Votes}\n")
text_file.write("-------------------------\n")
for key, value in Candidate_Dict.items() :
    text_file.write(f'{key}: {round(value/Total_Votes*100,2)}% ({value})\n')
text_file.write("-------------------------\n")
text_file.write(f'Winner: {Winner}\n')
text_file.write("-------------------------\n")
text_file.close
