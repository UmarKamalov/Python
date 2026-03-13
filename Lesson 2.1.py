# a = 1
# b = 632
# c = -134
# d = -2342
#
# a2 = 3.2
# # b2 = 3.323545
# # c2 = -34124
# """
# float вещественное число, - 324,13
# int - целочисленное число. 324, -324
# """
# a = 2 + 1 + 34
# print(a)
#
# a = 8 / 2
# print (a)
#
# a = 7 // 2
# print(a)
# a = 7 / 2
# print(a)
#

# 1. Создание переменных и вывод значений
a = 4.2 * 2
print(a)
name = "Umar"
age = 29
height = 1.78
print (name)
print (age)
print (height)

# 2. Изменение значений переменных
x = 10
print (type(x))
x = 25.5
print (type(x))
x = "Python"
print (type(x))

# 3. Копирование ссылок
a = 7
b = a
a = 10
print (a)
print (b)
#переменная а выводит последнее присвоенное значение и забывает ранее присвоенное число. Значение переменной б с последнего раза не меняли

# 4. Каскадное присваивание
x = 100
y = 100
z = 100
print (x)
print (y)
print (z)
#Множественное присвоение
x, y, z = 300, 3000, 40000
print(x)
print (y)
print (z)

# 5. Обмен значений переменных
a = 5
b = 10
a, b = b, a
print (a)
print (b)

# 6. Работа с именами переменных. При введении запрещенных имен переменных не смог перейти в режим написания кода

# 7. Использование функции
var1 = 42
var2 = 3.14
var3 = "Hello"
print (type(var1))
print (type(var2))
print (type(var3))

# Дополнительные задания (для закрепления)
lesson1 = "Python"
lesson2 = "Pytest"
lesson3 = "3"
lesson4 = "python1"
lesson5 = 5
lesson5 = str (lesson5)
print (lesson1)
print (lesson2)
print (lesson3)
print (lesson4)
print (lesson5)
print (type(lesson1))
print (type(lesson2))
print (type(lesson3))
print (type(lesson4))
print (type(lesson5))
print (type(lesson5))
results = "Age" + " " + "29"
print (results)

name = 'Ivan'
age = 30
height = 1.78
print (name, age, height)

X = 10
print (type(X)) #выведет тип int
X = 25.5
print (type(X)) #выведет тип float
X = "PYTHON"
print (type(X)) #выведет тип str
print (X) #выведет только последний присвоенный объект

a = 7
b = a
print (b)
a = 10
print (b) #объекту была присвоена два переменных, затем переменную "а" "отклеили" и "приклеили к следующему объекту.
print (a)

x = 1000
y = 1000
z = 1000
print (x, y, z)
x, y, z = 10, 20, 30
print (x,y,x)

a = 5
b = 10
a,b = b, a
print (a,b)
# или
a, b = 10, 5
print (a)
print (b)

var1 = 42
var2 = 3.4
var3 = "Мир"
print (type(var1))
print (type(var2))
print (type(var3))
print (str(var1))
var1 = str(var1)
print (type(var1))
# тут как бы говорит, мол, сходи к переменной var1, возьми значение и преврати их в строку
