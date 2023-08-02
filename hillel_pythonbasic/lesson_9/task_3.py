# 3. Написати функцію яка поверне найдовше слово у рядку:
#
# longest_word("What makes a good man") -> makes

def longest_word(sentence):

    words = sentence.split()

    longest = max(words, key=len)

    return longest


print(longest_word("hello my friend what's up?"))
