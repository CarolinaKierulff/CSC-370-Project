
import csv
import random


def writes_csv() -> None:

    with open('store.csv', 'w', newline='') as csvfile:
        
        header = ['storeId', 'location', 'revenue']
        writer = csv.writer(csvfile)
        
        writer.writerow(header)            #writes the header
        
        addresses = [
        "9546 Jefferson Street, Pitt Meadows, BC V3Y 2X7",
        "9275 Grand Street, L'Assomption, QC J5W 9B1",
        "17 Golf Drive, Monteregie-Est, QC J0J 8E6",
        "9171 Ocean St., Belledune, NB E8G 4K4",
        "5 W. Holly St., Yarmouth, NS B5A 2S6",
        "8260 Vale Ave., Grand-Mere, QC G9T 4P5",
        "8265 W. Gainsway Ave., Manotick, ON K4M 2A7",
        "40 Sage Court, Durham Bridge, NB E6C 8X9",
        "77 Hilltop Rd., Windsor, LB A2B 2B3",
        "196 New St., Sylvan Lake, AB T4S 4T8"  
        ]

        store_ids = ['001','002','003','004','005','006','007','008','009','110']

        revenue = [25000, 35000, 42000, 29000, 38000, 40000, 31000, 27000, 32000, 36000]

        for i in range(10):   
            line = [store_ids[i],addresses[i],revenue[i]] 
            writer.writerow(line)

def main():
    
    writes_csv()

    

if __name__ == '__main__':
    main()                
