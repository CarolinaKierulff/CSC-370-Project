import random 
import csv
import sys
from datetime import datetime, timedelta


def gen_IDnumber(start= 20000, end= 30000):
    available_numbers = list(range(start, end + 1))
    random.shuffle(available_numbers)
    for number in available_numbers:
        yield number

cID = gen_IDnumber()

def gen_transactionID():
    global cID
    try:
        line = next(cID)
        return line
    except StopIteration:
        # if all numbers are exhausted
        return "No more unique customer IDs available."


def gen_date():

    today = datetime.today().date()
    
    start_date = today - timedelta(days=6*30)  # Approximating 30 days per month
    end_date = today
    
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    return random_date 
    

def get_itemID():
    
    items_id = []

    with open('item.csv', 'r', newline='') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            formatted_id = row['itemId']
            items_id.append(formatted_id)
    return items_id


def get_customerID():
    
    customer_id = []

    with open('customer.csv', 'r', newline='') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            formatted_id = row['customerId']
            customer_id.append(formatted_id)
    return customer_id


def writes_csv(arg_amount) -> None:
    with open('purchases.csv', 'w', newline='') as csvfile:
        
        header = ['purchaseId','customersId','itemID','date']
        writer = csv.writer(csvfile)
        
        writer.writerow(header)            #writes the header

        items_id = get_itemID()
        customers_id = get_customerID()

        for i in range(arg_amount):
            quantity =  random.randint(1, 5)
            purchase_id = str(gen_transactionID())
            date = gen_date()
            for j in range(quantity):  
                ran_item = random.randint(0, 179)
                ran_cus = random.randint(0, 999)
                line = [purchase_id,customers_id[ran_cus],items_id[ran_item],date]                 #writes the output data
                writer.writerow(line)   

    return


def main():
    
    try:
        arg_amount = int(sys.argv[1])
        if arg_amount < 1 or arg_amount > 1000:
            print('Amount invalid: Please enter number between 1 and 20000.')
        else:
            writes_csv(arg_amount)

    except ValueError:
        print('Amount invalid: Please enter a whole number between 1 and 20000.')
    


if __name__ == '__main__':
    main()
