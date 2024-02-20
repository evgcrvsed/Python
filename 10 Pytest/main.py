import pytest


def calculate_average(numbers: list[float]) -> float:
    """
    Вычисляет среднее значение списка чисел.

    :param numbers: Список чисел
    :return: Среднее значение
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")

    return sum(numbers) / len(numbers)


def test_calculate_average_nonempty():
    numbers = [1, 2, 3, 4, 5]
    assert calculate_average(numbers) == 3.0


def test_calculate_average_negative():
    numbers = [-1, -2, -3, -4, -5]
    assert calculate_average(numbers) == -3.0


def test_calculate_average_float():
    numbers = [0.5, 1.5, 2.5, 3.5]
    assert calculate_average(numbers) == 2.0


def test_calculate_average_single_element():
    numbers = [10]
    assert calculate_average(numbers) == 10.0
