"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран. Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

from re import compile

result = {}

with open('5-06-subj.txt', 'r') as file:
    for line in file:
        # Фильтр символов
        filter1 = compile('[^a-zA-Zа-яА-Я0-9 ]')
        # Фильтр букв
        filter2 = compile('[^0-9 ]')

        # Записываем в переменную предмет
        elems = filter1.sub('', line).split(' ')
        subj = elems.pop(0)

        # Считаем общий балл
        mark = 0
        for num in elems:
            num = filter2.sub('', num)
            if num != '':
                mark += int(num)

        # Заполняем словарь
        result.update({subj: mark})

print(result)
