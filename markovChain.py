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
            self.words.append(line[:len(line)-1])
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


    #generowanie macierzy prawdopodobieństwa dla konretnej głębokości i stanu
    def createMatrix(self,start,letter,word):
        self.matrixOfProbabilty = [[0 for i in range(26)] for j in range(26)]
        for i in range(len(self.words)):
            if(word in self.words[i]):
                wordSplit=list(self.words[i])
                if(start+1>=len(wordSplit)-1 and start>=len(wordSplit)-1):
                    continue
                for j in range(start,start+1):
                    if(wordSplit[j]==letter):
                        self.matrixOfProbabilty[ord(wordSplit[j+1])-97][ord(wordSplit[j])-97]+=1
                        break
        total = sum([sum(row) for row in self.matrixOfProbabilty])
        for i in range(len(self.matrixOfProbabilty)):
            for j in range(len(self.matrixOfProbabilty[i])):
                if(self.matrixOfProbabilty[i][j]!=0):
                    self.matrixOfProbabilty[i][j]/=total


    def getTheMostLikelyWord(self,start,letter):
        theMostLikelyWord=letter
        self.createMatrix(start,letter,letter)
        maxValue=-2
        while(maxValue!=-1):
            index=-1
            maxValue = -1
            for i in range(len(self.matrixOfProbabilty)):
                if(self.matrixOfProbabilty[i][ord(letter)-97]>maxValue and self.matrixOfProbabilty[i][ord(letter)-97]!=0):
                    maxValue=self.matrixOfProbabilty[i][ord(letter)-97]
                    index=i
            newLetter=""
            if(index!=-1):
                newLetter=chr(index+97)
                theMostLikelyWord+=newLetter
            start+=1
            self.createMatrix(start,newLetter,theMostLikelyWord)
            self.printMatrix(self.matrixOfProbabilty)
            letter=newLetter
            print(theMostLikelyWord)


    @staticmethod
    def printMatrix(matrix):
        print()
        for i in range(len(matrix)):
            print(matrix[i])


markov=MarkovChain()
markov.readFile()
markov.splitWords()
markov.getProbalility("a")


markov.createMatrix(4,"t","t")
matrix3=markov.matrixOfProbabilty
#MarkovChain.printMatrix(markov.matrixOfProbabilty)
markov.getTheMostLikelyWord(0,"a")
