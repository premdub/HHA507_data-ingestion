from openpyxl import Workbook
import pandas as pd # import pandas for general files
import json # import json for json files
import requests # import requests for web requests
import xlrd # import xlrd for excel files, tab names

##This is command so i can read xl file
df = pd.read_excel('data\\assignment data.xlsx')
df

## Section 1
import xlrd
data = xlrd.open_workbook('data\\assignment_data.xls', on_demand=True)
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



### Section 3
##   Connecting to bigquery and create json file
import pandas as pd
import json 
import requests 
from google.cloud import bigquery 
##gcp_project = 'fresh-booster-361204'
client = bigquery.Client.from_service_account_json(r'data\fresh-booster-361204-ef0c0b10b27b.json')
## querying public dataset 1
## dataset_1 query only returning first 100 rows
query_job = client.query("SELECT * FROM `bigquery-public-data.covid19_open_data.covid19_open_data` LIMIT 100")
## getting results of query
results = query_job.result()
results
## putting the results into dataframe 
bigquery1 = pd.DataFrame(results.to_dataframe())
bigquery1


client = bigquery.Client.from_service_account_json('fresh-booster-361204-ef0c0b10b27b.json')
### Querying public dataset 2
## dataset_2 query only returning first 100 rows
query_job = client.query("SELECT * FROM `bigquery-public-data.covid19_italy_eu.data_by_province` LIMIT 100")
## getting results of query 
results = query_job.result()
## putting the results into dataframe 
Bigquery2 = pd.DataFrame(results.to_dataframe())
Bigquery2

## check whether if it was success
print(bigquery1, '/n', Bigquery2)
