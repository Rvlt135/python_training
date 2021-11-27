def game(secret_num, a_number):
    running = True

    while running:
        secret_number = str(secret_num)
        answer_user = str(a_number)
        """Преобразовываем значения в списки для валидации"""
        convert_secret_number = list(secret_number)
        convert_answer_user = list(answer_user)
        cows = []  # Будем добавлять коров
        bulls = []  # Будем добавлять быков

        if secret_number == answer_user:
            return "Вы выйграли!"
        """Очень плохая реализация"""
        """определяем точно быков"""
        if answer_user[0] == secret_number[0]:
            bulls.append(answer_user[0])

        if answer_user[1] == secret_number[1]:
            bulls.append(answer_user[1])

        if answer_user[2] == secret_number[2]:
            bulls.append(answer_user[2])

        if answer_user[3] == secret_number[3]:
            bulls.append(answer_user[3])
        # Высчитываем общие совпаденийя совпадения Коровы
        for i in convert_answer_user:
            if i in convert_secret_number:
                cows.append(i)
        # В этом блоке валидируем введенные значения
        if len(cows) == 0:
            return "Нет совпадений"
        elif len(answer_user) >= 5:
            return "Значение < 5 символов"
        elif len(answer_user) < 4:
            return "У вас число < 4-го"
        # Проверяем что нет повторений в веденном значении
        elif len(set(answer_user)) != len(set(secret_number)):
            return 'Числа не должны повторяться!'
        else:
            a = len(cows) - len(bulls)  # Высчитываем результат коров к быкам
            return f'{a} коровы, {len(bulls)} быка'
