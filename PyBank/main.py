import os #importing operating system module

import csv #importing the csv module

#csvpath variable created to access the csv file: budget data
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

#opening the csv path as a file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #reading the csv file
    next(csvreader) #skip the headers

    print("Financial Analysis") #header for the summary
    
    print("----------------------------") #printing a line to separate header from statistics 

    row_count = 0 #intializing the date column to be 0
    total_sum = 0 #intializing total sum of the profit loss column to be 0
    
    prior_value = None #initalizing prior value to equal none or null value
    amount_change = 0 #initalizing amount change to be 0

    greatest_increase = 0 #initialize the greatest increase to start at 0
    greatest_decrease = 0 #initialize the greatest decrease to start at 0

    greatest_increase_date = ''
    greatest_decrease_date = ''
   

    for rows in csvreader: #for loop to iterate through each row
        
        row_count = row_count + 1 #formula to find the total number of months 
        total_sum = total_sum + int(rows[1]) #formula to find the total sum of the profit/loss column
        
        current_value = int(rows[1]) #intitalizing the current value to be the first row in the profit/loss
        
        date = rows[0]

        if prior_value is not None: #if statement used to ensure the if the prior value is not null, then complete what is below
            change_in_value = current_value - prior_value #formula to find the change betweent the current value and the prior value
            amount_change = amount_change + change_in_value #amount change formula that will add the change in value between the two values to the amount change

            if change_in_value > greatest_increase:
                greatest_increase = change_in_value
                greatest_increase_date = date
            elif change_in_value < greatest_decrease:
                greatest_decrease = change_in_value
                greatest_decrease_date = date

        prior_value = current_value #updating the prior value to be the current value in the next loop iteration 
    
    average_change = amount_change / (row_count - 1) #need to subtract 1 to exclude the first row
    average_change = round(average_change, 2) #rounding the average to two decimal points to match with requested answer
   
    print('Total Months: ' + str(row_count)) #printing the total months
    print('Total: $' + str(total_sum)) #printing the total value of the profit/loss column
    print('Average Change: $' + str(average_change)) #printing the average of the changes in the profit/loss column
    print('Greatest Increase in Profits: ' + str(greatest_increase_date) +  ' ($' + str(greatest_increase)+ ')') #printing the date of the greatest increase and amount
    print('Greatest Decrease in Profits: ' + str(greatest_decrease_date) +  ' ($' + str(greatest_decrease) +')') #printing the date of the greatest decrease and the amount

file_path = os.path.join("PyBank", "analysis", "output_file.txt")

with open(file_path, 'w') as output_file:
    output_file.write("Financial Analysis"+'\n')
    output_file.write('----------------------------'+'\n')
    output_file.write('Total Months: ' + str(row_count)+'\n')
    output_file.write('Total: $' + str(total_sum)+'\n')
    output_file.write('Average Change: $' + str(average_change) + '\n')
    output_file.write('Greatest Increase in Profits: ' + str(greatest_increase_date) +  ' ($' + str(greatest_increase)+ ')' + '\n')
    output_file.write('Greatest Decrease in Profits: ' + str(greatest_decrease_date) +  ' ($' + str(greatest_decrease) +')'+'\n')                                                                  
