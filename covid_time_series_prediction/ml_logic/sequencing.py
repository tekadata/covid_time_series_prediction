import numpy as np
import pandas as pd
from covid_time_series_prediction.ml_logic.preprocessor import train_test_set, scaler

def subsample_sequence(X, y, X_len, y_len) -> pd.DataFrame:
    """
    Given the initial dataframe `df`, return a shorter dataframe sequence of length `length` (eg n_obs).
    This shorter sequence should be selected at random
    """
    last_possible = X.shape[0] - X_len - y_len
    # How to split sequences? we could do it manually...
    random_start = np.random.randint(0, last_possible)
    # X start and y end
    X_sample = X[random_start : random_start + X_len]
    y_sample = y[random_start : random_start + X_len + y_len]
    
    return np.array(X_sample), np.array(y_sample)

def get_X_y(X, y, X_len, y_len, n_sequences) -> tuple:
    '''Return a list of samples (X, y)'''
    X_list, y_list = [], []

    for i in range(n_sequences):
        # print('X_len', X_len, 'y_len', y_len)
        (xi, yi) = subsample_sequence(X, y, X_len=X_len, y_len=y_len)
        X_list.append(xi)
        y_list.append(yi)
        
    X = np.array(X_list)
    y = np.array(y_list)

    return X, y