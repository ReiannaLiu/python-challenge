# Modules 
import os
import csv

# Set up file path 
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# Create variable to store the total number of months included in the dataset
month_count = 0

# Create variable to store the net total of "profit/losses" over the entire period
net_profit = 0

# Create variable to store the "profit/losses" in the first month 
start_profit_loss = None

# Create variable to store the "profit/losses" in the last month 
end_profit_loss = None

# Create variable to store the greatest increase in profits over the entire period
greatest_increase = 0

# Create variable to store the greatest decrease in profits over the entire period 
greatest_decrease = 0

# Create variable to store previous month's "profit/losses"
prev_profit_loss = 0

# Open the CSV
with open(budget_data) as csvfile:

    # Initiate csv.writer
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row 
    next(csvreader)

    # Loop through to calculate
    for row in csvreader:

        # Update the month count
        month_count = month_count + 1

        # Update the net profit
        net_profit = net_profit + int(row[1])

        # Update the first month's "profit/losses"
        if start_profit_loss is None:
            start_profit_loss = int(row[1])
        
        # Update the last month's "profit/losses" while reading the file / also is the current row's "profit/losses"
        end_profit_loss = int(row[1])

        # Update greatest increase if needed
        if end_profit_loss - prev_profit_loss > greatest_increase:
            greatest_increase = end_profit_loss - prev_profit_loss
            greatest_increase_month = row[0]

        # Update greatest decrease if needed
        if end_profit_loss - prev_profit_loss < greatest_decrease:
            greatest_decrease = end_profit_loss - prev_profit_loss
            greastest_decrease_month = row[0]

        # Update the previous row data
        prev_profit_loss = end_profit_loss

# Create and define the variable to store the average of changes in "profit/losses" over the entire period
average_change = round((end_profit_loss -start_profit_loss)/(month_count-1), 2)

# Specify the file to write to
output_path = os.path.join("PyBank", "Analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write(f"""
Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${net_profit}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greastest_decrease_month} (${greatest_decrease}) 
    """)

# Open the file in read mode
with open(output_path, "r") as txtfile:
    content = txtfile.read()

# Print the content
print(content)