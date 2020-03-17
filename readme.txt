TEXT-SUMMARIZER APP

Automatic Text Summarizer is a windows application made using python and PyQt5.
When user inputs article, paragraph or a long text, the application summarizes the text.
The application tokenizes each word and sentence and removes stopwords. 
Each word is lemmatized and frequency of each word is calculated and stored in a python dictionary. 
Then, frequency of each sentence is calculated as per the frequency of each word in sentence. 
Average frequency of sentences is calculated and sentences that have frequency more than the average frequency are included in the summary.
In this way, the application summarizes the text.

modules used
-nltk

 