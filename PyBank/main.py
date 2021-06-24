import os
import csv

# Define variables
months = []
profit_loss_changes = []

monthcounter = 0
net = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# path to csv
csvpath = os.path.join("/", "Users", "tovadonahue", "Documents", "python-challenge", "PyBank", "Resources", "budget_data.csv")

# Open csv
with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvfile)
             
    # Read through each row of data after the header
    for row in csv_reader:

        # number of months
        monthcounter += 1

        # Total profit/losses
        current_month_profit_loss = int(row[1])
        net += current_month_profit_loss

        if (monthcounter == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            

        else:

            # calculate change 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Add months
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(monthcounter - 1), 2)

    #highest and lowest 
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    #Locate the index value 
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {monthcounter}")
print(f"Total:  ${net}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Profits:  {worst_month} (${lowest_change})")

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

