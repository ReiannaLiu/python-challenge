# Modules 
import os
import csv

# Set up file path 
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# Create variable to store the total number of votes cast 
total_votes = 0

# Create variable to store the list of candicates and number of votes each one of them won 
candidate_vote = {}

# Open the CSV
with open(election_data) as csvfile:

    # Initiate csv.writer
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row 
    next(csvreader)

    # Loop through the csv file
    for row in csvreader:

        # Update the total votes
        total_votes = total_votes + 1

        # case when the candidates already in the dictionary 
        if row[2] in candidate_vote:
            candidate_vote[row[2]] = candidate_vote[row[2]] + 1
        else:
            candidate_vote[row[2]] = 1

# Specify the file to write to
output_path = os.path.join("PyPoll", "Analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results \n")

    txtfile.write("------------------------- \n")

    txtfile.write(f"Total Votes: {total_votes} \n")

    txtfile.write("------------------------- \n")

    for key in candidate_vote:
        perc_vote = round(candidate_vote[key] / total_votes * 100, 3)
        txtfile.write(f"{key}: {perc_vote}% ({total_votes}) \n")

    txtfile.write("------------------------- \n")

    # Calculate the winner of the election based on popular vote 
    max_candidate = max(zip(candidate_vote.values(), candidate_vote.keys()))[1]
    
    txtfile.write(f"Winner: {max_candidate} \n")

    txtfile.write("------------------------- ")

# Open the file in read mode
with open(output_path, "r") as txtfile:
    content = txtfile.read()

# Print the content
print(content)