def calculate_average(numbers: list[float]) -> float:
    """
    Вычисляет среднее значение списка чисел.
    :param numbers: Список чисел
    :return: Среднее значение
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")

    return sum(numbers) / len(numbers)


def test_calculate_average():
    numbers = [1, 2, 3, 4, 5]
    expected_result = 3.0

    result = calculate_average(numbers)

    assert result == expected_result, f"Ожидалось {expected_result}, получено {result}"


def test_empty_list():
    numbers = []

    try:
        calculate_average(numbers)
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        # print(f'Ошибка вызвалась!')
        pass


def test_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    expected_result = -3.0

    result = calculate_average(numbers)

    assert result == expected_result, f"Ожидалось {expected_result}, получено {result}"


# Запуск всех тестов
test_calculate_average() # Passed
test_empty_list() # Passed
test_negative_numbers() # Passed
print(f"Все тесты успешно пройдены")

