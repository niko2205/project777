import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


# Загружаем модель
model = joblib.load('model.pkl')


def predict_loan_amount(data):
    # Преобразуем категориальные признаки в числовые
    data = pd.get_dummies(data, columns=['citizenship'])
    
    # Предсказываем сумму кредита
    loan_amount = model.predict(data)
    
    return loan_amount


# Заголовок приложения
st.title('Расчет потребительского кредита')

# Ввод данных пользователем
age = st.number_input('Возраст', min_value=18, max_value=80)
gender = st.selectbox('Пол', ['Мужской', 'Женский'])
citizenship = st.selectbox('Гражданство', ['Россия', 'Украина', 'Казахстан'])
income = st.number_input('Зарплата', min_value=0)
employment_status = st.selectbox('Статус занятости', ['Работаю', 'Неработаю'])
marital_status = st.selectbox('Семейное положение', ['Женат/Замужем', 'Холост'])
children = st.number_input('Количество детей', min_value=0, max_value=10)

# Сбор данных для предсказания
user_data = {
    'age': age,
    'gender_Male': int(gender == 'Мужской'),
    'citizenship_Russia': int(citizenship == 'Россия'),
    'citizenship_Ukraine': int(citizenship == 'Украина'),
    'citizenship_Kazakhstan': int(citizenship == 'Казахстан'),
    'income': income,
    'employment_status_Employed': int(employment_status == 'Работаю'),
    'employment_status_Unemployed': int(employment_status == 'Неработаю'),
    'marital_status_Married': int(marital_status == 'Женат/Замужем'),
    'marital_status_Single': int(marital_status == 'Холост'),
    'children': children
}

# Предсказание суммы кредита
loan_amount = predict_loan_amount(pd.DataFrame([user_data]))

# Вывод результата
st.write(f"Предполагаемая сумма кредита: {loan_amount[0]:,.0f} руб.")
