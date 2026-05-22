import requests

class WeatherTool:

    def __init__(self, api_key):

        self.api_key = api_key

    def invoke(self, city, country):
        print(f"\nFetching weather for {city}, {country}")

        # print(f"API Key: {self.api_key}")
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={self.api_key}&units=metric"

        weather_response = requests.get(weather_url)

        data = weather_response.json()

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "weather":
                data["weather"][0]["description"],
            "wind_speed":
                data["wind"]["speed"]
        }

        