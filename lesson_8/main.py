def read_file(filename):
    with open(filename, 'r') as data:
        data_array = [line.strip().split(',') for line in data]
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ','.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname='', firstname='', secondname='', phone=''):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    new_item = [str(next_id), lastname, firstname, secondname, phone]
    data_array.append(new_item)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)
    for item in data_array[1:]:
        print(f'ID: {item[0]}, Фамилия: {item[1]}, Имя: {item[2]}, Отчество: {item[3]}, Телефон: {item[4]}')

def change_item(filename, id):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        if int(data_array[i][0]) == id:
            data_array[i][1] = input('Фамилия: ')
            data_array[i][2] = input('Имя: ')
            data_array[i][3] = input('Отчество: ')
            phone = input('Телефон: ')
            while not phone.isdigit():
                phone = input('Неверный формат номера. Введите номер заново: ')
            data_array[i][4] = phone
            write_file(filename, data_array)
            print('Запись изменена')
            return
    print('Запись не найдена')

def delete_item(filename, id):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        if int(data_array[i][0]) == id:
            del data_array[i]
            write_file(filename, data_array)
            print('Запись удалена')
            return
    print('Запись не найдена')

def menu(filename):
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input('Введите номер операции: '))

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2:
        lastname = input('Фамилия: ')
        firstname = input('Имя: ')
        secondname = input('Отчество: ')
        phone = input('Телефон: ')
        while not phone.isdigit():
            phone = input('Неверный формат номера. Введите номер заново: ')
        add_item(filename, lastname, firstname, secondname, phone)
    elif user_operation == 3:
        id = int(input('Введите ID записи для изменения: '))
        change_item(filename, id)
    elif user_operation == 4:
        id = int(input('Введите ID записи для удаления: '))
        delete_item(filename, id)

filename = 'file.txt'
menu(filename)