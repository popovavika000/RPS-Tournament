def get_score(action1, action2):
    """
    Определяет, кто выиграл в игре "Камень, Ножницы, Бумага".
    :param action1: Действие первого игрока (0: Камень, 1: Бумага, 2: Ножницы)
    :param action2: Действие второго игрока (0: Камень, 1: Бумага, 2: Ножницы)
    :return: 1, если первый игрок выигрывает, -1 если он проигрывает, 0 если ничья
    """
    if action1 == action2:
        return 0  # Ничья
    elif (action1 == 0 and action2 == 2) or (action1 == 1 and action2 == 0) or (action1 == 2 and action2 == 1):
        return 1  # Первый игрок выигрывает
    else:
        return -1  # Первый игрок проигрывает
