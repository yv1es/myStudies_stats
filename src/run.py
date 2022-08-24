from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

# import user credentials
from creds import USERNAME, PASSWORD

# load Chrome webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# navigate to mystudies
driver.get("https://www.lehrbetrieb.ethz.ch/myStudies/login.view")

# navigate to login 
driver.find_element(By.CLASS_NAME, "submit").click()

# login 
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.clear()
password_field.clear()
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
driver.find_element(By.CLASS_NAME, "btn").click()

# navigate to "Leistungsüberblick"
driver.find_element(By.ID, "immatrik").click()
driver.find_element(By.ID, "studLeistungsueberblick").click()

# load "Leistungsüberblick" into a dataframe
table = driver.find_element(By.CLASS_NAME, "tablelist")
inner = '<table>' + table.get_attribute('innerHTML') + '</table>'
df = pd.read_html(inner)[0]

# close driver
driver.close()
driver.quit()

# drop where 'Ist' credits is Nan
df = df[~np.isnan(df['ECTS-Kreditpunkte']['Ist'])]

# use regex to filter for grades
df = df[df['Note']['Unnamed: 3_level_1'].str.contains('\d')]

# build a new dataframe
data = {
    'number':df['Unnamed: 0_level_0']['Unnamed: 0_level_1'],
    'title':df['Unnamed: 1_level_0']['Unnamed: 1_level_1'],
    'session':df['Sess.']['Unnamed: 2_level_1'],
    'credits':df['ECTS-Kreditpunkte']['Ist'].astype(float),
    'grade':df['Note']['Unnamed: 3_level_1'].astype(float)
}

df = pd.DataFrame(data)
df.reset_index(inplace=True, drop=True)


# stats
total_credits = df['credits'].sum()
unweighted_avg = df['grade'].mean()
weighted_avg = df['credits'].multiply(df['grade']).sum() / total_credits

# round
unweighted_avg = round(unweighted_avg, 3)
weighted_avg = round(weighted_avg, 3)


print(df, "\n")
print(f'Anzahl Credits: {total_credits}')
print(f'Ungewichteter Schnitt: {unweighted_avg}')
print(f'Gewichteter Schnitt: {weighted_avg}')



