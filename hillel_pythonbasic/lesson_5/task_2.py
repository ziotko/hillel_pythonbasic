#2. Написати програму яка поверне кількість введених користувачем слів та загальну кількість символів.
def count_words_and_characters():
    user_input = input("Введите текст: ")
    words = user_input.split()
    word_count = len(words)
    character_count = len(user_input)

    print("Количество слов: ", word_count)
    print("Общее количество символов: ", character_count)


count_words_and_characters()
