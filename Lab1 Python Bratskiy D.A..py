import math
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))

if 9 + (x-y)**2 > 0:
    a1 = ((9 + (x - y)**2)**(1/3)) / (x**2 + y**2 + 2)
    a2 = math.exp(abs(x - y))
    a3 = (math.tan(z))**3
    s = a1 - a2 * a3
    print("Результат ", s)
else:
    print("Значение выражения не может быть вычислено")