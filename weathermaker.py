from bs4 import BeautifulSoup
import requests


class WeatherMaker:

    def __init__(self):
        self.path = 'https://yandex.ru/pogoda/krasnodar/'
        self.selector_temperature = '.temp.forecast-briefly__temp.forecast-briefly__temp_day .temp__value'
        self.selector_weather = '.forecast-briefly__condition'
        self.selector_dates = '.time.forecast-briefly__date'
        self.parse_weather = list()

    def run(self):
        for date, temperature, weath in self.parser():
            iter_weather = {
                'weather': weath.text,
                'temperature': temperature.text,
                'date': date
            }
            self.parse_weather.append(iter_weather)

    def parser(self):
        response = requests.get(self.path)
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            temperatures = html_doc.select(self.selector_temperature)
            weather_status = html_doc.select(self.selector_weather)
            dates = [item['datetime'] for item in html_doc.select(self.selector_dates)]
            return zip(dates, temperatures, weather_status)


def get_weather():
    weather = WeatherMaker()
    weather.run()
    return weather.parse_weather
