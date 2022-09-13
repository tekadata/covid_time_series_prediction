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

## Setup

### 1 - Project Structure
Go to your local `~/code/Teky-Teka/covid_time_series_prediction` folder.
Display the project structure.

```bash
.
# Your whole code logic and data, this is your "package"
├── covid_time_series_prediction
    ├── raw_data                # Your data source (git ignored)
    |   ├──  oxford_dataset.csv
    |   ├──  vaccinations_dataset.csv
    |   ├──   ...
    |   ├── README.md       # database documentation
    |
    ├── covid_time_series_prediction        # Your data-processing logic
    |   ├── data.py
    |   ├── indicator.py
    |   ├── model.py
    |   ├── utils.py
    |   └── __init__.py.    # turns the covid_time_series_prediction folder into a "package"
    ├── notebooks             # Your notebooks & analyses, step-by-step
    |   ├──  eda.ipynb
    |   ├──  rnn.ipynb
    |   ├──   ...
    |   ├── README.md       # notebooks documentation
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
