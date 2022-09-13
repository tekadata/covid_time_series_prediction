import pandas as pd
import numpy as np

from covid_time_series_prediction.ml_logic.preprocessor import scaler

from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import GridSearchCV

import xgboost as xgb


def concat(country):
    
    X, y = scaler(country)
    data_confirmed_cases_days = X['total_cases']

    data_confirmed_cases_days = pd.concat([data_confirmed_cases_days,data_confirmed_cases_days.shift(periods=1)], axis=1)
    data_confirmed_cases_days = pd.concat([data_confirmed_cases_days,data_confirmed_cases_days.shift(periods=2)], axis=1)
    data_confirmed_cases_days = pd.concat([data_confirmed_cases_days,data_confirmed_cases_days.shift(periods=4)], axis=1)

    columns_names = ['confirmed_case']

    for day in range(1,data_confirmed_cases_days.shape[1]):
        columns_names.append(f'day-{day}')

    data_confirmed_cases_days.columns = columns_names

    X_new = X.merge(data_confirmed_cases_days, on='total_cases')

    X_new = X_new.dropna().reset_index(drop=True)
                        
    return X_new, y

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
    
    model_xgb = XGBRegressor(max_depth=10, n_estimators=300, learning_rate=0.1)

    model_xgb.fit(X_train, y_train,
            verbose=True,
            eval_set=[(X_train, y_train), (X_test, y_test)],
            eval_metric=["rmse"],
            early_stopping_rounds=10)

    # retrieve performance metrics
    results = model_xgb.evals_result()
    epochs = len(results['validation_0']["rmse"])
    x_axis = range(0, epochs)

    # plot rmsle loss
    fig, ax = plt.subplots()
    ax.plot(x_axis, results['validation_0']['rmse'], label='Train')
    ax.plot(x_axis, results['validation_1']['rmse'], label='Val')
    ax.legend(); plt.ylabel('RMSE (of log)'); plt.title('XGBoost Log Loss')

    print("Best Validation Score", min(results['validation_1']['rmse']))
    
    gsc = GridSearchCV(
            estimator=xgb.XGBRegressor(),
            param_grid={"learning_rate": (0.05, 0.10, 0.15),
                        "max_depth": [ 3, 4, 5, 6, 8],
                        "min_child_weight": [ 1, 3, 5, 7]},
            cv=3, scoring='neg_mean_squared_error', verbose=0, n_jobs=-1)

    grid_result = MultiOutputRegressor(gsc).fit(X_train, y_train)
    
    return grid_result.best_params_
