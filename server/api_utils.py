from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from datetime import datetime


local_csv_path1 = "./static/data/us_covid_data.csv"
local_csv_path2 = "./static/data/country_covid_data.csv"
local_json_path = "./static/data/timestamp.json"

def get_us_data():
    url = 'https://www.worldometers.info/coronavirus/country/us/'
    website_url=requests.get(url).text
    soup = BeautifulSoup(website_url,'html.parser')
    
    refresh_time = soup.find('div', style="font-size:13px; color:#999; text-align:center").get_text()
    date_dict = {}
    date_dict['last_updated'] = refresh_time[14:]
    out_file = open(local_json_path, "w") # Save timestamp dict as a json file
    json.dump(date_dict, out_file)    
    out_file.close() 

    my_table = soup.find('tbody')
    table_data = []
    for row in my_table.findAll('tr'):
        row_data = []
        for cell in row.findAll('td'):
            row_data.append(cell.text)
        if(len(row_data) > 0):
            data_item = {"RowNum": row_data[0],
                        "State": row_data[1],
                        "TotalCases": row_data[2],
                        "NewCases": row_data[3],
                        "TotalDeaths": row_data[4],
                        "NewDeaths": row_data[5],
                        "TotalRecovered": row_data[6],
                        "ActiveCases": row_data[7],
                        "Totcase1M": row_data[8],
                        "Totdeath1M": row_data[9],
                        "TotalTests": row_data[10],
                        "Tottest1M": row_data[11],
                        "Population": row_data[12],
            }
            table_data.append(data_item)

    df = pd.DataFrame(table_data)
    df = df.iloc[1: , :] #Drop USA totals which is the first line
    df = df.replace('\n','', regex=True) #Remove newline characters
    df = df.fillna(0) #Replace nan with zeroes
    df_sorted = df.sort_values(by = 'State')#Sort data in ABC order by State
    #Save data to csv
    df_sorted.to_csv(local_csv_path1, index = False)


def get_countries_data():
    non_countries=['Asia','North America','South America','Europe','Africa','Oceania']
    url = 'https://www.worldometers.info/coronavirus/#countries'
    website_url=requests.get(url).text
    soup = BeautifulSoup(website_url,'html.parser')
    my_table = soup.find('tbody')
    table_data = []

    for row in my_table.findAll('tr'):
        row_data = []
        for cell in row.findAll('td'):
            row_data.append(cell.text)
        testword = row_data[1]
        if(len(row_data) > 0 and testword not in non_countries and testword.isspace() == False):
            print(len(testword)) #TESTING
            data_item = {"Country": row_data[1],
                        "TotalCases": row_data[2],
                        "NewCases": row_data[3],
                        "TotalDeaths": row_data[4],
                        "NewDeaths": row_data[5],
                        "TotalRecovered": row_data[6],
                        "ActiveCases": row_data[7],
                        "CriticalCases": row_data[8],
                        "Totcase1M": row_data[9],
                        "Totdeath1M": row_data[10],
                        "TotalTests": row_data[11],
                        "Tottest1M": row_data[12],
                        "Population": row_data[13],
            }
            table_data.append(data_item)

    df = pd.DataFrame(table_data)
    df = df.iloc[1: , :] #Drop world totals which is the first line
    df = df.replace('\n','', regex=True) #Remove newline characters
    df = df.fillna(0) #Replace n/a with zeroes
    df_sorted = df.sort_values(by = 'Country')
    #Save data to csv--eventually will be a scheduled job
    df_sorted.to_csv(local_csv_path1, index = False)    

