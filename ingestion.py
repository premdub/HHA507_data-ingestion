from openpyxl import Workbook
import pandas as pd # import pandas for general files
import json # import json for json files
import requests # import requests for web requests
import xlrd # import xlrd for excel files, tab names

##This is command so i can read xl file
df = pd.read_excel('data\\assignment data.xlsx')
df





import xlrd
xls = xlrd.open_workbook('data\\assignment data.xlsx', on_demand=True)
## reviewing what tabs are within spreadsheet
sheet_name = xls.sheet_names()
sheet_name
## through that command user will discover there are two tabs: "tab1" and "tab2"



import pandas as pd
df = pd.read_excel('data\\assignment data.xlsx')
df
sheet1 = pd.read_excel('data\\assignment_data.xlsx', sheet_name="tab1")
sheet2 = pd.read_excel('data\\assignment_data.xlsx', sheet_name="tab2")
## check whether if the tabs were imported/assigned properly to its respective variable
print(sheet1)
print(sheet2)


### Section 1
## this step i will open the excel workbook file
xls = xlrd.open_workbook('data\\assignment data.xlsx')
xls.sheet_names()


data = xlrd.open_workbook('data\\assignment data.xlsx', on_demand=True)
print(data.sheet_names())

tab1 = pd.read_excel('data\\assignment data.xlsx', sheet_name="tab1")
tab2 = pd.read_excel('data\\assignment data.xlsx', sheet_name="tab2")

print(tab1)
print(tab2)

#########Code below is for main desktop
data = xlrd.open_workbook('data\\assignment data.xlsx', on_demand=True)
print(data.sheet_names())
tab1 = pd.read_excel('data\\assignment data.xlsx', sheet_name="tab1")
tab2 = pd.read_excel('data\\assignment data.xlsx', sheet_name="tab2")
print(tab1)
print(tab2)















### Section 2
## importing CMS dataset as 'apidataset' via the request module with ge
import requests 
import json
## URL for dataset
url = "https://data.cms.gov/data-api/v1/dataset/7171ef6c-a2cf-43d4-b8ab-774b0de9b90a/data"
## Calling in dataset
apiDataset = requests.get ('https://data.cms.gov/data-api/v1/dataset/7171ef6c-a2cf-43d4-b8ab-774b0de9b90a/data')
## setting the variable as a json file format
apiDataset = apiDataset.json()
## check whether if it was success
print (apiDataset)



3

##Section 3 - Pull 2 open source bigquery datasets; limiting to the first 100 rows as a dataframe
import pandas as pd # import pandas for general files

from google.cloud import bigquery
from google.oauth2 import service_account
client = bigquery.Client.from_service_account_json('data\\fresh-booster-361204-ef0c0b10b27b.json')
##First Dataset
query_job1 = client.query("SELECT * FROM 'patents-public-data.google_patents_research.publications_201710' LIMIT 100")
dataresults1 = query_job1.results()
bigquery1 = pd.DataFrame(dataresults1.to_dataframe())





### Section 3
##   Connecting to bigquery and creating a bigquery client with specific json key
from google.cloud import bigquery 
gcp_project = 'fresh-booster-361204'
client = bigquery.Client.from_service_account_json(r"C:\Users\premd\OneDrive\Documents\GitHub\HHA507-data-ingestion\data\fresh-booster-361204-ef0c0b10b27b.json")
## querying public dataset 1
## dataset_1 query only returning first 100 rows
query_job = client.query("SELECT * FROM 'patents-public-data.google_patents_research.publications_201710' LIMIT 100")
## getting results of query
results = query_job.result()
## use "pip install db db-dtypes if terminal says its not functioning"
bigquery1 = pd.DataFrame(results.to_DataFrame())
bigquery1


client = bigquery.Client.from_service_account_json('fresh-booster-361204-ef0c0b10b27b.json')
### Querying public dataset 2
## dataset_2 query only returning first 100 rows
query_job = client.query("SELECT * FROM `patents-public-data.google_patents_research.publications_201802` LIMIT 100")

## getting results of query 
results = query_job.result()
## putting the results into dataframe as the variable bigquery 2
Bigquery2 = pd.DataFrame(results.to_DataFrame())
Bigquery2

## check whether if it was success
print(bigquery1, '/n', bigquery2)
##   THIS IS ALMOST DONE