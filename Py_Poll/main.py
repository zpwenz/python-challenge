#Import os and csv
import os
import csv
#Import data by creating empty lists and appending them
election = os.path.join("election.csv")
ID = []
County = []
Candidate= []
with open(election) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
 #Find total votes cast       
Total_votes = len(ID)
#Find Uinque Candidates
Candidate_list = set(Candidate)
print(Candidate_list)

#Count number of votes for each candidate
Li = (Candidate.count("Li"))
OTooley = (Candidate.count("O'Tooley"))
Correy = (Candidate.count("Correy"))
Khan = (Candidate.count("Khan"))

#Find vote percentage for each candidate
Li_P = round(Li / Total_votes, 2) * 100
OTooley_P = round(OTooley / Total_votes, 2) * 100
Correy_P = round(Correy / Total_votes, 2) * 100
Khan_P = round(Khan / Total_votes, 2) * 100

#Find the most frequent candidate (the winner)
import statistics 
from statistics import mode
winner = mode(Candidate)

#Print results
print("Election Results",
     "----------------------------------------------",sep = "\n")
print ("Total Votes:", Total_votes)
print ("Li: ", Li_P, "Percent", "(", Li, ")")
print ("O'Tooley: ", OTooley_P, "Percent", "(", OTooley, ")")
print ("Correy: ", Correy_P, "Percent", "(", Correy, ")")
print ("Khan: ", Khan_P, "Percent", "(", Khan, ")")
print ("The winner is", winner)

#Output txt file with results
file = open("Output2.txt","w")
file.writelines("Election Results\n")
file.writelines(f"----------------------------------------------\n")
file.writelines(f"Total Votes: {Total_votes}\n")
file.writelines(f"Li:{Li_P}% ({Li})\n")
file.writelines(f"O'Tooley:{OTooley_P}% ({OTooley})\n")
file.writelines(f"Correy:{Correy_P}% ({Correy})\n")
file.writelines(f"Khan:{Khan_P}% ({Khan})\n")
file.writelines(f"The winner is: {winner}\n")
file.close()
