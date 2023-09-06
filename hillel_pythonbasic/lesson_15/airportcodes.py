import csv


class AirportNotFoundError(Exception):
    def __init__(self, message, iata_code):
        self.message = message
        self.iata_code = iata_code


class CountryNotFoundError(Exception):
    def __init__(self, message, country):
        self.message = message
        self.country = country


class IATACodeError(Exception):
    def __init__(self, message):
        self.message = message


class MultipleOptionsError(Exception):
    def __init__(self, message):
        self.message = message


class NoOptionsFoundError(Exception):
    def __init__(self, message):
        self.message = message


def search_airports(parameter, value):
    airports = []
    with open('airport-codes_csv.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            airports.append(row)

    if parameter == 'iata_code':
        if len(value) != 3 or not value.isupper():
            raise IATACodeError('IATA code must be exactly 3 uppercase letters')
        result = [airport for airport in airports if airport['IATA_code'] == value]
        if not result:
            raise AirportNotFoundError('Airport not found', value)
        elif len(result) > 1:
            raise MultipleOptionsError('Multiple airports found')
        return result[0]

    elif parameter == 'country':
        result = [airport for airport in airports if airport['Country'] == value]
        if not result:
            raise CountryNotFoundError('Country not found', value)
        return result

    elif parameter == 'name':
        result = [airport for airport in airports if value.lower() in airport['Airport_name'].lower()]
        if not result:
            raise AirportNotFoundError('Airport not found', value)
        return result

    else:
        raise ValueError('Invalid parameter')


# Приклад використання:
try:
    parameter = input("Введіть параметр пошуку (iata_code/country/name): ").strip().lower()
    value = input("Введіть значення для пошуку: ").strip()

    result = search_airports(parameter, value)

    if isinstance(result, list):
        if len(result) == 1:
            print("Знайдено 1 аеропорт:")
        else:
            print(f"Знайдено {len(result)} аеропортів:")
        for airport in result:
            print(f"IATA код: {airport['IATA_code']}, Назва: {airport['Airport_name']}, Країна: {airport['Country']}")
    else:
        print("Знайдено аеропорт:")
        print(f"IATA код: {result['IATA_code']}, Назва: {result['Airport_name']}, Країна: {result['Country']}")
except (IATACodeError, AirportNotFoundError, CountryNotFoundError, MultipleOptionsError, NoOptionsFoundError) as e:
    print(e.message)
