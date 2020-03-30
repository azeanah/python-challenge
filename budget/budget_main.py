# create script for analyzing financial records. 
# Total number of months included in dataset y 
# net total amount of "p/L" over the entire period y 
# avg of changes in "P/L" over entire period y 
# greatest increase in profits (date & amount) over period
# greatest decrease in losses (date & amount) over period

import os
import csv

azBankcsv = os.path.join('..', 'budget_data.csv')

count = 0
total_PnL = 0
months_count = 0

months = []
PnL = []
PnL_delta = []

with open(azBankcsv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
                                                
        # net total amount of "P/L" over period
            total_PnL = total_PnL + int(row[1])
        
        #store months count 
            months_count = months_count + 1    
            
        # add the PnLs into the list PnL    
            PnL.append(int(row[1]))
            
    # create new for loop to define deltas in PnL
        for i in <len(PnL)>:
            
    # define deltas in PnL        
            
            delta_PnL = PnL[index+1] - PnL[index]
            
            PnL_delta.append(delta_PnL)



total_delta = sum(PnL_delta)                   
# Calculate average delta in PnL
monthly_delta = (total_delta/months_count)
max_PnL = max(PnL_delta)
low_PnL = min(PnL_delta)




print("The number of months in dataset is " + str(months_count))
print("The total amount of P/L for period is " + str(total_PnL))
print("The average change in P/L is " + str(monthly_delta))
print("The maximum increase in P/L is " + str(max_PnL))
print("The greatest decrease in Losses was " + str(low_PnL))




