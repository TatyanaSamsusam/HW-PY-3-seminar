# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input('введите десятичное число, и я переведу его в двоичное: '))

def find_binary_digit (num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    return(result)

binary_digit = find_binary_digit(number)
print(f'двоичное число: {binary_digit}')

