# Написати програму "Онлайн конвертер валют". =)
#
# Додаток запитує користувача:
#
#   currency_from: string (default USD)
#   currency_to: string (default UAH)
# Перевірка введення параметра валют (from, to) має бути у symbols.json за ключом symbols
#
#   amount: float (default 100.00)
#   start_date:string
# (приклад. 2020-09-22 якщо дата не в цьому форматі, виставляти за замовчуванням дату поточного дня, якщо дата перевищує поточний день (майбутнє), також виставляємо дату поточного дня)
#
#   save_to_file: опціональний
#   Якщо дата менша чи дорівнює поточному дню, то від start_date до поточного йде ітерація:
#
#   Додаток робить GET запит:
#
#   https://api.exchangerate.host/convert
#   Параметри, що приймаються from, to, amount, date
#
# from=USD&to=UAH&amount=10000.5&date=2020-09-18
#   Підсумковий результат повинен бути точно в такому ж форматі (наприклад, якщо start_date == 2020-09-18):
#
#   [['date', 'from', 'to', 'amount', 'rate', 'result'],
#   ['2020-09-18', 'USD', 'UAH', 10000.5, 28.163466, 281648.743085],
#   ['2020-09-19', 'USD', 'UAH', 10000.5, 28.163466, 281648.737791],
#   ['2020-09-20', 'USD', 'UAH', 10000.5, 28.163455, 281648.630637],
#   ['2020-09-21', 'USD', 'UAH', 10000.5, 28.23733, 282387.419415],
#   ['2020-09-22', 'USD', 'UAH', 10000.5, 28.265772, 282671.854989]]
#   ** Введення даних повинно прийматися парсингом аргументів, модуль argparse.
#
#       У результаті, щоб була можливість запустити додаток командою:
#
#       python exchange_rates.py USD UAH 100 --start_date 2022-06-18 --save_to_file
#
#   *** Додати опцію: або збереження даних в файл, або виводу даних користувачеві.
#
#   **** Форматування даних для виводу: Зробити кожну клітину на відстані за допомогою ljust або tabulate

import requests
import argparse
from datetime import datetime, timedelta
from tabulate import tabulate


def get_exchange_rate(date, currency_from, currency_to, amount):
    url = "https://api.exchangerate.host/convert"
    params = {"from": currency_from, "to": currency_to, "amount": amount, "date": date}
    response = requests.get(url, params=params)
    data = response.json()
    return data["info"]["rate"], data["result"]


def main():
    parser = argparse.ArgumentParser(description="Online Currency Converter")
    parser.add_argument("currency_from", type=str, default="USD", help="Currency to convert from")
    parser.add_argument("currency_to", type=str, default="UAH", help="Currency to convert to")
    parser.add_argument("amount", type=float, default=100.00, help="Amount to convert")
    parser.add_argument("--start_date", type=str, default=None, help="Start date in the format YYYY-MM-DD")
    parser.add_argument("--save_to_file", action="store_true", help="Save data to a file")
    args = parser.parse_args()

    if args.start_date:
        try:
            start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
            if start_date > datetime.now():
                start_date = datetime.now()
        except ValueError:
            start_date = datetime.now()
    else:
        start_date = datetime.now()

    currency_from = args.currency_from
    currency_to = args.currency_to
    amount = args.amount

    table_data = [["date", "from", "to", "amount", "rate", "result"]]

    current_date = start_date
    while current_date <= datetime.now():
        date_str = current_date.strftime("%Y-%m-%d")
        rate, result = get_exchange_rate(date_str, currency_from, currency_to, amount)
        table_data.append([date_str, currency_from, currency_to, amount, rate, result])
        current_date += timedelta(days=1)

    if args.save_to_file:
        with open("exchange_rates.txt", "w") as f:
            for row in table_data:
                f.write("\t".join(str(cell) for cell in row))
                f.write("\n")
    else:
        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()

# python exchange_rates.py USD UAH 100 --start_date 2023-08-01 --save_to_file
