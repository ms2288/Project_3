from flask import Flask, render_template
import requests
import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect('house.db', check_same_thread=False)
cur = conn.cursor()

# query = "SELECT *  FROM HouseData"
# df = pd.read_sql(query, conn)

app = Flask(__name__)
# print(df['ID'])


# @app.route('/')
# def index():
#     return render_template('index.html')


SGG_NM = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '금천구', '영등포구', '은평구', '양천구',
          '강북구', '강서구', '도봉구', '노원구', '강남구', '서초구', '송파구', '구로구', '강동구', '동작구', '서대문구', '마포구', '관악구']
SGG_NM_AVG = list()
SGG_NM_EXP = list()


@app.route('/')
def check():
    all_features = ['RENT_AREA', 'CNTRCT_YEAR', 'BUILD_YEAR', 'RENT_GTN']
    features = ['RENT_AREA', 'CNTRCT_YEAR', 'BUILD_YEAR']
    target = ['RENT_GTN']
    for i in range(len(SGG_NM)):
        RENT_CASE_NM = '전세'
        query = f"""
                SELECT * 
                FROM HouseRentPriceInfo 
                WHERE SGG_NM='{SGG_NM[i]}' AND
                RENT_CASE_NM='{RENT_CASE_NM}';
                """
        df = pd.read_sql(query, conn)
        df = df[all_features].apply(pd.to_numeric)
        df = df.dropna(axis=0)
        mean = int(df[target].mean())
        SGG_NM_AVG.append(mean)
        x_train = df[features]
        y_train = df[target]
        model = LinearRegression()
        model.fit(x_train.values, y_train.values)
        input_data = [[df['RENT_AREA'].mean(), 2022, df['BUILD_YEAR'].mean()]]
        exp = int(model.predict(input_data)[0][0])
        SGG_NM_EXP.append(exp)
    return render_template('index.html', AVG=SGG_NM_AVG, EXP=SGG_NM_EXP)
