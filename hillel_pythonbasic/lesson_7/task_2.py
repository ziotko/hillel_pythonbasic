# 2. Написати калькулятор температури.
#
#     Користувач вводить число та тип температури (C, F, K - Цельсій, Фарренгейт, Кельвін відповідно)
#
#     Програма має вивести температуру у трьох шкалах температур – Цельсій, Фарренгейт, Кельвін.


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9 / 5 - 459.67


def temperature_converter():
    temperature = float(input("Введите значение температуры: "))
    temp_type = input("Введите тип температуры (C, F, K): ").upper()

    if temp_type == 'C':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif temp_type == 'F':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif temp_type == 'K':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Некорректный тип температуры.")
        return

    print(f"{celsius:.2f} °C")
    print(f"{fahrenheit:.2f} °F")
    print(f"{kelvin:.2f} K")


if __name__ == "__main__":
    temperature_converter()
