# myStudies_stats
A short script that scrapes myStudies and creates a dataframe from the transcript of records. 
It allows you to compute weighted averages etc. 

## Disclaimer
This program will automatically login and access your mystudies page. Hence a software bug could lead to unintended changes on your mystudies profile.
Further is it (in most cases) not allowed to use a bot for webscraping without consent of the owner of the concerned website. 

I do not take any responsibility for the use of this tool.  

## Installation
Google Chrome browser needs to be installed on your system. \
Run the following commands in powershell (Windows) or in terminal (Linux).

### 1. Clone the repo 
```
git clone https://github.com/yv1es/myStudies_stats.git
cd myStudies_stats
``` 

### 2. Create a virtual environment 
```
pip install virtualenv
python -m venv . 
```

### 3. Install dependencies 
```
.\Scripts\activate
pip install -r requirements.txt
``` 

### 4. Create a credentials file. 
In the folder `/src` create a file named `creds.py`.
The credentials file should have following format:
```
USERNAME = "your mystudies username"
PASSWORD = "your mystudies password"
``` 
The `creds.py` file will be ignored by git with the intention of preventing accidental credential leaks. 

## Running the Script

### 1. Activate the virutal environment. 
`.\Scripts\activate`
### 2. Execute the script 
`python .\src\run.py`  
