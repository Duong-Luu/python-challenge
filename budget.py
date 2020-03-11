import os
import csv

total_months = 0
total_revenue = 0
total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
change = []
dates = []


with open('budget_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader)
    first_row = next(reader)
    total_months = 1
    total_revenue = int(first_row[1])
    pre_row = int(first_row[1])
    
    for row in reader:
        total_months += 1
        total_revenue += int(row[1])
        
        revenue_change = int(row[1]) - pre_row
        pre_row = int(row[1])

        change.append(revenue_change)

    total_change = sum(change)
    print(total_change)

    average_change = total_change / len(change)
    greatest_increase = max(change)
    greatest_decrease = min(change)


    print("Finanicla Analysis")
    print("--------------------")
    print(f"Total: {total_revenue}")
    print(f"Greatest Decrease: {greatest_decrease}")
    print(f"Greatest Increase: {greatest_increase}")
    print(f"Average Change: {average_change}")
            
