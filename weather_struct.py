class Weather:
    def __init__(self, data):
        self._data = data
        self.temperature = None
        self.wind_speed = None 
        self.pressure = None
        self.city_name = None 
        self.descript = None
        self.__parce()

    def __parce (self):

        
        self.temperature = self._data["main"]["temp"]
        self.wind_speed = self._data["wind"]["speed"]
        self.pressure = self._data["main"]["pressure"]
        self.city_name = self._data["name"]
        self.descript = self._data["weather"][0]["description"]

    def to_dict(self) -> dict:
        weather_dict = {
            "city_name": self.city_name,
            "temperature": self.temperature,
            "wind": {
                "speed": self.wind_speed,
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

        conclusion = f"{con_temp}. {con_wind}. And it's {self.descript} in {self.city_name}. Wonderful..."

        return conclusion

