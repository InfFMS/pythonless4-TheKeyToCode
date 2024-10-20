# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def easy_numbers(num):
    answer = ""
    for i in range(2, num+1):
        while(num % i == 0):
            answer += str(i) + "*"
            num /= i
    answer = answer[0:-1]
    return answer
n = int(input("Введите число: "))
print(easy_numbers(n))
