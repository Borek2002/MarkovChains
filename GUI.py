from tkinter import *

from markovChain import MarkovChain


class GUI:
    def __init__(self):
        self.window=Tk()
        self.window.title("Markov Chain")
        self.window.geometry("750x500")
        self.markovChain=MarkovChain()
        self.iterator = 0
        self.data=self.markovChain.data[self.iterator]


    def loadWindow(self):
        self.mainLabel=Label(self.window,text="Enter the text",font=("Helvetica",15))
        self.mainLabel.pack(pady=20)
        self.entry=Entry(self.window,font=("Helvetica",10),width=100)
        self.entry.pack()
        self.list=Listbox(self.window,width=60,height=60,font=("Helvetica",10))
        self.list.pack(pady=40)
        self.mloop()

    def mloop(self):
        self.update(self.data)
        self.list.bind("<<ListboxSelect>>", self.fillout)
        self.entry.bind("<KeyRelease>", self.check)
        self.window.mainloop()

    def update(self,data):
        self.list.delete(0,END)
        for item in data:
            self.list.insert(END,item)

    # event/ when clicked on item on list fill entrybox
    def fillout(self,e):
        self.entry.delete(0,END)
        self.entry.insert(0,self.list.get(ANCHOR))

    # Function to check listbox and entry
    def check(self,e):
        typed=self.entry.get()
        if typed=='':
            self.data=self.markovChain.data[self.iterator]
        else:
            self.data=[]
            for item in self.markovChain.data[self.iterator]:
                if typed.lower() in item.lower():
                    self.data.append(item)
        self.update(self.data)


app=GUI()
app.loadWindow()
