import os
import streamlit as st
from covid_time_series_prediction import predict




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

('BRAZIL', 'FRANCE', 'INDIA', 'MEXICO', 'UNITED KINGDOM'))


st.write('YOU SELECTED:', option)



# if country_code = 'Brazil':
# if country_code = 'France'
# if country_code = 'India'
# if country_code = 'Mexico'
# if country_code = 'United Kingdom'

# prediction_window = 1st to 10th september 2022

country_list=['Brazil','France', 'India', 'Mexico', 'United Kingdom']
countries=[]


path_begin='/root/code/bkyan69/Teki-Teka/covid_time_series_prediction/data/out_csv'

csv_name = f'index_{option}.csv'
csv_path = os.path.join(path_begin, csv_name)
X_test, data, y, = sumedha_function((csv_path))
date_prediction=['2022/09/01', '2022/09/02', '2022/09/03', '2022/09/04', '2022/09/05'
'2022/09/06', '2022/09/07', '2022/09/08', '2022/09/09', '2022/09/10']



list_pred,X_predict=predict(X_test=?, country=option.capitalize(), data= ?, y=? )

st.line_chart(data=[y_test, list_pred] *, x=None, y=None, width=0, height=0, use_container_width=True)




# plot the predicted and real total deaths by COVID-19
# find csv
# read csv
# preprocess csv with Sumedha process
# predict the X_predict(dataframe)
