#from inspect import CORO_SUSPENDED
from preprocessor import train_test_set

from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.model_selection import cross_val_score


def concat(country):
    
    n_days = 10
    
    data_confirmed_cases_days = train_test_set(country)[0]

    for n in range(2,n_days+1):
        data_confirmed_cases_days = pd.concat(
        [data_confirmed_cases,data_confirmed_cases.shift(periods=n)], axis=1)
        
    data_confirmed_cases_days.columns = ['confirmed_case','day-2','day-3','day-4','day-5','day-6','day-7','day-8','day-9','day-10']
                        
    return data_confirmed_cases_days

def model_ml(country):
    
    X_train, y_train, X_test, y_test = train_test_set(country)
    
    # Ridge Model
    ridge_model = Ridge()
    
    ridge_score = cross_val_score(ridge_model, X_train, y_train, cv=5, n_jobs=-1).mean()
    print(ridge_score)
    
    # Lasso Model 
    lasso_model = Lasso()
    
    lasso_score = cross_val_score(lasso_model, X_train, y_train, cv=5, n_jobs=-1).mean()
    print(lasso_score)
    
    # Linear Regression
    lin_reg_model = LinearRegression()
    
    lin_reg_score = cross_val_score(lin_reg_model, X_train, y_train, cv=5, n_jobs=-1).mean()
    print(lin_reg_score)
    
    return 
    
    
    