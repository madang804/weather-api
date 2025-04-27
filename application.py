from flask import Flask, request, jsonify
import random


application = Flask(__name__)

@application.route('/')
def home():
    return '''
        <h1>How to make an API call</h1>
        <h3>Append the following path and your chosen location after the url to get the current weather stat</h3>
        <ul>/api/v1.0/weather?location=<b>&#60;input location&#62;</b></ul>
        <h3>Append the following path and your chosen location after the url to get the current temperature stat</h3>
        <ul>/api/v1.0/temperature?location=<b>&#60;input location&#62;</b></ul>
        <h3>Append the following path and your chosen location after the url to get the current wind stat</h3>
        <ul>/api/v1.0/wind?location=<b>&#60;input location&#62;</b></ul>
    '''

@application.route('/api/v1.0/weather')
def weather():
    location = request.args.get('location')
    weather_list = ['rain', 'hurricanes', 'cloudy', 'partly cloudy', 'blizzard', 'tornado', 'thunderstorm', 'fog', 'lightning', 'snow', 'wind', 'hail', 'winter storm', 'stormy']
    weather = random.choice(weather_list)
    return jsonify({
        'location': location,
        'weather': weather
    })

@application.route('/api/v1.0/temperature')
def temperature():
    location = request.args.get('location')
    temperature = round(random.uniform(-20, 50), 2)
    return jsonify({
        'location': location,
        'temperature': f'{temperature} °C'
    })

@application.route('/api/v1.0/wind')
def wind():
    location = request.args.get('location')
    wind_speed = round(random.uniform(0, 100), 2)
    wind_direction = round(random.uniform(0, 360), 2)
    return jsonify({
        'location': location,
        'wind speed': f'{wind_speed} kts',
        'wind direction': f'{wind_direction} deg'
    })


