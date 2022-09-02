import pandas as pd # import pandas for general files
import json # import json for json files
import requests # import requests for web requests
from termios import TAB1, TAB2
import xlrd # import xlrd for excel files, tab names
##This is command so i can read xl file
df = pd.read_excel('data\\assignment data.xlsx')
df

### Section 1
## this step i will open the excel workook file
xls = xlrd.open_workbook ("C:\Users\premd\OneDrive\Desktop\Python Projects\HHA507_data ingestion\assignment data.xlsx", on demand=True)
xls.sheet_names()

## Importing excel workbook file
xls = xlrd.open_workbook('C:\Users\premd\OneDrive\Desktop\Python Projects\HHA507_data ingestion\assignment data.xlsx', on_demand=True)
tab1 = pd.read_excel("C:\Users\premd\OneDrive\Desktop\Python Projects\HHA507_data ingestion\assignment data.xlsx", sheet_name="tab1")
tab2 = pd.read_excel("C:\Users\premd\OneDrive\Desktop\Python Projects\HHA507_data ingestion\assignment data.xlsx", sheet_name='tab2')
## check whether if the tabs were imported/assigned properly to its respective variable
print(tab1)
print(tab2)

### Section 2
## importing CMS dataset as 'apidataset' via the request module with ge
import requests 
import json
## URL for dataset
url = "https://data.cms.gov/data-api/v1/dataset/7171ef6c-a2cf-43d4-b8ab-774b0de9b90a/data"
## Calling in dataset
apiDataset = request.get ('https://data.cms.gov/data-api/v1/dataset/7171ef6c-a2cf-43d4-b8ab-774b0de9b90a/data')
## setting the variable as a json file format
apiDataset = apiDataset.json()
## check whether if it was success
print (apiDataset)

### Section 3
##   Connecting to bigquery and creating a bigquery client with specific json key
from google.cloud import bigquery 
gcp_project = 'fresh-booster-361204'
client = bigquery.Client.from_service_account_json(r'C:\Users\premd\Downloads\fresh-booster-361204-ef0c0b10b27b.json')
## querying public dataset 1
## dataset_1 query only returning first 100 rows
query_job = client.query("SELECT * FROM `patents-public-data.google_patents_research.publications_201710` LIMIT 100")
## getting results of query
results = query_job.result()
## use "pip install db db-dtypes if terminal says its not functioning"
Bigquery1 = pd.Dataframe(results.to_dataframe())
Bigquery1

client = bigquery.Clinet.from_service_account_json(r'C:\Users\premd\Downloads\fresh-booster-361204-ef0c0b10b27b.json')
### Querying public dataset 2
## dataset_2 query only returning first 100 rows
query_job = client.query("SELECT * FROM `patents-public-data.google_patents_research.publications_201802` LIMIT 100")

## getting results of query 
results = query_job.result()
## putting the results into dataframe as the variable bigquery 2
Bigquery2 = pd.Dataframe(results.to_dataframe())
Bigquery2

## check whether if it was success
print(bigquery1, '/n', bigquery2)