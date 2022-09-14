import os
import pandas as pd

from covid_time_series_prediction.data import data_raw

from covid_time_series_prediction.ml_logic.country_data import country_output

from sklearn.preprocessing import MinMaxScaler


def scale_country(country):
    
    path = "../covid_time_series_prediction/data/data_raw"
    
    csv_path = os.path.join(path, f"data_{country}")
    
    country_indicator = pd.read_csv(csv_path)
    
    X = country_indicator.drop(columns = ['date','new_cases', 'new_deaths', 'total_deaths'])

    y = country_indicator['total_deaths']

    scaler = MinMaxScaler()

    X_scaled = scaler.fit_transform(X)


    return X_scaled, y


def scale_country_index(country):
    
    print("Hello new function here for index (of Sumedha)...")
    
    path = "../data/out_csv"
    
    csv_path = os.path.join(path, f"index_{country}.csv")
    
    country_indicator = pd.read_csv(csv_path)
    
    X = country_indicator.drop(columns = ['date','new_cases', 'new_deaths', 'total_deaths'])

    y = country_indicator['total_deaths']

    scaler = MinMaxScaler()

    X_scaled = scaler.fit_transform(X)


    return X_scaled, y


def train_test_set(country, split_train=0.8, split_val=0, switch_to_index=False):
    
    if switch_to_index == True:
        X, y = scale_country_index(country)
    else:
        X, y = scale_country(country)
    
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
