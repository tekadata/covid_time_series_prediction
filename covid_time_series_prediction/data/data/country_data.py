import pandas as pd
import matplotlib.pyplot as plt

def get_csv():

    # Index URLs
    url_index_strigency = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/stringency_index_avg.csv'
    url_index_gov_response = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/government_response_index_avg.csv'
    url_index_health = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/containment_health_index_avg.csv'
    url_index_economic = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/economic_support_index.csv'

    # Indicators URLs
    # C sub-indicators
    url_c1 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c1m_school_closing.csv'
    url_c2 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c2m_workplace_closing.csv'
    url_c3 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c3m_cancel_public_events.csv'
    url_c4 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c4m_restrictions_on_gatherings.csv'
    url_c5 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c5m_close_public_transport.csv'
    url_c6 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c6m_stay_at_home_requirements.csv'
    url_c7 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c7m_movementrestrictions.csv'
    url_c8 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c8ev_internationaltravel.csv'

    # E sub-indicators
    url_e1 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/e1_income_support.csv'
    url_e2 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/e2_debtrelief.csv'

    # H sub-indicators
    url_h1 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h1_public_information_campaigns.csv'
    url_h2 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h2_testing_policy.csv'
    url_h3 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h3_contact_tracing.csv'
    url_h6 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h6m_facial_coverings.csv'
    url_h7 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h7_vaccination_policy.csv'
    url_h8 = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h8m_protection_of_elderly_ppl.csv'

     # Vacination Dataset
    url_vaccination = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
    
    # Target URLs
    url_cases = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/confirmed_cases.csv'
    url_deaths = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/confirmed_deaths.csv'

    # DataFrame Index
    
    df_gov_response_raw = pd.read_csv(url_index_gov_response)
    df_strigency_raw = pd.read_csv(url_index_strigency)
    df_health_raw = pd.read_csv(url_index_health)
    df_economic_raw = pd.read_csv(url_index_economic)

    # DataFrames Indicator
    df_c1_raw = pd.read_csv(url_c1)
    df_c2_raw = pd.read_csv(url_c2)
    df_c3_raw = pd.read_csv(url_c3)
    df_c4_raw = pd.read_csv(url_c4)
    df_c5_raw = pd.read_csv(url_c5)
    df_c6_raw = pd.read_csv(url_c6)
    df_c7_raw = pd.read_csv(url_c7)
    df_c8_raw = pd.read_csv(url_c8)

    df_e1_raw = pd.read_csv(url_e1)
    df_e2_raw = pd.read_csv(url_e2)

    df_h1_raw = pd.read_csv(url_h1)
    df_h2_raw = pd.read_csv(url_h2)
    df_h3_raw = pd.read_csv(url_h3)
    df_h6_raw = pd.read_csv(url_h6)
    df_h7_raw = pd.read_csv(url_h7)
    df_h8_raw = pd.read_csv(url_h8)
    
    # DataFrame Vaccination
    df_vaccination_raw = pd.read_csv(url_vaccination)

    # Data Frame target
    df_cases_raw = pd.read_csv(url_cases)
    df_deaths_raw = pd.read_csv(url_deaths)
    
    # Crear lista con los df_raw
    
    df_raw_list = [df_gov_response_raw, df_strigency_raw, df_health_raw,df_economic_raw,
               df_c1_raw,df_c2_raw,df_c3_raw,df_c4_raw,df_c5_raw,df_c6_raw,df_c7_raw,df_c8_raw,df_e1_raw,df_e2_raw,
               df_h1_raw,df_h2_raw,df_h3_raw,df_h6_raw,df_h7_raw,df_h8_raw,
               df_vaccination_raw,
               df_cases_raw,df_deaths_raw]
    
    return df_raw_list

# Cleaninng Features

def clean_data():
    
    df_gov_response_raw, df_strigency_raw, df_health_raw, df_economic_raw, df_c1_raw, df_c2_raw, df_c3_raw, df_c4_raw, df_c5_raw,df_c6_raw,df_c7_raw,df_c8_raw,df_e1_raw,df_e2_raw,df_h1_raw,df_h2_raw,df_h3_raw,df_h6_raw,df_h7_raw,df_h8_raw,df_vaccination_raw,df_cases_raw,df_deaths_raw = get_csv()

    drop_columns = ['Unnamed: 0','country_code','region_code','region_name','jurisdiction']

    df_gov_response = df_gov_response_raw.drop(columns = drop_columns)
    df_gov_response.set_index(keys='country_name', inplace=True)
    df_gov_response = df_gov_response.T
    df_gov_response = df_gov_response.fillna(0)

    df_health = df_health_raw.drop(columns = drop_columns)
    df_health.set_index(keys='country_name', inplace=True)
    df_health = df_health.T
    df_health = df_health.fillna(0)

    df_strigency = df_strigency_raw.drop(columns = drop_columns)
    df_strigency.set_index(keys='country_name', inplace=True)
    df_strigency = df_strigency.T
    df_strigency = df_strigency.fillna(0)

    df_economic = df_economic_raw.drop(columns = drop_columns)
    df_economic.set_index(keys='country_name', inplace=True)
    df_economic = df_economic.T
    df_economic = df_economic.fillna(0)

    # Cleaning Indicators

    df_c1 = df_c1_raw.copy()
    df_c1 = df_c1.drop(columns = drop_columns)
    df_c1.set_index(keys='country_name', inplace=True)
    df_c1 = df_c1.T

    df_c2 = df_c2_raw.copy()
    df_c2 = df_c2.drop(columns = drop_columns)
    df_c2.set_index(keys='country_name', inplace=True)
    df_c2 = df_c2.T

    df_c3 = df_c3_raw.copy()
    df_c3 = df_c3.drop(columns = drop_columns)
    df_c3.set_index(keys='country_name', inplace=True)
    df_c3 = df_c3.T

    df_c4 = df_c4_raw.copy()
    df_c4 = df_c4.drop(columns = drop_columns)
    df_c4.set_index(keys='country_name', inplace=True)
    df_c4 = df_c4.T

    df_c5 = df_c5_raw.copy()
    df_c5 = df_c5.drop(columns = drop_columns)
    df_c5.set_index(keys='country_name', inplace=True)
    df_c5 = df_c5.T

    df_c6 = df_c6_raw.copy()
    df_c6 = df_c6.drop(columns = drop_columns)
    df_c6.set_index(keys='country_name', inplace=True)
    df_c6 = df_c6.T

    df_c7 = df_c7_raw.copy()
    df_c7 = df_c7.drop(columns = drop_columns)
    df_c7.set_index(keys='country_name', inplace=True)
    df_c7 = df_c7.T

    df_c8 = df_c8_raw.copy()
    df_c8 = df_c8.drop(columns = drop_columns)
    df_c8.set_index(keys='country_name', inplace=True)
    df_c8 = df_c8.T

    df_e1 = df_e1_raw.copy()
    df_e1 = df_e1.drop(columns = drop_columns)
    df_e1.set_index(keys='country_name', inplace=True)
    df_e1 = df_e1.T

    df_e2 = df_e2_raw.copy()
    df_e2 = df_e2.drop(columns = drop_columns)
    df_e2.set_index(keys='country_name', inplace=True)
    df_e2 = df_e2.T

    df_h1 = df_h1_raw.copy()
    df_h1 = df_h1.drop(columns = drop_columns)
    df_h1.set_index(keys='country_name', inplace=True)
    df_h1 = df_h1.T

    df_h2 = df_h2_raw.copy()
    df_h2 = df_h2.drop(columns = drop_columns)
    df_h2.set_index(keys='country_name', inplace=True)
    df_h2 = df_h2.T

    df_h3 = df_h3_raw.copy()
    df_h3 = df_h3.drop(columns = drop_columns)
    df_h3.set_index(keys='country_name', inplace=True)
    df_h3 = df_h3.T

    df_h6 = df_h6_raw.copy()
    df_h6 = df_h6.drop(columns = drop_columns)
    df_h6.set_index(keys='country_name', inplace=True)
    df_h6 = df_h6.T

    df_h7 = df_h7_raw.copy()
    df_h7 = df_h7.drop(columns = drop_columns)
    df_h7.set_index(keys='country_name', inplace=True)
    df_h7 = df_h7.T

    df_h8 = df_h8_raw.copy()
    df_h8 = df_h8.drop(columns = drop_columns)
    df_h8.set_index(keys='country_name', inplace=True)
    df_h8 = df_h8.T

    # Cleaning Vaccination Features
    df_vaccination = df_vaccination_raw.copy()
    df_vaccination = df_vaccination[['date','location','people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred']]

    # Cleaninng Target

    # Cases per country
    df_cases = df_cases_raw.drop(columns = drop_columns)
    df_cases.set_index(keys='country_name', inplace=True)
    df_cases = df_cases.T
    df_cases = df_cases.fillna(0)

    # Deaths per country
    df_deaths = df_deaths_raw.drop(columns = drop_columns)
    df_deaths.set_index(keys='country_name', inplace=True)
    df_deaths = df_deaths.T
    df_deaths = df_deaths.fillna(0)
    
    df_clean_list = [df_gov_response, df_strigency, df_health,df_economic,
               df_c1,df_c2,df_c3,df_c4,df_c5,df_c6,df_c7,df_c8,df_e1,df_e2,
               df_h1,df_h2,df_h3,df_h6,df_h7,df_h8,
               df_vaccination,
               df_cases,df_deaths]
    
    return df_clean_list
    
def country_output(country):
    
    df_gov_response, df_strigency, df_health,df_economic,df_c1,df_c2,df_c3,df_c4,df_c5,df_c6,df_c7,df_c8,df_e1,df_e2,df_h1,df_h2,df_h3,df_h6,df_h7,df_h8,df_vaccination,df_cases,df_deaths = clean_data()

    # INDEX FEATURES
    country_index = df_gov_response.copy()
    country_index = pd.DataFrame(country_index[[country]].iloc[:,0])
    country_index.index.name = country
    country_index.columns = ['gov_response']
    country_index['containment_and_health'] = df_health[[country]].iloc[:,0]
    country_index['stringency'] = df_strigency[[country]].iloc[:,0]
    country_index['economics_sup'] = df_economic[[country]].iloc[:,0]

    # INDICATOR FEATRUES
    df = pd.DataFrame(df_c1[[country]].rename(columns = {country:'school_closing'}).iloc[:,0])
    df.index.name = country
    df['workplace_closing'] = df_c2[[country]].iloc[:,0]
    df['cancel_public_events'] = df_c3[[country]].iloc[:,0]
    df['restrictions_on_gatherings'] = df_c4[[country]].iloc[:,0]
    df['close_public_transport'] = df_c5[[country]].iloc[:,0]
    df['stay_at_home_requirements'] = df_c6[[country]].iloc[:,0]
    df['restrictions_on_internal_movement'] = df_c7[[country]].iloc[:,0]
    df['international_travel_controls'] = df_c8[[country]].iloc[:,0]
    df['income_support'] = df_e1[[country]].iloc[:,0]
    df['debt/contract_relief'] = df_e2[[country]].iloc[:,0]
    df['public_information_campaigns'] = df_h1[[country]].iloc[:,0]
    df['testing_policy'] = df_h2[[country]].iloc[:,0]
    df['contact_tracing'] = df_h3[[country]].iloc[:,0]
    df['facial_coverings'] = df_h6[[country]].iloc[:,0]
    df['vaccination_policy'] = df_h7[[country]].iloc[:,0]
    df['protection_of_elderly_people'] = df_h8[[country]].iloc[:,0]
    df = df.fillna(method = 'ffill')
    country_indicator = df
    
    # POPULATION VACCINATED

    country_vaccination = df_vaccination.loc[df_vaccination['location']==country]
    country_vaccination = country_vaccination.fillna(method='ffill').drop(columns = 'location')
    country_vaccination.index.name = country
    country_vaccination = country_vaccination.fillna(0)

    # TARGET
    
    country_target = df_cases.copy()
    country_target = pd.DataFrame(country_target[[country]].iloc[:,0])
    country_target.index.name = country
    country_target.columns = ['total_cases']
    country_target['new_cases'] = country_target - country_target.shift(1)
    country_target['total_deaths'] = df_deaths[[country]].iloc[:,0]
    country_target['new_deaths'] = df_deaths[[country]].iloc[:,0] - df_deaths[[country]].iloc[:,0].shift(1)

    country_target['new_cases'].loc[country_target['new_cases'] < 0] = 0
    country_target['new_deaths'].loc[country_target['new_deaths'] < 0] = 0

    # Days no update counter

    def non_uptade(country_target):

        counter = 0
        x = 1
        while country_target['total_deaths'][-x] == 0:
            counter += 1
            x += 1

        return counter

    counter = non_uptade(country_target)

    # Last Update Data
    country_index = country_index[15:-counter]
    country_indicator = country_indicator[15:-counter]
    country_vaccination = country_vaccination[15:-counter]
    country_target = country_target[15:-counter]
    
    # JOIN INDEX-TARGET AND INDICATOR-TARGET
    country_index = country_index.join(country_target)
    
    country_indicator = country_indicator.join(country_target)
    
    # JOIN INDEX AND VACCINATION
    country_vaccination.reset_index(inplace=True)
    country_vaccination['date'] = pd.to_datetime(country_vaccination['date'])

    country_index.reset_index(inplace=True)
    country_index[country] = country_index[country].apply(lambda x: pd.to_datetime( x, format='%y%b%d', infer_datetime_format=True))
    
    country_index.rename(columns = {country: 'date'}, inplace = True)
    country_index = country_index.merge(country_vaccination, how = 'left' , on = 'date')

    country_index.fillna(method = 'ffill', inplace=True)
    country_index.fillna(0, inplace=True)
    country_index.drop(columns = country, inplace=True)
    
    # JOIN INDICATOR AND VACCINATION

    country_indicator.reset_index(inplace=True)
    country_indicator[country] = country_indicator[country].apply(lambda x: pd.to_datetime( x, format='%y%b%d', infer_datetime_format=True))

    country_indicator.rename(columns = {country: 'date'}, inplace = True)
    country_indicator = country_indicator.merge(country_vaccination, how = 'left' , on = 'date')

    country_indicator.fillna(method = 'ffill', inplace=True)
    country_indicator.fillna(0, inplace=True)
    country_indicator.drop(columns = country, inplace=True)
    
    return country_index, country_indicator
