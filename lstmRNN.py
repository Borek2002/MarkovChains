import pickle

import pandas as pd
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tensorflow import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, GlobalMaxPooling1D, SpatialDropout1D, TimeDistributed
import numpy as np


class NeutralNetwork:
    words = []
    encodedWord = None
    wordsInInt = None
    model_lstm = None
    xtrain = None
    ytrain = None
    MAX_LENGTH = 16

    def readData(self):
        file = open("words.txt", 'r')
        line = file.readline()
        while (line != ''):
            self.words.append(line[:len(line) - 1])
            line = file.readline()

    def encodedCharacters(self):
        results = np.zeros((len(self.words), 20, 27), dtype=int)
        for i in range(len(self.words)):
            for j in range(len(list(self.words[i]))):
                # Hash the word into a "random" integer index
                # that is between 0 and 1000
                index = ord(self.words[i][j]) - 96
                results[i, j, index] = 1
            for k in range(j + 1, 20):
                results[i, k, 0] = 1
        self.encodedWord = results

    def wordToIntWithZero(self):
        self.wordsInInt = []
        for w in self.words:
            if (len(list(w)) < self.MAX_LENGTH):
                word = [0] * self.MAX_LENGTH
                for j in range(len(list(w))):
                    word[j] = ord(w[j]) - 96
                self.wordsInInt.append(word)

        self.xtrain = []
        self.ytrain = []

        for x in range(len(self.wordsInInt)):
            letters = []
            for y in range(2, self.MAX_LENGTH + 1):
                self.xtrain.append(self.wordsInInt[x][:y] + [0] * (self.MAX_LENGTH - y))
                self.ytrain.append(self.wordsInInt[x])

    def trainModel(self):
        self.model_lstm = tf.keras.Sequential()

        self.model_lstm.add(LSTM(units=27 * 2, input_shape=(self.MAX_LENGTH, 27),
                                 dropout=0.2, recurrent_dropout=0.2, use_bias=True, return_sequences=True,
                                 activation="relu"))
        self.model_lstm.add(TimeDistributed(Dense(units=27, activation="softmax")))
        self.model_lstm.summary()

        one_hot_resultX = tf.one_hot(self.xtrain, depth=27)
        one_hot_resultY = tf.one_hot(self.ytrain, depth=27)
        one_hot_resultX = tf.reshape(one_hot_resultX, (-1, self.MAX_LENGTH, 27))
        one_hot_resultY = tf.reshape(one_hot_resultY, (-1, self.MAX_LENGTH, 27))

        self.model_lstm.compile(
            loss='categorical_crossentropy',
            optimizer='Adam',
            metrics=['mse']
        )

        self.model_lstm.fit(one_hot_resultX, one_hot_resultY, epochs=250, batch_size=32, shuffle=True)

    def predict(self, letters):
        letter_indices = [ord(letter) - 96 for letter in letters]
        letter_indices += [0] * (nn.MAX_LENGTH - len(letter_indices))
        input_data = np.array(letter_indices)
        input_data = input_data.reshape((1, nn.MAX_LENGTH, 1))  # Reshape the input to match the model's input shape

        one_hot_resultX = tf.one_hot(input_data, depth=27)
        input_data = tf.reshape(one_hot_resultX, (-1, nn.MAX_LENGTH, 27))

        predictions = nn.model_lstm.predict(input_data)
        argmax_result = tf.argmax(predictions, axis=-1)
        array_sync_result = argmax_result.numpy()  # Convert TensorFlow tensor to NumPy array

        print(array_sync_result)
        i = len(list(letters))
        while (array_sync_result[0][i] != 0):
            letters += str(chr(array_sync_result[0][i] + 96))
            i += 1
        return letters


nn = NeutralNetwork()
nn.readData()
# nn.wordToIntWithZero()
# nn.encodedCharacters()
# print(nn.xtrain[0])
# print(nn.wordsInInt[0])
# nn.trainModel()
filename = 'finalized_model.sav'
# pickle.dump(nn.model_lstm, open(filename, 'wb'))
letters = "ack"
nn.model_lstm = pickle.load(open(filename, 'rb'))

letters = nn.predict(letters)
print(letters)
