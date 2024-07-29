import requests
import json

API_KEY = "af59b8c618b44925b2955707242802"
URL = "http://api.weatherapi.com/v1/current.json"


class Weather:

    @staticmethod
    def location(loc):
        params = {
            "key": API_KEY,
            "q": loc
        }
        data = (requests.get(url=URL, params=params)).json()
        print(data["current"]["condition"]["text"])
        di = {"temp_c": int(data["current"]["temp_c"]),
              "name": data["location"]["name"],
              "country": data["location"]["country"],
              "condition": data["current"]["condition"]["text"]}
        return di
