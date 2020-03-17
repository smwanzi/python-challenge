import os
import csv

with open("election_data.csv") as csvfile:
    csvread = csv.reader(csvfile, delimiter = ',')
    head = next(csvread)
# declare variables for; total votes, candidates votes and a list of candidates.
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    for row in csvread:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
  
    # total votes cast
    total_votes = (len(votes))
    print(total_votes)

    # number of for each candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
        
    # percentage of votes each candidate won
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)
    
    # Determine the overal winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

# Print Statements to the terminal and export a text file with the results

    print(f"Election Results") 
    print(f"-----------------------------------") 
    print(f"Total Votes: {total_votes}") 
    print(f"-----------------------------------") 
    print(f"Khan: {khan_percent}% ({khan_votes})") 
    print(f"Correy: {correy_percent}% ({correy_votes})") 
    print(f"Li: {li_percent}% ({li_votes})") 
    print(f"O'Tooley: {otooley_percent}% ({otooley_votes})") 
    print(f"-----------------------------------") 
    print(f"Winner: {winner}") 
    print(f"-----------------------------------")
    
# export the results of the election as a text file

with open("output.txt", "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {total_votes}")
    txt_file.write("\n")
    txt_file.write(f"Khan: {khan_percent}% ({khan_votes})")
    txt_file.write("\n")
    txt_file.write(f"Correy: {correy_percent}% ({correy_votes})")
    txt_file.write("\n")
    txt_file.write(f"Li: {li_percent}% ({li_votes})")
    txt_file.write("\n")
    txt_file.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
    txt_file.write("\n")
    txt_file.write(f"-----------------------------------")
    txt_file.write("\n")
    txt_file.write(f"Winner: {winner}")
    txt_file.write("\n")    
    txt_file.write(f"-----------------------------------")