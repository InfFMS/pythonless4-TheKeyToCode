# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.

def reverse_number(num):
    delta = 1
    reverse_num=0
    while(delta<=num):
        reverse_num*=10
        reverse_num+=int(num/delta%10)
        delta*=10
    return reverse_num
a = int(input("Введите число: "))
print(reverse_number(a))
