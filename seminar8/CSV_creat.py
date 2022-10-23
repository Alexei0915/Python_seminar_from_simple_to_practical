# 
def creat ():
    file = 'Phone_book.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Имя;Фамилия;Номер телефона;Описание\n')