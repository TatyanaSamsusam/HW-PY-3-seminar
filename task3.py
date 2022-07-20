# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

import random
list_of_nums = []
for i in range(1,6):
    list_of_nums.append(random.random()*100)
print(list_of_nums)

max = list_of_nums[0] - int(list_of_nums[0])
min = list_of_nums[0] - int(list_of_nums[0])

for i in list_of_nums:
    number = i - int(i)
    if number > max:
        max = number
    if number < max:
        min = number

diff = max - min
print(f'разница между {max:.3f} и {min:.3f} равна {diff:.3f}')
