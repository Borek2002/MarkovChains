import operator
from collections import defaultdict

end_of_sentence = "."

# parsing text file
with open("queries.txt", "r", encoding="utf8") as file:
    data = file.read()
sentences = data.lower().replace('[','').replace(']','').replace('!','.').replace('?','.').replace('“','').replace('\'','').replace('”','').replace('‘',' ').replace('-',' ').replace('’','').splitlines()
with open("dataset.txt", "w", encoding="utf8") as datafile:
    for sentence in sentences:
        if sentence[-1] != '.':
            sentence = " " + end_of_sentence
        else:
            sentence = sentence[:-1] + " " + end_of_sentence
        datafile.write("".join(sentence + '\n'))
with open ("dataset.txt", "r", encoding="utf8") as dataset:
    sentences = dataset.read().splitlines()

#dictionaries
first = {}
second = {}
third = {}
order = 5
test = ""
def update_occ(d, seq, w):
    if seq not in d:
        d[seq] = defaultdict(int)

    d[seq][w] = d[seq][w]+1

for s in sentences:
    words=s.replace(',',' ').split(" ")
    #words=remove_empty_words(words)

    if len(words)==0:
        continue
    for i in range(len(words)):
        # only two words available:
        if i >= 1:
            update_occ(first, words[i-1], words[i])
        # three words available:
        if i >= 2:
            update_occ(second, words[i-2]+" "+words[i-1], words[i])
        # four words available:
        if i >= 3:
            update_occ(third, words[i-3]+" "+words[i-2]+" "+words[i-1], words[i])
# printing dictionaries
# print ("first table:")
# for k in first:
#     print (k)
#     s=sorted(first[k].items(), key=operator.itemgetter(1), reverse=True)
#     print (s[:20])
#     print ("")
#
# print ("second table:")
# for k in second:
#     print (k)
#     s=sorted(second[k].items(), key=operator.itemgetter(1), reverse=True)
#     print (s[:20])
#     print ("")
#
# print ("third table:")
# for k in third:
#     print (k)
#     s=sorted(third[k].items(), key=operator.itemgetter(1), reverse=True)
#     print (s[:20])
#     print ("")

def mainFunc(text):
    test_words = text.split(" ")
    test_len = len(test_words)
    last_idx = test_len-1
    first_order_words, second_order_words, third_order_words = predictWords(test_len, test_words, last_idx)
    return first_order_words, second_order_words, third_order_words

def printStat(t):
    total = float(sum(t.values()))
    s = sorted(t.items(), key=operator.itemgetter(1), reverse=True)
    words_idx = len(s)

    if words_idx == 0:
        words_idx = 0
    elif words_idx > order:
        words_idx = order
    else:
        words_idx -= 1

    if words_idx <= 1:
        return s[0]
    else:
        return s[:words_idx]
def predictWords(test_len, test_words, last_idx):
    first_order_words = None
    second_order_words = None
    third_order_words = None
    if test_len>=3:
        tmp = test_words[last_idx-2]+" "+test_words[last_idx-1]+" "+test_words[last_idx]
        if tmp in third:
            third_order_words = printStat(third[tmp])

    if test_len>=2:
        tmp = test_words[last_idx-1]+" "+test_words[last_idx]
        if tmp in second:
            second_order_words = printStat(second[tmp])

    if test_len>=1:
        tmp = test_words[last_idx]
        if tmp in first:
            first_order_words = printStat(first[tmp])
    return first_order_words, second_order_words, third_order_words
mainFunc("she tried to")