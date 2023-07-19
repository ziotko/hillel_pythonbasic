#2. У додатку є json файл. Написати програму, яка прочитає його та порахує загальну тривалість всіх треків в альбомі.

#  Базовий кейс - поверне кількість секунд.

#  * Дод. ускладнення повернути у вигляді рядка години:хвилини:секунди, прик. 0:41:39


import json as task_2


def calculate_total_duration(album_data):
    total_seconds = 0

    for track in album_data["tracks"]:
        duration_parts = track["duration"].split(":")
        hours = int(duration_parts[0])
        minutes = int(duration_parts[1])
        seconds = int(duration_parts[2])
        total_seconds += hours * 3600 + minutes * 60 + seconds

    return total_seconds


def format_duration(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"


with open("task_2.json", "r") as file:
    album_data = task_2.load(file)

total_seconds = calculate_total_duration(album_data)
formatted_duration = format_duration(total_seconds)

print("Длительность всех треков в секундах:", total_seconds)
print("Длительность всех треков в формате часа: минуты: секунды:", formatted_duration)
