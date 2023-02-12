#  Licensed under the Apache License, Version 2.0 (the "License");

import os

#? dictionary is used to store collection of data in the format of key:value pairs that are useful for filtering values that connects two different elements (grocery items and its price). 
itemAvailableDict = {}

#? this variable is the main dictionary that interacts between the algorithm of the program from the user as consumer/customer.
shoppingDict = {}
# shoppingDict={"eggs":{"quantity":2,"subtotal":itemAvailableDict["egg"]*2}}
#welcome User

#? userName is the name of the user itself. This is used to identify the user and the user can access the information.
userName = input("Please enter your name: ")

#? variable for welcoming the user intended for greetings.
welcomeMessage = f" \bWelcome to VILLARIZA South Supermarket, \n{userName}."
lenWCMsg = len(welcomeMessage)
print("*" * lenWCMsg)
print(welcomeMessage)
print("*" * lenWCMsg)

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

#? for loop through the list in appending the element to a dictionary (itemAvailableDict)
def main_menu():
    for item in itemsAvailable:
        item_name = item.split()[0] #? split[0] to obtain string and store to its assigned local variable
        item_price = item.split()[1] #? split[1] to obtain string and store to its assigned local variable
        print(f"{item_name}: {item_price}") #? display the item name and price attribute in the program for console purposes.
        
        #? this line is essential as it needs to reserve the elements accurately right in key:value order for accessing the program from the user interface input (shoppingDict).
        itemAvailableDict.update({item_name: float(item_price)})
   
main_menu()
print("*" * 20)
# print(itemAvailableDict)
#prompt user to add items
shopping_Cart = True

#? executes the command and returns a list of items available for the user to purchase if it wants to proceed shopping for a particular item.

def purchaseItems():
    while shopping_Cart:
        os.system('cls')
        proceedShopping = input(" \bDo you wish to proceed? (yes / no) \n>>> ")
        try:
            if proceedShopping.lower() == "no":
                shopping_Cart = False
                
        except ValueError:
            print('Please input a correct feed into our program.')
            
        
        def browseItems():
            while True:
                item_added = input("Add an item: ")
            
                if item_added.title() in itemAvailableDict:
                    item_qty = int(input("Add quantity: "))
                    shoppingDict.update({item_added:{"quantity":item_qty,"subtotal":itemAvailableDict[item_added.title()]*item_qty}})
                    print(shoppingDict)
                
                elif item_added.isdigit() or item_added.isdecimal() or item_added.isspace():
                    print("Please input a correct feed into our program.")
                
                else:
                    print("unable to add unavailable item")
            
        continueShopping = input("Do you wish to add more items? (yes / no) \n>>> ")
        
        if 

purchaseItems()
continueShopping = input("Do you wish to add more items (yes/no): ")


  
#? prints out the total amount of items the user shopped from the global user variable shoppingDict{} with the summary of total prices aligned to quantity input.
else:
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