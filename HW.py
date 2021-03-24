from random import randint

class Matrix:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols

    def create_matrix(self):
        self.matrix = []
        mas = []
        for i in range(self.rows):
            for j in range(self.cols):
                mas.append(randint(0,100))

        self.matrix.append(mas)
        return self.matrix

    def __add__(self, other):
        new_matrix = []
        if len(self.matrix) == len(other.matrix):
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        res = self.matrix[i][j] + other.matrix[i][j]
                        new_matrix.append(res)
                return "Sum:{}".format(new_matrix)

    def __mul__(self, other):
        def mul(row, col):
            return  sum(a * b for a, b in zip(row, col))

        res_mtrx = []
        for row in self.matrix:
            if isinstance(other, int):
                res_mtrx.append([col * other for col in row])
            else:
                res_mtrx.append([mul(row, col) for col in zip(*other.matrix)])
        return "Mul:{}".format(res_mtrx)
matrix = Matrix(3,3)
matrix2 = Matrix(3,3)
matrix.create_matrix()
matrix2.create_matrix()

matrix.__add__(matrix2)
matrix.__mul__(matrix2)

print(matrix.create_matrix())
print(matrix2.create_matrix())
print(matrix.__add__(matrix2))
print(matrix.__mul__(matrix2))




class Driver:
    def __init__(self,name,surname,seniority):
        self.name = name
        self.surname = surname
        self.seniority = seniority

class Engine:

    def starting_motor(self):
        print("Motor started")
    def engine_stop(self):
        print("Motor stopped")
    def left_turn(self):
        print("Car turn left")
    def right_turn(self):
        print("Car turn right")
class Car:
    def __init__(self,model):
        self.model = model


    def get_info(self,driver):
        print("Model :{},Driver:{},{},Seniority:{}".format(self.model,driver.name,driver.surname,driver.seniority,))

driver = Driver("Ivan","Petrov",10)
engine = Engine()
engine.starting_motor()
car = Car("BMW")
car.get_info(driver)