# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

number = int(input('Введите количество видов фруктов\n'))
print('Введите названия фруктов')
i = 0
fruits = []
max_len = 0
while i < number:
    fruits.append(input())
    if len(fruits[i]) > max_len:
        max_len = len(fruits[i])
    i = i + 1

#Выводим
i = 0
while i < number:
    space  = ' ' * (max_len - len(fruits[i]) +1)
    print(f'{i+1}.{space}{fruits[i].title()}')
    i = i + 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = [1, 4, 78, 35, 19, 456, 'r', 'h', '']
list_2 = [4, 67, 892, 35, 'hello', 'world', 'h']
set_1 = set(list_1)
set_2 = set(list_2)
set_filter = set_1.difference(set_2)
list_final = list(set_filter)
print(list_final)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_number = [2, 8, 129, 36, 287, 8, 916, 34567, 917643, 6, 99]
list_final = []
for i in list_number:
    if (i % 2) == 0:
        list_final.append(i / 4)
    else:
        list_final.append(i * 2)
print(list_final)