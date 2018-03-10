import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

data = "Potholes have been causing a lot of inconvenience in Bangalore, there has already been a lot of accidents in the place bacause of these potholes. Please look into this matter."
# print(word_tokenize(data))

tokenizer = RegexpTokenizer(r'\w+')
# tokenizer.tokenize(data)

stopWords = set(stopwords.words('english'))
words = tokenizer.tokenize(data)
wordsFiltered = []
 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print (wordsFiltered)

stemWords = []
ps = PorterStemmer()
 
for word in wordsFiltered:
    stemWords.append(ps.stem(word))

# print (stemWords)












