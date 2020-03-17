# import OS and CSV modules
import os
import csv

# open and read the budget data as a csv file
with open('C:PyBank_Resources_budget_data (1).csv') as csvfile:
    csvfile = csv.reader(csvfile, delimiter = ',')
#preview data contained in budget csv file
    # for row in csvfile:
    #      print(row)
# declare variables to hold month count and profit and loss      
# Count the total number of months in the data set excluding the Header row
# Calculate the net total amount of profit/loss for the period
    csv_header = next(csvfile)

    Months = []
    profit_loss = [] 
    Net_profit_loss = 0  
     
    for row in csvfile:
        Months.append(str(row[0]))
        profit_loss.append(int(row[1])) 
        Total_Months = len(Months)
        
    for i in profit_loss:
        Net_profit_loss = Net_profit_loss + i
    print(Total_Months)
    print(Net_profit_loss)
           
# Declare variables to hold the average of the changes in Profit/Losses
# calculate the average change in profit and loss, note- change starts on
# the second row
    Average_change = []
    previous_month_amount = 0
    
    for i in range(len(profit_loss)):
        if i == 0:
            previous_month_amount = profit_loss[i]            
        else:
            monthly_change = profit_loss[i] - previous_month_amount
            Average_change.append(monthly_change)
            previous_month_amount = profit_loss[i]
     
    Length = len(Average_change)
    Total = sum(Average_change)
    profit_loss_average = round(Total / Length, 2)
    print(profit_loss_average)
    
# Determine the greatest increase in profits by month and amount
# note - Month list has 1 more value than Average_change list.
    profit_increase = max(Average_change)
    j = Average_change.index(profit_increase)
    month_increase = Months[j+1]
    print(month_increase)
    print(profit_increase)
    
# Determine the greatest decrease in profits by month and amount    
    profit_decrease = min(Average_change)
    k = Average_change.index(profit_decrease)
    month_decrease = Months[k+1]
    print(month_decrease)
    print(profit_decrease)
    print("----------------------------")
# print the analysis to the terminal and export a text file with the results
# print Financial Analysis to Terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(Months)}")
    print(f"Total P\L: ${sum(profit_loss)}")
    print(f"Average Change: ${round(sum(Average_change)/len(Average_change),2)}")
    print(f"Greatest Increase: {Months[Average_change.index(max(Average_change))+1]} ({max(Average_change)})")
    print(f"Greatest Decrease: {Months[Average_change.index(min(Average_change))+1]} ({min(Average_change)})")


# write output to txt File
with open("output.txt", "w") as txt_file:
    txt_file.write(f"Total Months: {len(Months)}")
    txt_file.write("\n")
    txt_file.write(f"Total P\L: ${sum(profit_loss)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: ${sum(Average_change)/len(Average_change)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase: {Months[Average_change.index(max(Average_change))+1]} \
        ({max(Average_change)})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease: {Months[Average_change.index(min(Average_change))+1]} \
         ({min(Average_change)})\n")
