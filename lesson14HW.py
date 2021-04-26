
import threading
import time
import random
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
        rand = random.randrange(0,30)
        # sleep = random.randrange(1, 5)
        # time.sleep(sleep)
        # print("I am Person {}, I slept for {} seconds".format(self.name, sleep))

        file = open("write_user"+str(rand)+".txt", 'w')
        file.write(str(self.get_info()))
        file.close()

user = User("Alex" , "Voronin", 23, "Rome",345634564)
user1 = User("Ivan" , "Ponkratov", 19, "Kiev",39945645)
user2 = User("John" , "Dir", 22, "London",3999123123)
user3 = User("Travis" , "Topalov", 25, "Tokyo",399978978)
user4 = User("Anna" , "Semenova", 45, "Paris",399993423456)

u = threading.Thread(target=user.write())
u.start()

u1 = threading.Thread(target=user1.write())
u1.start()

u2 = threading.Thread(target=user2.write())
u2.start()

u3 = threading.Thread(target=user3.write())
u3.start()

u4 = threading.Thread(target=user4.write())
u4.start()



#import multiprocessing
#from random import randint

# class Matrix:
#     def __init__(self,rows,cols):
#         self.rows = rows
#         self.cols = cols
#         self.matrix = []
#     def create_matrix(self):
#
#         for i in range(self.rows):
#             mas = []
#             for j in range(self.cols):
#                 mas.append(randint(0,100))
#             self.matrix.append(mas)
#
#         return self.matrix
#
#     def __add__(self, other):
#
#         if len(self.matrix) == len(other.matrix):
#                 new_matrix = []
#                 for i in range(len(self.matrix)):
#                     for j in range(len(self.matrix[0])):
#                         res = self.matrix[i][j] + other.matrix[i][j]
#                         new_matrix.append(res)
#                         k = open("Result.txt","w")
#                         k.write(str("Sum:{}".format(new_matrix)))
#                         k.close()
#                 # return "Sum:{}".format(new_matrix)
#                 # return new_matrix
#
#     def __mul__(self, other):
#         def mul(row, col):
#             return  sum(a * b for a, b in zip(row, col))
#
#         res_mtrx = []
#         for row in self.matrix:
#             if isinstance(other, int):
#                 res_mtrx.append([col * other for col in row])
#             else:
#                 res_mtrx.append([mul(row, col) for col in zip(*other.matrix)])
#         # return "Mul:{}".format(res_mtrx)
#         q = open("Result.txt", "a")
#         q.write(str("Mul:{}".format(res_mtrx)))
#         q.close()
#         # return res_mtrx
# matrix = Matrix(3,3)
# matrix2 = Matrix(3,3)
#
# print(matrix.create_matrix())
# print(matrix2.create_matrix())
# # print(matrix.__add__(matrix2))
# # print(matrix.__mul__(matrix2))
#
# a = multiprocessing.Process(target=matrix.__add__(matrix2))
# a.start()
# print('Start')
# print(a.is_alive())
# a.join()
# print(a.is_alive())
#
# m = multiprocessing.Process(target=matrix.__mul__(matrix2))
# m.start()
# print('Start2')
# print(m.is_alive())
# m.join()
# print(m.is_alive())



