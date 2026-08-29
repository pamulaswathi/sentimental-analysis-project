import streamlit as st
import joblib
from deep_translator import GoogleTranslator

# Load saved files
model = joblib.load("model.pkl")
tfidf = joblib.load("tfidf.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Page configuration
st.set_page_config(
    page_title="NLP Sentiment Analysis",
    page_icon="😊",
    layout="centered"
)

st.title("NLP Sentiment Analysis")
st.write("Analyze the sentiment of a customer review in any language.")
# User input
review = st.text_area(
    "Enter your customer review:",
    placeholder="Example: The product is excellent and I really love it!"
)
# Prediction button
if st.button("Predict Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a customer review.")

    else:
        try:
            #translate review to English
            translated_review = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(review)

            #display translated review
            st.write("**Translated Review:**")
            st.write(translated_review)

            #convert translated review into TF-IDF features
            review_tfidf = tfidf.transform([translated_review])

            #predict encoded sentiment
            prediction = model.predict(review_tfidf)

            #convert encoded label back to original sentiment
            sentiment = label_encoder.inverse_transform(prediction)[0]

            #display result
            st.subheader("Prediction")

            if sentiment.lower() == "positive":
                st.success(f"😊 {sentiment}")

            elif sentiment.lower() == "negative":
                st.error(f"😞 {sentiment}")

            elif sentiment.lower() == "neutral":
                st.info(f"😐 {sentiment}")

            else:
                st.info(sentiment)
                
        except Exception as e:
            st.error(f"Translation or prediction error: {e}")