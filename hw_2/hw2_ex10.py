"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток,которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть"""
import random

def CoinCheck(coins_gen):
    tails = 0
    eagle = 0
    for i in coins_gen:
        if i == 0:
            tails += 1
        else:
            eagle += 1
    if tails > eagle:
        return f"минимальное число монеток со стороной решка, что бы все стороны были одинаковы = {eagle}"
    else:
        return f"минимальное число монеток со стороной орёл, что бы все стороны были одинаковы = {tails}"


n = int(input())
coins_gen = [random.randint(0, 1) for i in range(n)]
print(coins_gen)
tails = 0
eagle = 0
result = CoinCheck(coins_gen)
if "решка" in result:
    eagle = n - tails
else:
    tails = n - eagle
print(result.format(tails=tails, eagle=eagle))