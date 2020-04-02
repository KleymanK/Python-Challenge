import csv 
import os

csv_file = os.path.join("election_data.csv")

Total_Votes = 0
Candidate_Votes = [0, 0, 0, 0]
Candidates_List = ["Khan","Correy","Li","O'Tooley"]


with open (csv_file,'r') as csvwrapper:
    csvreader = csv.reader(csvwrapper, delimiter=',')

Candidate_Choice = int(row[2]) - 1

    for row in csvreader:
        print(row[0],row[1])
        Total_Votes += 1
        for Candidate_Index in range(len(Candidates_List))
            Candidates_Count = str(Candidate_Votes[Candidate_Index])

print("Total_Votes = " + str(Total_Votes))