import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.svm import SVR
import grid_search_SVR as sv



def model(params):
    model=SVR(params)
    return model

def fit_model(X_train,y_train):
    model.fit(X_train,y_train)
    return model
