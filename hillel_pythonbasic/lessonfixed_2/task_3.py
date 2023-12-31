# 3. Довжина маршруту велоралі "100 кілометрів за 10 годин" - приблизно 100 кілометрів. Велосипедист Вася стартує з нульового кілометра маршруту та їде зі швидкістю `v` кілометрів на годину. На якій відмітці він зупиниться через `t` годин?
#
# Програма отримує на вхід значення `v` та `t`. Якщо `v > 0`, то Вася рухається у позитивному напрямку за маршрутом, якщо ж значення `v < 0`, то негативному.
#
# Програма має вивести ціле число від 0 до 100 – номер позначки, на якій зупиниться Вася.

v = int(input("Введіть швидкість (км/год): "))
t = int(input("Введіть час (год): "))

position = v * t

print(f"Вася зупиниться на {position} км від початку маршруту.")
