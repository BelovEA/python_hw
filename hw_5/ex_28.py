"""Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4"""


def sum_of_numbers(a, b):
    if b < 1:
        return a
    else:
        return sum_of_numbers(a + 1, b - 1)

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

print("The sum of numbers from A to A+B is:", sum_of_numbers(a, b))