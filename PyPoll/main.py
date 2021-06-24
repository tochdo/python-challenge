import os
import csv

# path to csv
csvpath = os.path.join("/", "Users", "tovadonahue", "Documents", "python-challenge", "PyPoll", "Resources", "election_data.csv")

# Open csv
with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvfile)
             
    # Read through each row of data after the header
    for row in csv_reader:

        
# Specify the file to write to
#output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
