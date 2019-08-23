# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacci_list = []
    start_number_1 = 1
    start_number_2 = 1
    while start_number_2 < m:
        if start_number_2 > n:
            fibonacci_list.append(start_number_2)
        start_number_1, start_number_2 = start_number_2, start_number_1 + start_number_2
    return fibonacci_list

print(*fibonacci(int(input()), int(input())))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    idx = 0
    indicator = False
    len_list = len(origin_list)
    if len_list == 0:
        return []
    while idx < len_list:
        if (idx + 1 != len_list) and (origin_list[idx] > origin_list[idx + 1]):
            origin_list[idx], origin_list[idx + 1] = origin_list[idx + 1], origin_list[idx]
            indicator = True
        idx += 1
        if (idx == len_list) and indicator:
            indicator = not indicator
            idx = 0
    return (origin_list)

print(*sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(filter_func, list_filter):
    list_result = []
    for idx in list_filter:
        if filter_func(idx):
            list_result.append(idx)
    return list_result

print(my_filter(lambda x: x == abs(x), [-10, 0, 234, -123672, 9, 80, 123, 4527783746, -2, 876]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('Введите координаты точек')
coordinate = []
i = 1
while i <= 4:
    coordinate.append([float(input(f'x{i} = ')), float(input(f'y{i} = '))])
    i += 1
coordinate = list(zip(coordinate[0], coordinate[1], coordinate[2], coordinate[3]))
coord_1 = list(coordinate[0])
coord_2 = list(coordinate[1])
coord_1.sort()
coord_2.sort()
if ((coord_1[1] - coord_1[0]) == (coord_1[-1] - coord_1[-2])) and ((coord_2[1] - coord_2[0]) == (coord_2[-1]-coord_2[-2])):
    print('Параллелограмм')
else:
    print('Не параллелограмм')