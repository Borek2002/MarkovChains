from tkinter import *

class GUI:
    def __init__(self):
        self.window=Tk()
        self.window.title("Markov Chain")
        self.window.geometry("750x500")

    def loadWindow(self):
        self.mainLabel=Label(self.window,text="Enter the text",font=("Helvetica",15))
        self.mainLabel.pack(pady=20)
        self.entry=Entry(self.window,font=("Helvetica",10),width=100)
        self.entry.pack()
        self.list=Listbox(self.window,width=60,height=60)
        self.list.pack(pady=40)

        self.window.mainloop()

app=GUI()
app.loadWindow()