
import csv
import random
import sys

# global varible

count = 999

def gen_itemID():
    global count
    count += 1
    return count

def get_item_info(index):

    water_sports_items = [
    ["Kayak", 800, 719.82], ["Stand-Up Paddleboard", 700, 624.29], ["Wetsuit", 250, 224.09], ["Snorkeling Gear", 100, 93.77], 
    ["Surfboard", 500, 448.97], ["Life Jacket", 80, 71.94], ["Diving Mask and Fin", 150, 136.5], ["Waterproof Dry Bag", 50, 46.25], 
    ["Inflatable Raft", 300, 278.95], ["Fishing Gear", 200, 186.65], ["Towable Tube", 250, 230.98], ["Water Ski", 400, 366.8], 
    ["Wakeboard", 400, 342.65], ["Kayak Paddle", 100, 91.89], ["Swim Goggle", 30, 28.04], ["Scuba Tank", 250, 222.69], 
    ["Underwater Camera", 350, 300.57], ["Personal Flotation Device", 80, 74.28], ["Water Shoe", 50, 43.77], ["Hydration Pack", 60, 52.95], 
    ["Sailing Equipment", 500, 465.24], ["Jet Ski", 10000, 8692.0], ["Bodyboard", 100, 91.96], ["Waterproof Watch", 150, 132.79], 
    ["Paddleboard Leash", 30, 28.29], ["Underwater Scooter", 1000, 945.16], ["Swim Fin", 50, 44.38], ["Waterproof Phone Case", 20, 18.85], 
    ["Beach Tent", 100, 89.87], ["Inflatable Kayak", 500, 429.87], ["Marine GPS System", 500, 454.0], ["Spearfishing Gear", 300, 272.46], 
    ["Sun Protection Clothing", 50, 44.16], ["Boating Accessory", 100, 91.02], ["Marine Binocular", 150, 132.24], ["Waterproof Backpack", 80, 69.44], 
    ["Dock Line and Fender", 50, 45.2], ["Marine Safety Equipment", 100, 90.13], ["Fish Finder", 400, 360.4], ["Waterproof Bluetooth Speaker", 100, 94.36], 
    ["Kiteboarding Equipment", 800, 696.75], ["Floating Cooler", 50, 44.31], ["Swim Cap", 10, 9.48], ["Wet Bag", 30, 28.24], ["Marine Radio", 150, 134.0], 
    ["Fishing Kayak", 800, 707.2], ["Boat Cover", 200, 170.91], ["Boat Maintenance Kit", 50, 45.15], ["Snorkel Vest", 50, 46.2], 
    ["Underwater Flashlight", 80, 75.42], ["Kayak Cart", 100, 92.1], ["Boat Seat and Cushion", 150, 141.86], ["Tow Rope", 50, 43.36], 
    ["Waterproof Notebook", 20, 17.73], ["Oar Lock and Rowing Accessory", 50, 43.43], ["Floating Keychain", 10, 8.85], ["Dock Cleat", 20, 17.14], 
    ["Deck Shoe", 80, 70.89], ["Pontoon Boat Accessory", 200, 179.61], ["Jet Ski Cover", 100, 88.35]
    ]

    return water_sports_items[index]
    
    
def writes_csv(arg_amount) -> None:
    with open('item.csv', 'w', newline='') as csvfile:
        
        header = ['itemId', 'name', 'price', 'cost']
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
                cost = get_item_info(i)
                line = [item_id,name[0] + ' ' + colors[ran_color],price[1],cost[2]] 
                ran_color = ran_color + 1
                writer.writerow(line)
    return


def main():   
    try:
        arg_amount = int(sys.argv[1])
        if arg_amount < 1 or arg_amount > 180:
            print('Amount invalid: Please enter number between 1 and 180.')
        else:
            writes_csv(arg_amount)

    except ValueError:
        print('Amount invalid: Please enter a whole number between 1 and 20000.')


if __name__ == '__main__':
    main()
