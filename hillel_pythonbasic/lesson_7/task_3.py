# 3. Отримати прогноз погоди для Одеси на наступні 5 днів та записати у файл з ім'ям поточної дати
#
# http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8
#
#  Параметр cnt = кількість днів
#  Параметр q = місто
#  Так ми отримаємо та обробимо дату з відповіді (ключ dt):
#
#  datetime.datetime.fromtimestamp(1600419600)
#  Застосувавши до отриманого об'єкта дати strftime("%d-%m-%Y") отримаємо строкову дату для запису у файл.
#
#  Приклад імені файлу: 19-09-2020-Odessa-5-days-weather-forecast.txt
#  Записаний файл має виглядати так:
#
#  Дата Температура вдень
#  18-09-2020 17.86 11.18
#  19-09-2020 15.75 11.21
#  20-09-2020 20.37 17.49
#  21-09-2020 20.75 18.08
#  22-09-2020 20.96 17.47
#   * Дод. надати користувачеві вибір міста та кількості днів, а також додати колонку Температура вночі

import requests
import datetime


def get_weather_forecast(city, days):
    api_key = "f9ada9efec6a3934dad5f30068fdcbb8"
    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={days}&units=metric&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["list"]
    else:
        print("Ошибка при получении данных о погоде.")
        return None


def write_weather_forecast_to_file(city, days, forecast):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    filename = f"{current_date}-{city}-{days}-days-weather-forecast.txt"

    with open(filename, "w") as file:
        file.write("Дата Температура вдень Температура вночі\n")
        for day in forecast:
            date = datetime.datetime.fromtimestamp(day["dt"]).strftime("%d-%m-%Y")
            day_temp = day["temp"]["day"]
            night_temp = day["temp"]["night"]
            file.write(f"{date} {day_temp:.2f} {night_temp:.2f}\n")


if __name__ == "__main__":
    city = input("Введите название города: ")
    days = int(input("Введите количество дней для прогноза (целое число): "))

    weather_forecast = get_weather_forecast(city, days)
    if weather_forecast:
        write_weather_forecast_to_file(city, days, weather_forecast)
        print("Прогноз погоды успешно записан в файл.")
