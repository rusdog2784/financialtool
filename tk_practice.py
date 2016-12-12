#!/usr/bin/python

import Tkinter as Tk


class App(object):
    def __init__(self):
        self.root = Tk.Tk()
        self.root.wm_title("Financial Tool")
        self.label = Tk.Label(self.root, text="Enter the Company's ticker:")
        self.label.pack()
        
        self.ticker = Tk.StringVar()
        Tk.Entry(self.root, textvariable=self.ticker).pack()
        
        self.buttontext = Tk.StringVar()
        self.buttontext.set("Research!")
        Tk.Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.label = Tk.Label(self.root, text="")
        self.label.pack()
                  
        self.root.mainloop()
    
    def clicked1(self):
        ticker = self.ticker.get()
        self.label.configure(text="Gathering info for " + ticker)

App()
