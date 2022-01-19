import os
import csv
import pathlib

csv_path = os.path.join(pathlib.Path(__file__).parent.resolve(),"Resources", "budget_data.csv")

with open(csv_path) as csv_file_interacter:
     csvreader = csv.reader(csv_file_interacter, delimiter=",")
     header = next(csvreader)

#Declaring Variables
     row_month_count = 0
     profit_total = 0
     profit_changes = []
     previous_month = 0
     max_change = ["Jan-2000",0]
     min_change = ["Jan-2000",0]
     
#Iterating CSV & Gathering Profit Information     
     for rowVariable in csvreader:

          row_month_count += 1
          profit_total += int(rowVariable[1])

          if row_month_count != 1:
               profit_changes.append(int(rowVariable[1]) - previous_month)

          previous_month = int(rowVariable[1])

          if int(rowVariable[1]) >= int(max_change[1]):
               max_change = rowVariable

          if int(rowVariable[1]) <= int(min_change[1]):
               min_change = rowVariable

#Printing Results        
print("Financial Analysis")
print("----------------------------")  
print("Total Months: " + str(row_month_count -1))
print("Total: $:" + str(profit_total))
print("Average Change: $" + str(round(sum(profit_changes) / (row_month_count -1),2)))
print("Greatest Increase in Profits: "+ str(max_change[0])+" $" + str(max_change[1]))
print("Greatest Decrease in Profits: " + str(min_change[0])+ " $" + str(min_change[1]))

#Writing Results to Text File
with open("PyBank/Analysis/budget.txt","w") as f:
     f.write("Financial Analysis")
     f.write("----------------------------")  
     f.write("Total Months: " + str(row_month_count -1))
     f.write("Total: $:" + str(profit_total))
     f.write("Average Change: $" + str(round(sum(profit_changes) / (row_month_count -1),2)))
     f.write("Greatest Increase in Profits: "+ str(max_change[0])+" $" + str(max_change[1]))
     f.write("Greatest Decrease in Profits: " + str(min_change[0])+ " $" + str(min_change[1]))