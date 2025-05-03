# fake-news-detector
# 📰 Fake News Detection App

A machine learning-powered web app that detects whether a news article is **real** or **fake**, built using Python, NLP, and Streamlit.

## 🔍 Features
- Takes user input of news content
- Cleans and processes text using NLP
- Uses a trained ML model to predict authenticity
- Simple and clean web interface

## 🚀 Tech Stack
- Python
- Scikit-learn (PassiveAggressiveClassifier)
- NLTK for text preprocessing
- TfidfVectorizer for feature extraction
- Streamlit for web UI
- Joblib for saving/loading the model

## 📦 Setup Instructions

1. Clone the repo or download the files.
2. Make sure you have Python 3.8+ installed.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4.Add your trained model.pkl and vectorizer.pkl to the project folder.

5.Run the app locally:
 streamlit run app.py
🌐 Deploy on Streamlit Cloud
Push the files to a public GitHub repository.

Go to https://streamlit.io/cloud

Click "New App" and connect your repo.

Set the entry file to app.py and deploy!
📚 Dataset
Dataset used: Fake and Real News Dataset (Kaggle)
🧠 Model Training
Train your model using train_model.py script:

python train_model.py
This generates the model.pkl and vectorizer.pkl files needed for the app.

