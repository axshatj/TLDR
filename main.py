import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget, QScrollArea
from newspaper import Article
from textblob import TextBlob


class ArticleSummarizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Article Summarizer")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def summarize(self):
        url = self.url_text.toPlainText().strip()
        self.url_text.clear()

        # Download, parse, and extract keywords from the article
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Set the extracted values in their respective QTextEdit widgets
        self.title.setPlainText(article.title)
        AU = ""
        if(len(article.authors)>0) :
            AU = article.authors[0]
        else:
            AU = "No author found"
        self.author.setPlainText(AU)
        self.summary.setPlainText(article.summary)

        # Perform sentiment analysis on the article's text
        analysis = TextBlob(article.text)
        polarity = analysis.polarity
        sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
        self.sentiment.setPlainText(f'Polarity: {polarity}, sentiment: {sentiment}')

    def close_application(self):
        self.close()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Title section
        title_label = QLabel("Title")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.title = QTextEdit()
        self.title.setFixedHeight(80)
        self.title.setDisabled(True)
        self.title.setStyleSheet("font-size: 16px; font-family: Arial; color: white; background-color: black;")
        layout.addWidget(self.title)

        # Author section
        author_label = QLabel("Author")
        author_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        author_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(author_label)

        self.author = QTextEdit()
        self.author.setFixedHeight(80)
        self.author.setDisabled(True)
        self.author.setStyleSheet("font-size: 16px; font-family: Arial; color: white; background-color: black;")
        layout.addWidget(self.author)

        # Summary section
        summary_label = QLabel("Summary")
        summary_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        summary_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(summary_label)

        scroll_area = QScrollArea()
        self.summary = QTextEdit()
        self.summary.setDisabled(True)
        self.summary.setStyleSheet("font-size: 16px; font-family: Arial; color: white; background-color: black;")
        scroll_area.setWidget(self.summary)
        scroll_area.setWidgetResizable(True)  # Make the widget inside scrollable
        layout.addWidget(scroll_area)

        # Sentiment section
        sentiment_label = QLabel("Sentiment")
        sentiment_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        sentiment_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(sentiment_label)

        self.sentiment = QTextEdit()
        self.sentiment.setFixedHeight(80)
        self.sentiment.setDisabled(True)
        self.sentiment.setStyleSheet("font-size: 16px; font-family: Arial; color: white; background-color: black;")
        layout.addWidget(self.sentiment)

        # URL section
        url_label = QLabel("URL")
        url_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        url_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(url_label)

        self.url_text = QTextEdit()
        self.url_text.setFixedHeight(80)
        self.url_text.setStyleSheet("font-size: 16px; font-family: Arial;")
        layout.addWidget(self.url_text)

        # Submit button
        btn = QPushButton("Submit")
        btn.setStyleSheet(
            "QPushButton {"
            "   min-width: 100px;"
            "   height: 40px;"
            "   font-size: 14px;"
            "   font-weight: bold;"
            "   background-color: #4CAF50;"
            "   color: white;"
            "   border-radius: 5px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #45a049;"
            "   cursor: pointer;"
            "}"
        )
        layout.addWidget(btn)

        btn.clicked.connect(self.summarize)  # Connect the clicked signal to the summarize function

        # Close button
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet(
            "QPushButton {"
            "   min-width: 100px;"
            "   height: 40px;"
            "   font-size: 14px;"
            "   font-weight: bold;"
            "   background-color: #f44336;"
            "   color: white;"
            "   border-radius: 5px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #d32f2f;"
            "   cursor: pointer;"
            "}"
        )
        layout.addWidget(close_btn)

        close_btn.clicked.connect(self.close_application)  # Connect the clicked signal to the close_application function

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArticleSummarizer()
    sys.exit(app.exec_())
