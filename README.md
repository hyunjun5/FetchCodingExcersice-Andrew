# FetchCodingExcersice-Hyunjun

The code reads in a transactions.csv file within the current directory. 
It will take one argument which is the points to be spent by the user. Once the csv is read, two data structures are going to be filled as we iterate through the rows, i.e. order and rtrn. rtrn is a dictionary which is going to be tracking the total points paid by payers and order is going to keep track of the list of transactions and will be sorted after processing the csv via a lambda function. 

The code will then loop through the entire list of transactions in ascending order of timestamps, deducting total available point paid by payers and the amount of points remaining to be spent by the user. 

FYI, code written and tested on python version 3.9.11.
For some reason, i was not able to run it with "python3 mycode.py 'amount'" but with "python mycode.py 'amount'" in my environment.
