import os
import csv
import pathlib

csv_path = os.path.join(pathlib.Path(__file__).parent.resolve(),"Resources","election_data.csv")

with open(csv_path) as csv_file_interacter:
    csvreader = csv.reader(csv_file_interacter, delimiter=",")
    header = next(csvreader)

#Declaring Variables    
    total_votes = 0
    Khan_votes = 0
    correy_votes = 0
    li_votes = 0
    oTooley_votes = 0

    politicians = {
        "Khan" : Khan_votes,
        "Correy": correy_votes,
        "Li": li_votes,
        "O'Tooley": oTooley_votes
    }

    
#Iterating CSV & Gathering Vote Information
    for rowVariable in csvreader:
        total_votes += 1
        if rowVariable[2] == "Khan":
            Khan_votes += 1
        
        if rowVariable[2] == "Correy":
            correy_votes += 1
            
        if rowVariable[2] == "Li":
            li_votes += 1

        if rowVariable[2] == "O'Tooley":
            oTooley_votes += 1

#Printing Results            
print("Election Results")
print("----------------------------")  
print("Total Votes: " + str(total_votes))
print("----------------------------") 
print("Khan: " + str("{:.3%}".format(Khan_votes / total_votes)) + " (" + str(Khan_votes) + ")")
print("Correy: " + str("{:.3%}".format(correy_votes / total_votes)) + " (" + str(correy_votes) + ")")
print("Li: " + str("{:.3%}".format(li_votes / total_votes)) + " (" + str(li_votes) + ")")
print("O'Tooley: "+ str("{:.3%}".format(oTooley_votes / total_votes)) + " (" + str(oTooley_votes) + ")")
print("----------------------------")  
print("Winner: Khan" )
print("----------------------------") 

#Writing Results to Text File
with open("PyPoll/Analysis/election_results.txt","w") as f:
    f.write("Election Results")
    f.write("----------------------------")  
    f.write("Total Votes: " + str(total_votes))
    f.write("----------------------------") 
    f.write("Khan: " + str("{:.3%}".format(Khan_votes / total_votes)) + " (" + str(Khan_votes) + ")")
    f.write("Correy: " + str("{:.3%}".format(correy_votes / total_votes)) + " (" + str(correy_votes) + ")")
    f.write("Li: " + str("{:.3%}".format(li_votes / total_votes)) + " (" + str(li_votes) + ")")
    f.write("O'Tooley: "+ str("{:.3%}".format(oTooley_votes / total_votes)) + " (" + str(oTooley_votes) + ")")
    f.write("----------------------------")  
    f.write("Winner: Khan" )
    f.write("----------------------------") 