import random 
import csv
 

def get_itemID():
    
    items_id = []

    with open('item.csv', 'r', newline='') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            formatted_id = row['itemId']
            items_id.append(formatted_id)
    return items_id


def get_storeID():
    
    store_id = []

    with open('store.csv', 'r', newline='') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            formatted_id = row['storeId']
            store_id.append(formatted_id)
    return store_id


def writes_csv() -> None:
    with open('stock.csv', 'w', newline='') as csvfile:
        
        header = ['storeId','itemID','quantity']
        writer = csv.writer(csvfile)
        
        writer.writerow(header)            #writes the header

        items_id = get_itemID()
        store_id = get_storeID()

        for i in range(len(store_id)):
            store = store_id[i]
            for j in range(len(items_id)): 
                quantity = random.randint(1, 100)
                line = [store,items_id[j],quantity]                 #writes the output data
                writer.writerow(line)   

    return


def main():
    
    writes_csv()


if __name__ == '__main__':
    main()
