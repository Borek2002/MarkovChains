import random
from collections import Counter
from tkinter import *
import ngrams
from ngrams import *
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Markov Chain")
        self.window.geometry("480x320")
        self.iterator = 0
        self.data = []
        self.word_lists = []
        self.number_of_lists = 5
        self.likely_sentences = []

    def loadWindow(self):
        self.window.configure(bg="#27214A")
        self.mainLabel = Label(self.window, text="Enter text", font=("Helvetica", 15))
        self.mainLabel.configure(foreground='white', bg="#27214A")
        self.mainLabel.pack(pady=20)
        self.entry = Entry(self.window, font=("Helvetica", 12), width=40)
        self.entry.pack()
        self.predictLabel = Label(self.window, text="Predict text", font=("Helvetica", 15))
        self.predictLabel.configure(foreground='white', bg="#27214A")
        self.predictLabel.pack(pady=10)
        self.mloop()

    #main loop
    def mloop(self):
        self.update(self.data)
        self.entry.bind("<KeyRelease>", self.check)
        self.window.mainloop()
    def update(self, data):
        for list in self.word_lists:
            list.delete(0, END)
            for item in data:
                list.insert(END, item)

    #Fill the entry box with generated text
    def fillout(self, list):
        selected_word = list.get(0)
        if selected_word:
            last_word = selected_word.split()[-1]
            print("selected word: ", last_word)
            current_text = self.entry.get()
            current_text_words = current_text.split()
            if current_text_words:
                current_text_words[-1] = last_word
                if(current_text[-1] != " "):
                    updated_text = selected_word + " "
                else:
                    updated_text = selected_word + " "

                self.entry.delete(0, END)
                self.entry.insert(END, updated_text)

    # Function to check listbox and entry
    def check(self, e, custom_entry=None):
        if custom_entry is None:
            typed = self.entry.get()
            self.clearWordLists()
        else:
            typed = custom_entry

        typed_words = typed.split()
        likely_words = []
        pairs = []
        self.data = []

        if typed == '':
            pass
        else:
            if typed[-1] == " ":
                typed = typed[:-1]
            f, s, t = mainFunc(typed)

            if t is not None:
                pairs = t
            elif s is not None:
                pairs = s
            else:
                pairs = f
            if pairs is not None:
                if type(pairs) == list: #
                    for pair in pairs:
                        if pair is not None:
                            likely_words.append(pair[0])  # pairs [WORD][NUMBER OF OCCURRENCES]
                else:
                    #self.createWordList(pairs[0])
                    likely_words.append(pairs[0])    # only one tuple
            if len(likely_words) > order:
                sentences_to_complete = order
            else:
                sentences_to_complete = len(likely_words)
            for word in likely_words:
                # completedSentence = self.completeSentence(typed + " " + word, sentences_to_complete)
                # if completedSentence:
                #     self.createWordList(completedSentence)
                # else:
                #     self.createWordList(typed + " " + word)
                if word != ngrams.end_of_sentence:
                    self.check(e=None, custom_entry=typed + " " + word)
                else:
                    self.likely_sentences.append(typed)
                    self.createWordList(typed)

        #self.data.append(words[0])
        #self.update(self.data)

    def completeSentence(self, partial_sentence, number_of_sentences):
        possible_sentences = []
        for sentence in sentences:
            if sentence.startswith(' '):
                sentence = sentence[1:]
            if sentence.startswith(partial_sentence):
                possible_sentences.append(sentence)
        possible_sentences_counts = Counter(possible_sentences)

        if possible_sentences:
            sorted_possible_sentences = sorted(possible_sentences, key=lambda s: possible_sentences_counts[s], reverse=True)
            completed_sentence = random.choice(sorted_possible_sentences[:number_of_sentences])
            return completed_sentence

        return None

    def createWordList(self, word):
        if self.number_of_lists > 0:
            listbox = Listbox(self.window, width=30, height=1, font=("Helvetica", 12))
            listbox.insert(END, word)
            listbox.pack(pady=5)
            listbox.bind("<Button-1>", lambda event, lb=listbox: self.fillout(list=lb))
            self.word_lists.append(listbox)
            self.number_of_lists -= 1
        else:
            pass

    def clearWordLists(self):
        for listbox in self.word_lists:
            listbox.destroy()
        self.word_lists = []
        self.number_of_lists = 5

app = GUI()
app.loadWindow()
