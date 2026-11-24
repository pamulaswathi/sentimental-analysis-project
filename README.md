Project: Amazon Review Sentiment Analysis using NLP

S – Situation

"My project was Amazon Review Sentiment Analysis using Natural Language Processing.

Nowadays, customers share their experiences through online product reviews. However, manually analyzing thousands of reviews to understand customer opinions is time-consuming.

So, we wanted to build an automated system that could understand customer reviews and classify them into three categories: Positive, Negative, and Neutral."

T – Task

"My main responsibility was to develop an end-to-end NLP-based sentiment classification system.

I worked on the complete pipeline, including data preprocessing, exploratory data analysis, feature extraction, machine learning model development, model evaluation, and deployment.

The objective was to identify customer sentiment from review text and provide predictions through a user-friendly application."

A – Action

"First, I loaded the Amazon review dataset containing approximately more than 5000 records using Pandas. It consisted of three main columns: title, rating, and review body.

Since the dataset contained ratings instead of sentiment labels, I created a target column by mapping ratings 4 and 5 to Positive, rating 3 to Neutral, and ratings 1 and 2 to Negative.

Next, I performed Exploratory Data Analysis using Pandas, Matplotlib, and Seaborn. I checked missing values, duplicate records, rating distribution, sentiment distribution, and review lengths. I also identified Hindi reviews and translated them into English.

For text preprocessing, I combined the review title and body. Then I converted the text into lowercase, removed emojis, URLs, email IDs, numbers, special characters, and extra spaces. I also performed stopword removal and lemmatization using spaCy.

After preprocessing, I used CountVectorizer and WordCloud for analyzing frequently occurring words in different sentiment categories.

For model development, I used TF-IDF vectorization with a maximum of 5,000 features to convert text into numerical representations. I used LabelEncoder to convert sentiment labels into numerical values and divided the dataset into 80% training and 20% testing data.

I trained and compared three machine learning algorithms: Logistic Regression, Decision Tree, and Random Forest. I also used GridSearchCV for hyperparameter tuning of the tree-based models.

After comparing the test accuracies, Logistic Regression performed best, achieving approximately 80.9% accuracy.

Finally, I saved the trained model, TF-IDF vectorizer, and label encoder using Joblib and developed an interactive application using Streamlit. The application accepts customer reviews, translates the input into English when required, predicts the sentiment, and displays the result."

R – Result

"Finally, I successfully developed an end-to-end sentiment analysis application that automatically classifies customer reviews into Positive, Negative, and Neutral categories.

Through this project, I gained practical experience in NLP preprocessing, feature extraction, machine learning model comparison, and deploying an ML application using Streamlit."
