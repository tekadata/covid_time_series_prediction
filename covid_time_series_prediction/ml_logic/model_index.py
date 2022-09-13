import os
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV

def create_df_index(country):
    
    path = "../covid_time_series_prediction/data/data_raw_index"
    
    csv_path = os.path.join(path, f"data_{country}")
    
    country_index = pd.read_csv(csv_path, index_col=False)

    data_index = country_index['total_deaths'].copy()
    data_index = pd.DataFrame(data_index)
    
    data_index['day-1']=data_index['total_deaths'].shift(periods=1)
    data_index['day-2']=data_index['total_deaths'].shift(periods=2)
    data_index['day-3']=data_index['total_deaths'].shift(periods=3)
    data_index['day-4']=data_index['total_deaths'].shift(periods=4)
    data_index['day-5']=data_index['total_deaths'].shift(periods=5)
    data_index['day-6']=data_index['total_deaths'].shift(periods=6)
    data_index['day-7']=data_index['total_deaths'].shift(periods=7)
    data_index['day-8']=data_index['total_deaths'].shift(periods=8)
    data_index['day-9']=data_index['total_deaths'].shift(periods=9)
    data_index['day-10']=data_index['total_deaths'].shift(periods=10)
    data_index['day-11']=data_index['total_deaths'].shift(periods=11)
    data_index['day-12']=data_index['total_deaths'].shift(periods=12)
    data_index['day-13']=data_index['total_deaths'].shift(periods=13)
    data_index['day-14']=data_index['total_deaths'].shift(periods=14)
    data_index['day-15']=data_index['total_deaths'].shift(periods=15)

    columns_names = ['total_deaths']
    
    for day in range(1,data_index.shape[1]):
        columns_names.append(f'day-{day}')

    data_index.columns = columns_names
    
    data_index.drop(columns= 'total_deaths', inplace = True)

    y = country_index['total_deaths']
    X = country_index.copy()
    X = pd.concat([X, data_index], axis=1)
    X = X.drop(columns = ['Unnamed: 0','date','new_cases', 'new_deaths', 'total_deaths'])

    y = y[:-7]
    X = pd.DataFrame(X).dropna().reset_index(drop=True)
                       
    return  X, y 

def train_test_set_ml_index(country, days):
    
    X, y = create_df_index(country)
    
    train = int(((len(X)-days)))

    X_train = X[:train]
    y_train = y[:train]

    X_test = X[train:]
    y_test = y[train:]
    
    scaler = MinMaxScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, y_train, X_test_scaled, y_test

def model_ml_index(country, days):
    
    X_train, y_train, X_test, y_test = train_test_set_ml_index(country, days)
    
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