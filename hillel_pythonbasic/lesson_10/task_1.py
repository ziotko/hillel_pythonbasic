def main():
    filename = input("Введите имя файла (вместе с расширением .txt): ")

    try:

        with open(filename, 'w') as file:
            while True:

                text = input("Введите текст (пустая строка для завершения): ")

                if text == "":
                    break

                file.write(text + '\n')

        print("Данные успешно записаны в файл", filename)

    except Exception as e:
        print("Произошла ошибка:", str(e))


if __name__ == "__main__":
    main()
