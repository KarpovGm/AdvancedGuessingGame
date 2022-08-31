"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
максимальное число попыток: 20"""

import numpy as np


def binary_search(number: int = 1) -> int:
    """Угадываем число путем бинарного поска
    Args:
        number (int, optional): Загаданное число. по умолчанию равно 1.
    Returns:
        int: Число попыток
    """
    
    array = range(1,101)
    count = 0
    start = 0
    end = len(array)

    while True:
        count += 1
        mid = (start + end) // 2
        if number < array[mid]:
            start = mid + 1 
        if number > array[mid]:
            end = mid -1 
        if number == array[mid]:
            break
          # выход из цикла если угадали
    return count


def score_game(binary_search) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        binary_search ([type]): функция угадывания на основе бинарного поиска
    Returns:
        int: среднее количество попыток из 1000 подходов
    """
    count_ls = []
    
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == '__main__':
    score_game(binary_search)