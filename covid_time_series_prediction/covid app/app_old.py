import streamlit as st

from covid_time_series_prediction import prediction




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




country_list=['Brazil','France', 'India', 'Mexico', 'United Kingdom']
countries=[]


for country in country_list:
    path=f'../data/out_csv/index_{country}.csv'
    df=pd.read_csv(path)
    countries=[{'name':country,'df':df}]
# countries[0]['name']


model=pickle.load(open(f'{path}/model_{country}.pkl','rb'))

data_index=pd.read_csv(path)
data_index=data_index.set_index('date')

best_params=[]
best_score=[]
best_df={}
for country in countries:
    df=country['name']
    df=country['df']
    df=df.set_index('date')
    df['day-1']=df['total_deaths'].shift(periods=1)
    df['day-2']=df['total_deaths'].shift(periods=2)
    df['day-3']=df['total_deaths'].shift(periods=3)
    df['day-4']=df['total_deaths'].shift(periods=4)
    df['day-5']=df['total_deaths'].shift(periods=5)
    df['day-6']=df['total_deaths'].shift(periods=6)
    df['day-7']=df['total_deaths'].shift(periods=7)
    df['day-8']=df['total_deaths'].shift(periods=8)
    df['day-9']=df['total_deaths'].shift(periods=9)
    df['day-10']=df['total_deaths'].shift(periods=10)
    df = df.iloc[10: , :]
    df=df.fillna(0)
    X=df.drop(columns=['total_deaths','new_deaths','new_cases'])
    y=df['total_deaths']
    # scaler = MinMaxScaler()
    # scaler.fit(X)
    # X=scaler.transform(X)


X=data_index.drop(columns=['total_deaths','new_deaths','new_cases'])
y=data_index['total_deaths']


scaler = MinMaxScaler()
scaler.fit(X)
X=scaler.transform(X)

n = len(X)
X_train = X[0:int(n-15)]
X_test=X[int(n-15):]
y_train=y[0:int(n-15)]
y_test=y[int(n-15):]

# model =SVR(C=5, coef0=10, epsilon=0.05, kernel='poly')
# param={'kernel' : ('poly', 'rbf'),'C' : [5,6],'degree' : [3,8],'coef0' : [0.01,0.5,10]}
# grid_search = GridSearchCV(model, param_grid = param,
#                       cv = 2, n_jobs = -1, verbose = 2)
# grid_search.fit(X_train,y_train)
# best=grid_search.best_estimator_

path='/data/models'
model=[]
y_pred=[]
X_predict=[]

for country in country_list:
    model.append(pickle.load(open(f'{path}/model_{country}.pkl','rb')))
    y_pred.append(model.predict(X_test))

# model_load=pickle.load(open(f'{path}/model{country}.pkl','rb'))
# with open(f'{path}/model_{country}.pkl','wb') as f:
#     pickle.dump(model, f)




X_test_columns=data_index.drop(columns=['total_deaths','new_cases','new_deaths'])
X_test_columns.columns

X_test_df=pd.DataFrame(X_test,columns=X_test_columns.columns)
X_predict=X_test_df.tail(10)
X_predict=X_predict.reset_index(drop=True)

for i in range(1,10):
    X_predict.loc[i,'containment_and_health':'total_boosters']=X_predict.loc[0,'containment_and_health':'total_boosters']



min_num=min(y)
max_num=max(y)

list_pred=[]

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[0]).T))
print(y_pred_)
print(y_train.tail(1))
if (y_pred_ < y_train.tail(1).tolist())[0]:
        y_pred_=y_train.tail(1)
        y_pred_2=y_train.tail(1)
else:
    y_pred_2=y_pred_

y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)
for j in range(1,10):

    X_predict.loc[j,f'day-{j}']=y_pred_scale
    print(j)
    print(y_pred_scale)


y_pred_ = np.round(model.predict(pd.DataFrame(X_predict.loc[1]).T))
if y_pred_ < y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_

y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)
for j in range(2,10):
    X_predict.loc[j,f'day-{j-1}']=y_pred_scale
    print(j)
    print(y_pred_scale)

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[2]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)
for j in range(3,10):
    X_predict.loc[j,f'day-{j-2}']=y_pred_scale
    print(y_pred_scale)
    print(j)

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[3]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)
for j in range(4,10):
    X_predict.loc[j,f'day-{j-3}']=y_pred_scale
    print(y_pred_scale)
    print(j)

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[4]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)
for j in range(5,10):
    X_predict.loc[j,f'day-{j-4}']=y_pred_scale
    print(y_pred_scale)
    print(j)

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[5]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)
for j in range(6,10):
    X_predict.loc[j,f'day-{j-5}']=y_pred_scale
    print(y_pred_scale)
    print(j)

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[6]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)

for j in range(7,10):
    X_predict.loc[j,f'day-{j-6}']=y_pred_scale
    print(y_pred_scale)
    print(j)
y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[7]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)

for j in range(8,1):
    X_predict.loc[j,f'day-{j-7}']=y_pred_scale
    print(y_pred_scale)
    print(j)

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[8]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
list_pred.append(y_pred_)
for j in range(9,10):
    X_predict.loc[j,f'day-{j-8}']=y_pred_scale
    print(y_pred_scale)
    print(j)

y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[8]).T))
if y_pred_< y_pred_2:
    y_pred_=y_pred_2
else:
    y_pred_2=y_pred_
list_pred.append(y_pred_)

X_predict

y_test

# plot the predicted and real total deaths by COVID-19
# find csv
# read csv
# preprocess csv with Sumedha process
# predict the X_predict(dataframe)
