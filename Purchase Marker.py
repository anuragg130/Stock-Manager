import tkinter as tk
from tkinter import messagebox

class form_purchasemarker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Purchase Marker")
        self.root.geometry("1000x1000")

        self.lb1 = tk.Label(self.root, text="")
        self.lb1.place(x=40, y=40)

        self.ent1 = tk.Entry(self.root, textvariable=self.disname)
        self.ent1.place(x=150, y=40)

        self.lb2 = tk.Label(self.root, text="Address")
        self.lb2.place(x=40, y=70)

        self.ent2 = tk.Entry(self.root, textvariable=self.add)
        self.ent2.place(x=150, y=70)

        self.lb3 = tk.Label(self.root, text="City")
        self.lb3.place(x=40, y=100)

        self.ent3 = tk.Entry(self.root, textvariable=self.city)
        self.ent3.place(x=150, y=100)

        self.lb4 = tk.Label(self.root, text="Contact No.")
        self.lb4.place(x=40, y=130)

        self.ent4 = tk.Entry(self.root, textvariable=self.contact)
        self.ent4.place(x=150, y=130)

        self.btn1 = tk.Button(self.root, text="Save", command=self.save_clicked)
        self.btn1.place(x=150, y=160)

        self.root.mainloop()