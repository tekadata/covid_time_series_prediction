import os
import pandas as pd
import streamlit as st
from covid_time_series_prediction.prediction import predict
from covid_time_series_prediction.ml_logic.sumedha_preprocessing import preprocessing



primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

st.markdown(
    '''
    #        HELLO !
    '''
    '''
    #        Welcome to COVID-19 Prediction App !
    '''



    '''
    ##### Our COVID-19 prediction models for TOTAL NUMBER OF DEATHS on next 10 days were based on restriction indicators, stringency index, and vaccination campaigns



    They were performed by Alberto, Sumedha, Thomas, and Kim under supervision of Arnaud and TAs


    ''')



option=st.selectbox('PLEASE SELECT YOUR COUNTRY',

('Brazil', 'France', 'India', 'Mexico', 'United Kingdom'))


st.write('YOU SELECTED:', option)



# if country_code = 'Brazil':
# if country_code = 'France'
# if country_code = 'India'
# if country_code = 'Mexico'
# if country_code = 'United Kingdom'

# prediction_window = 1st to 10th september 2022

country_list=['Brazil','France', 'India', 'Mexico', 'United Kingdom']
countries=[]


#path_begin= f'data/out_csv/index_{option}.csv'

# csv_name = f'index_{option}.csv'
# csv_path = os.path.join(path_begin, csv_name)

X_test,y_test,X_train,y_train,df,y= preprocessing(option)
date_prediction=['2022/09/01', '2022/09/02', '2022/09/03', '2022/09/04', '2022/09/05'
'2022/09/06', '2022/09/07', '2022/09/08', '2022/09/09', '2022/09/10']

list_pred,X_predict=predict(X_test=X_test, country=option.capitalize(), data=df, y=y)

st.line_chart(data=[y_test, list_pred], x=date_prediction)




# plot the predicted and real total deaths by COVID-19
# find csv
# read csv
# preprocess csv with Sumedha process
# predict the X_predict(dataframe)
