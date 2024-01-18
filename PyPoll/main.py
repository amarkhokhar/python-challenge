import os #importing the os module

import csv #importing csv module

#creating a path to the Resources folder and election data csv file
csvpath = os.path.join('Resources','election_data.csv')

#intializing a variable to count the number of rows, which will be the total votes
row_count = 0

#creating a list that will hold the unique name of each candidate    
unique_candidate_name = []

#creating a dictionary that will store the # of votes for each candidate
candidate_vote = {}

#opening the csv file election_data as csvfile
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter =',') #reading the csv file
    next(csvreader) #skipping the header row

#creating a for loop to loop through all the rows of the csv file
    for rows in csvreader:
        row_count = row_count + 1 #counting the total votes by iterating through the rows and adding to row_count
        candidate_name = rows[2] #initializng a candidate name variable to be a list that will store the candidate column
       
     #using an if statement to fill the unique candidate name list
        if candidate_name not in unique_candidate_name: 
            unique_candidate_name.append(candidate_name) #if the name is not in the unique candidate list, add it there
            candidate_vote[candidate_name] = 0 #intialize the vote count for each candidate to be 0

        candidate_vote[candidate_name] += 1 #everytime the candidate name is iterated in the for loop, add 1 to the candidate's vote count
    
#printing the results for the total vote count
print('Election Results')
print('')
print('--------------------------------------------------------')
print('')
print('Total Votes: ' + str(row_count))
print('')
print('--------------------------------------------------------') 
print('')
#intitalizing the winning candidate to be a string
winning_candidate = ''   

#intitalizing the winning count for the winning candidate to be 0 
winning_count = 0

#creating a file path to write a txt file with analysis
filepath = os.path.join('analysis','output_file.txt')

#opening the path to write the output information
with open(filepath, 'w') as output_file:
     
     #writing the txt file information: election results and total votes
     output_file.write('Election Results'+'\n')
     output_file.write('--------------------------------------------------------'+'\n')
     output_file.write('Total Votes: ' + str(row_count)+'\n')
     output_file.write('--------------------------------------------------------'+'\n')


     #creating a for loop to access the unqiue names and add votes counts to each name
     for name in unique_candidate_name:
        votes = candidate_vote[name] #initializing votes variable to be the candidate dictionary storing name
        votes_percentage = (votes/ row_count)*100 #formula to find the vote percentage
        print(f'{name}: {votes_percentage:.3f}% ({votes})') #printing and formatting the vote percentage and printing the number of votes for the candidate
        output_file.write(f'{name}: {votes_percentage:.3f}% ({votes})\n')
       #if statement to find the winning vote count
        if votes > winning_count: 
            winning_count = votes #if votes greater than winning count, then winning count becomes votes
            winning_candidate = name #and winning candidate equals the name of winning candidate
     
     #writing the the winner to the txt file
     output_file.write('--------------------------------------------------------'+'\n')
     output_file.write(f'Winner: {winning_candidate}\n')
     output_file.write('--------------------------------------------------------'+'\n')

#printing the the winning candidate to the terminal
print('')
print('--------------------------------------------------------') 
print ('')
print(f'Winner: {winning_candidate}')
print('')
print('--------------------------------------------------------')
