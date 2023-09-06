import re


def format_phone_number(input_str):
    digits = re.sub(r'\D', '', input_str)

    if len(digits) == 10:
        formatted_number = f"(+38) {digits[:3]} {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
        return formatted_number
    else:
        return "Failed to recognize number"


input_str = input("Введіть номер телефону: ")
result = format_phone_number(input_str)
print(result)


