import os
import sys

def path_dir(directory):
    if (directory in os.listdir(os.getcwd())) and os.path.isdir(os.path.join(os.getcwd(), directory)):
        return os.path.join(os.getcwd(), directory)
    else:
        return directory

def get_dir():
    try:
        os.chdir(path_dir(input('Введите имя папки (краткое, если папка находится в текущей, или полное): ')))
        print('Текущая папка изменена')
    except FileNotFoundError:
        print('Ошибка в указанном пути')

def lst_current_dir():
    return print(f'Список папок в текущей папке "{os.getcwd()}":\n',
                 [_ for _ in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), _))])

def del_dir():
    try:
        os.rmdir(path_dir(input('Введите имя папки (краткое, если папка находится в текущей, или полное): ')))
        print('Папка удалена')
    except FileNotFoundError:
        print('Указанной папки не существует')

def creat_dir():
    try:
        os.mkdir(input('Введите имя папки (краткое, папка будет создана в текущей): '))
        print('Папка создана')
    except FileExistsError:
        print('Указанная папка уже существует')

def exit_prog():
    input('Для завершения работы программы нажмите "Ввод"')
    sys.exit(0)