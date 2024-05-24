
import csv
import random
import sys

def gen_IDnumber(start= 10000, end= 15000):
    available_numbers = list(range(start, end + 1))
    random.shuffle(available_numbers)
    for number in available_numbers:
        yield number

cID = gen_IDnumber()

def gen_customerID():
    global cID
    try:
        line = next(cID)
        return line
    except StopIteration:
        # if all numbers are exhausted
        return "No more unique customer IDs available."


def get_names(filename):
    names = []

    with open(filename, 'r', newline='') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            formatted_name = row['name'].capitalize()
            names.append(formatted_name)
    return names


def gen_name():
    all_names = get_names('just_names.csv')
    all_surnames = get_names('just_surnames.csv')

    ran_name = random.randint(1, 258001)
    ran_surname = random.randint(1, 151672)

    name = all_names[ran_name] + ' ' + all_surnames[ran_surname]

    return name


def gen_phone():
    area_code = [587, 368, 403, 825, 780, 236, 672, 604, 778, 250, 584, 
                 431, 204, 506, 709, 867, 782, 902, 867, 365, 226, 647, 
                 519, 289, 742, 807, 548, 753, 249, 683, 437, 905, 343, 
                 613, 705, 416, 782, 902, 450, 418, 873, 468, 367, 819, 
                 579, 581, 438, 354, 514, 263, 306, 474, 639, 867]
    
    phone_first = random.randint(200, 999)
    phone_second = random.randint(1000, 9999)
    ran_area = random.randint(0, 53)

    phone = '(' + str(area_code[ran_area]) + ')' + str(phone_first) + '-' + str(phone_second)
    return phone


def gen_email(full_name):
    
    #types of email generated:
    #1. fullname + email domain
    #2. name + half surname + email domain
    #3. name + '.' + half surname + email domain
    #4. surname + number + email domain
    #5. name + number + half surname + email domain
    #email domains: '@gmail.com' or '@hotmail.com' or '@yahoo.com'

    domains = ['@gmail.com','@hotmail.com','@yahoo.com','@yahoo.ca','@aol.com','@msn.com','@outlook.com','@live.com']
    which_dom = random.randint(0, 7)
    type = random.randint(1, 9)
    number1 = str(random.randint(10, 2999))
    number2 = str(random.randint(1950, 2010))
    parts = full_name.split()
    name = str(parts[0]).lower()
    surname = str(parts[-1]).lower()

    midpoint_nam = len(name) // 2
    midpoint_sur = len(surname) // 2
    half_nam = name[:midpoint_nam]
    half_sur = surname[:midpoint_sur]

    if type == 1:
        email = str(name + surname + domains[which_dom])
    elif type == 2:
        email = str(name + half_sur + domains[which_dom])
    elif type == 3:
        email = str(name + '.' + half_sur + domains[which_dom])
    elif type == 4:
        email = str(surname + number2 + domains[which_dom])
    elif type == 5:
        email = str(half_nam + number1 + domains[which_dom])   
    elif type == 6:
        email = str(half_nam + half_sur + domains[which_dom])    
    elif type == 7:
        email = str(half_nam + '.' + half_sur + number2 + domains[which_dom])
    elif type == 8:
        email = str(name + surname + number1 + domains[which_dom])           
    else:
        email = str(name + number1 + half_sur + domains[which_dom])

    return email    


def writes_csv(arg_amount) -> None:
    with open('customer.csv', 'w', newline='') as csvfile:
        
        header = ['customerId', 'name', 'phoneNumber','email']
        writer = csv.writer(csvfile)
        
        writer.writerow(header)            #writes the header
        
        for i in range(arg_amount):
            customer_id = str(gen_customerID())
            full_name = gen_name()
            phone_number = gen_phone()
            email = gen_email(full_name)
            line = [customer_id,full_name,phone_number,email]                 #writes the output data
            writer.writerow(line)

    return


def is_integer(value):
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False


def main():
    """Main entry point of the program."""
    try:
        arg_amount = int(sys.argv[1])
        if arg_amount < 1 or arg_amount > 20000:
            print('Amount invalid: Please enter number between 1 and 20000.')
        else:
            writes_csv(arg_amount)

    except ValueError:
        print('Amount invalid: Please enter a whole number between 1 and 20000.')


if __name__ == '__main__':
    main()
