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

# pyCanvas.pack()
root.mainloop()