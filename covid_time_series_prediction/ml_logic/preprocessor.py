from covid_time_series_prediction.ml_logic.country_data import country_output

from sklearn.preprocessing import MinMaxScaler


def scaler(country):

    country_indicator = country_output(country)[1]

    X = country_indicator.drop(columns = ['date','new_cases', 'new_deaths', 'total_deaths'])

    y = country_indicator['total_deaths']

    scaler = MinMaxScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, y


def train_test_set(country, split_train=0.8, split_val=0):

    X, y = scaler(country)



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
