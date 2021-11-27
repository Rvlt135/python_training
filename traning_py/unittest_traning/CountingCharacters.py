def counter(text):
    txt = str(text)
    text_length = len(str(txt))
    output = ""
    count = 1
    index = 0

    while index < text_length - 1:
        if txt[index] == txt[index + 1]:
            count += 1  # Обновляем count совпадением
        else:
            output += txt[index]
            if count > 1:  # Не должно быть 1 внутри текста
                output += str(count)
            count = 1
        index += 1
    output += txt[text_length - 1]
    if count > 1:  # В последнем симовле не должно быть 1
        output += str(count)
    return output
