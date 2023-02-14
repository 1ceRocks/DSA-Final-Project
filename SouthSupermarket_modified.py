#  Licensed under the Apache License, Version 2.0 (the "License");

import os, time

#? dictionary is used to store collection of data in the format of key:value pairs that are useful for filtering values that connects two different elements (grocery items and its price). 
itemAvailableDict = {}

#? this variable is the main dictionary that interacts between the algorithm of the program from the user as consumer/customer.
shoppingDict = {}
# shoppingDict={"eggs":{"quantity":2,"subtotal":itemAvailableDict["egg"]*2}}
#welcome User

def openProduct1(Avail):
    promos = open("grocerySection/promos.txt")
    Avail = promos.readlines()
    promos.close()
    return Avail

def openProduct2(Avail):
    freshMeatSeafoods = open("grocerySection/freshMeatSeafoods.txt")
    Avail = freshMeatSeafoods.readlines()
    freshMeatSeafoods.close()
    return Avail

def openProduct3(Avail):
    freshProduce = open("grocerySection/freshProduce.txt")
    Avail = freshProduce.readlines()
    freshProduce.close()
    return Avail

def openProduct4(Avail):
    snacks = open("grocerySection/snacks.txt")
    Avail = snacks.readlines()
    snacks.close()
    return Avail

def openProduct5(Avail):
    beverage = open("grocerySection/beverage.txt")
    Avail = beverage.readlines()
    beverage.close()
    return Avail

itemsAvailable = openProduct1(1)
itemsAvailable2 = openProduct2(2)
itemsAvailable3 = openProduct3(3)
itemsAvailable4 = openProduct4(4)
itemsAvailable5 = openProduct5(5)

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
        
    for item in itemsAvailable4:
        item_name = item.split()[0]
        item_price = item.split()[1] 
        itemAvailableDict.update({item_name: float(item_price)})
        
    for item in itemsAvailable5:
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

def welcomeMsg():
    #? userName is the name of the user itself. This is used to identify the user and the user can access the information.
    os.system('cls')
    userName = input(f"{yellow}{bold} CUSTOMER NAME {reset}\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} ")

    #? variable for welcoming the user intended for greetings.
    os.system('cls')
    welcomeMessage = f"{reset} \bWelcome to {bgBlack}{bold} VILLARIZA South Supermarket {reset}\n\n{bold}{cyan}{userName.upper()}{reset}"
    lenWCMsg = len(welcomeMessage)
    print(f"{reset}{bold}{blue}="*lenWCMsg)
    print(f"\n{welcomeMessage}\n")
    print(f"{reset}{bold}{yellow}-"*lenWCMsg)
    time.sleep(3)
welcomeMsg()

def yourCart():
    os.system('cls')
    progDesign = f"{bold}{white}={reset}"*80
    progIndicator = "{}".format("%-40s %-40s %s" %(f"{bold}{blue}Product", f"{green}Quantity", f"{red}Subtotal{reset}"))
    print(f"\n \b{bold}{yellow}Your Cart{reset}\n{progDesign}\n \b{progIndicator}")
    for key in shoppingDict:
        print("%-39s %-40s %s" %(f"{blue}\b{key}", f"{green}\b{shoppingDict[key]['quantity']} pcs.", f"{red}PHP {shoppingDict[key]['subtotal']}{reset}"))
    print(f"{bold}{white}-{reset}"*80)

#? for loop through the list in appending the element to a dictionary (itemAvailableDict)
def main_menu(usrChoice):
    os.system('cls')
    progTitle = "{}".format(f"\n{reset}{bgYellow}{bold}{black} Available Product Category {reset}\n")
    progTitle2 = "{}".format(f"\n\n{reset}{bgYellow}{bold}{black} Consumer Options {reset}\n")
    progNum = "{}".format(f"\n \b{bold}{blue}1. {yellow}Promos \n{blue}2. {yellow}Fresh Meat and Seafoods \n{blue}3. {yellow}Fresh Produce \n{blue}4. {yellow}Snacks \n{blue}5. {yellow}Beverage{reset}")
    progNum2 = "{}".format(f"\n \b{bold}{blue}6. {yellow}View My Cart \n{blue}7. {yellow}Edit My Cart \n{blue}8. {yellow}Checkout{reset}")
    def progInf():
        print(progTitle, progNum, progTitle2, progNum2)
    progInf()
    
    while True:
        try:
            usrChoice = int(input(f"\n{reset}Select the following {bold}{white}{underlined}category{reset} you want to browse by typing the indicated number {bold}{blue}(1-8){reset}\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} "))
            if usrChoice > 8:
                os.system('cls')
                main_menu(usrChoice)
                print(f'{reset}Input not recognized or out of range.')
        except ValueError:
            os.system('cls')
            main_menu(usrChoice)
            print(f'{reset}Input not recognized. Please try again.')
        finally:
            productAisle(usrChoice)
            break
    return usrChoice  
   
def sumItems():
    os.system('cls')
    print(f"{reset}{bold}{red}{bgWhite}TRANSACTION MANAGEMENT{reset}\n")
    heading = f"{'Product':31s}{'Quantity':31s}{'Subtotal'}{reset}"
    print("="*len(heading))
    print(f"{reset}{bold}{heading}{reset}")
    print("-"*len(heading))
    shopping_Sum = 0
    for key in shoppingDict:
        print("%-30s %-30s %s" %(key, shoppingDict[key]['quantity'], shoppingDict[key]['subtotal']))
        shopping_Sum = shoppingDict[key]['subtotal'] + shopping_Sum
    print(f"{reset}\n \b{bold}{red}TOTAL{white}: {green}PHP {shopping_Sum:.2f}{reset}\n")
    progExit = "{}".format(f"{reset}Type and enter the {bold}{white}Q{reset} key to exit viewing {italic}{yellow}your cart{reset} anytime.")
    varBreak = True
    while varBreak:
        verUser = input(f"\n{progExit}\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} ")    
        if verUser.title() == "Q":
            browseItems(main_menu(usrChoice))
            varBreak = False
        else:
            print(f"\n{reset}{italic}{red}Input not recognized. Please try again.{reset}")
            sumItems()     
   
def productAisle(usrChoice):
    os.system('cls')
    gap = ' '*3
    print(f"{bold}{white}={reset}"*53)
    heading = f"{reset}{bold}{blue}{'PRODUCT':40s}{gap}{green}{'QUANTITY':>6s}{reset}"
    print(heading)
    if usrChoice == 1:   
        def promoSec():
            print(f"{reset}{bold}{yellow:20s}PROMOS PRODUCT CATEGORY{reset}\n")
            for item in itemsAvailable:
                item_name = item.split()[0]
                item_price = item.split()[1]
                rec = f"{reset}{blue}{item_name:40s}{gap}{green}PHP {item_price:^6s}{reset}"
                print(rec)
            print(f"{bold}{white}-{reset}"*53)
        promoSec()
        return usrChoice
    elif usrChoice == 2:
        def fMSSec():    
            print(f"{reset}{bold}{yellow:15s}FRESH MEAT & SEAFOODS CATEGORY{reset}\n")
            for item in itemsAvailable2:
                item_name = item.split()[0]
                item_price = item.split()[1]
                rec = f"{reset}{blue}{item_name:40s}{gap}{green}PHP {item_price:^6s}{reset}" 
                print(rec)
            print(f"{bold}{white}-{reset}"*53)
        fMSSec()
        return usrChoice
    elif usrChoice == 3:
        def fPRSec():    
            print(f"{reset}{bold}{yellow:20s}FRESH PRODUCE CATEGORY{reset}\n")
            for item in itemsAvailable3:
                item_name = item.split()[0]
                item_price = item.split()[1]
                rec = f"{reset}{blue}{item_name:40s}{gap}{green}PHP {item_price:^6s}{reset}" 
                print(rec)
            print(f"{bold}{white}-{reset}"*53)
        fPRSec()
        return usrChoice
    elif usrChoice == 4:
        def snacksSec():    
            print(f"{reset}{bold}{yellow:22s}SNACKS CATEGORY{reset}\n")
            for item in itemsAvailable4:
                item_name = item.split()[0]
                item_price = item.split()[1]
                rec = f"{reset}{blue}{item_name:40s}{gap}{green}PHP {item_price:^6s}{reset}" 
                print(rec)
            print(f"{bold}{white}-{reset}"*53)
        snacksSec()
        return usrChoice
    elif usrChoice == 5:
        def bvgSec():    
            print(f"{reset}{bold}{yellow:21s}BEVERAGE CATEGORY{reset}\n")
            for item in itemsAvailable5:
                item_name = item.split()[0]
                item_price = item.split()[1]
                rec = f"{reset}{blue}{item_name:40s}{gap}{green}PHP {item_price:^6s}{reset}" 
                print(rec)
            print(f"{bold}{white}-{reset}"*53)
        bvgSec()
        return usrChoice
    elif usrChoice == 6:
        def usr6():
            yourCart()
            progExit = "{}".format(f"{reset}Type and enter the {bold}{white}Q{reset} key to exit viewing {italic}{yellow}your cart{reset} anytime.")
            varBreak = True
            while varBreak:
                verUser = input(f"\n{progExit}\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} ")    
                if verUser.title() == "Q":
                    browseItems(main_menu(usrChoice))
                    varBreak = False
                else:
                    print(f"\n{reset}{italic}{red}Input not recognized. Please try again.{reset}")
                    usr6()
        usr6()
    elif usrChoice == 7:
        def usr7():
            os.system('cls')
            yourCart()
            progEdit = "{}".format(f"{reset}Type and enter the {bold}{blue}item{reset} that you want to {bold}{yellow}edit{reset}.{reset} Type and enter the {bold}{white}Q{reset} key once you've done editing {italic}{yellow}your cart{reset}.")
            verUser = input(f"\n{progEdit}\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} ")
            varBreak = True
            while varBreak:
                if verUser.title() == "Q":
                    browseItems(main_menu(usrChoice))
                    varBreak = False
                for item in shoppingDict:
                    if verUser == item:
                        os.system('cls')
                        yourCart()
                        editOpt = input(f"\n{reset}Do you want to {bgRed}{bold} remove {reset} the item {bold}{blue}{verUser}{reset} or {bgYellow}{bold}{black} change {reset} its {bold}{green}Quantity{reset}? ({bold}remove{reset} / {bold}change{reset})\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} ")
                        if editOpt.lower() == "remove":
                            del shoppingDict[item]
                            usr7()
                            break
                        elif editOpt.lower() == "change":
                            os.system('cls')
                            yourCart()
                            editQty = input(f"\n{reset}Update the {bold}{green}Quantity{reset} that you want for {bold}{blue}{verUser}{reset}.\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} ")
                            right_qty = int(editQty)
                            shoppingDict.update({verUser:{"quantity":right_qty,"subtotal":itemAvailableDict[verUser.title()]*right_qty}})
                            # shoppingDict[item]['quantity'] = float(editQty)
                            # shoppingDict.update({"subtotal":itemAvailableDict[verUser.title()]['subtotal']*right_qty})
                            usr7()
                            break
                else:
                    print(f"\n{reset}{italic}{red}Input not recognized. Please try again.{reset}")
                    usr7()
        usr7()
    elif usrChoice == 8:
        sumItems()
             
def browseItems(usrChoice):
    progExit = "{}".format(f"{reset}Type and enter the {bold}{white}Q{reset} key to exit the {italic}{yellow}Product Category{reset} anytime.")
    def askUser():
        print("\n" + progExit)
    askUser()
    item_added = input(f"{reset}\n \bAdd an item:{bold}{white} ")
    
    if item_added.title() in itemAvailableDict:
        os.system('cls')
        def productQuantity():
            productAisle(usrChoice)
            def inputError():
                    os.system('cls')
                    productAisle(usrChoice)
                    print(f"\n{reset}{italic}{red}Input not recognized. Please try again.{reset}")
            askUser()
            
            def usrQuantity():
                print(f"\n \b{reset}Chosen Item: {blue}{item_added.title()}{reset}")
                try:
                    item_qty = input(f"Enter Quantity:{bold}{white} ")
                    usrRepeat = True
                
                    if str(item_qty).title() == "Q":
                        os.system('cls')
                        usrRepeat = False
                        main_menu(usrChoice)
                    
                    elif str(item_qty).isalpha():
                        inputError()
                        askUser()
                        usrQuantity()
                        
                    elif int(item_qty) > 0:
                        right_qty = int(item_qty)
                        shoppingDict.update({item_added:{"quantity":right_qty,"subtotal":itemAvailableDict[item_added.title()]*right_qty}})
                        def consumerCart():
                            os.system('cls')
                            productAisle(usrChoice)
                            progIndicator = "{}".format("%-40s %-40s %s" %(f"{bold}{blue}Product", f"{green}Quantity", f"{red}Subtotal{reset}"))
                            print(f"\n \b{bold}{yellow}Your Cart{reset}\n\n \b{progIndicator}")
                            for key in shoppingDict:
                                print("%-39s %-40s %s" %(f"{blue}\b{key}", f"{green}\b{shoppingDict[key]['quantity']} pcs.", f"{red}PHP {shoppingDict[key]['subtotal']}{reset}"))
                        consumerCart()
                        while usrRepeat:
                            verUser = input(f"\n \bDo you wish to {bold}{underlined}{green}add{reset} more {bold}{blue}items?{reset} ({bold}{white}yes {reset}/ {bold}{white}no{reset})\n\n \b{blue}>{yellow}>{blue}>{bold}{blue} ")
                            if verUser.lower() == "no":
                                browseItems(main_menu(usrChoice))
                                usrRepeat = False

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
                    elif int(item_qty) <= 0:
                        print("Unable to read 0 or less than quantity for the said item.")
                        productQuantity() 
                except ValueError:
                    inputError()
                    askUser()
                    usrQuantity()  
            usrQuantity()
        productQuantity()
        
    elif item_added.title() == "Q":
        os.system('cls')
        main_menu(usrChoice)
         
    elif item_added.title() not in itemAvailableDict:
        productAisle(usrChoice)
        print(f"\n{reset}{italic}{red}Item not found from the chosen category.{reset}")
        browseItems(usrChoice)
               
    else:
        os.system('cls')
        productAisle(usrChoice)
        print(f"\n{reset}{italic}{red}Input not recognized. Please try again.{reset}")
        browseItems(usrChoice)
                  
usrChoice = 0    
browseItems(main_menu(usrChoice))