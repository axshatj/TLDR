import streamlit as st
from newspaper import Article
from textblob import TextBlob

def summarize():
    url = st.text_input("Enter URL")
    if st.button("Submit"):
        # Download, parse, and extract keywords from the article
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Set the extracted values in the UI
        st.subheader("Title")
        st.text(article.title)

        st.subheader("Author")
        if len(article.authors) > 0:
            st.text(article.authors[0])
        else:
            st.text("No author found")

        st.subheader("Summary")
        st.text(article.summary)

        # Perform sentiment analysis on the article's text
        analysis = TextBlob(article.text)
        polarity = analysis.polarity
        sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"

        st.subheader("Sentiment")
        st.text(f'Polarity: {polarity}, sentiment: {sentiment}')

def main():
    st.title("Article Summarizer")
    summarize()

if __name__ == "__main__":
    main()
