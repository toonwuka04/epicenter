from flask import Flask, render_template, request
import folium
import requests, json

url = ('http://newsapi.org/v2/everything?'
       'q=texas&weather'
       'from=2021-02-18&'
       'sortBy=popularity&'
       'apiKey=53a218ace3974c7990cad1a004593ee8')

news_response = requests.get(url)
news_json = news_response.json()
news = news_json["articles"][:15]

news_passed = ""
for article in news:
    news_passed += article["title"] + "::" + article["url"] + "---" + article["urlToImage"] + ",,,"

app = Flask(__name__, static_folder="static")

@app.route("/", methods=['GET', 'POST'])
def index():
    #map
    map1 = folium.Map(location=["29.7604", "-95.3698"], zoom_start=6, 
            tiles='https://api.mapbox.com/styles/v1/xdonaldduckftwx/cklf0uw4d35zq17med1sur2wa/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoieGRvbmFsZGR1Y2tmdHd4IiwiYSI6ImNrbGYwc2p3ajFlYTUyb3M0czJ1ODF2aXIifQ.9st5K9vntIAZ_nK1JnbbfA',
            attr="Navigation Mapbox Attribution")
    #map markers
    folium.Marker(location=["32.9791", "-96.8922"], popup="Newman Smith High School Center", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["30.284180", "-97.736430"], popup="Gregory Gymnasium Warming Center", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["30.293440", "-97.727371"], popup="Russell Lee Elementary School (Warm up)", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["30.735880", "-95.582910"], popup="Walker County Shelter", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["29.961850", "-95.373870"], popup="National Association of Christian Churches", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["30.400336", "-95.70874"], popup="Montgomery County Lone Star Community Center", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["30.2221109", "-95.7267013"], popup="Wildwood UMC Warming Center", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["32.9631139", "-96.726821"], popup="First Baptist Richardson", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["30.3978111", "-95.6134237"], popup="Madeley Ranch Elementry", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["29.4205326", "-98.4836466"], popup="Henry B. Gonzalez Convention Center", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["31.8573755", "-102.3447222"], popup="St. Elizabeth Ann Seaton Catholic Parish Gym", icon=folium.Icon(color="green"),).add_to(map1)
    folium.Marker(location=["31.847566", "-102.36907"], popup="Copper Rose Building Warming Center", icon=folium.Icon(color="green"),).add_to(map1)
    
    map1.save("templates/map.html") 
    return render_template("index.html", map=map1, news=news_passed)

#allows map to be opened on index.html
@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gethelp')
def gethelp():
    return render_template('helpform.html')
