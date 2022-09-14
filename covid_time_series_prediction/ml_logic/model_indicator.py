import os
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV

def create_df_indicator(country):
    
    path = "../covid_time_series_prediction/data/data_raw"
    
    csv_path = os.path.join(path, f"data_{country}")
    
    country_indicator = pd.read_csv(csv_path, index_col=False)

    data_indicator = country_indicator['total_deaths'].copy()
    data_indicator = pd.DataFrame(data_indicator)
    #data_confirmed_deaths_days = pd.concat([data_confirmed_deaths_days,data_confirmed_deaths_days.shift(periods=1)], axis=1)
    #data_confirmed_deaths_days = pd.concat([data_confirmed_deaths_days,data_confirmed_deaths_days.shift(periods=2)], axis=1)
    #data_confirmed_deaths_days = pd.concat([data_confirmed_deaths_days,data_confirmed_deaths_days.shift(periods=4)], axis=1)
    
    data_indicator['day-1']=data_indicator['total_deaths'].shift(periods=1)
    data_indicator['day-2']=data_indicator['total_deaths'].shift(periods=2)
    data_indicator['day-3']=data_indicator['total_deaths'].shift(periods=3)
    data_indicator['day-4']=data_indicator['total_deaths'].shift(periods=4)
    data_indicator['day-5']=data_indicator['total_deaths'].shift(periods=5)
    data_indicator['day-6']=data_indicator['total_deaths'].shift(periods=6)
    data_indicator['day-7']=data_indicator['total_deaths'].shift(periods=7)
    data_indicator['day-8']=data_indicator['total_deaths'].shift(periods=8)
    data_indicator['day-9']=data_indicator['total_deaths'].shift(periods=9)
    data_indicator['day-10']=data_indicator['total_deaths'].shift(periods=10)
    data_indicator['day-11']=data_indicator['total_deaths'].shift(periods=11)
    data_indicator['day-12']=data_indicator['total_deaths'].shift(periods=12)
    data_indicator['day-13']=data_indicator['total_deaths'].shift(periods=13)
    data_indicator['day-14']=data_indicator['total_deaths'].shift(periods=14)
    data_indicator['day-15']=data_indicator['total_deaths'].shift(periods=15)

    columns_names = ['total_deaths']
    
    for day in range(1,data_indicator.shape[1]):
        columns_names.append(f'day-{day}')

    data_indicator.columns = columns_names
    
    data_indicator.drop(columns= 'total_deaths', inplace = True)

    y = country_indicator['total_deaths']
    X = country_indicator.copy()
    X = pd.concat([X, data_indicator], axis=1)
    X = X.drop(columns = ['Unnamed: 0','date','new_cases', 'new_deaths', 'total_deaths'])

    y = y[:-7]
    X = pd.DataFrame(X).dropna().reset_index(drop=True)
                       
    return  X, y 

def train_test_set_ml_indicator(country, days):
    
    X, y = create_df_indicator(country)
    
    train = int(((len(X)-days)))

    X_train = X[:train]
    y_train = y[:train]

    X_test = X[train:]
    y_test = y[train:]
    
    scaler = MinMaxScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, y_train, X_test_scaled, y_test

def model_ml_indicator(country, days):
    
    X_train, y_train, X_test, y_test = train_test_set_ml_indicator(country, days)
    
    model = SVR()
        
    param={'kernel' : ('linear', 'poly', 'rbf', 'sigmoid'),'C' : [1,5,10],'degree' : [2,3,5],
        'coef0' : [0.1,0.5,1],'gamma' : ('auto','scale')}

    grid_search = GridSearchCV(model, param_grid = param, scoring= 'neg_mean_absolute_percentage_error', 
                        cv = 2, n_jobs = -1, verbose = 2, refit=True)

    grid_search.fit(X_train,y_train)
    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    return best_model, best_params, best_score
