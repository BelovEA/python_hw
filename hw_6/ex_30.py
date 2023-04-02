"""Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

first_element = int(input("Enter the first element of the arithmetic progression: "))
difference = int(input("Enter the difference of the arithmetic progression: "))
quantity = int(input("Enter the number of elements in the progression: "))

progression = []
count = 0

while count < quantity:
    progression.append(first_element)
    first_element += difference
    count += 1

print("The arithmetic progression is:", progression)