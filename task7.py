# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
def is_triangle(a,b,c):
    if(a < b + c and b < a + c and c < a + b):
        return True
    return False
a, b, c = map(int,input("Введите 3 стороны в строку: ").split())
print(is_triangle(a,b,c))
