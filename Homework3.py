
 #1. У вас есть массив чисел. Напишите три функции, которые вычисляют
# сумму этих чисел: с for-циклом, с while-циклом, с *рекурсией
 # Задача 1.1
def func_for(a):
 sum = 0
 for i in list1:
    sum += i
 return sum

def func_while(a):
 i = 0
 k = 0
 while i < len(list1):
    k += list1[i]
    i += 1
 return k

def func_recurs(a):
 l = 0
 for i in list1:
    if (type(i) == type([])):
        l += list1[i]
    else:
        l += i
 return l

list1 = [10, 12, 14, 15, 16, 13, 1, 5, 6, 3]
for v in (func_for,func_while,func_recurs):
        print(v(list1))


#2. Напишите функцию, которая создаёт комбинацию двух списков таким
# образом: [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
def comb_list (a,b):
 i = 0
 c = []
 while i < len(a):
    c.append(a[i])
    c.append(b[i])
    i += 1
 return c

a = [1, 2, 3]
b = [11, 22, 33]
print (repr(comb_list(a,b)))

#3.Существует ли треугольник с заданными сторонами.
a = int(input("Введите сторону А :"))  # Задача 3
b = int(input("Введите сторону B :"))
c = int(input("Введите сторону C :"))
def triangle (a,b,c):
    return a + b > c and a + c > b and b + c > a
print(triangle(a,b,c))
# 4. Расстояние между точками. На вход поступает два значение (кортежа) с
# координатами - широта и долгота.
# Найти расстояние между этими точками. cos(d) = sin(φА)·sin(φB) +
# cos(φА)·cos(φB)·cos(λА − λB), где φА и φB — широты, λА, λB — долготы
# данных пунктов, d — расстояние между пунктами, измеряется в
# радианах длиной дуги большого круга земного шара. Расстояние между
# пунктами, измеряемое в километрах, определяется по формуле: L = d·R,
# где R = 6371 км — средний радиус земного шара.
import math
fiA = math.radians(int(input("Enter latitude A :")))
fiB = math.radians(int(input("Enter latitude B :")))
lamA = math.radians(int(input("Enter lambda A :")))
lamB = math.radians(int(input("Enter lambda B :")))
def distance(fiA,fiB,lamA,lamB):
    import math
    R = 6371
    cos_d = math.sin(fiA)*math.sin(fiB)+math.cos(fiA)*math.cos(fiB)*math.cos(lamA-lamB)
    d = math.acos(math.cos(cos_d))
    L = d*R
    return L
print(distance(fiA,fiB,lamA,lamB))

# 5.. Поиск квадратных уравнений, имеющих решение. Программа принимает
# от пользователя диапазоны для коэффициентов a, b, c квадратного
# уравнения: ax2 + bx + c = 0. Перебирает все варианты целочисленных
# коэффициентов в указанных диапазонах, определяет квадратные уравнения,
# которые имеют решение.
import math
a = float(input(" a = "))
b = float(input(" b = "))
c = float(input(" c = "))
def quadequ(a,b,c):
 D = b ** 2 - 4 * a * c
 if D > 0:
    return("Уровнение имеет решение,будет два корня ")
 elif D == 0:
    return("Уровнение имеет решение,будет один корнень ")
 else:
    return("Уровнение не имеет решения ! ")
print (quadequ(a,b,c))
    # 6.Заданы M строк символов, которые вводятся с клавиатуры. Каждая строка
    # представляет собой последовательность символов, включающих в себя
    # вопросительные знаки. Заменить в каждой строке все имеющиеся
    # вопросительные знаки звёздочками.
def replacement():
 arr = []
 M = 3
 for i in range(0,M):
    arr.append(input().replace('?','*'))
 print(arr)
replacement()
# 7.Системная дата имеет вид 2009-06-15. Нужно преобразовать это значение
# в строку, строку разделить на компоненты (символ→разделитель→дефис),
# потом из этих компонентов сконструировать нужную строку. (2009-06-15 ->
# 15/06/2009)
def system_time():
 string = '2009-06-15'
 d = string.split("-")
 print(d[2] + "/" + d[1] + "/" + d[0])
system_time()
# 8.Задан вес в граммах. Определить вес в тоннах и килограммах.
def gram_to_kg_and_t():
 gram =int(input("Введите вес в гарммах :"))
 print("Вес в килограммах  :", gram / 1000)
 print("Вес в тоннах :", gram / 1000000)
gram_to_kg_and_t()
#9. Имеется коробка со сторонами: A × B × C. Определить, пройдёт ли она в
#дверь с размерами M × K.
def box():
 s = int(input("Введите сторону А :"))
 e = int(input("Введите сторону B :"))
 t = int(input("Введите сторону C :"))
 o = int(input("Введите сторону M :"))
 p = int(input("Введите сторону K :"))
 if (s<o and e<p)or(s<p and e<o):
   return"Коробка пройдет"
 elif (e<o and t<p)or(e<p and t<o):
   return"Коробка пройдет"
 elif (s<o and t<p)or(s<p and t<o):
   return "Коробка пройдет"
 else:
     return"Коробка не пройдет"
print(box())
# 10.Можно ли из бревна, имеющего диаметр поперечного сечения D,
# выпилить квадратный брус шириной A?
D = int(input("Введите диаметр бревна :"))
A = int(input("Введите ширину бруса :"))
def calculations(D,A):
 from math import sqrt
 B = sqrt(((A ** 2)+(A ** 2)))
 if B <= D:
    return("Выпилить брус возможно ")
 else :
    return("Выпилить брус невозможно ")
print(calculations(D,A))
# 11.Дан номер места в плацкартном вагоне. Определить, какое это место:
# верхнее или нижнее, в купе или боковое.
inp = int(input("Enter number :"))
def seat_on_train(inp):
 if inp > 37:
    print("Боковое")
 else:
    print("Купе")
 if inp % 2 == 0:
    print("Вверхнее")
 else:
    print("Нижнее")
print(seat_on_train(inp))
#12.Известна денежная сумма. Разменять её купюрами 500, 100, 10 и
#монетой 2 грн., если это возможно.
P =int(input("Введите сумму :"))
def money(P):
   A=P%500
   A1=P//500
   print("500 ="+str(A1))
   B=A%100
   B1=A//100
   print("100 ="+str(B1))
   C = B % 10
   C1 = B // 10
   print("10 =" + str(C1))
   D1 = C//2
   print("2 =" + str(D1))
print(money(P))
#13.Пользователь вводит число n, программа должна проверить является ли
#оно простым и сообщить об этом.
n = int(input("Enter n :"))
def prime_number(n):
 if n > 2 and n % 2 != 0 and n % n == 0:
    return("Число  простое !")
 else:
    return("Число не простое !")
print(prime_number(n))
# 14. Вывести таблицу умножения числа M в диапазоне от числа a до числа b.
# Числа M, a и b вводит пользователь.
M = int(input("Введите M :"))
v = int(input("Введите a :"))
q = int(input("Введите b :"))
def multiplication_table(M,v,q):
 if v <= 0 and q <= 0:
    print("Введите a и b больше 0 !")
 elif v >= q:
    print("Введите a и b больше 0 !")
 else:
    for v in range(v-1,q):
        v += 1
        print(M,"x",v,"=",M *v)
print(multiplication_table(M,v,q))
# 15.Дан одномерный массив числовых значений, насчитывающий N
# элементов. Поменять местами элементы, стоящие на чётных и нечётных
# местах: A[1] ↔ A[2]; A[3] ↔ A[4]
list_j = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(list_j)
def chet_nechet(list_j):
 for i in range (0,len(list_j),3):
    list_j[i],list_j[i + 1] = list_j[i + 1],list_j[i]
 return(list_j)
print(chet_nechet(list_j))
# 16.Вывести список простых чисел в диапазоне d. Диапазон d вводит
# пользователь.
h = int(input("Введите диапазон :"))
def list_of_prime_number(h):
 for h in range(3,h):
    for i in range(2,h):
        if (h % i == 0):
            break
        else:
            print(h)
            break
print(list_of_prime_number(h))
