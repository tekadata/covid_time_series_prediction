import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def preprocessing(country):
    #countries=[]
    #path='data/out_csv'
    #for country in country_list:
    path=f'../data/out_csv/index_{country}.csv'
    df=pd.read_csv(path)
    df=df.set_index('date')
    df['day-1']=df['total_deaths'].shift(periods=1)
    df['day-2']=df['total_deaths'].shift(periods=2)
    df['day-3']=df['total_deaths'].shift(periods=3)
    df['day-4']=df['total_deaths'].shift(periods=4)
    df['day-5']=df['total_deaths'].shift(periods=5)
    df['day-6']=df['total_deaths'].shift(periods=6)
    df['day-7']=df['total_deaths'].shift(periods=7)
    df['day-8']=df['total_deaths'].shift(periods=8)
    df['day-9']=df['total_deaths'].shift(periods=9)
    df['day-10']=df['total_deaths'].shift(periods=10)
    df = df.iloc[10: , :]
    df=df.fillna(0)
    X=df.drop(columns=['total_deaths','new_deaths','new_cases'])
    y=df['total_deaths']
    scaler = MinMaxScaler()
    scaler.fit(X)
    X=scaler.transform(X)
    n = len(X)
    X_train = X[0:int(n-15)]
    X_test=X[int(n-15):]
    y_train=y[0:int(n-15)]
    y_test=y[int(n-10):]

    return X_test,y_test,X_train,y_train,df
