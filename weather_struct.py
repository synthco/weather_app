class Weather:
    def __init__(self, data):
        self._data = data
        self.temperature = None
        self.wind_speed = None 
        self.wind_gust = None
        self.pressure = None
        self.city_name = None 
        self.descript = None
        self.__parce()

    def __parce (self):
        self.temperature = self._data["main"]["temp"]
        self.wind_speed = self._data["wind"]["speed"]
        self.wind_gust = self._data["wind"]["gust"]
        self.pressure = self._data["main"]["pressure"]
        self.city_name = self._data["name"]
        self.descript = self._data["weather"][0]["description"]
    def to_dict(self) -> dict:
        weather_dict = {
            "city_name": self.city_name,
            "temperature": self.temperature,
            "wind": {
                "speed": self.wind_speed,
                "gust": self.wind_gust
            },
            "pressure": self.pressure
        }
        return weather_dict
        
    def conclusion(self) -> str:
        # temperature
        if self.temperature >= 25:
            con_temp = "Damn it's hot"
        elif self.temperature <= 10:
            con_temp = "Eewww, it's freezing"
        else:
            con_temp = "Meh, it's just there"

        # wind
        if self.wind_speed > 15:
            con_wind = "Thanks for the good hairstyle, it's windy..."
        elif self.wind_speed < 5:
            con_wind = "A gentle breeze, how delightful..."
        else:
            con_wind = "The wind is doing its thing, I guess..."

        #main state
        

        conclusion = f"{con_temp}. {con_wind}. And it's {self.descript}. Wonderful..."

        return conclusion


# data = {'coord': {'lon': 30.5167, 'lat': 50.4333}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 276.54, 'feels_like': 276.54, 'temp_min': 275.71, 'temp_max': 277.96, 'pressure': 1007, 'humidity': 94}, 'visibility': 10000, 'wind': {'speed': 0.89, 'deg': 42, 'gust': 2.24}, 'clouds': {'all': 92}, 'dt': 1707932731, 'sys': {'type': 2, 'id': 2003742, 'country': 'UA', 'sunrise': 1707887570, 'sunset': 1707923499}, 'timezone': 7200, 'id': 703448, 'name': 'Kyiv', 'cod': 200}
# print(data["main"].keys())

# w = Weather(data)
# print(w.to_dict())
# print(w.conclusion())