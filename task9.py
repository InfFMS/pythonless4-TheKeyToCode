# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!

def is_stepen_of_2(n):
    if(n<=0):
        return False
    if n%2==0:
        n=n//2
    else:
        # print(n==1)
        return (n==1)
    # print(n)
    return is_stepen_of_2(n)
i = int(input("Введите число: "))
# print(is_stepen_of_2(i))
if(is_stepen_of_2(i)):
    print("YES")
else:
    print("NO")
