#import csv file / read from it
import os
import csv



absolute_path = os.path.dirname(__file__)
budget_data = os.path.join(absolute_path, "Resources", "budget_data.csv")


# list to store data
dates_counter = []
profits_loss_total = []
monthly_profit_change = []




#open file as csv file
with open(budget_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for rows in csvreader:
        #add dates to list
        month = rows[0]
        dates_counter.append(month)
       
        
        #add profit/loss to list

        profits_loss = int(rows[1])
        profits_loss_total.append(profits_loss)

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes

    for x in range(len(profits_loss_total)-1):
       currentmonth = profits_loss_total[x]
       nextmonth = profits_loss_total[x+1]
       monthly_profit_change.append(nextmonth - currentmonth)
    
    #calculate average change 
    average_change = round(sum(monthly_profit_change)/len(monthly_profit_change),2)
    
    #calculate total months in dataset
    total_months = (len(dates_counter))
    
    #calculate the net total over entire period 
    net_total = sum(profits_loss_total)

    #calculate greatest increase/decrease in profits (date and amount)
    max_profit = max(monthly_profit_change)
    
    min_profit = min(monthly_profit_change)

    #index with dates of max/min + 1 to tell it the max/min of the next month since its average
    index_max = monthly_profit_change.index(max_profit)+1
    max_month = dates_counter[index_max]

    index_min = monthly_profit_change.index(min_profit)+1
    min_month =dates_counter[index_min]
    
#print statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_month}(${min_profit})")

#export as a txt file
output_path = os.path.join(absolute_path,"Analysis","financialanalysis.txt")
 #specify where to hold contents
with open(output_path,"w") as file:
    #intialize csv.writer
    csvwriter = csv.writer(file, delimiter=',')
    #first row 
    csvwriter.writerow(["Financial Analysis"])
    #second row
    csvwriter.writerow(["----------------------------"])
    #third row
    csvwriter.writerow([f"Total Months: {total_months}"])
    #fourth row
    csvwriter.writerow([f"Total: ${average_change}"])
    #fifth row
    csvwriter.writerow([f"Greatest Increase in Profits: {max_month} (${max_profit})"])
    #sixth row
    csvwriter.writerow([f"Greatest Decrease in Profits: {min_month}(${min_profit})"])





    
    
    
    



















    
