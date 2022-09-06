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

Unittest test:
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
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
covid_time_series_prediction
```
