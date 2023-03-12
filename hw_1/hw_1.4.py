"""Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no"""
while True:
    try:
        n = int(input("Введите число n (количество строк шоколадки): "))
        if n <= 0:
            print("Число должно быть положительным")
            continue
        break
    except ValueError:
        print("Введите целое число")

while True:
    try:
        m = int(input("Введите число m (количество столбцов шоколадки): "))
        if m <= 0:
            print("Число должно быть положительным")
            continue
        break
    except ValueError:
        print("Введите целое число")

while True:
    try:
        k = int(input("Введите число k (количество долек для отлома): "))
        if k <= 0:
            print("Число должно быть положительным")
            continue
        break
    except ValueError:
        print("Введите целое число")

if k > n * m:
    print("NO")
elif k == n * m:
    print("YES")
elif k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")
