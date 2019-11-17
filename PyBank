#Import os and csv
import os
import csv

#Load data by appending blank lists
bank = os.path.join("py_bank.csv")
months = []
net = []
with open(bank) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        months.append(row[0])
        net.append(row[1])

#Sum all net rows to find total
total= 0
for i in range(0,len(net)):
    total = total+ int(net[i])
    
#Find average difference 
difference= [int(net[i+1])-int(net[i])for i in range (len(net)-1)]
Average_difference = (sum(difference) / (len(net)-1))

#Find maximum and minimum
Min_difference = (min(difference))
Max_difference = (max(difference))

#Print results
print("Finicial Data",
     "----------------------------------------------",sep = "\n")
print ("Months:", len(months))
print ("Net Total", total)
print ("Average Difference", Average_difference)
print ("Greatest Increase in profits",Max_difference)
print("Greatest Decrease in profits", Min_difference)
file = open("Output.txt","w")

#Output txt file
file.writelines(f"Finicial Data\n")
file.writelines(f"----------------------------------------------\n")
file.writelines(f"Months:{ len(months)}\n")
file.writelines(f"Net Total:{ total}\n")
file.writelines(f"Average Difference: {Average_difference}\n")
file.writelines(f"Greatest Increase in profits:{Max_difference}\n")
file.writelines(f"Greatest Decrease in profits: {Min_difference}\n")
file.close()
