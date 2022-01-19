import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date
from sqlalchemy import create_engine

hostname = "XXXX"
dbname = "XXXX"
uname = "XXXX"
pwd = "XXXX"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))

today = date.today()
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
s = Service('[CHROMDRIVER PATH]')
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://apps.health.ny.gov/pdpw/SearchDrugs/Home.action")
drugselection = '//*[@id="availableDrugs"]'
adddrug = '//*[@id="AddDrugs"]'
ZIPinsert = '//*[@id="zip"]'
ZIPsearch = '//*[@id="SearchbyZip"]'

Drugs = []
with open("./DrugIDs.txt", "r") as fp:
    line_list = fp.readlines()
    for line in line_list:
        line = line.rstrip()
        try:
            Drugs.append(line)
        except:
            pass
print(Drugs)

ZIPs = []
with open("./NYZIPS.txt", "r") as fp:
    line_list = fp.readlines()
    for line in line_list:
        line = line.rstrip()
        try:
            ZIPs.append(line)
        except:
            pass
print(ZIPs)

for drug in Drugs:
    print(drug)
    driver.find_element(By.XPATH, drug).click()
    driver.find_element(By.XPATH, adddrug).click()
    driver.implicitly_wait(30)
    for zip in ZIPs:
        try:
            driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(zip)
            driver.find_element(By.XPATH, '//*[@id="SearchbyZip"]').click()
            driver.get('https://apps.health.ny.gov/pdpw/SearchDrugs/PrintDrugSearchResults.action')
            html = driver.page_source
            df = pd.read_html(html)[2]
            newdf = df[['Pharmacy', 'Total Cost']]
            FINAL = newdf[newdf['Pharmacy'].str.contains(zip)]
            FINAL.insert(1, "ZIP code", zip)
            FINAL.insert(0, "Drug XPath", drug)
            FINAL.insert(0, "Scraped Date", today)
            FINAL.to_csv('./export.csv', mode='a', header=False)
            FINAL.to_sql(drug, engine, if_exists='append')
            time.sleep(2)
            driver.get("https://apps.health.ny.gov/pdpw/SearchDrugs/Home.action")
            driver.find_element(By.XPATH, drug).click()
            driver.find_element(By.XPATH, adddrug).click()
        except TimeoutException:
            driver.refresh()
    time.sleep(2)
    driver.get("https://apps.health.ny.gov/pdpw/SearchDrugs/Home.action")

driver.quit()
