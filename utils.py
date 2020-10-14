import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from math import log

def preprocess(string):
    #Removing punctuation and lower all characters
    wordsList = nltk.word_tokenize(string)
    wordsList = [word.lower() for word in wordsList if word.isalnum()]

    #Removing stop words
    stop_words = set(stopwords.words('english'))
    wordsList = [i for i in wordsList if i not in stop_words]

    #Reducing inflected words to their word stem : stemming
    stemmer = PorterStemmer()
    wordsList = [stemmer.stem(word) for word in wordsList]

    return wordsList

def computeTfIdf(wordId, listOfStrings, vocabulary, indexDictionary, allFiles = 30000):

    tf = listOfStrings.count(vocabulary[wordId]) / len(listOfStrings)  #computing tf

    idf = 1.0 + log( allFiles / len(indexDictionary[wordId])) #computing idf

    return tf * idf  #making the product to find the tfIdf
