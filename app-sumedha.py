import streamlit as st
from covid_time_series_prediction.ml_logic.sumedha_prep import preprocessing
from covid_time_series_prediction.prediction import predict
import matplotlib.pyplot as plt
#st.write("Hello ,let's learn how to build a streamlit app together")
#st.title ("Welcome to COVID-19 Prediction App !")
st.markdown( '''
    #        HELLO !
    '''
    '''
    #        Welcome to COVID-19 Prediction App !
    '''



    '''
    ##### In Our COVID-19 prediction model , we are predicting TOTAL NUMBER OF DEATHS for the next 10 days. This is based on restriction indicators, stringency index and vaccination campaigns.



    This was developed by Alberto, Sumedha, Thomas and Kim under the supervision of Arnaud and TAs


    ''')

option=st.selectbox('PLEASE SELECT YOUR COUNTRY',

('Brazil', 'France','Mexico','Spain','Russia'))


st.write('YOU SELECTED:', option)


country_list=['Brazil','France', 'Mexico','Spain','Russia']
path_begin='data/out_csv/index_Brazil.csv'
X_test,y_test,X_train,y_train,df,y = preprocessing(option.capitalize())
date_prediction=['2022/09/01', '2022/09/02', '2022/09/03', '2022/09/04', '2022/09/05'
'2022/09/06', '2022/09/07', '2022/09/08', '2022/09/09', '2022/09/10']
list_pred,X_predict=predict(X_test=X_test, country=option, data=df, y=y)

#st.line_chart(data=[y_test.tolist(), list_pred], x=y_test.index.tolist())

fig, ax = plt.subplots(1, figsize=(17,7))
plt.plot(y_test.index,list_pred,color='r');
plt.plot(y_test.index,y_test);
ax.set_title("Covid 19 calculation for different countries", size=10)
ax.set_ylabel("Number of death cases", size=10)
ax.set_xlabel("Date", size=13)
st.pyplot(fig)
