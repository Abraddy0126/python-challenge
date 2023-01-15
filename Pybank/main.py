import os
import csv



# Variables
total_months = 0
total_profit_loss = 0
value = 0
change = 0
dates = []
profits = []

# Read csv file
csvpath = os.path.join('pybank', 'resources', 'budget_data.csv')
with open(csvpath, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")

    # Reading header row and move to first row 
    csv_header = next(csvreader)
    first_row = next(csvreader)

    # month counter
    total_months += 1

    # profit and loss counter
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])

    # Read the rows after the header row and set date
    for row in csvreader:
        dates.append(row[0])

        # record of changes in rows
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        # month counter
        total_months += 1

        # The net total amount of profit
        total_profit_loss = total_profit_loss + int(row[1])

        # Average of the changes 
        avg_change = sum(profits)/len(profits)

  # The max increase in profits
    greatest_increase = max(profits)
    greatest_inc_index = profits.index(greatest_increase)
    greatest__inc_date = dates[greatest_inc_index]

    # The maxdecrease in profits
    greatest_decrease = min(profits)
    greatest__dec_index = profits.index(greatest_decrease)
    greatest__dec_date = dates[greatest__dec_index]

# analysiss output
printoutput = (
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_profit_loss)}\n"
    f"Average Change: ${str(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})\n")
print(printoutput)

# Exporting to text file

output_file = os.path.join('pybank','analysis', 'pyBank_output.txt')


pyBankoutput = open(output_file, "w")

line1 = str(f"Total Months: {str(total_months)}")
line2 = str(f"Total: ${str(total_profit_loss)}")
line3 = str(f"Average Change: ${str(round(avg_change,2))}")
line4 = str(f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})")
line5 = str(f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})")
pyBankoutput.write('{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5 )); 
