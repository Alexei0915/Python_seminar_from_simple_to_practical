def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_num = ''
    valid =False
    while not valid:
        try:
            phone_num = input('Введите номер телефона: ')
            if len(phone_num) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_num = int(phone_num)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_num)
    descript = input('Введите описание: ')
    info.append(descript)
    return info