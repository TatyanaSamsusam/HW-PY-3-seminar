# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

number = int(input('введите число, и я покажу список Фибоначчи: '))

def Fibonacci_positive (num):
    fibo_list = [0, 1]
    for i in range (2, num +1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return(fibo_list)

pos_res = Fibonacci_positive(number)

def Fibonacci_negative(num):
    fibo_list = [0,1]
    for i in range (2,num +1):
        fibo_list.append(fibo_list[i-2] - fibo_list[i-1])
    return(fibo_list)

neg_res = Fibonacci_negative(number)

negative_reversed = list(reversed(neg_res))

final_list = negative_reversed + pos_res[1:]
print(final_list)