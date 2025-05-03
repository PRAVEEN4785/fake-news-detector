import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)

# Scrape article text from URL
def fetch_article_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return None

# Streamlit UI
st.title("📰 Real-Time Fake News Detection App")

tab1, tab2 = st.tabs(["✍️ Text Input", "🌐 URL Input"])

with tab1:
    news_input = st.text_area("Enter News Content Here:")
    if st.button("Predict from Text"):
        cleaned = clean_text(news_input)
        vectorized = vectorizer.transform([cleaned])
        result = model.predict(vectorized)[0]
        label = "REAL ✅" if result == 1 else "FAKE ❌"
        st.success(f"The news is: **{label}**")

with tab2:
    url_input = st.text_input("Paste a News Article URL:")
    if st.button("Fetch & Predict from URL"):
        article_text = fetch_article_from_url(url_input)
        if article_text:
            cleaned = clean_text(article_text)
            vectorized = vectorizer.transform([cleaned])
            result = model.predict(vectorized)[0]
            label = "REAL ✅" if result == 1 else "FAKE ❌"
            st.success(f"The news is: **{label}**")
            st.markdown("### Article Preview:")
            st.info(article_text[:1000] + ("..." if len(article_text) > 1000 else ""))
        else:
            st.error("Failed to fetch or parse article from the URL.")

