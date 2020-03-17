from PyQt5 import QtCore, QtWidgets

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 800, 300))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 400, 800, 300))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 300, 460, 100))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Generate Summary"))

        self.pushButton.clicked.connect(self.generateSummary)

    def generateSummary(self):
        text = self.textEdit.toPlainText()#input text
        words = word_tokenize(text)#tokenise wrt words
        sentences = sent_tokenize(text)#tokenise wrt sentence
        sWords = set(stopwords.words("english"))#all stopwords
        w_net = WordNetLemmatizer()#lemmatize

#stemming is used to reduce words to original form
#walks walked walking == walk (lemmatizer)
#Lemmatisation is closely related to stemming. The difference is that a stemmer operates on a single word without knowledge of the context, and therefore cannot discriminate between words which have different meanings depending on part of speech. However, stemmers are typically easier to implement and run faster, and the reduced accuracy may not matter for some applications.

        
        



        freq_dist = dict()

        for word in words:
            word = word.lower()

            if word in sWords:
                continue

            word = w_net.lemmatize(word, pos='v')

            if word in freq_dist:
                freq_dist[word] += 1
            else:
                freq_dist[word] = 1

        sent_dist = dict()

        for sentence in sentences:
            for word, freq in freq_dist.items():
                if word in sentence:
                    if sentence in sent_dist:
                        print("Word =>", word)
                        print("Sentence =>", sentence)
                        sent_dist[sentence] += freq
                    else:
                        print("Word =>", word)
                        print("Sentence =>", sentence)
                        sent_dist[sentence] = freq

        avg = int(sum(sent_dist.values()) / len(sent_dist))
        summary = ""
        for sentence in sentences:
            if sent_dist[sentence] > avg * 1.1:
                #         print(sentence)
                summary += " " + sentence

        self.textEdit_2.setText(summary)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())








"""I’ve been asked by a few friends to develop a feature for a
WhatsApp chatbot of mine, that summarizes articles based on
URL inputs. So when a friend sends an article to a WhatsApp
group, the bot will reply with a summary of the given URL
article. I like this feature because from my personal
research, 65% of group users don’t even click the shared URLs,
but 97% of them will read a few lines of the articles summary.
As part of being a Fullstack developer, it is important to
know how to choose the right stack for each product you
develop, depending on the requirements and limitations.
For web crawling, I love using Python. The Python community
is filled with efficient, easy to implement open source
libraries both for web crawling and text summarization.
Once you’re done with this tutorial, you won’t believe how
simple it is to implement the task."""
