import random
from tabulate import tabulate


class House:
    def __init__(self):
        self.population = random.randint(1, 100)


class Street:
    def __init__(self):
        self.houses = [House() for _ in range(random.randint(5, 20))]


class City:
    def __init__(self):
        self.streets = [Street() for _ in range(random.randint(3, 10))]

    def calculate_population(self):
        total_population = sum(house.population for street in self.streets for house in street.houses)
        return total_population

    def print_city_table(self):
        city_table = []
        for street_num, street in enumerate(self.streets, start=1):
            for house_num, house in enumerate(street.houses, start=1):
                city_table.append([street_num, house_num, house.population])

        headers = ["Вулиця", "Будинок", "Населення"]
        print(tabulate(city_table, headers=headers, tablefmt="grid"))


city = City()
city.print_city_table()
print(f"Загальне населення міста: {city.calculate_population()}")
