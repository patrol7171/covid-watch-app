from flask_cors import CORS
import os
import flask
from flask import Flask, render_template, json, request, redirect, url_for, jsonify
import requests
import pandas as pd
import api_utils as au
import config



app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

###**CONFIG FOR LOCAL DEV**### -->
# app.config.from_object(config.DevelopmentConfig)

# ###**CONFIG FOR PRODUCTION**### -->
app.config.from_object(config.ProductionConfig)

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')

local_csv_path1 = "./static/data/us_covid_data.csv"
local_csv_path2 = "./static/data/country_covid_data.csv"
local_json_path = "./static/data/timestamp.json"

#Create csv file of downloaded data
au.get_us_data()


@app.route('/home', methods=['GET'])
def home():
    #Top 10 US states with highest # of total cases -->
    labels1, data1 = get_top10_chart_data('TotalCases')
    legendLabel1 = 'COVID-19 Case Total'    
    #Top 10 US states with highest # of deaths -->
    labels2, data2 = get_top10_chart_data('TotalDeaths')
    legendLabel2 = 'COVID-19 Death Total'
    #Top 10 US states with highest # of tests -->
    labels3, data3 = get_top10_chart_data('TotalTests')
    legendLabel3 = 'COVID-19 Test Total' 
    #Last date and time data was updated on World-o-meter site -->
    json_obj = get_timestamp()
    timestamp = json_obj['last_updated']
    
    return flask.jsonify({'timestamp':timestamp, 'data1':data1, 'legendLabel1':legendLabel1, 'labels1':labels1, 'data2':data2, 'legendLabel2':legendLabel2, 'labels2':labels2, 'data3':data3, 'legendLabel3':legendLabel3, 'labels3':labels3})


@app.route('/topTenUSCovidCases', methods=['GET'])
def topTenUSCovidCases():
    #Top 10 US states with highest # of total cases -->
    labels1, data1 = get_top10_chart_data('TotalCases')
    legendLabel1 = 'COVID-19 Case Total'   
    #Top 10 US states with highest # of cases per 1 million population -->
    labels2, data2 = get_top10_chart_data('Totcase1M')
    legendLabel2 = 'COVID-19 Case Total Per 1M Population' 
    #Last date and time data was updated on World-o-meter site -->
    json_obj = get_timestamp()
    timestamp = json_obj['last_updated']    
    
    return flask.jsonify({'timestamp':timestamp, 'data1':data1, 'legendLabel1':legendLabel1, 'labels1':labels1, 'data2':data2, 'legendLabel2':legendLabel2, 'labels2':labels2})


@app.route('/totalUSCovidCases', methods=['GET'])
def totalUSCovidCases():
    labels, data = get_all_chart_data('TotalCases')
    legendLabel = 'COVID-19 Case Total' 
    #Last date and time data was updated on World-o-meter site -->
    json_obj = get_timestamp()
    timestamp = json_obj['last_updated']    
    
    return flask.jsonify({'timestamp':timestamp, 'data':data, 'legendLabel':legendLabel, 'labels':labels})


@app.route('/topTenUSCovidDeaths', methods=['GET'])
def topTenUSCovidDeaths():
    #Top 10 US states with highest # of total deaths -->
    labels1, data1 = get_top10_chart_data('TotalDeaths')
    legendLabel1 = 'COVID-19 Death Total'   
    #Top 10 US states with highest # of deaths per 1 million population -->
    labels2, data2 = get_top10_chart_data('Totdeath1M')
    legendLabel2 = 'COVID-19 Death Total Per 1M Population' 
    #Last date and time data was updated on World-o-meter site -->
    json_obj = get_timestamp()
    timestamp = json_obj['last_updated']    
    
    return flask.jsonify({'timestamp':timestamp, 'data1':data1, 'legendLabel1':legendLabel1, 'labels1':labels1, 'data2':data2, 'legendLabel2':legendLabel2, 'labels2':labels2})


@app.route('/totalUSCovidDeaths', methods=['GET'])
def totalUSCovidDeaths():
    labels, data = get_all_chart_data('TotalDeaths')
    legendLabel = 'COVID-19 Death Total'
    #Last date and time data was updated on World-o-meter site -->
    json_obj = get_timestamp()
    timestamp = json_obj['last_updated']
    
    return flask.jsonify({'timestamp':timestamp, 'data':data, 'legendLabel':legendLabel, 'labels':labels})


@app.route('/topTenUSCovidTests', methods=['GET'])
def topTenUSCovidTests():
    #Top 10 US states with highest # of total tests -->
    labels1, data1 = get_top10_chart_data('TotalTests')
    legendLabel1 = 'COVID-19 Test Total'   
    #Top 10 US states with highest # of tests per 1 million population -->
    labels2, data2 = get_top10_chart_data('Tottest1M')
    legendLabel2 = 'COVID-19 Test Total Per 1M Population' 
    #Last date and time data was updated on World-o-meter site -->
    json_obj = get_timestamp()
    timestamp = json_obj['last_updated']
    
    return flask.jsonify({'timestamp':timestamp, 'data1':data1, 'legendLabel1':legendLabel1, 'labels1':labels1, 'data2':data2, 'legendLabel2':legendLabel2, 'labels2':labels2})


@app.route('/totalUSCovidTests', methods=['GET'])
def totalUSCovidTests():
    labels, data = get_all_chart_data('TotalTests')
    legendLabel = 'COVID-19 Test Total'
    #Last date and time data was updated on World-o-meter site -->
    json_obj = get_timestamp()
    timestamp = json_obj['last_updated']
    
    return flask.jsonify({'timestamp':timestamp, 'data':data, 'legendLabel':legendLabel, 'labels':labels})



#**** CHART DATA PREP ****

def get_top10_chart_data(df_col):
    df = pd.read_csv(local_csv_path1)
    df[df_col] = df[df_col].str.replace(',', '').astype(int)    
    tctop10 = df.nlargest(10,df_col)
    labels = tctop10['State'].tolist()
    values_list = tctop10[df_col].tolist()
    integer_map = map(int, values_list)
    data = list(integer_map)
    
    return labels, data


def get_all_chart_data(df_col):
    df = pd.read_csv(local_csv_path1)
    df[df_col] = df[df_col].str.replace(',', '').astype(int) 
    labels = df['State'].tolist()
    values_list = df[df_col].tolist()
    integer_map = map(int, values_list)
    data = list(integer_map)
    
    return labels, data


def get_timestamp():
    f = open (local_json_path, "r")
    timestamp = json.loads(f.read())
    
    return timestamp
    


#**** DATA RETRIEVAL/DOWNLOAD ****

@app.route('/dwnld_us_chart_info', methods=['GET'])
def dwnld_us_chart_info():
    au.get_us_data()


@app.route('/dwnld_countries_chart_info', methods=['GET'])
def dwnld_countries_data():
    au.get_countries_data()



#**** APP ERROR HANDLING ****

@app.errorhandler(404)
def not_found(e):
    """Page not found."""
    return flask.render_template("404.html"),404
 

@app.errorhandler(400)
def bad_request(e):
    """Bad request."""
    return flask.render_template("400.html"),400


@app.errorhandler(500)
def server_error(e):
    """Internal server error."""
    return flask.render_template("500.html"),500



if __name__ == "__main__":
    app.run()