"""Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)"""
num = int(input("Enter a three-digit integer number: "))
sum_of_el = 0
while num != 0:
    sum_of_el += num % 10
    num //= 10

print(f"summ of digit = {sum_of_el}")

