import pandas as pd
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, GlobalMaxPooling1D, SpatialDropout1D
import numpy as np
class NeutralNetwork:
    words=[]
    encodedWord=None
    model_lstm=None
    def readData(self):
        file = open("words.txt", 'r')
        line = file.readline()
        while (line != ''):
            self.words.append(line[:len(line) - 1])
            line = file.readline()

    def encodedCharacters(self):
        results = np.zeros((len(self.words), 20, 27),dtype=int)
        for i in range (len(self.words)):
            for j in range(len(list(self.words[i]))):
                # Hash the word into a "random" integer index
                # that is between 0 and 1000
                index = ord(self.words[i][j])-96
                results[i, j, index] = 1
            for k in range(j+1,20):
                results[i, k, 0] = 1
        self.encodedWord=results

    def printEncoded(self):
        for i in range(len(self.encodedWord)):
            for j in range(len(self.encodedWord[i])):
                print(self.encodedWord[i][j])
            print("\n")

    def trainModel(self):
        self.model_lstm=Sequential()
        self.model_lstm.add(Dense(27, activation="relu", input_shape=(20,27)))
        #self.model_lstm.summary()
        self.model_lstm.compile(
            loss='categorical_crossentropy',
            optimizer='Adam',
            metrics=['mse']
        )
        self.model_lstm.fit(self.encodedWord,self.encodedWord,epochs=200,batch_size=20)


nn=NeutralNetwork()
nn.readData()
nn.encodedCharacters()
print(nn.printEncoded())
nn.trainModel()
