import csv
import sys
from datetime import datetime 


# transaction object that will be iterated through when paying for the points to spend.
class txn:
    def __init__(self, name, points, time):
        self.name = name
        self.points = points
        self.time = time

def main(argv):
    # amount to be spent
    amount = int(argv)
    with open("transactions.csv", 'r') as file:
        csvread = csv.reader(file)

        # date format for sorting from oldest transactions to the latest transactions.
        date_format = '%Y-%m-%dT%H:%M:%SZ'

        # order list will contain the transactions from the given csv file
        order = []

        # dictionary that contains the total points from each of the payers 
        rtrn = dict()

        # for each transaction in the csv file
        for t in csvread:
            
            current = txn(t[0],int(t[1]),t[2])
            order.append(current)  

            if current.name in rtrn:    
                rtrn[current.name] += current.points
            else:
                rtrn[current.name] = current.points

        #sorting the list of transactions by their timestamps with a lambda function.
        res = sorted(order, key=lambda x: datetime.strptime(x.time, date_format))
        
        while res:
            pay = res.pop(0)

            # if the remaining amount to be spent is still greater,
            # then we will just deduct the points for this particular
            # transaction we are looking at to make sure no payer goes to negative balance.
            if amount > pay.points:
                amount -= pay.points
                rtrn[pay.name] -= pay.points

            else:
                
                rtrn[pay.name] -= amount
                break

    print(rtrn)






if __name__ == "__main__":
    main(sys.argv[1])