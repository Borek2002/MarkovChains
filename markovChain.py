import pandas as pd
class MarkovChain:
    wordCases=None
    probability=[]
    words=[]
    matrixOfProbabilty=[[0 for i in range(26)] for j in range(26)]
    max_lenght=0

    def readFile(self):
        file=open("words.txt",'r')
        line=file.readline()
        while(line!=''):
            self.words.append(line[:len(line)-2])
            line=file.readline()

    def splitWords(self):
        self.max_length = max(len(word) for word in self.words)
        self.wordCases=[[]for j in range(self.max_length)]
        for i in range(len(self.words)):
            for j in range(len(self.words[i])):
                    self.wordCases[j].append(self.words[i][:j+1])

    def getProbalility(self,text):
        tempProbability=[[]for j in range(self.max_length)]
        words=[]

        #prawdopodobieństwo dla każdego stanu
        for i in range(len(text),len(self.wordCases)):
            cases = [case for case in self.wordCases[i] if text in case]
            unique=list(set(cases))
            unique.sort()
            for j in range(len(unique)):
                tempProbability[i].append({"letter": unique[j],"probalility":self.wordCases[i].count(unique[j])/len(cases)})

        #prawdopodobieństwo wyrazu
        for i in range(len(tempProbability)):
            for j in range(len(tempProbability[i])):
                if "\n" in tempProbability[i][j]["letter"]:
                    words.append({"word": tempProbability[i][j]["letter"],"prob":tempProbability[i][j]["probalility"]})

        #prawdopodobieństwo końcowe
        for i in range(len(words)):
            for j in range(len(tempProbability)):
                for k in range(len(tempProbability[j])-1):
                    if tempProbability[j][k]["letter"] in words[i]["word"]:
                        words[i]["prob"]*=tempProbability[j][k]["probalility"]

        for i in range(len(words)):
            words[i]["prob"] *=100.0

        self.probability=words


    def createMatrix(self,start):
        for i in range(len(self.words)):
            word=list(self.words[i])
            for j in range(start,len(word)-1):
                self.matrixOfProbabilty[ord(word[j+1])-97][ord(word[j])-97]+=1
                break



markov=MarkovChain()
markov.readFile()
markov.splitWords()
markov.getProbalility("a")
markov.createMatrix(1)
print(markov.matrixOfProbabilty)