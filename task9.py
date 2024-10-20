# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!

def is_stepen_of_2(n):
    if(n<=0):
        return False
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            if(n!=1):
                return False
    return True

i = int(input("Введите число: "))
if(is_stepen_of_2(i)):
    print("YES")
else:
    print("NO")
