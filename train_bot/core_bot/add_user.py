

file_path = 'users.txt'  # Замените на путь к вашему файлу
text_to_add = 'This is a new line of text.'


def add_user(name, id, nickname):
    try:
        # Открываем файл в режиме добавления (a), если файла нет, он будет создан
        with open(file_path, 'a') as file:
            # Записываем текст в файл
            file.write(name + ' ' + str(id) + ' ' + ' ' + nickname + '\n')  # Добавляем символ новой строки для разделения строк
        print(f'Text added to {file_path} successfully.')
    except Exception as e:
        print(f'Error: {e}')

# add_text_to_file(file_path, text_to_add)
