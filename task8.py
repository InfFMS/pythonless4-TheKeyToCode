# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def is_prime_number(n):
    i=2
    while(i<n):
        if(n%i==0):
            return False
        i+=1
    return True

def prime_numbers(num, i, answer):
    if(num==1):
        return answer[0:-1]
    while(is_prime_number(i) and num % i == 0):
        answer += str(i) + "*"
        num//=i

    return prime_numbers(num,i+1,answer)
n = int(input("Введите число: "))
print(prime_numbers(n, 2, ""))
