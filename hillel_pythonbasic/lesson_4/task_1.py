def find_day(x, y):
    distance = x
    day = 1

    while distance < y:
        distance += distance * 0.1
        day += 1

    return day


x = float(input("Введите расстояние, пробежанное в первый день (x): "))
y = float(input("Введите желаемое расстояние (y): "))

result = find_day(x, y)
print("Номер дня, на который расстояние составляет не менее", y, "километров:", result)
