
class User:
    def __init__(self, name,surname, age,city,ID):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.ID = ID

    def get_info(self):
        return "Name:{}, Surname:{}, Age:{}, City:{}, ID:{}".format(self.name,self.surname ,self.age,self.city,self.ID)

    def write(self):
        file = open("write_user.txt", 'w')
        file.write(str(self.get_info()))
        file.close()
    def read(self):
        line = []
        file  = open("write_user.txt", 'r')
        line.append( file.read())
        return line
user = User("Alex" , "Voronin", 23, "Rome",345634564)
user.write()
print(user.read())


print("//////////////////////////////////////////////////////////////////////////////////")


import os
import re
class Read:
    def __init__(self,path):
        self.path = path

    def count(self):

        words = 0
        symbols = 0

        if os.path.exists(str(self.path)):
            file_text = open(self.path,'r')
            text = file_text.read()
            file_text.close()

            ntext= re.sub(r'[.!?]\s', r'|', text)
            suggestions = len(ntext.split('|'))

            pos = 'out'
            for i in text:

                if i !=' ' and pos == 'out':
                    words += 1
                    pos = 'in'
                elif i ==' ':
                    pos = 'out'
                if i !=' ':
                   symbols += 1
            return "suggestions :{}, words :{},symbols :{}\n {} ".format(suggestions, words, symbols, text)
        else:
            print('Не удалось найти файл: {}'.format(self.path))
read = Read("test.txt")
print(read.count())