from tkinter import *

from markovChain import MarkovChain


# TEST TEST
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Markov Chain")
        self.window.geometry("480x480")
        self.markovChain=MarkovChain()
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
        #self.list.bind("<<ListboxSelect>>", self.fillout)
        self.entry.bind("<KeyRelease>", self.check)
        self.entry.bind("<Right>",self.rightSet)
        #self.window.bind("<Key>", self.handle_key_press)
        self.window.mainloop()

    def handle_key_press(self, event):
        if event.keysym == "Tab":
            self.fillout(None)
        else:
            # Obsługa innych klawiszy, jeśli wymagane
            pass
    def update(self, data):
        self.list.delete(0, END)
        for item in data:
            #print(item)
            self.list.insert(END, item)

    def rightSet(self,e):
        selected_word = self.list.get(0)
        print(selected_word)
        if selected_word:
            last_word = selected_word.split()[-1]
            current_text = self.entry.get()
            current_text_words = current_text.split()
            if current_text_words:
                current_text_words[-1] = last_word
                updated_text = " ".join(current_text_words)
                self.entry.delete(0, END)
                self.entry.insert(0, updated_text)
    # event/ when clicked on item on list fill entrybox
    # def fillout(self, e):
    #     self.entry.delete(0, END)
    #     self.entry.insert(0, self.list.get(ANCHOR))
    def fillout(self, e):
        selected_word = self.list.get(ANCHOR)
        if selected_word:
            last_word = selected_word.split()[-1]
            current_text = self.entry.get()
            current_text_words = current_text.split()
            if current_text_words:
                current_text_words[-1] = last_word
                updated_text = " ".join(current_text_words)
                self.entry.delete(0, END)
                self.entry.insert(0, updated_text)

    # Function to check listbox and entry
    def check(self, e):
        typed = self.entry.get()
        lastWord = typed.split()
        currentWord = lastWord[-1] if lastWord else ""
        if currentWord == '':
            self.data = []
        else:
            self.data = []
            print("XD")
            if currentWord[len(currentWord)-1] != ' ':
                print("typed: ", currentWord)
                words=self.markovChain.writingOutWords(currentWord)
                #words = self.lstm.predict(typed)
                self.data.append(words)
        self.update(self.data)


app = GUI()
app.loadWindow()