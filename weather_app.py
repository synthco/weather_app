import datetime as dt 
import json 
import weather_struct
import requests
from flask import Flask, jsonify, request

API_TOKEN = "f0r_w3ath3r_use_0nly"
RSA_KEY = "cfee65c7b176da50b5efd2d377c470c2"

app = Flask(__name__)

    
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        self.message = message 
        if status_code is not None:
            self.status_code = status_code

        self.payload = payload

    def to_dict(self):
        res = dict(self.payload or ())
        res ["message"] = self.message
        return res
    

def get_weather(exclude: str, limit:int = 1):
    url_base = "https://api.openweathermap.org/data/2.5/weather?"
    limit = 1
    location = "Kyiv"

    date_obj = dt.datetime.now()
    # date = date_obj.strftime("%Y-%m-%d")
    units = "metric"
    url = url_base + "q=" + location + "&appid=" + RSA_KEY +"&units=" + units

    response = requests.get(url)
    # return json.loads(response.text)
    
    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    else:
        raise InvalidUsage(response.text, status_code=response.status_code)
    

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    res = jsonify(error.to_dict())
    res.status_code = error.status_code
    return res

@app.route("/")
def home_page():
    return "<p><h2> It's a weather. And I'm working =) </h2></p>"

@app.route("/content/api/integration/get/weather", methods=["POST"])  #Try to change path
def weather_endpoint():
    start_time = dt.datetime.now()
    json_data = request.get_json()

    if json_data.get("token") is None:
        raise InvalidUsage("There no token =( ", status_code=400)

    token = json_data.get("token")

    if token != API_TOKEN:
        raise InvalidUsage("Wrong API token, try to use smth else =( ", status_code=403)

    exclude = ""
    if json_data.get("exclude"):
        exclude = json_data.get("exclude")

    weather_data = get_weather(exclude)
    weather = weather_struct.Weather(weather_data)
    end_time =dt.datetime.now()

    result ={
        "event_start_datetime": start_time.isoformat(),
        "event_finished_datetime": end_time.isoformat(),
        "event_duration": str(end_time - start_time),
        "weather": str(weather.to_dict()),
        "description": weather.conclusion()
    }
    return result
    

if __name__ == "__main__":
    app.run(debug=True)


    




