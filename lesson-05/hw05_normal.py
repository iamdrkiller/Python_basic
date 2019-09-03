# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import easy
main_menu = {
    '1': ['. Перейти в папку', easy.get_dir],
    '2': ['. Просмотреть содержимое текущей папки', easy.lst_current_dir],
    '3': ['. Удалить папку', easy.del_dir],
    '4': ['. Создать папку', easy.creat_dir],
    '5': ['. Выход', easy.exit_prog],
}

while True:
    for key in main_menu:
        print(key, main_menu[key][0], end='\n')
    key = input()
    if key.isdigit():
        if (int(key) < 1) or (int(key) > 5):
            key = None
            print('Номер пункта меню - целое число от 1 до 5')
    else:
        print('Введите номер пункта меню.')
        key = None
    if key:
        if main_menu.get(str(key)):
            main_menu[str(key)][1]()