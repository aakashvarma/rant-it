import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import PunktSentenceTokenizer

data = "guess who thinks keeping super bright hording screens in VIT Vellore at night is a good idea? new hording screens in VIT Vellore would be nice if they are less bright. riviera 2018 held at VIT Vellore was lit. hording screens at VIT Vellore looks good in the afternoon"
# print(word_tokenize(data))

tokenizer = RegexpTokenizer(r'\w+')
# tokenizer.tokenize(data)

stopWords = set(stopwords.words('english'))
words = tokenizer.tokenize(data)
wordsFiltered = []
 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
# print (wordsFiltered)


tagged = nltk.pos_tag(wordsFiltered)
# print (tagged)

#############################################################################

sentences = nltk.sent_tokenize(data)   
 
d = []
for sent in sentences:
    d = d + nltk.pos_tag(nltk.word_tokenize(sent))
 
for word in d: 
    if 'NN' in word[1]: 
        print(word)

#############################################################################














