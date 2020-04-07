# Text Summarizer App


_Automatic Text Summarizer_ is a windows application made using python and PyQt5.

**working :**

1. When user inputs article, paragraph or a long text, the application summarizes the text.
2. The application _tokenizes_ each word and sentence and removes _stopwords_. 
3. Each word is _lemmatized_ and _frequency of each word_ is calculated and stored in a python dictionary. 
4. Then, _frequency of each sentence_ is calculated as per the frequency of each word in sentence. 
5. _Average frequency of sentences_ is calculated and sentences that have frequency more than the average frequency are included in the summary.
In this way, the application summarizes the text.

**modules used**
-nltk

