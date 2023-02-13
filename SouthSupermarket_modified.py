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

promos = open("grocerySection/promos.txt")
freshMeatSeafoods = open("grocerySection/freshMeatSeafoods.txt")
freshProduce = open("grocerySection/freshProduce.txt")
promosAvail = promos.readlines()
fMSAvail = freshMeatSeafoods.readlines()
fPRAvail = freshProduce.readlines()
promos.close() 
freshMeatSeafoods.close()
freshProduce.close()

itemsAvailable = promosAvail
itemsAvailable2 = fMSAvail
itemsAvailable3 = fPRAvail

def produceItems():
    for item in itemsAvailable:
        item_name = item.split()[0]
        item_price = item.split()[1] 
        itemAvailableDict.update({item_name: float(item_price)})
        
    for item in itemsAvailable2:
        item_name = item.split()[0]
        item_price = item.split()[1] 
        itemAvailableDict.update({item_name: float(item_price)})
        
    for item in itemsAvailable3:
        item_name = item.split()[0]
        item_price = item.split()[1] 
        itemAvailableDict.update({item_name: float(item_price)})
produceItems()

#* PYTHON COLOR CLASS
def textFormat(r, b, f, i, u):
    r = '\033[0m'
    b = '\033[1m'
    f = '\033[2m'
    i = '\033[3m'
    u = '\033[4m'
    return r, b, f, i, u
    
def foregroundColors(bk, rd, gr, yl, bl, ma, cy ,wh):
    bk = '\033[30m'
    rd = '\033[31m'
    gr = '\033[32m'
    yl = '\033[33m'
    bl = '\033[34m'
    ma = '\033[35m'
    cy = '\033[36m'
    wh = '\033[37m'
    return bk, rd, gr, yl, bl, ma, cy, wh

def backgroundColors(bgBk, bgRd, bgGr, bgYl, bgBl, bgMa, bgCy, bgWh):
    bgBk = '\033[40m'
    bgRd = '\033[41m'
    bgGr = '\033[42m'
    bgYl = '\033[43m'
    bgBl = '\033[44m'
    bgMa = '\033[45m'
    bgCy = '\033[46m'
    bgWh = '\033[47m'
    return bgBk, bgRd, bgGr, bgYl, bgBl, bgMa, bgCy, bgWh

reset, bold, faint, italic, underlined = textFormat(1, 2, 3, 4, 5)
    
black, red, green, yellow, blue, magenta, cyan, white = foregroundColors(1, 2, 3, 4, 5, 6, 7, 8)

bgBlack, bgRed, bgGreen, bgYellow, bgBlue, bgMagenta, bgCyan, bgWhite = backgroundColors(1, 2, 3, 4, 5, 6, 7, 8)

#? for loop through the list in appending the element to a dictionary (itemAvailableDict)
def main_menu(usrChoice):
    progTitle = "{}".format(f"\nConsumer-Product Category\n")
    progGreet = "{}".format(f"\b1. Promos \n2. Fresh Meat and Seafoods \n3. Fresh Produce")
    def progInf():
        print(progTitle, progGreet.ljust(10))
    progInf()
    
    while True:
        try:
            usrChoice = int(input("\nSelect the following aisle/section you want to browse by typing the indicated number (1-3) \n \b>>> "))
            if usrChoice > 4:
                os.system('cls')
                print('Input not recognized or out of range.')
                main_menu()
        except ValueError:
            os.system('cls')
            print('Input not recognized. Please try again.')
            main_menu(usrChoice)
        finally:
            productAisle(usrChoice)
            break
    return usrChoice  
   
def productAisle(usrChoice):
    if usrChoice == 1:   
        def promoSec():
            for item in promosAvail:
                item_name = item.split()[0]
                item_price = item.split()[1] 
                print(f"{item_name}: {bold}{green}PHP {item_price}{reset}")
        promoSec()
        return usrChoice
    elif usrChoice == 2:
        def fMSSec():    
            for item in fMSAvail:
                item_name = item.split()[0]
                item_price = item.split()[1] 
                print(f"{item_name}: {bold}{green}PHP {item_price}{reset}")
        fMSSec()
        return usrChoice
    elif usrChoice == 3:
        def fPRSec():    
            for item in fPRAvail:
                item_name = item.split()[0]
                item_price = item.split()[1] 
                print(f"{item_name}: {bold}{green}PHP {item_price}{reset}")
        fPRSec()
        return usrChoice

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
    
def purchaseItems(usrChoice):
    proceedShopping = input(" \bDo you wish to proceed? (yes / no) \n>>> ")
    try:
        if proceedShopping.lower() == "no":
            sumItems()

        elif proceedShopping.lower() == "yes":
            os.system('cls')
            productAisle(usrChoice)     
            browseItems(usrChoice)  
            
        else:    
            print('Please input a correct feed into our program.')
            purchaseItems(usrChoice)
                
    except ValueError:
        print('Please input a correct feed into our program.')       
       
        
def browseItems(usrChoice):
    item_added = input("\n \bAdd an item: ")
    
    if item_added.title() in itemAvailableDict:
        item_qty = int(input("Add quantity: "))
        shoppingDict.update({item_added:{"quantity":item_qty,"subtotal":itemAvailableDict[item_added.title()]*item_qty}})
        def consumerCart():
            os.system('cls')
            productAisle(usrChoice)
            print(f"\n \b{bold}{yellow}Your Cart{reset}")
            for key in shoppingDict:
                print(f"{blue}{key} {green}Quantity:{reset} {shoppingDict[key]['quantity']}")
        consumerCart()
        while True:
            verUser = input("\n \bDo you wish to add more items? (yes / no) \n>>> ")
            if verUser.lower() == "no":
                sumItems()
                break

            elif verUser.lower() == "yes":
                os.system('cls')
                productAisle(usrChoice)
                consumerCart()
                browseItems(usrChoice)  
                
            else:    
                os.system('cls')
                productAisle(usrChoice)
                print('Please input a correct feed on the program.')
                continue

    else:
        print("Unable to add unavailable item.")
        browseItems(usrChoice)
                  
usrChoice = 0        
purchaseItems(main_menu(usrChoice))