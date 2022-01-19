# NYS Drug Pricing Scraper
Python (Selenium) Scraper of https://apps.health.ny.gov/pdpw/SearchDrugs/Home.action with output to CSV & MySQL
 
If you want to reuse this scraper, please read these instructions:

First, download all files in the repository: DrugIDs.txt, export.csv, NYZIPS.txt & scraper.py. 
Note: export.csv is where the scraped output will go (in addition to your MySQL server). 
DrugIDs.txt contains a list of 150 XPaths, each corresponding to a Prescription Drug in the scraper's loop. 
NYZIPS.txt contains a list of roughly 2,000 New York State ZIP codes that have results in the website's database; original list was taken from Simple Maps and reduced down to entries in the .txt file after parsing through the website. 
scraper.py is the scraper (obviously). 

Second, download Chromedriver for your Operating System (Mac, Windows & Linux). 
Here is the URL for installation: https://chromedriver.chromium.org/downloads. 
Make sure to download the same version as your version of Chrome (check the version by going to 'Settings', then 'About Chrome' in the Browser). 

Third, make sure to have MySQL installed and running on your operating system. 
Here is the URL for installation: https://dev.mysql.com/downloads/mysql/ . 
Download the program and start running the MySQL server.    
Use a MySQL GUI tool to view the data (MySQLWorkbench, for example). 
*If you don't want to use a SQL database to store your data (the script will also output to csv), then comment out or delete lines 11-17 & 71. 
Next, replace the four 'XXXX's with your hostname, database name, username (default set to 'root'), and password. 

Fourth, make sure to update the paths for all of the .txt files, export.csv and chromedriver in scraper.py & run the script. 
This scraper utilizes the selenium, pandas, time, datetime & sqlalchemy packages, so make sure they are installed into your python library before running the scraper. 
It is recommended you edit the DrugIDs.txt file to only contain 3-10 entries (XPaths) per script, so the scraper does not become overwhelmed. 
