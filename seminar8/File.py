# 
from User_int import get_info as gi

info = gi()
def writing_scv ():
    file = 'Phone_book.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt ():
    file = 'Phone_book.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\n Имя: {info[1]}\n\n Номер телефона: {info[2]}\n\n Описание: {info[3]}\n\n\n')