

import csv
import random
import sys
from datetime import datetime, timedelta
import time


count = 9999

def gen_customerID():
    global count
    count += 1
    return count


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

def gen_birth_date():

    today = datetime.today()
    min_age_date = today - timedelta(days=18*365)
    max_age_date = today - timedelta(days=75*365)
    
    random_date = min_age_date - timedelta(days=random.randint(0, (min_age_date - max_age_date).days))
    
    return random_date.date()


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


def gen_postal_code():
    postal_code = 'V'
    postal_code += str(random.randint(0, 9))
    postal_code += random.choice([chr(i) for i in range(65, 91) if chr(i) not in 'DFIOQU'])
    postal_code += str(random.randint(0, 9))
    postal_code += random.choice([chr(i) for i in range(65, 91) if chr(i) not in 'DFIOQU'])  
    postal_code += str(random.randint(0, 9))
    
    return postal_code


def gen_address():

    street_names = [
    "Main", "High", "Oak", "Maple", "Cedar", "Elm", "Pine", "Walnut", "Willow", "Birch", "Ash", "Spruce", "Chestnut", "Poplar", "Fir", "Beech", 
    "Sycamore", "Hickory", "Alder", "Aspen", "Redwood", "Sequoia", "Magnolia", "Dogwood", "Cypress", "Hawthorn", "Juniper", "Linden", "Olive", 
    "Palm", "Peach", "Plum", "Apple", "Cherry", "Pear", "Grove", "Park", "Ridge", "Hill", "Valley", "Lake", "River", "Creek", "Brook", "Spring", 
    "Summer", "Autumn", "Winter", "Sunset", "Sunrise", "Meadow", "Field", "Forest", "Woodland", "Glade", "Clearwater", "Lakeside", "Riverside", 
    "Hillside", "Seaside", "Harbor", "Bay", "Beach", "Coast", "Shore", "Bluff", "Cliff", "Canyon", "Valleyview", "Mountainview", "Pinecrest", 
    "Hillcrest", "Oakwood", "Elmwood", "Cedarwood", "Maplewood", "Redwood", "Hickorywood", "Birchwood", "Sprucewood", "Magnoliawood", "Dogwoodwood", 
    "Cypresswood", "Sycamorewood", "Juniperwood", "Lindenwood", "Olivewood", "Palmwood", "Peachwood", "Plumwood", "Applewood", "Cherrywood", 
    "Pearwood", "Grovewood", "Parkwood", "Ridgewood", "Hillwood", "Valleywood", "Lakewood", "Riverwood", "Aspenwood", "Pinewood", "Briarwood", 
    "Brookside", "Chestnutwood", "Cottonwood", "Evergreen", "Fairview", "Greenwood", "Hidden", "Holly", "Laurel", "Lilac", "Locust", "Mountain", 
    "Mulberry", "New", "North", "Oakridge", "Overlook", "Prairie", "Raven", "Shadow", "South", "Timber", "Tranquil", "Victoria", "Water", 
    "Wildwood", "Woodbine", "Woodland", "Yellowstone", "York", "Windermere", "Kingswood", "Fairway", "Forestview", "Woodbridge", "Birchtree", 
    "Misty", "Brookstone", "Foxglove", "Gardenia", "Glenview", "Harborview", "Highland", "Honeysuckle", "Horizon", "Independence", "Jackson", 
    "Jefferson", "Liberty", "Madison", "Morning", "Pioneer", "Prairieview", "Prospect", "Raintree", "Rosewood", "Saddle", "Sage", "Summit", 
    "Sycamoreview", "Trillium", "Tuscany", "Violet", "Whispering", "Williams", "Willowbrook", "Woodlandview", "Amber", "Arcadia", "Arlington", 
    "Azalea", "Barberry", "Bayberry", "Bluebell", "Brentwood", "Briar", "Brookdale", "Canyonview", "Capitol", "Cedarview", "Colonial", 
    "Concord", "Copper", "Crescent", "Daisy", "Edgewood", "Elderberry", "Elmview", "Emerald", "Falcon", "Garden", "Golden", "Grandview", 
    "Hawthorne", "Hazel", "Heritage", "Hiddenview"
    ]
    
    suffix = ["St", "Rd", "Ave", "Blvd", "Dr", "Ln", "Ct", "Pl", "Way", "Pkwy", "Sq"]

    cities_bc = [
    "Vancouver", "Surrey", "Burnaby", "Richmond", "Abbotsford",
    "Coquitlam", "Kelowna", "Langley", "Saanich", "Delta",
    "Kamloops", "Nanaimo", "Victoria", "Chilliwack", "Maple Ridge",
    "New Westminster", "Port Coquitlam", "North Vancouver", "West Vancouver", "Penticton",
    "Port Moody", "Prince George", "Vernon", "Courtenay", "Campbell River",
    "Fort St. John", "Pitt Meadows", "Dawson Creek", "Squamish", "Cranbrook"
    ]

    postal_code = gen_postal_code()

    ran_number = random.randint(299, 9999)
    ran_street = random.randint(1, len(street_names) - 1)
    ran_suffix = random.randint(1, len(suffix) - 1)
    ran_city = random.randint(1, len(cities_bc) - 1)

    address = f"{ran_number} {street_names[ran_street]} {suffix[ran_suffix]} {cities_bc[ran_city]} BC {postal_code}"

    return address 
    

def writes_csv(arg_amount) -> None:
    with open('customer.csv', 'w', newline='') as csvfile:
        
        header = ['customerId','name','birthDate','phoneNumber','email','address']
        writer = csv.writer(csvfile)
        
        writer.writerow(header)            #writes the header
        
        for i in range(arg_amount):
            customer_id = str(gen_customerID())
            full_name = gen_name()
            birth_date = gen_birth_date()
            phone_number = gen_phone()
            email = gen_email(full_name)
            address = gen_address()
            line = [customer_id,full_name,birth_date,phone_number,email,address]                 #writes the output data
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
            print('Amount invalid: Please enter a number between 1 and 20000.')
        else:
            start_time = time.time()  #record start time
            writes_csv(arg_amount)
            end_time = time.time()    #record end time
            execution_time = end_time - start_time
            print(f"Generated {arg_amount} customers in {execution_time:.2f} seconds.")

    except (ValueError, IndexError):
        print('Amount invalid: Please enter a whole number between 1 and 20000.')


if __name__ == '__main__':
    main()
