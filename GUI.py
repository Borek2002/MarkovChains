from tkinter import *

from lstmRNN import NeutralNetwork
from markovChain import MarkovChain


# TEST TEST
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Markov Chain")
        self.window.geometry("300x300")
        # self.markovChain=MarkovChain()
        self.lstm = NeutralNetwork()
        self.iterator = 0
        self.data = []

    def loadWindow(self):
        self.window.configure(bg="#27214A")
        self.mainLabel = Label(self.window, text="Enter text", font=("Helvetica", 15))
        self.mainLabel.configure(foreground='white', bg="#27214A")
        self.mainLabel.pack(pady=20)
        self.entry = Entry(self.window, font=("Helvetica", 12), width=30)
        self.entry.pack()
        self.predictLabel = Label(self.window, text="Predict text", font=("Helvetica", 15))
        self.predictLabel.configure(foreground='white', bg="#27214A")
        self.predictLabel.pack(pady=10)
        self.list = Listbox(self.window, width=30, height=1, font=("Helvetica", 12))
        self.list.pack(pady=10)
        self.mloop()

    def mloop(self):
        self.update(self.data)
        self.list.bind("<<ListboxSelect>>", self.fillout)
        self.entry.bind("<KeyRelease>", self.check)
        self.window.mainloop()

    def update(self, data):
        self.list.delete(0, END)
        for item in data:
            self.list.insert(END, item)

    # event/ when clicked on item on list fill entrybox
    def fillout(self, e):
        self.entry.delete(0, END)
        self.entry.insert(0, self.list.get(ANCHOR))

    # Function to check listbox and entry
    def check(self, e):
        typed = self.entry.get()
        if typed == '':
            self.data = []
        else:
            self.data = []
            # words=self.markovChain.writingOutWords(typed)
            words = self.lstm.predict(typed)
            self.data.append(words)
        self.update(self.data)


app = GUI()
app.loadWindow()
