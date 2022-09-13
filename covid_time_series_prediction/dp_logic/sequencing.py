import numpy as np
import pandas as pd
from covid_time_series_prediction.ml_logic.preprocessor import train_test_set, scaler

def subsample_sequence(X, y, X_len, y_len) -> pd.DataFrame:
    """
    Given the initial arrays `X` and `y`, return shorter array sequences.
    This shorter sequence should be selected at random
    """
    X_y_len = X_len + y_len
    # print('X_len', X_len,  'y_len',   y_len)
    # print('X.shape[0]', X.shape[0], ' >= X_y_len ', X_y_len)
    if X.shape[0] >= X_y_len:
        last_possible = X.shape[0] - X_y_len
    else:
        last_possible = X.shape[0]
        # print('X_y_len = ?', X.shape[0])
    random_start = np.random.randint(0, last_possible)
    # X start and y end
    X_sample = X[random_start : random_start + X_len]
    y_sample = y[random_start + X_len : (random_start + X_y_len)]
    # print("X[random_start : random_start + X_len]   -> ", f"X[{random_start} : {random_start + X_len}]")
    # print("y[random_start : random_start + X_y_len] -> ", f"y[{random_start} : {(random_start + X_y_len)}]")
    
    return np.array(X_sample), np.array(y_sample)


def get_X_y(df, n_sequences, length, feature='VNM') -> tuple:
    '''Return a list of samples (`X`,`y`)'''
    X, y = [], []

    for i in range(n_sequences):
        (xi, yi) = split_subsample_sequence(df, length, feature=feature)
        X.append(xi)
        y.append(yi)
        
    X = np.array(X)
    y = np.array(y)

    return X, y


def get_X_y_2(X, y, X_len, y_len, n_sequences) -> tuple:
    '''Return a list of samples (X, y)'''
    X_list, y_list = [], []

    for i in range(n_sequences):
        (xi, yi) = subsample_sequence(X, y, X_len=X_len, y_len=y_len)
        X_list.append(xi)
        y_list.append(yi)
        
    X = np.array(X_list)
    y = np.array(y_list)

    return X, y

