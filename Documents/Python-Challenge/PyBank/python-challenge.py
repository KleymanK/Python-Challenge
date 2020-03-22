import csv 
import os

csv_file = os.path.join("budget_data.csv")

Total_Month = 0
Total = 0
Monthly_Difference = row[1] - (row[1] - 1))

with open (csv_file,'r') as csvwrapper:
    csvreader = csv.reader(csvwrapper, delimiter=',')

    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        print(row[0],row[1])
        Total_Month += 1
        Total +=int(row[1])

            if Monthly_Difference > Monthly_Difference - 1
            print(Monthly_Difference)
            else Monthly_Difference - 1


print("Total Months = " + str(Total_Month))
print("Total Profit/Loss = $" + str(Total))
print("Average Change "+ str(Average))

 
