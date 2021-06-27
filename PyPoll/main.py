import os
import csv


# Define Variables
total_vote_counter = 0
candidate_names_dict= {}

# path to csv
csvpath = os.path.join("/", "Users", "tovadonahue", "Documents", "python-challenge", "PyPoll", "Resources", "election_data.csv")

# Open csv
with open(csvpath) as csvfile:

    py_poll = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in py_poll:
        
        total_vote_counter += 1

        # Read candidate names from csv
        candidate_name_original_key = (row[2])

        # Add names to dictionary while counting how many times
        if candidate_name_original_key in candidate_names_dict:
            candidate_names_dict[candidate_name_original_key]+=1
           
        else:
            candidate_names_dict[candidate_name_original_key] = 1

#calculate percentage
    for candidate_name_original_key, value in candidate_names_dict.items() :
        win_percent = (value / total_vote_counter) * 100
        #print (win_percent)
        #print (candidate_name_original_key, win_percent, value)

#print
print("Election Results")
print("----------------------------")
print(f"Total Votes:  {total_vote_counter}")
print("----------------------------")
print(candidate_name_original_key, win_percent, value))

