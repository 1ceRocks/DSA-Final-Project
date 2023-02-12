#  Licensed under the Apache License, Version 2.0 (the "License");

import os, time

#? dictionary is used to store collection of data in the format of key:value pairs that are useful for filtering values that connects two different elements (grocery items and its price). 
itemAvailableDict = {}

#? this variable is the main dictionary that interacts between the algorithm of the program from the user as consumer/customer.
shoppingDict = {}
# shoppingDict={"eggs":{"quantity":2,"subtotal":itemAvailableDict["egg"]*2}}
#welcome User

#? userName is the name of the user itself. This is used to identify the user and the user can access the information.
os.system('cls')
userName = input("Please enter your name: ")

#? variable for welcoming the user intended for greetings.
os.system('cls')
welcomeMessage = f" \bWelcome to VILLARIZA South Supermarket, \n{userName}."
lenWCMsg = len(welcomeMessage)
print("*" * lenWCMsg + "\n")
print(welcomeMessage)
print("\n" + "*" * lenWCMsg)
time.sleep(2)

#read data from text file 
#? access the text file and read the data and stored information 
my_file = open("available_grocery_items.txt")
file_line = my_file.readline()

#? readlines() method is used to read the entire contents of the text file.
itemsAvailable = my_file.readlines()
# print(itemsAvailable)
my_file.close()

#fetch items from list and add to a dictionary
print("***********Items Available in Our Store****************")

#* PYTHON COLOR CLASS
def pyColors(bk, rd, gr, yl, bl, ma, cy ,wh):
    bk = '\033[30m'
    gr = '\033[32m'
    return bk, rd, gr, yl, bl, ma, cy, wh
    
black, red, green, yellow, blue, magenta, cyan, white = pyColors(1, 2, 3, 4, 5, 6, 7, 8)
RED = '\033[31m]'

#? for loop through the list in appending the element to a dictionary (itemAvailableDict)
def main_menu():
    for item in itemsAvailable:
        item_name = item.split()[0] #? split[0] to obtain string and store to its assigned local variable
        item_price = item.split()[1] #? split[1] to obtain string and store to its assigned local variable
        print(f"{item_name}: {green}PHP {item_price}\033[0m") #? display the item name and price attribute in the program for console purposes.
        
        #? this line is essential as it needs to reserve the elements accurately right in key:value order for accessing the program from the user interface input (shoppingDict).
        itemAvailableDict.update({item_name: float(item_price)})
   
main_menu()
print("*" * 20)
# print(itemAvailableDict)
#prompt user to add items
# shopping_Cart = True

def sumItems():
    os.system('cls')
    print("\n")
    print("****Bill Summary***** ")
    print("\n")
    print("Item    Quantity    SubTotal")
    shopping_Sum = 0
    for key in shoppingDict:
        print(f"{key}    {shoppingDict[key]['quantity']}        {shoppingDict[key]['subtotal']}")
        shopping_Sum = shoppingDict[key]['subtotal'] + shopping_Sum
    print(f" \bTotal: {shoppingDict}")
    print("***********Thank You********")
    print("Hope to see you back soon!")
    
def purchaseItems():
    proceedShopping = input(" \bDo you wish to proceed? (yes / no) \n>>> ")
    try:
        if proceedShopping.lower() == "no":
            sumItems()

        elif proceedShopping.lower() == "yes":
            os.system('cls')     
            main_menu()
            browseItems()  
            
        else:    
            print('Please input a correct feed into our program.')
            purchaseItems()
                
    except ValueError:
        print('Please input a correct feed into our program.')       
       
        
def browseItems():
    os.system('cls')
    main_menu()
    item_added = input("\n \bAdd an item: ")
    
    if item_added.title() in itemAvailableDict:
        item_qty = int(input("Add quantity: "))
        shoppingDict.update({item_added:{"quantity":item_qty,"subtotal":itemAvailableDict[item_added.title()]*item_qty}})
        print(shoppingDict)
        while True:
            verUser = input("\n \bDo you wish to add more items? (yes / no) \n>>> ")
            if verUser.lower() == "no":
                sumItems()
                break

            elif verUser.lower() == "yes":
                os.system('cls')
                browseItems()  
                
            else:    
                os.system('cls')
                print('Please input a correct feed into our program.')
                continue

    else:
        print("Unable to add unavailable item.")
        browseItems()
                  
purchaseItems()