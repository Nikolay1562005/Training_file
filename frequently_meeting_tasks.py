str = input('Введите строку (в строке минимально должно быть 6 разных символов): \n')  #  Ввод строки для анализа
frequently_meeting = {letter: str.count(letter) for letter in set(str)} #  Создание частотного списка
#  при помощи втроенной возможности функции сортировки в виде ключа,
#  который является методом который применяет записанную в ней функцию к итерируемому объекту (тоесть перебираются значения по очереди)
frequently_meeting_sotred = sorted(frequently_meeting, key=lambda iter: frequently_meeting[iter])
# Функция ниже делает точно также только тут используется функция get которая по ключу возвращяет значения и их уже сортирует  sorted
# frequently_meeting = sorted(frequently_meeting, key=frequently_meeting.get)
# Заменяем буквы в строке
finished_str = str.replace(frequently_meeting_sotred[-1], frequently_meeting_sotred[0]).replace(frequently_meeting_sotred[-2], frequently_meeting_sotred[1]).replace(frequently_meeting_sotred[-3], frequently_meeting_sotred[2])
print(finished_str)