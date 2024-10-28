# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def GCD(a,b): #greatest common divisor
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a


a, b = map(int,input("Введите 2 числа в 1 строку: ").split())
print(GCD(a,b))
