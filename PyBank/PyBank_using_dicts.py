# This code should be used for the PyBank homework for the Rice Bootcamp, May 2020.
# Requires a set of financial data called budget_data.csv in the Resources sub folder.
# The dataset should compose of two columns, Date and Profit/Losses.
# Uses dictionaries.

#1 Import modules
#2 Create Lists to hold the data.
#3 Find the file path.
#4 Upload and read the CSV file
#5 Populate the lists by looping through all the data.
#6 Tidy up the list of changes by removing the first value.
#7 Print the analysis to terminal.
#8 Save the analysis to a text file.

#1 Import modules
import os
import csv

#2 Create dictionary to hold the data
Date_List = []
PL_List = []
Change_List = []
PL_Dict = {"Date": Date_List, "P&L": PL_List, "Change": Change_List}
Previous = int(0)

#3 find file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#4 Upload and read the CSV file
with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip the header
    csv_header = next(csvreader)
#5 Populate the lists by looping through all the data.
    for row in csvreader:
        Date_List.append(row[0])
        PL_List.append(int(row[1]))
        Change_List.append(int(row[1])-Previous)
        Previous = int(row[1])
#6 Tidy up the list of changes by removing the first value, calculcating average, then adding back.
Change_List.pop(0)
Change_List_Average = sum(Change_List)/len(Change_List)
Change_List.insert(0,0)
i=Change_List.index(max(Change_List))
y=Change_List.index(min(Change_List))

#7 Print the analysis to terminal.
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(PL_List)}")
print(f"Total: ${sum(PL_List)}")
print(f"Average Change: ${round(Change_List_Average ,2)}")
print(f'Greatest Increase in Profits: {PL_Dict["Date"][i]} (${PL_Dict["Change"][i]})')
print(f'Greatest Decrease in Profits: {PL_Dict["Date"][y]} (${PL_Dict["Change"][y]})')

#8 Save the analysis to a text file.
output_path = os.path.join("Analysis", "PyBank_Output_using_dicts.txt")
text_file = open(output_path, 'w')
text_file.write("Financial Analysis\n")
text_file.write("----------------------------\n")
text_file.write(f"Total Months: {len(PL_List)}\n")
text_file.write(f"Total: ${sum(PL_List)}\n")
text_file.write(f"Average Change: ${round(Change_List_Average ,2)}\n")
text_file.write(f'Greatest Increase in Profits: {PL_Dict["Date"][i]} (${PL_Dict["Change"][i]})\n')
text_file.write(f'Greatest Decrease in Profits: {PL_Dict["Date"][y]} (${PL_Dict["Change"][y]})\n')
text_file.close