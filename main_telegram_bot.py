import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Назовите город!")


@dp.message_handler()
async def get_weather(message: types.message):
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
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()


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

        await message.reply(f"****{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}****\n"
              f"Город: {city}\nТемпература: {cur_weather}C°{wd}\n"
              f"Температура максимальная: {temp_max}C°\n"
              f"Температура минимальная: {temp_min}C°\n"
              f"Скорость ветра: {wind}м/с\n"
              f"Рассвет: {sunrise_time}\n"
              f"Закат: {sunset_time}")




    except:
        await message.reply("Это то  название  города?")



if __name__ =='__main__':
    executor.start_polling(dp)

