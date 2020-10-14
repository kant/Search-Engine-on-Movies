
Here you will find the total coding steps leading to a precise search between a data set of 30 000 different movies that allow a user to find the ones he is looking for regarding to a genre, a topic, a date or whatever she wants. 

On the first step named collector.py, we have created our own dataset using the 30000 wikipedia URLs given. We have collected all the html pages in the folder Movies

On the second part : parser.py, we have used a function to transform the raw files form from HTML Wikipedia files to TSV files. We have extract specific informations from the HTML files (the title, the introduction, the plot, the urls and some infobox informations) of each ones. We used the MoviesTSV folder to store all the tsvs.

utils.py : on this python file there are some functions that we have used in the index.py and in the main.py files:
      - the preprocess function : this function sorts all our data. It has 3 features : the first one is to remove every punctuation and lower all characteres. The second one remove all the english stopwords (according to a predefine list), and the last one stem all the words. 
      - the computeTfidf function : this function create the tfidf by multiplied the compued tf and computed idf created with the mathematical formulas. 
      
in the index.py there is the code for building up and save the three dictionaries: vocabulary, indexDict and tfIdfIndexDict and other three dictionaries used for question 3.

in the main.py there are the three Search engines, where the third uses the euclidean distance to find the best movies to show. 


The exercise_4.py is a pyton code that finds the length of the longest palindromic substring of a string. We have used dynamic programming to resolve it. 

