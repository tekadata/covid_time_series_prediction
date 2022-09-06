# covid_time_series_prediction

## Data analysis
- Document here the project: covid_vn_pred
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

## Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for covid_vn_pred in gitlab.com/Teky-Teka.
If your project is not set please add it:

- Create a new project on `gitlab.com/Teky-Teka/covid_vn_pred`
- Then populate it:

```bash
###   e.g. if group is "Teky-Teka" and project_name is "covid_vn_pred"
git remote add origin git@github.com:Teky-Teka/covid_vn_pred.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
covid_vn_pred-run
```

## Install

Go to `https://github.com/Teky-Teka/covid_vn_pred` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:Teky-Teka/covid_vn_pred.git
cd covid_vn_pred
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
covid_vn_pred-run
```
