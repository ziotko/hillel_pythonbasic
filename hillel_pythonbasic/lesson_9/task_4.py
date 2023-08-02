# 4. Написати функцію яка замінить у тексті слово на інше.
#
#  Функція приймає 4 аргументи, початковий рядок, слово, що замінюється, нове слово, кількість замін, приклад:
#
#  fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1) -> 'Marvel makes good movies, DC makes good comics'
#
#  fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2) -> 'Marvel makes good movies, Marvel makes good comics'

def fake_string(original_str, old_word, new_word, replacements):
    words = original_str.split()

    replaced_str = ' '.join(new_word if word == old_word and replacements > 0 else word for word in words)
    return replaced_str


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))

print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2))
