# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:56:27 2019

One-hot encoding

@author: jae woong Han
"""

import pandas as pd
from math import sqrt
from sklearn.preprocessing import LabelEncoder
journey = pd.read_csv('./disposition.csv', encoding='euc-kr')


# 사용자들의 여행 성향
journey.head()

# 변수에 대한 유형
journey.dtypes

# 숫자형 데이터만 인식
journey.describe()

# 성별 분석
journey['sex'].value_counts()

#성별 명목형에서 수치형으로 변환
journey.loc[journey["sex"] == "남성", "sex"] = 0
journey.loc[journey["sex"] == "여성", "sex"] = 1

# Q1에 대한 분류
journey['Q1'].value_counts()

journey_copy = journey.copy()
journey_copy.head()

def dummy_data(data, columns) :
    for column in columns:
        data = pd.concat([data, pd.get_dummies(data[column], prefix = column)], axis=1)
        data = data.drop(column, axis=1)
    return data

dummy_columns = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]
journey_dummy = dummy_data(journey_copy, dummy_columns)

print('원핫인코딩 전')
print(journey.shape)

print('원핫인코딩 후')
print(journey_dummy.shape)


# Save
journey_dummy.to_csv('./ditribution.csv', sep=',', encoding='euc-kr')