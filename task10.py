# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.
numbers_from = {
  "0": 0,
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "A": 10,
  "B": 11,
  "C": 12,
  "D": 13,
  "E": 14,
  "F": 15,
  "G": 16,
  "H": 17,
  "I": 18,
  "J": 19,
  "K": 20,
  "L": 21,
  "M": 22,
  "N": 23,
  "O": 24,
  "P": 25,
  "Q": 26,
  "R": 27,
  "S": 28,
  "T": 29,
  "U": 30,
  "V": 31,
  "W": 32,
  "X": 33,
  "Y": 34,
  "Z": 35
}
numbers_to = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def convert_to_ten_base(num, from_base):
    ten_base = 0
    for i in range(len(num)):
        #print(ten_base)
        ten_base *= from_base
        #print(" ", numbers_from[str(num[i])])
        #print(i)
        ten_base += int(numbers_from[str(num[i])])
        #print(int(numbers_from[str(num[i])]))
    return ten_base
def conver_to_base(num, from_base):
    answer = ""
    while(num > 0):
        answer += numbers_to[int(num % from_base)]
        num=int(num/from_base)
    answer=answer[::-1]
    return answer
        
def convert_base(num, from_base, to_base):
    return conver_to_base(convert_to_ten_base(num, from_base), to_base)
num, from_base, to_base = map(str, input("Введите 3 стороны в строку: ").split())
from_base = int(from_base)
to_base = int(to_base)
print(convert_base(num, from_base,to_base))
