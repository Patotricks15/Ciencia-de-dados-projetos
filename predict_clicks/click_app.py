import pandas as pd
import streamlit as st
import numpy as np
from math import sqrt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/Patotricks15/Datasets/main/Datasets/advertising.csv')
df2 = df[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Clicked on Ad']]

X = df2[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']]
Y = df2['Clicked on Ad']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# user -> scaler -> model.predict
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)

#model = LogisticRegression()
model = RandomForestClassifier()
model.fit(X_train, Y_train)


st.markdown('# Predicting clicks on Ad')

Daily_Time_Spent_on_Site = st.slider('Daily Time Spent on Site (in minutes)',min_value=0, max_value=100)

Age =  st.slider('Age (in years)',min_value=18, max_value=120)

Area_Income = st.slider('Area Income (in dollars)',min_value=10000, max_value=100000)

Daily_Internet_Usage = st.slider('Daily Internet Usage (in minutes)',min_value=0, max_value=600)


user = scaler.transform(np.array([Daily_Time_Spent_on_Site,  Age,  Area_Income, Daily_Internet_Usage]).reshape(1,-1))


new_predict = model.predict_proba(user)
prob_click = new_predict[0][1]

st.write(f'The probability of the user click on ad is about:')
st.write(round(prob_click*100, 2)-1,'%')