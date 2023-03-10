"""Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no"""
def Lucky_number(number):
    if type(number) != int or len(str(number)) != 6:
        return "Input a 6-digit integer!"
    else:
        first_digits = 0
        last_digits = 0
        while number != 0:
            if len(str(number)) < 4:
                first_digits += number % 10
            else:
                last_digits += number % 10
            number //= 10
        if last_digits == first_digits:
            return "Ticket is lucky!"
        else:
            return "Better luck next time!"


while True:
    number_str = input("Input a 6-digit integer number of the ticket: ")
    try:
        number = int(number_str)
    except ValueError:
        print("Invalid input! Please input an integer number.")
        continue
    if len(number_str) != 6:
        print("Invalid input! Please input a 6-digit integer number.")
        continue
    break

print(Lucky_number(number))
