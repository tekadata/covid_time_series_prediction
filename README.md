# covid_time_series_prediction

## Data analysis
- Document here the project: covid_time_series_prediction
- Description: Deep Learning Time Series Prediction of Daily COVID-19 Cases according to Government Responses
- Data Source: https://www.bsg.ox.ac.uk/research/research-projects/covid-19-government-response-tracker
- Type of analysis: Machine Learning ARIMA model + Deep Learning RNN model

Please document the project the better you can.


## Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
pyenv virtualenv covid_tsp_env
cd ~/code/Teky-Teka/covid_time_series_prediction
pyenv local covid_tsp_env
pip install --upgrade pip; pip install -r requirements.txt
pip freeze
```

Unit test:
```bash
make clean install test
```

Check for covid_time_series_prediction in [github.com/Teky-Teka](https://github.com/Teky-Teka/).
If your project is not set please add it:

- Create a new project on `github.com/Teky-Teka/covid_time_series_prediction`
- Then populate it:

```bash
###   e.g. if group is "Teky-Teka" and project_name is "covid_time_series_prediction"
git remote add origin git@github.com:Teky-Teka/covid_time_series_prediction.git
git push -u origin main
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
covid_time_series_prediction-run
```

## Install

Go to `https://github.com/Teky-Teka/covid_time_series_prediction` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
pyenv virtualenv covid_tsp_env
cd ~/code/Teky-Teka/covid_time_series_prediction
pyenv local covid_tsp_env
pip install --upgrade pip; pip install -r requirements.txt
pip freeze
```

Clone the project and install it:

```bash
git clone git@github.com:Teky-Teka/covid_time_series_prediction.git
cd covid_time_series_prediction
pip install -r requirements.txt
make clean install test                * install and test *
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
covid_time_series_prediction
```

## Setup

### 1 - Project Structure
Go to your local `~/code/Teky-Teka/covid_time_series_prediction` folder.
Display the project structure.

```bash
.
```
## Repository structure
```
├── MANIFEST.in
├── Makefile
├── README.md
├── covid_time_series_prediction
│   ├── __init__.py
│   │   * turns the covid_time_series_prediction folder into a "package" *
│   │   
│   ├── arima_model.py
│   │ 
│   ├── data
│   │   ├── __init__.py
│   │   │   * turns the data folder into a "package" *
│   │   │
│   │   ├── best_models
│   │   │   └── best_1
│   │   ├── data_raw
│   │   │   ├──data_<Country_name>
│   │   │   ├ ... * all datasets in input
│   │   └── models
│   │       └── model_France.pkl
│   ├── dp_logic
│   │   ├── RNN_model.py
│   │   ├── __init__.py
│   ├── grid_search_SVR.py
│   ├── indicator.py
│   ├── ml_logic
│   │   ├── SVN_model.py
│   │   ├── __init__.py
│   │   ├── country_data.py
│   │   ├── country_data_2.py
│   │   ├── model.py
│   │   ├── model_index.py
│   │   ├── model_indicator.py
│   │   ├── preprocessor.py
│   │   └── visualization.py
│   ├── model.py
│   └── prediction.py
│ 
├── data
│   │   * all the datasets (except those in covid_time_series_prediction/data/data_raw/data/ folder
│   ├── out_csv
│   │   ├── index_Afghanistan.csv
│   └── raw_data
│       ├── OxCGRT_timeseries_all.csv
│       ├── README.md # database documentation
│       ├── c1m_school_closing.csv
│       ├── c1m_school_closing.csv
│       ├── c2m_workplace_closing.csv
│       ├── c3m_cancel_public_events.csv
│       ├── c4m_restrictions_on_gatherings.csv
│       ├── c5m_close_public_transport.csv
│       ├── c6m_stay_at_home_requirements.csv
│       ├── c7m_movementrestrictions.csv
│       ├── c8ev_internationaltravel.csv
│       ├── cm5_close_public_transport.csv
│       ├── confirmed_cases.csv
│       ├── confirmed_deaths.csv
│       ├── containment_health_index_avg.csv
│       ├── e1_income_support.csv
│       ├── e2_debtrelief.csv
│       ├── economic_support_index.csv
│       ├── government_response_index_avg.csv
│       ├── h1_public_information_campaigns.csv
│       ├── h2_testing_policy.csv
│       ├── h3_contact_tracing.csv
│       ├── h6m_facial_coverings.csv
│       ├── h7_vaccination_policy.csv
│       ├── h8m_protection_of_elderly_ppl.csv
│       ├── stringency_index_avg.csv
│       ├── vaccinations-by-age-group.csv
│       └── vaccinations.csv
│ 
├── notebooks # Notebooks & analysis, step-by-step
│   ├── Data.ipynb
│   ├── Data_alberto.ipynb
│   ├── Data_analysis-USA.ipynb
│   ├── Data_analysis-multiple_data.ipynb
│   ├── Data_analysis.ipynb
│   ├── Data_ready_for_all_countries_sumedha.ipynb
│   ├── Data_to_work.ipynb
│   ├── EDA_TeKa.ipynb
│   ├── README.md # notebooks documentation
│   ├── RNN_FRA_model.ipynb
│   ├── RNN_TeKa.ipynb
│   ├── RNN_mode_with_USA_TeKa.ipynb
│   ├── data_to_work_alb.ipynb
│   ├── first_rnn_model.ipynb
│   ├── india_rnn_kim.ipynb
│   ├── model--SVR-index.ipynb
│   ├── model-Australia-SVR-index.ipynb
│   ├── model-Brazil-SVR-index.ipynb
│   ├── model-France-SVR-index.ipynb
│   ├── model-France-pickle-prediction.ipynb
│   ├── model-France-pickle.ipynb
│   ├── model-India-SVR-index-.ipynb
│   ├── model-Mexico-SVR-index.ipynb
│   ├── model-Russia -China-SVR-index-Copy1.ipynb
│   ├── model-UK-Arima.ipynb
│   ├── model-UK-SVR-index.ipynb
│   ├── model-UK-SVR.ipynb
│   ├── model-UK.ipynb
│   ├── model-USA.ipynb
│   ├── model_France.pkl
│   ├── time_series_prediction_covid_usa.ipynb
│   └── visualization_alb.ipynb
├── requirements.txt
├── scripts
│   └── covid_time_series_prediction-run
├── setup.py
├── test.py
└── tests
    └── __init__.py
```

### 2 - Edit the `PYTHONPATH`

Add `covid_time_series_prediction` path to your `PYTHONPATH`.

This will allow you to easily import modules defined in `covid_time_series_prediction` in your notebooks throughout the week.

Open your terminal and navigate to your home directory by running:

```bash
cd
```

Now you'll need to open your `.zshrc` file. As you might have noticed the file starts with a dot which means it's a hidden file. To be able to see this file in your terminal you'll need to run the command below, the flag `-a` will allow you to see hidden files:

```bash
ls -a
```

Next lets open the file using your text editor:

```bash
code .zshrc
```

Now in your terminal run:
```bash
cd ~/code/Teky-Teka/covid_time_series_prediction/ && echo "export PYTHONPATH=\"$(pwd):\$PYTHONPATH\""
```

👉 Copy the resulting output line from your terminal and paste it at the bottom of your ~/.zshrc file. Don't forget to save and restart all your terminal windows to take this change into account.



### 🔥 Check your setup

Go to your `covid_time_series_prediction` sub-folder (the one with the Python .py files) and run an `ipython` session:

```bash
cd ~/code/Teky-Teka/covid_time_series_prediction
ipython
```

Then type the following to check that the setup phase from the previous exercise worked:

```python
from indicator import Indicator
Indicator().ping()
# => pong
```

If you get something else than `pong`, ask teammates or raise a ticket to get some help from a TA. You might have a problem with the `$PYTHONPATH`.
