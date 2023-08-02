# 2. Написати функцію яка частково приховуватиме e-mail, приклад:
#
#  hide_email(somebody_email@gmail.com) -> em***@**il.com

def hide_email(email):
    login, domain = email.split('@')

    hidden_login = login[:2] + '*' * 3 + login[-2:]

    hidden_email = hidden_login + '@' + domain

    return hidden_email


print(hide_email('vadym04@gmail.com'))
