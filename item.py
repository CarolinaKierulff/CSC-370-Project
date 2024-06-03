
import csv
import random
import sys


def gen_number(start= 1000, end= 9999):
    available_numbers = list(range(start, end + 1))
    random.shuffle(available_numbers)
    for number in available_numbers:
        yield number


cID = gen_number()

def gen_itemID():
    global cID
    try:
        line = next(cID)
        return line
    except StopIteration:
        # if all numbers are exhausted
        return "No more unique customer IDs available."

def get_item_info(index):

    water_sports_items = [
    ["Kayak", 800], ["Stand-Up Paddleboard", 700], ["Wetsuit", 250], ["Snorkeling Gear", 100], ["Surfboard", 500],
    ["Life Jacket", 80], ["Diving Mask and Fin", 150], ["Waterproof Dry Bag", 50], ["Inflatable Raft", 300], ["Fishing Gear", 200],
    ["Towable Tube", 250], ["Water Ski", 400], ["Wakeboard", 400], ["Kayak Paddle", 100], ["Swim Goggle", 30],
    ["Scuba Tank", 250], ["Underwater Camera", 350], ["Personal Flotation Device", 80], ["Water Shoe", 50], ["Hydration Pack", 60],
    ["Sailing Equipment", 500], ["Jet Ski", 10000], ["Bodyboard", 100], ["Waterproof Watch", 150], ["Paddleboard Leash", 30],
    ["Underwater Scooter", 1000], ["Swim Fin", 50], ["Waterproof Phone Case", 20], ["Beach Tent", 100], ["Inflatable Kayak", 500],
    ["Marine GPS System", 500], ["Spearfishing Gear", 300], ["Sun Protection Clothing", 50], ["Boating Accessory", 100], ["Marine Binocular", 150],
    ["Waterproof Backpack", 80], ["Dock Line and Fender", 50], ["Marine Safety Equipment", 100], ["Fish Finder", 400], ["Waterproof Bluetooth Speaker", 100],
    ["Kiteboarding Equipment", 800], ["Floating Cooler", 50], ["Swim Cap", 10], ["Wet Bag", 30], ["Marine Radio", 150],
    ["Fishing Kayak", 800], ["Boat Cover", 200], ["Boat Maintenance Kit", 50], ["Snorkel Vest", 50], ["Underwater Flashlight", 80],
    ["Kayak Cart", 100], ["Boat Seat and Cushion", 150], ["Tow Rope", 50], ["Waterproof Notebook", 20], ["Oar Lock and Rowing Accessory", 50],
    ["Floating Keychain", 10], ["Dock Cleat", 20], ["Deck Shoe", 80], ["Pontoon Boat Accessory", 200], ["Jet Ski Cover", 100]
    ]

    return water_sports_items[index]

    
def writes_csv(arg_amount) -> None:
    with open('item.csv', 'w', newline='') as csvfile:
        
        header = ['itemId', 'name', 'price']
        writer = csv.writer(csvfile)
        
        writer.writerow(header)            #writes the header
        
        colors = ['Blue','Green','Yellow','Purple','Orange','Pink','Brown',
                  'Black','White','Gray','Cyan','Magenta','Lime','Teal']

        for i in range(arg_amount):
            ran_color = random.randint(0, 11)
            for j in range(3):    
                item_id = str(gen_itemID()) 
                name = get_item_info(i)
                price = get_item_info(i)
                line = [item_id,name[0] + ' ' + colors[ran_color],price[1]] 
                ran_color = ran_color + 1
                writer.writerow(line)
    return


def main():   
    try:
        arg_amount = int(sys.argv[1])
        if arg_amount < 1 or arg_amount > 180:
            print('Amount invalid: Please enter number between 1 and 20000.')
        else:
            writes_csv(arg_amount)

    except ValueError:
        print('Amount invalid: Please enter a whole number between 1 and 20000.')


if __name__ == '__main__':
    main()
