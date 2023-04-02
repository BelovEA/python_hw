"""Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)"""
import random

array = [random.randint(1, 100) for i in range(10)]
print("Generated array:", array)

min_number = int(input("Enter the minimum number of the range to search for numbers in the array: "))
max_number = int(input("Enter the maximum number of the range to search for numbers in the array: "))

indices = []
for i in range(len(array)):
    if min_number <= array[i] <= max_number:
        indices.append(i)

if indices:
    print(f"The following numbers in the 'array' are within the range of {min_number} to {max_number}:")
    for index in indices:
        print(array[index], "at index", index)
else:
    print(f"No numbers in the 'array' are within the range of {min_number} to {max_number}.")