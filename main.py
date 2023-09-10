import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002611",
        "Drizzle": "Ливень \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U00001F328 ",
        "Fog": "Туман \0000F32B"


    }

    try:
        r = requests.get(
           f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Выгляни  в окно"
        cur_weather = data["main"]["temp"]

        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        wind = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"****{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}****\n"
              f"Город: {city}\nТемпература:{cur_weather}C°{wd}\n"
              f"Температура максимальная:{temp_max}C°\n"
              f"Температура минимальная:{temp_min}C°\n"
              f"Скорость ветра:{wind}м/с\n"
              f"Рассвет:{sunrise_time}\n"
              f"Закат:{sunset_time}")




    except Exception as ex:
        print(ex)
        print("Это то  название  города?")

def main():
    city = input("Название города: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()




