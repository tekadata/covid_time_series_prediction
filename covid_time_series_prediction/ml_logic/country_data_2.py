import pandas as pd
import matplotlib.pyplot as plt


def data_cleaning_all_index(name_data_table):
    trans_table=name_data_table.groupby('country_code').sum().T.drop('Unnamed: 0')
    trans_table.index = pd.to_datetime(trans_table.index)
    
    return trans_table


def data_cleaning_all_indicator(name_data_table):
    trans_table=name_data_table.groupby('country_code').mean().round(decimals = 0).T.drop('Unnamed: 0')
    trans_table.index = pd.to_datetime( trans_table.index)
    
    return trans_table


def country_output_2(country):
    df_gov_response_usa=df_gov_response[country]
    country_index=df_gov_response_usa
    country_index=pd.DataFrame(country_index)
    country_index.columns = ['gov_response']
    country_index.insert(0, 'containment_and_health', df_health[country])
    country_index.insert(1, 'stringency', df_strigency[country])
    country_index.insert(2,'economics_sup',df_economic[country])
    country_index.insert(3,'total_cases',df_cases[country])
    country_index.insert(4,'new_cases',df_cases[country]-df_cases[country].shift(1))
    country_index.insert(5,'total_deaths',df_deaths[country])
    country_index.insert(6,'new_deaths',df_deaths[country] - df_deaths[country].shift(1))
    country_index.index.name='date'
    country_index['new_cases'].loc[country_index['new_cases'] < 0] = 0
    country_index['new_deaths'].loc[country_index['new_deaths'] < 0] = 0
    country_index['gov_response'] = (country_index['gov_response'] / country_index['gov_response'].sum()) * 100
    country_index['containment_and_health'] = (country_index['containment_and_health'] / country_index['containment_and_health'].sum()) * 100
    country_index['stringency'] = (country_index['stringency'] / country_index['stringency'].sum()) * 100
    country_index['economics_sup'] = (country_index['economics_sup'] / country_index['economics_sup'].sum()) * 100
    country_index['economics_sup'] = (country_index['economics_sup'] / country_index['stringency'].sum()) * 100
    
    
    
    
    #vaccination
    country_vaccination=df_vaccination[df_vaccination['iso_code']==country]
    country_vaccination=country_vaccination[['total_vaccinations', 'people_vaccinated','people_fully_vaccinated', 'total_boosters']]
    
    #indicator
    df_c2_usa=df_c2[country]
    country_indicator= df_c2_usa
    country_indicator=pd.DataFrame(country_indicator)
    country_indicator.columns = ['workplace_closing']
    country_indicator.insert(0, 'cancel_public_events', df_c3[country])
    country_indicator.insert(1, 'school_closing', df_c1[country])
    country_indicator.insert(2, 'restrictions_on_gathering', df_c4[country])
    country_indicator.insert(3,'close_public_transport',df_c5[country])
    country_indicator.insert(4,'stay_at_home_requirements',df_c6[country])
    country_indicator.insert(5,'restrictions_on_internal_movement',df_c7[country])
    country_indicator.insert(6,'international_travel_controls',df_c8[country])
    country_indicator.insert(7,'income_support',df_e1[country])
    country_indicator.insert(8,'debt/contract_relief',df_e2[country])
    country_indicator.insert(9,'public_information_campaigns',df_h1[country])
    country_indicator.insert(10,'testing_policy',df_h2[country])
    country_indicator.insert(11,'contact_tracing',df_h3[country])
    country_indicator.insert(12,'facial_coverings',df_h6[country])
    country_indicator.insert(13,'vaccination_policy',df_h7[country])
    country_indicator.insert(14,'protection_of_elderly_people',df_h8[country])
    country_indicator.insert(15,'total_cases',df_cases[country])
    country_indicator.insert(16,'new_cases',df_cases[country]-df_cases[country].shift(1))
    country_indicator.insert(17,'total_deaths',df_deaths[country])
    country_indicator.insert(18,'new_deaths',df_deaths[country] - df_deaths[country].shift(1))
    country_indicator.index.name='date'
    country_indicator['new_cases'].loc[country_indicator['new_cases'] < 0] = 0
    country_indicator['new_deaths'].loc[country_indicator['new_deaths'] < 0] = 0
    
    
    country_index = country_index.merge(country_vaccination, how = 'left' , on = 'date')
    country_indicator=country_indicator.merge(country_vaccination, how = 'left' , on = 'date')
 
    
    indicator_death=country_indicator[country_indicator['total_deaths']>0]
    first_death_date=indicator_death.index[0]
    last_death_date=indicator_death.index[-1]
    country_indicator=country_indicator[~(country_indicator.index < first_death_date)]
    country_indicator=country_indicator[~(country_indicator.index > last_death_date)]
    
    index_death=country_index[country_index['total_deaths']>0]
    first_death_date_index=index_death.index[0]
    last_death_date_index=index_death.index[-1]
    country_index=country_index[~(country_index.index < first_death_date_index)]
    country_index=country_index[~(country_index.index > last_death_date_index)]
    
    country_indicator = country_indicator.fillna(0)
    country_index = country_index.fillna(0)
    
    return country_index,country_indicator