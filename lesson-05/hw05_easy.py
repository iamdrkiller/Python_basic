# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys

def print_help():
    print('помощь - справка\nсоздать_папки - создание папок\nудалить_папки - удаление созданных папок')

def new_dir():
    for _ in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f'dir_{_}')
        try:
            os.mkdir(dir_path)
            print(f'Папка "dir_{_}" создана')
        except FileExistsError:
            print(f'Папка "dir_{_}" уже существует')

def del_dir():
    for _ in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f'dir_{_}')
        try:
            os.rmdir(dir_path)
            print(f'Папка "dir_{_}" удалена')
        except FileNotFoundError:
            print(f'Папки "dir_{_}" не существует')

do = {
    'помощь': print_help,
    'создать_папки': new_dir,
    'удалить_папки': del_dir,
}
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print('Указан неверный параметр, для получения справки введите "помощь"')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
import sys

def print_help():
    print('помощь - справка\nсписок_папок - список папок в текущей папке')

def lst_current_dir():
    return print(f'Список папок в текущей папке "{os.getcwd()}":\n',
                 [_ for _ in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), _))])

do = {
    'помощь': print_help,
    'список_папок': lst_current_dir,
}
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print('Указан неверный параметр, для получения справки введите "помощь"')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import sys
import shutil

def print_help():
    print('помощь - справка\nсоздать_копию - создание копии файла скрипта')

def copy_script():
    print(f'Путь к копии текущего скрипта:\n{os.getcwd()}/', shutil.copy(f'{sys.argv[0]}', f'copy_{sys.argv[0]}'))

do = {
    'помощь': print_help,
    'создать_копию': copy_script,
}
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print('Указан неверный параметр, для получения справки введите "помощь"')