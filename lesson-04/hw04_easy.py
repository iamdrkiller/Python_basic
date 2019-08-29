# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
lst_main = [random.randint(-100, 100) for _ in range(random.randint(1, 50))]
print(lst_main)
new_lst = [_**2 for _ in lst_main]
print(new_lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

import random
lst_fruit_main = ['Алыча', 'Ананас', 'Астрокариум колючий', 'Бакау', 'Баэль', 'Вампи', 'Виноград', 'Воаванга',
                  'Генипа', 'Горлянка', 'Гранадилла сладкая', 'Гранат', 'Десертный квандонг', 'Дуку', 'Дуриан',
                  'Земляничная груша', 'Индийский инжир', 'Каламондин', 'Киви', 'Лимон Мейера', 'Маракуйя']
lst_random_1 = [lst_fruit_main[_] for _ in [random.randint(0, len(lst_fruit_main)-1) \
                                            for __ in range(random.randint(1, len(lst_fruit_main)))]]
lst_random_2 = [lst_fruit_main[_] for _ in [random.randint(0, len(lst_fruit_main)-1) \
                                            for __ in range(random.randint(1, len(lst_fruit_main)))]]
lst_random_1.sort()
lst_random_2.sort()
print(lst_random_1, '\n', lst_random_2)
if len(lst_random_1) < len(lst_random_2):
    lst_filter = [_ for _ in lst_random_1 if _ in lst_random_2]
else:
    lst_filter = [_ for _ in lst_random_2 if _ in lst_random_1]
print(lst_filter)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
lst_main = [random.randint(-100, 100) for _ in range(random.randint(1, 50))]
print(lst_main)
lst_result = [_ for _ in lst_main if (_ % 3 == 0) and (_ > 0) and (_ % 4 != 0)]
print(lst_result)