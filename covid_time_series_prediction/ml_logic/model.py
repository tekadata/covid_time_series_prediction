import os
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler

def concat(country):
    
    path = "../covid_time_series_prediction/data/data_raw"
    
    csv_path = os.path.join(path, f"data_{country}")
    
    country_indicator = pd.read_csv(csv_path)

    X = country_indicator.drop(columns = ['date','new_cases', 'new_deaths', 'total_deaths'])
    y = country_indicator['total_deaths']

    data_confirmed_cases_days = X['total_cases']
    data_confirmed_cases_days = pd.concat([data_confirmed_cases_days,data_confirmed_cases_days.shift(periods=1)], axis=1)
    data_confirmed_cases_days = pd.concat([data_confirmed_cases_days,data_confirmed_cases_days.shift(periods=2)], axis=1)
    data_confirmed_cases_days = pd.concat([data_confirmed_cases_days,data_confirmed_cases_days.shift(periods=4)], axis=1)

    columns_names = ['total_cases']

    for day in range(1,data_confirmed_cases_days.shape[1]):
        columns_names.append(f'day-{day}')

    data_confirmed_cases_days.columns = columns_names

    X = X.merge(data_confirmed_cases_days, on='total_cases')

    scaler = MinMaxScaler()

    X_scaled = scaler.fit_transform(X)

    X_scaled = pd.DataFrame(X_scaled).dropna().reset_index(drop=True)
                       
    return X_scaled, y

def train_test_set_ml(country, split_train=0.8, split_val=0):
    
    X, y = concat(country)
    
    train = int((len(X)*split_train))
    val = int(len(X)*split_val)

    X_train = X[:train]
    y_train = y[:train]
    
    if split_val <= split_train:  
        X_test = X[train:]
        y_test = y[train:]
        return X_train, y_train, X_test, y_test
    
    X_val = X[train:val]
    y_val = y[train:val]

    X_test = X[val:]
    y_test = y[val:]
    
    return X_train, y_train, X_val, y_val, X_test, y_test

def model_ml(country):
    
    X_train, y_train, X_test, y_test = train_test_set_ml(country)
    
    model = SVR(C=1, coef0=10, degree=8, epsilon=0.05, gamma='auto', kernel='poly')
    
    model = model.fit(X_train, y_train)
               
    return model 
