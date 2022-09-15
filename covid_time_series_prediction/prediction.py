import pickle
import pandas as pd
import numpy as np

def predict(X_test,country,data,y_train):
    path=f'/data/models'
    model=pickle.load(open(f'{path}/model_{country}.pkl','rb'))
    X_test_columns=data.drop(columns=['total_deaths','new_cases','new_deaths'])
    X_test_columns.columns
    X_test_df=pd.DataFrame(X_test,columns=X_test_columns.columns)
    X_predict=X_test_df.tail(10)
    X_predict=X_predict.reset_index(drop=True)
    for i in range(1,10):
        X_predict.loc[i,'containment_and_health':'total_boosters']=X_predict.loc[0,'containment_and_health':'total_boosters']
    min_num=min(y_train)
    max_num=max(y_train)
    list_pred=[]
    list_pred_scale=[]
    for k in range(0,9):
        y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[k]).T))
        y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
        list_pred.append(y_pred_)
        list_pred_scale.append(y_pred_scale)

    for j in range(1,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[0]
    for j in range(2,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[1]
    for j in range(3,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[2]
    for j in range(4,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[3]

    for j in range(5,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[4]
    for j in range(6,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[5]
    for j in range(7,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[6]
    for j in range(8,9):
        X_predict.loc[j,f'day-{j}']=list_pred_scale[8]
    return list_pred,X_predict,
