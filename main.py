#!/usr/bin/python

import tkinter as Tk


class Main(object):
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Financial Tool")
        self.root.minsize(width=500, height=500)
        self.root.maxsize(width=500, height=500)
        self.label = Tk.Label(self.root, text="Enter the Company's ticker:")
        self.label.pack()
        
        self.ticker = Tk.StringVar()
        Tk.Entry(self.root, textvariable=self.ticker).pack()
        
        self.buttontext = Tk.StringVar()
        self.buttontext.set("Research!")
        Tk.Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()
        
        self.label = Tk.Label(self.root, text="")
        self.label.pack()
        
        self.root.attributes('-alpha', 0.0)
        self.center()
        self.root.attributes('-alpha', 1.0)
        self.root.mainloop()

    def center(self):
        self.root.update_idletasks()
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        size = tuple(int(_) for _ in self.root.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.root.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def clicked1(self):
        ticker = self.ticker.get()
        self.label.configure(text="Gathering info for " + ticker + "...")


Main()
