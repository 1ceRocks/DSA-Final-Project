from tkinter import *

root = Tk()
root.geometry("1500x570")
root.title("VILLARIZA South Supermarket")
root.resizable(False, False)

# pyCanvas = Canvas(root, bg = "gray16", height = 200, width = 200)
# imageFile = PhotoImage(file = "")

# FRAME = Frame(root, bg="blue", height=100, width=300)
# imageFile = PhotoImage(file = "supermarket.png")
# background_label = Label(root, image = imageFile, anchor="center")
# background_label.place(x=0, y=0, relwidth = 1, relheight = 1)

def Reset():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    entry_8.delete(0, END)
    entry_9.delete(0, END)
    entry_10.delete(0, END)
    
def Total():
    try: a1 = int(promo1.get())
    except: a1 = 0
    
    try: a2 = int(promo2.get())
    except: a2 = 0
    
    try: a3 = int(promo3.get()) 
    except: a3 = 0
    
    try: a4 = int(promo4.get()) 
    except: a4 = 0
    
    try: a5 = int(promo5.get()) 
    except: a5 = 0
    
    try: a6 = int(promo6.get()) 
    except: a6 = 0
    
    try: a7 = int(promo7.get()) 
    except: a7 = 0
    
    try: a8 = int(promo8.get()) 
    except: a8 = 0
    
    try: a9 = int(promo9.get()) 
    except: a9 = 0
    
    try: a10 = int(promo10.get()) 
    except: a10 = 0
    
    #? define cost of each item per quantity
    c1 = 13.50 * a1
    c2 = 14.50 * a2
    c3 = 15.00 * a3
    c4 = 16.00 * a4
    c5 = 17.50 * a5
    c6 = 17.75 * a6
    c7 = 18.50 * a7
    c8 = 19.50 * a8
    c9 = 20.50 * a9
    c10 = 21.00 * a10
    
    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7 +  c8 + c9 + c10

Label(text = "VILLARIZA South Supermarket", bg = "black", fg = "white", font = ("Verdana", 33), width = "300", height = "2").pack()

#? MENU CARD
f = Frame(root, bg = "lightgreen", highlightbackground = "black", highlightthickness = 1, width = 450, height = 440)
f.place(x = 10, y = 120)

Label(f, text = "Menu", font = ("Gabriola", 40, "bold"), fg = "black", bg = "lightgreen").place(x = 160, y = 0)

Label(f, font = ("Verdana", 11, 'bold'), text = "Pancit Canton                                 = PHP 13.50/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 90)
Label(f, font = ("Verdana", 11, 'bold'), text = "Knorr Sinigang                               = PHP 14.50/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 125)
Label(f, font = ("Verdana", 11, 'bold'), text = "Master Gulaman Gelatin                = PHP 15.00/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 160)
Label(f, font = ("Verdana", 11, 'bold'), text = "Silver Swan Suka Sup                    = PHP 16.00/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 195)
Label(f, font = ("Verdana", 11, 'bold'), text = "Ajinomoto Sarsaya Oyster Sauce = PHP 17.50/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 230)
Label(f, font = ("Verdana", 11, 'bold'), text = "Silka Soap Papaya                         = PHP 17.75/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 265)
Label(f, font = ("Verdana", 11, 'bold'), text = "CDO Meat Loaf                               = PHP 18.50/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 300)
Label(f, font = ("Verdana", 11, 'bold'), text = "Tang Powdered Juice                     = PHP 19.50/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 335)
Label(f, font = ("Verdana", 11, 'bold'), text = "Dutch Mill Yoghurt Drink                = PHP 20.50/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 370)
Label(f, font = ("Verdana", 11, 'bold'), text = "Lucky Me Batchoy                          = PHP 21.00/qty.", fg = "black", bg = "lightgreen").place(x = 10, y = 405)

#? BILL
f2 = Frame(root, bg = "lightblue", highlightbackground = "black", highlightthickness = 1, width = 450, height = 440)
f2.place(x = 1040, y = 120)

Bill = Label(f2, text = "Bill Management", font = ('Gabriola', 40, "bold"), fg = "black", bg = "lightblue").place(x = 80, y = 0)

#? ENTRY WORK
f1 = Frame(root, bd = 5, width = 500, height = 670, relief = RAISED)
f1.pack()
f1.place(x = 475, y = 120)

Total_bill = StringVar()
promo1 = StringVar()
promo2 = StringVar()
promo3 = StringVar()
promo4 = StringVar()
promo5 = StringVar()
promo6 = StringVar()
promo7 = StringVar()
promo8 = StringVar()
promo9 = StringVar()
promo10 = StringVar()

#? LABEL
lbl_promo1 = Label(f1, font = ("Verdana", 15, "bold"), text = "Pancit Canton", width = 28, fg = "blue4")
lbl_promo2 = Label(f1, font = ("Verdana", 15, "bold"), text = "Knorr Sinigang", width = 28, fg = "blue4")
lbl_promo3 = Label(f1, font = ("Verdana", 15, "bold"), text = "Master Gulaman Gelatin", width = 28, fg = "blue4")
lbl_promo4 = Label(f1, font = ("Verdana", 15, "bold"), text = "Silver Swan Suka Sup", width = 28, fg = "blue4")
lbl_promo5 = Label(f1, font = ("Verdana", 15, "bold"), text = "Ajinomoto Sarsaya Oyster Sauce", width = 28, fg = "blue4")
lbl_promo6 = Label(f1, font = ("Verdana", 15, "bold"), text = "Silka Soap Papaya", width = 28, fg = "blue4")
lbl_promo7 = Label(f1, font = ("Verdana", 15, "bold"), text = "CDO Meat Loaf", width = 28, fg = "blue4")
lbl_promo8 = Label(f1, font = ("Verdana", 15, "bold"), text = "Tang Powdered Juice", width = 28, fg = "blue4")
lbl_promo9 = Label(f1, font = ("Verdana", 15, "bold"), text = "Dutch Mill Yoghurt Drink", width = 28, fg = "blue4")
lbl_promo10 = Label(f1, font = ("Verdana", 15, "bold"), text = "Lucky Me Batchoy", width = 28, fg = "blue4")

lbl_promo1.grid(row = 1, column = 0)
lbl_promo2.grid(row = 2, column = 0)
lbl_promo3.grid(row = 3, column = 0)
lbl_promo4.grid(row = 4, column = 0)
lbl_promo5.grid(row = 5, column = 0)
lbl_promo6.grid(row = 6, column = 0)
lbl_promo7.grid(row = 7, column = 0)
lbl_promo8.grid(row = 8, column = 0)
lbl_promo9.grid(row = 9, column = 0)
lbl_promo10.grid(row = 10, column = 0)

#? Entry
entry_1 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo1, bd = 2, width = 8, bg = "cyan")
entry_2 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo2, bd = 2, width = 8, bg = "cyan")
entry_3 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo3, bd = 2, width = 8, bg = "cyan")
entry_4 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo4, bd = 2, width = 8, bg = "cyan")
entry_5 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo5, bd = 2, width = 8, bg = "cyan")
entry_6 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo6, bd = 2, width = 8, bg = "cyan")
entry_7 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo7, bd = 2, width = 8, bg = "cyan")
entry_8 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo8, bd = 2, width = 8, bg = "cyan")
entry_9 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo9, bd = 2, width = 8, bg = "cyan")
entry_10 = Entry(f1, font = ("aria", 20, 'bold'), textvariable = promo10, bd = 2, width = 8, bg = "cyan")

entry_1.grid(row = 1, column = 1)
entry_2.grid(row = 2, column = 1)
entry_3.grid(row = 3, column = 1)
entry_4.grid(row = 4, column = 1)
entry_5.grid(row = 5, column = 1)
entry_6.grid(row = 6, column = 1)
entry_7.grid(row = 7, column = 1)
entry_8.grid(row = 8, column = 1)
entry_9.grid(row = 9, column = 1)
entry_10.grid(row = 10, column = 1)

#? buttons

btn_reset = Button(f1, bd = 5, fg = "black", bg = "lightblue", font = ("arial", 16, 'bold'), width = 10, text = "Reset", command = Reset)
btn_reset.place(x = 0, y = -50)
btn_reset.grid(row = 13, column = 0)

btn_total = Button(f1, bd = 5, fg = "black", bg = "lightblue", font = ("arial", 16, 'bold'), width = 10, text = "Total", command = Total)
btn_total.grid(row = 13, column = 1)

# pyCanvas.pack()
root.mainloop()