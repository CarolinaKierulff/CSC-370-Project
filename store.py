
import csv
import random


def writes_csv() -> None:

    with open('store.csv', 'w', newline='') as csvfile:
        
        header = ['storeId','storeName','managerId','location','revenue']
        writer = csv.writer(csvfile)
        
        writer.writerow(header)            #writes the header

        stores_names = [
        "Aquatic Adventures","Wave Rider Pro","Ocean Gear Outlet","Surf and Sail Emporium",
        "Seaside Sports Supply","Aqua Gear Galore","Tidal Thrills",
        "Waves and Wetsuits","Splash Zone Gear","Marine Sports Mart"
        ]
        
        addresses = [
        '9546 Jefferson Street Vancouver BC V3Y2X7', '9275 Grand Street Port Moody BC J5W9B1', 
        '17 Golf Drive Langley BC J0J8E6', '9171 Ocean St Kelowna BC E8G4K4', '5 W. Holly St Victoria BC B5A2S6', 
        '8260 Vale Ave Kamloops BC G9T4P5', '8265 W. Gainsway Ave Maple Ridge BC K4M2A7', 
        '40 Sage Court North Vancouver BC E6C8X9', '77 Hilltop Rd Saanich BC A2B2B3', '196 New St New Westminster BC T4S4T8'
        ]
        
        store_ids = ['001','002','003','004','005','006','007','008','009','110']

        manager_id = ['501','502','503','504','505','506','507','508','509','510']

        revenue = [25000, 35000, 42000, 29000, 38000, 40000, 31000, 27000, 32000, 36000]

        for i in range(10):   
            line = [store_ids[i],stores_names[i],manager_id[i],addresses[i],revenue[i]] 
            writer.writerow(line)

def main():
    
    writes_csv()

    

if __name__ == '__main__':
    main()                
