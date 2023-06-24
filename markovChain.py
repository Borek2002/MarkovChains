import pandas as pd


class MarkovChain:
    wordCases = None
    probability = []
    words = []
    matrixOfProbabilty = None
    max_lenght = 0

    def __init__(self):
        self.matrixOfProbabilty = [[0 for i in range(26)] for j in range(26)]
        self.readFile()
        self.splitWords()

    def readFile(self):
        file = open("words.txt", 'r')
        line = file.readline()
        while (line != ''):
            self.words.append(line[:len(line) - 1])
            line = file.readline()

    def splitWords(self):
        self.max_length = max(len(word) for word in self.words)
        self.wordCases = [[] for j in range(self.max_length)]
        for i in range(len(self.words)):
            for j in range(len(self.words[i])):
                self.wordCases[j].append(self.words[i][:j + 1])

    def createMatrix(self, start, letter, word):
        self.matrixOfProbabilty = [[0 for i in range(26)] for j in range(26)]
        for i in range(len(self.words)):
            wordSplit = list(self.words[i])
            if (start + 1 >= len(wordSplit) - 1 and start >= len(wordSplit) - 1):
                continue
            if (word == self.words[i][:start + 1] and self.words[i][start] == letter):
                if (wordSplit[start] == letter):
                    self.matrixOfProbabilty[ord(wordSplit[start + 1]) - 97][ord(wordSplit[start]) - 97] += 1

        total = sum([sum(row) for row in self.matrixOfProbabilty])
        for i in range(len(self.matrixOfProbabilty)):
            for j in range(len(self.matrixOfProbabilty[i])):
                if (self.matrixOfProbabilty[i][j] != 0):
                    self.matrixOfProbabilty[i][j] /= total

    def getTheMostLikelyWord(self, start, word):
        theMostLikelyWord = word
        letter = word[len(word) - 1]
        self.createMatrix(start, letter, theMostLikelyWord)
        maxValue = -2
        while (maxValue != -1):
            index = -1
            maxValue = -1
            for i in range(len(self.matrixOfProbabilty)):
                if (self.matrixOfProbabilty[i][ord(letter) - 97] > maxValue and self.matrixOfProbabilty[i][
                    ord(letter) - 97] != 0):
                    maxValue = self.matrixOfProbabilty[i][ord(letter) - 97]
                    index = i
            newLetter = ""
            if (index != -1):
                newLetter = chr(index + 97)
                theMostLikelyWord += newLetter
            start += 1
            self.createMatrix(start, newLetter, theMostLikelyWord)
            #self.printMatrix(self.matrixOfProbabilty)
            letter = newLetter
            #print(theMostLikelyWord)
        return theMostLikelyWord

    def writingOutWords(self, text):
        return self.getTheMostLikelyWord(len(text) - 1, text)

    @staticmethod
    def printMatrix(matrix):
        print()
        for i in range(len(matrix)):
            print(matrix[i])


markov = MarkovChain()
markov.readFile()
markov.splitWords()
# #markov.getProbalility("a")
#
## markov.createMatrix(4,"t","t")
# matrix3=markov.matrixOfProbabilty
MarkovChain.printMatrix(markov.matrixOfProbabilty)
markov.getTheMostLikelyWord(3, "disa")
