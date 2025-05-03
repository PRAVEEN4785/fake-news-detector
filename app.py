import streamlit as st
import joblib
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)

# Streamlit UI
st.title("📰 Fake News Detection App")
news_input = st.text_area("Enter News Content Here:")

if st.button("Predict"):
    cleaned = clean_text(news_input)
    vectorized = vectorizer.transform([cleaned])
    result = model.predict(vectorized)[0]
    label = "REAL" if result == 1 else "FAKE"
    st.success(f"The news is: **{label}**")
