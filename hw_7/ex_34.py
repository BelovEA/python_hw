"""Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам  """


def Winnie_the_pooh(winnie_poem):
    vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    phrases = winnie_poem.split()
    res = []
    for phrase in phrases:
        k = 0
        for letter in phrase:
            if letter in vowels:
                k += 1
        res.append(k)
    if len(set(res)) != 1:
        return "Пам парам"
    else:
        return "Парам пам-пам"


winnie_poem = input("Winnie composed a new song. Enter it here: ").lower()
print(Winnie_the_pooh(winnie_poem))










Winnie_poem = list(map(str, input().split()))
print(f"Winnie composed next song: {Winnie_poem}")
print(winnie_the_pooh(Winnie_poem))