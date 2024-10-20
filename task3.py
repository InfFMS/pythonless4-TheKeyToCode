# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

def from_arabic_to_roman(num):
    if(num>3999):
        return "ERROR: число должно быть меньше, чем 4000, но num = " + str(num) + "<---"
    if(num<0):
        return "ERROR: число должно быть больше или равно, чем 0, но num = " + str(num) + "<---"
    thousand = int(num/1000)
    hundread = int(num/100%10)
    ten = int(num/10%10)
    unit = int(num%10)
    thousands = ["", "M", "MM", "MMM"]
    hundreads = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[thousand] + hundreads[hundread] + tens[ten] + units[unit]
n = int(input("Введите число арабскими числами: "))
print(from_arabic_to_roman(n))

#for i in range(-1,4001):
#    print(from_arabic_to_roman(i))
