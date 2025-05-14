def game_core_v3(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict = (low + high) // 2  # угадываем середину диапазона
        if predict == number:
            break
        elif predict < number:
            low = predict + 1
        else:
            high = predict - 1

    return count
