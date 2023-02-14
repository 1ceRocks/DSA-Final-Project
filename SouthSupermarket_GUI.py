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

# pyCanvas.pack()
root.mainloop()