from os.path import exists
from CSV_creat import creat
from File import writing_scv
from File import writing_txt


path = 'Phone_book.csv'
valid = exists(path)
if not valid:
    creat()

writing_scv()
writing_txt()