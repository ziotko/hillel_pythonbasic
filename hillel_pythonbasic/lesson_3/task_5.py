# 5. Користувач вводить число від 1 до 10, програма генерує рандомне число від 1 до 10, якщо числа співпадають надрукувати 'You won!' якщо ні - 'You lose!'.
# Дати користувачеві три спроби;)

import random

attempts = 3

for _ in range(attempts):
    user_number = int(input("Введіть число від 1 до 10: "))
    random_number = random.randint(1, 10)

    if random_number == user_number:
        print("You won!")
        break
    else:
        print("You lose!")

if user_number != random_number:
    pass
else:
    print("Гра закінчена. Ви не вгадали число.")