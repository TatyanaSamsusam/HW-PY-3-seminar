# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

list_of_nums = []
for i in range(1,10):
    list_of_nums.append (randint(0, 10))
print(list_of_nums)

def find_sum_of_odd_elements (some_list):
    result = 0
    for i in range (1, len(some_list),2):
        result = result + some_list[i]
    return(result)

sum = find_sum_of_odd_elements(list_of_nums)
print (f'сумма элементов списка, стоящих на нечётной позиции, равна {sum}')

