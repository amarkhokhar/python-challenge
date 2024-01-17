# python-challenge
This is a repository for my python scripts that will analyze financial data for a budget and also analyze election results.

For both the financial data and the election results, a for loop was used to loop through the csv file that was added read and opened in both of the main.py files. 
As for the financial data, the for loop iterated through each row to count the number of months.
Total profit loss was calculated by looping through the second column and adding all of the figures together.
Average change was executed with the assitance of the Learning Assistants. They provided the logic to use a prior value and a current value to track the difference or amount change. Differences were calculated using and if statement. Additionally, Learning Assistants provided the logic to initialize the greatest increase and decrease profit loss variable to be 0, so when the for loop iterated, the if statement would update the values for each. 

As for the election results, Learning Asssitants gave me the idea to use a dictionary to store the values of the unique names that were stored in a list. With the dictionary initialized, adding the vote count for each candidate was possible. 

AskBCS Learning Assistants also assisted me to create the export txt files and to help me read the csv file. The issue with the file path that needed to be correct was to add the name of the current folders, either PyBank or PyPoll to the file path variable in order to access the csv file or to write the txt file in the correct location. 

StackOverflow was used to figure out how to write a new line '\n' for the output files and to create the to initialize the prior_value variable to None and not null.
