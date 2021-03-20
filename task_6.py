"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random


def guess_number(max_count, number):
    if max_count == 0:
        print(f'Вы проиграли, правильное число {number}')
    if max_count > 0:
        print(f'осталось попыток: {max_count}')
        user_number = int(input('Введите число от  0 до 100'))
        if user_number == number:
            print('Вы выиграли')
            return
        elif user_number > number:
            print('вы ввели слишком большое число')
        else:
            print('вы ввели слишком маленькое число')
        guess_number(max_count - 1, number)


count = 10
print(f'всего {count} попыток')
guess_number(count, random.randint(1, 100))