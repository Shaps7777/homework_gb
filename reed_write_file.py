"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

# with open('wr.txt', 'w', encoding='utf-8') as fw:
#     while True:
#         line = input('Введите строку - ')
#         if not line:
#             break
#         fw.write(f'{line}\n')

"""
2. Создать текстовый файл (не программно), 
сохранить в нем несколько строк, 
выполнить подсчет количества строк, 
количества слов в каждой строке.
"""
# with open('wr.txt', 'r', encoding='utf-8') as fr:
#     usefullness = [f'{num}.{" ".join(line.split())} - {len(line.split())} слов '
#                    for num, line in enumerate(fr, 1)]
#     print(*usefullness, f'всего строк - {len(usefullness)}.', sep='\n')

"""
3. Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников 
и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""
# with open('fio.txt', 'r', encoding='utf-8') as fr:
#     empl_dict = {line.split()[0]: float(line.split()[1]) for line in fr}
#     for key in empl_dict:
#         print(key, empl_dict[key])
#     print(f'Всего рабочих: {len(empl_dict)}\n')
#     print(f'Средняя з/пл = {round(sum(empl_dict.values()) / len(empl_dict))}\n'
#           f'Рабочие с з/пл меньше 20000: {[el[0] for el in empl_dict.items() if el[1] < 20000]}')
#     print(len(empl_dict))
"""
4. Создать (не программно) текстовый файл 
со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, 
открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""
# rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
# with open('kir_lat.txt', 'w', encoding='utf-8') as fw:
#     with open('lat_kir.txt', 'r', encoding='utf-8') as fr:
#         fw.write(str([line.replace(line.split()[0],
#         rus_dict.get(line.split()[0])) for line in fr]))
"""
5. Создать (программно) текстовый файл, 
записать в него программно набор чисел, 
разделенных пробелами. Программа должна 
подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

with open('num_sum.txt', mode='w+', encoding='utf-8') as f:
    f.write(" ".join([str(randint(1, 100)) for _ in range(100)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))
"""
6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет 
и наличие лекционных, практических и лабораторных занятий 
по этому предмету и их количество. Важно, 
чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

""""
7. Создать (не программно) текстовый файл, 
в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, 
вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, 
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать 
словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, 
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта 
в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
