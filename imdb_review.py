# -*- coding: utf-8 -*-
"""IMDB Review.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UzYuCJJKpySke1sUOHNV4CX_cqrJD950
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/IMDB Dataset.csv')
df

df.shape

df.describe()

df.info()

df.isnull().sum()

sns.countplot(df['sentiment'])

df.dtypes

x = df["review"]
y = df["sentiment"]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.75)

x_train

x_test

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()

x_train_vect = vect.fit_transform(x_train)
x_train_vect

x_test_vect = vect.transform(x_test)
x_test_vect

"""SVC"""

from sklearn.svm import SVC

model1 = SVC()

model1.fit(x_train_vect,y_train)

y_pred1 = model1.predict(x_test_vect)
y_pred1

from sklearn.metrics import accuracy_score, precision_score, confusion_matrix

accuracy_score(y_test,y_pred1)

confusion_matrix(y_test,y_pred1)

"""SVC with PIPELINE"""

from sklearn.pipeline import make_pipeline

model2 = make_pipeline(CountVectorizer(),SVC())

model2.fit(x_train,y_train)

y_pred2 = model2.predict(x_test)
y_pred2

accuracy_score(y_test,y_pred2)

confusion_matrix(y_test,y_pred2)

"""Multinomial Naive Bayes"""

from sklearn.naive_bayes import MultinomialNB

model3 = MultinomialNB()

model3.fit(x_train_vect,y_train)

y_pred3 = model3.predict(x_test_vect)
y_pred3

accuracy_score(y_test,y_pred3)

confusion_matrix(y_test,y_pred3)

"""MultinomialNB with Pipeline

"""

model4 = make_pipeline(CountVectorizer(),MultinomialNB())

model4.fit(x_train,y_train)

y_pred4 = model4.predict(x_test)
y_pred4

accuracy_score(y_test,y_pred4)

confusion_matrix(y_test,y_pred4)

"""Joblib"""

import joblib

joblib.dump(model2,"IMDB_Review_Analysis")

"""Streamlit Deployment"""

!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile imdb_review.py
# import streamlit as st
# import joblib
# 
# reloaded_model = joblib.load("IMDB_Review_Analysis")
# 
# st.title("    IMDB MOVIE REVIEW       ")
# st.header("Model used for analysis is ")
# st.write(reloaded_model)
# 
# review = st.text_input("Write your review :  ")
# 
# if not review:
#   st.warning("Please give a review")
#   st.stop()
# st.success("Thank you giving a review")
# 
# output = reloaded_model.predict(review)
# 
# if st.button("Analyse"):
#   print(output[0])

#Run the streamlit webapp
!streamlit run imdb_review.py & npx localtunnel --port 8501

