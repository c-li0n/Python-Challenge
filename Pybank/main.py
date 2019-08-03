#import budget_data.csv
import os
import csv

#declare file path
csvpath = os.path.join("..", "..", "Python Datasets", "Python Homework", "budget_data.csv")

#define lists and item values
Months=[]
Total=[]
Change=[]
ListItem= 0
NextListItem= 1

#open csv file and indicate data beneath header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    #indicate data that goes in each list
    for row in csvreader:
        Months.append(row[0])
        Total.append(int(row[1]))

#Create a loop that locates the values for the "change" variable
for iRow in range(len(Total)-1):
    change_calc= (Total[NextListItem]-Total[ListItem])
    Change.append(float(change_calc))
    NextListItem= NextListItem+1
    ListItem= ListItem+1

#define months variable and total amount variables using previous lists
month_count= len(Months)
amount= sum(Total)

#define the average change and format average change
avg_change= float(sum(Change)/len(Change))
formatted_change= round(avg_change, 2)

#define variables for max and min Change based off of previous list
max_increase= max(Change)
max_decrease= min(Change)

#define index for date of max Change
max_profit_index= Change.index(max(Change))+1
date_max_profit= Months[max_profit_index]

#define index for date of min Change
max_loss_index= Change.index(min(Change))+1
date_max_loss= Months[max_loss_index]

#print results using previously defined variables
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${amount}")
print(f"Average Change: ${formatted_change}")
print(f"Greatest Increase in Profits: {date_max_profit} (${max_increase})")
print(f"Greatest Decrease in Profits: {date_max_loss} (${max_decrease})")

#Create text file for presentation of results
file= open("Financial Analysis", mode= 'w')

file.write("Financial Analysis\n")
file.write("--------------------------\n")
file.write(f"Total Months: {month_count}\n")
file.write(f"Total: ${amount}\n")
file.write(f"Average Change: ${formatted_change}\n")
file.write(f"Greatest Increase in Profits: {date_max_profit} (${max_increase})\n")
file.write(f"Greatest Decrease in Profits: {date_max_loss} (${max_decrease})\n")

file.close()
