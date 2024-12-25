from builtins import PythonFinalizationError
from calendar import weekday
from functools import total_ordering
from glob import translate
from idlelib.autocomplete import FORCE
from multiprocessing.context import set_spawning_popen
from operator import truediv
from token import NUMBER

# INTEGER = (1,2,3,4,5,6,7,8,9,0)
#  float = (2.3, 4.6, 2.7)
#  string = ("Hello world")
#  Boolean = (true,false)
#
#
# a=5
# d=4
# b=12
# y=43
# print(a)
# print(b)
# print(d)
# print(y)
# #
# ########################### String #######################
# print("Hello world")
#
# a = "Game over"
# print(type(a))


# a = 1,2,3,
# print(type(a))
#
# command = 2.4
# print("ответ",command)

#
#
#
#
#
#
# print(type(d))
#
############# аты жонуу жазуу##########
#
# a = input("ведите фамилию\n")
# d = input("ведите имя\n")
# b = input("ведите отчество\n")
# print(f"ответ,{b}:{a}:{d}")
#
# name = ("esentur")



#
# num1 =int (input("ведите первое число!"))
# num2 =int (input("ведите второе число!"))
# sun_result = num1 + num2
# print(f"Сумма{num1} + {num2} сумма равна {sun_result}")

#
# ###################  ГОД РОЖДЕНИЯ#########################
# birth_year = int(input("год рождения"))
# current_year = 2024
# age = current_year - birth_year
# print(f"ваш год рождения {age} лет")


# user_string = input("ведите строку!")
# length = len(user_string)
# print(f"длинна строки {length}")


################ДЗ########################
# a = input("ведите имя")
# print(a)
#
# birth_year = int(input("год рождения"))
# current_year = 2024
# age = current_year - birth_year
# print(f"ваш год рождения {age} лет")
#





########
# a = input("какой ваш любимый предмет")
# d = input("ваша нация")
# print(f"ответ",a+d)
# ###############################
# print("результат: ", 7,15,".",  sep="/", end=" ")
# print('Second" l/a/n/e/')

#################### Стандарттык INPUT() Функциясы ################






# name = input("атынызды жазыныз!")
# surname = input("фамилия жазыныз!")
# age = input("жашынызды жазыныз!")
# adress = input("адресс проживания")
# tel = input("номер телефона")
# pol = input("ваш пол")






#     print(f"Аты: {name}\n"
#       f"фамилия: {surname}\n"
#       f"жаш: {age}\n"
#       f"adress: {adress}\n"
#       f"tel: {tel}\n"
#       f"pol: input{pol}\n")
#
#
#
#
# ############ плюс минус #######
# a = int(input("a"))
# b = int(input("b"))
# d = a+b
# print(f"{a} + {b} = {d}")

##########среднее статистечиский рейтинг#########



# score1 = float(input("ведите первую строку"))
# score2 = float(input("ведите вторую строку"))
# score3 = float(input("ведите третью строку"))
# score4 = float(input("ведите четвертую строку"))
# score5 = float(input("ведите пятую строку"))
# overage = (score1 + score2 + score3 + score4 + score5)/5
# print(f"средний балл: {overage:2f}" )


# text = input("ведите текст")
# print("верхний регистр", text.upper())
# print("нижний регистр", text.lower())


# #######умножения########
# a = int(input("a"))
# b = int(input("b"))
# d = a*b
# print(f"{a}*{b} = {d}")
#
#
# d = int(input("d"))
# b = int(input("b"))
# a = d/b
# print(f"{d}/{b}={a}")
#
#
# Hello = input("ваше имя")
# pol = input ("ваш пол не обьязательно")
# print(f",ответ  {Hello} + {pol}")
#
# name = input("esentur")
# surname = input("toktogulov")
# d = (name + surname)
# print("ответ ваше полное имя,{d}")


############# логические операторы ###############



# >чон же кичине
# <чон же кичине
# and жана/и
# or же/или
# not наоборот егерде false болсо true чыгарат true болсо false чыгарат
# == салыштыруу : барабар бы же барабар эмеспи
#
#
#
#
# x = 5
# y = 10
# print(x > 2 and y > 5)
#
#
#
# x = 5
# print(not x > 10)
#
#
#
#
# x = 30
# print(x == 10)
#
#
# b = 40
# a = 20
# c = 90
# d = 67
# print(a == 20 and b > 35 and d > a and c < d)
#
#
#
# a = 10
# d = 15
# print(a < d)
#
# a = 50
# d = 30
# f = 40
# print(a > d and f > 20)
#
# a = 3
# b = 4
# print(a == b) не равенство !=
#
#
# or +
# and *
#
#
# a = 3
# b = 2
# c = 1
# print(a < b and a > d and b < a and a == b)
#
#
# a = 3
# b = 2
# c = 1
# d = 5
# print((a < b and a < d ) or (a > b or a >= c) and (c < a and c < b))
#
# t = True
# f = False
# print( t == f and t < f)

#
# 1
# a = 5
# y = 3
# z = 7
# d = 13
# print( a ==5 and  y > 2 or  z > d)
#
#
#
#
# 2
# a = 2
# b = 5
# c = 4
# d = 6
# print(a < b and c == d)




# if elif ilse
# a = int(input("number a "))
# o = input("operation o")
# b = int(input("number b "))
#
# if o == "+":
#     print (a+b)
#
# elif o == "-":
#     print(a-b)
#
# elif o == "*":
#     print(a*b)
#
# elif o == "/":
#     print(a/b)
#
# else:
#     print("туура амал эмес")

# # a =  10
# # b =  20
# # c =  30
# # if
# # if a > b:
# # print ("a < b")
# #
# # elif a > b:
#

# a = int(input("ведите число"))
# b =  int(input("ведите число"))
# c = int(input("ведите число"))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > a and c > b:
#     print(c)
# else:
#     print("туура эмес амал")

# a = int(input("a"))
#
# if a <= 18:
#     print("вам еще нет 18")
#
# b =  int(input("b"))
#
#
#
# if b < 20:
#     print(" вам меньше 20")
#
# elif b > 20 and b <= 60:
#     print("взрослый")
#
# else:
#     print("пенсионер")

# name = input("введите имя")
# password = input("password")
#
# if name =='esentur' and password == "123":
#     print("успешно")
# else:
#     print("неправильно ввели")
#
# a =  int(input("ведите число"))
# b = int(input("ведите второе число "))
# c = int(input("ведите третье число"))
# if a > b and a >c:
#     print(a)
# elif b> a and b > c:
#     print(b)
# elif c > a and c > b :
#     print(c)
# else:
#     print("неправильно пиши правильно")
#
# a = int( input("ведите дня недели (1-7):"))
#
# if  a ==1:
#     print("понедельник")
# elif a ==2:
#     print("вторник")
# elif a ==3:
#     print("среда")
# elif a == 4:
#     print("четверг")
# elif a == 5:
#     print("пятница")
# elif a == 6:
#     print("субота")
# elif a == 7:
#     print("воскресенье")
# else:
#     print("неправильно ввели")

# a = int(input("ведите число (50-90):"))
# b = int(input("ведите число (90-70):"))
#
# if a >= 90:
#     print("отлично")
# elif a >= 90 and a <= 70:
#     print("отлично")



# a = (input("ведите имя"))
# b = (input("ведите имя"))
# c = (input("ведите имя"))
#
# if len(a) > len(b) and len(a) > len(c):
#     print(a)
# elif len(b) > len(c) and len(b) > len(a):
#     print(b)
# elif len(c) > len(a) and len(c) > len(b):
#     print(c)
# else:
#  print("неправильно ввели ")
#
# a = int(input("ведите число"))
#
# if a %5==0:
#     print("четное")
# else:
#     print("не четное")
#
# a = int(input("ведите первое число"))
# b = int(input("ведите второе число"))
#
# v = a + b
# if a % 2 == 0 :
#     print(f"  {v}  жуп сан")
# else:
#     print(f"так сан {v}

# a = float(input(" введите расстояние до место назначения (км):"))
#
# if a<=10:
#     доставка=10
#
# elif a>10:
#     print(f"сумма доставки: $ 5 ")
#
# b = float(input("введите расстояние до место назначения (км): "))
#
# if b <= 10:
#     доставка = 5
#
#
# else:
#     доставка = 10
# print(f"сумма доставки:$ {доставка}")


############## while цикл ###############
#
# a = 1
#
# while a <= 10:
#     print(a)
#     a = a + 1

# b = 1
# while b <= 99:
#     print(b)
    # b = b + 1


# while True:
#     user_input = input("введите 'стоп' для выхода:")
#     if user_input.lower () == 'stope':
#         print("цикл завершен")
#         break




# a = 2
# while a <= 20:
#     if a % 2 == 0:
#         print(a)
# else:
#     print("жуп сандар")

# number = int(input("введите число:"))
# i = 1
# while i <= 10:
#     print(f"{number} * {i} = {number*i}")
#     i += 1


########## ДОБАВЛЯЕМ ###########



# total = 0
# while True:
#     number = int(input("ведите число"))
#     if number == 0:
#         break
#     total += number
# print(f"ваша сумма{total}")
#
# name = (input("ведите ваше имя "))
# while True:
#     name = (input("ведите имя"))




#
# while True:
#     user_input  = input("ведите число")
#     if user_input.isdigit():
#         print(f"вы вели число {user_input}")
#     else:
#         print("это не число побробуйте еще раз ")
#         break


############## ИЗУЧИТЬ ВАЙЛ И СДЕЛАТЬ ПРИМЕРЫ ###########
# i = 0
# while i < 10:
#      print(i)
#      i += 1
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
#
# n = int(input(" N ; "))
# if  0 < n  and n <= 12:
#     if n == 12 and n >= 2:
#         print("zima")
#     elif n >= 3 and n <= 5:
#         print("vesna")
#     elif n >= 6 and n <= 8:
#         print("leto")
#     elif n >= 9 and n <= 11:
#         print("osen")
#     else:
#         print("введите правильный месяца года")
#
#
# i = 0
# j = 10
#
# while i < 10 and j >= 0:
#     print(f" i = {i} j = {j}")
#     i = i + 1 = 1:
#     j = i + 1 = 1:


################# FOR ЦИКЛ ################

#range (start stop step)


# for i in range(1,10+1, 1):
#     print(i)



# text = "Python"
# for i in text:
#     print(i)

# for i in range (5):
#     print("hello")




# for i in range(1 ,6+1):
#     if i == 4:
#         continue
#     print(i)




# for i in range(1,9+1):
#     if i == 5:
#         break
#     print(i)





# for i in range(1, 6):
#     if 1 % 2 == 0:
#         print(f"{i} -четное число")
#
#     else:
#         print(f"{i} не четное число")



# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(my_list[13])

# text = "hello world"
# print(text[5])
# print(text[:1])


# my_list = [1,2,3,4,5]
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i = i + 1


# my_list = [1,2,3,4,5]
#
# for i in my_list:
#     print(i)

############ APPEND () ФУНКЦИЯ ДОБАВЛЕНИЕ #############
# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# print(f"вы добавили,{my_list}")
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(my_list[15])


# a = ['aple', 'banana', 'orahge']
#
# for i in a:
#     print(i)


# a = ["Python"]
# for i  in a:
#     print(i)

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f"{i} четное число")
#
#     else:
#         print(f"{i} не четное число")



# my_list = [ 2,4 ,6,9,7,20,30,50]
# for  i in my_list:
#     if  i==2:
#             print(f" мин{i}")
#     elif i==50:
#         print(f"макс {i}")


# my_list =[" тажикистан, Кыгызстан, кипр"]
#
#
# country = "Кыгызстан"
#
# country in my_list
# print(f"СТРАНА НАЙДЕНО: {country}")


# b = ["бека,сека,дискотека"]
# a = ["кошка , мышка"]
# if b + a:
#     print( b + a )


# my_list = [6,4,7,3,11,13,65,43,76,73,10]
# for  i in my_list:
#     if i>=10:
#         print(i)


# a = [10,13,53,32,45,78,23,34]
# b = []
# i = 0
# while i < len(a):
#     if a [i] > 10:
#         b.append(a[i])
#     i += 1

# print("элементы больше 10",b)


# a = int(input("a"))
# b = int(input("b"))
#
# for i in range(a,b+1):
#
#     print(i)




# a = [1,2,3,4,5,6,7,8,9,10]
# b = []
#
# for i in a:
#     if i% 2 !=0:
#         print(f"не четные числа {i}")
#     else:
#         print(f"только не четные числа")


############## задания ##########

# a = [2,3,5,2,6,87,45,32,32,45]
# for i in a:
#     if i <= 5:
#         print(i)


# a = [3, 2, 4, 3, 6, 7, 6, 43, 44, 32, 23, 1]
# for num in a:
#     if num <= 5:
#         print(num)


# my_list = []
#
# for i in  range  (100+1):
#     my_list.append(i)
# print(f"удалить кылуудан алдын{my_list}")
#
#
# i = 1
# for i in range (100):
#     if i % 2 == 0:
#         my_list.remove(i)
# print(f"удалить кылуудан кийин{my_list}")
#
#
# list = [1,2,5,4,3]
# n = 0
# for i in list:
#     n += i
# print(n)







################### Set ##############

# ""
# set бир учурда оз ичине уникалдуу элементтердии  сактай алат
# ""

#
# myset = {1,2,4,3,5,7,4,4,5,5,3,2}
# myset.add(110)
# print(myset.clear())




#################### DICTIONARY ##############


# my_dic = {'name': '23', '1': "esentur"}
# print(my_dic['1'])





##################### pop #####################

""""""

        # pop создукту удалить кылуу


""""""

# thisdict = {
#     "brand":"ford",
#      "model":"mustang",
#      "year":2010,
#
# }
# thisdict.pop('model')
# print(thisdict)


# ##################################### keys ##############################################
# thidist = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# print (thidist.keys())
# keys - берет ключи (brand , model , year)



###################################### value ##################################################

#values - выводит только те которые внутри ключа (ford , mustang , 1964 )
# thidist = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# print (thidist.keys())
# keys - берет ключи (brand , model , year)



###################################### value ##################################################
""""""
#values - выводит только те которые внутри ключа (ford)
""""""
# thidist = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# print (thidist.values())






# a = {}
#
# for i in range(1,101,):
#     a[i] = [i]
#     print(a[i])





# mydic = {i: i for i in range(1, 100)}
#
#
# print(mydic)



# mydic = {}
# for i in range(2,100,):
#     if i % 2 == 0:
#         mydic[i] = i
# print(mydic)





# mydic = {
#     'apple':"яблоко",
#     'banana':"банан",
#     'cherry':"вишня",
# }
# word = input("Ведите слова на английском")
# translate = mydic.get(word,"слова не найдено")
# print(translate)



###################### дз Даннные  #################

# people = [
#     {"name":"Tom", "age":39, "company":"Supercorp", "languages": ["Python", "javaScropt"]},
#     {"name":"Bob", "age":43, "company":"BigCorp", "languages": ["Python", "c++","c#"]},
#     {"name":"Sam", "age":28, "company":"LittleCorp", "languages": ["Python", "java"]}
# ]
# search_name = input("ведите имя человека").strip()
# person_data = next((person for person in people if person['name'].lower() == search_name.lower()), None)
#
# if person_data :
#     print(f"данные о {search_name}"
#     f"{person_data}")
# else:
#     print(f"данные об этой человеке не найденно:> {search_name}")

#
#
# a = {
#     "name":"esentur", "age":57, "company":"Supercorp", "languages": ["mustang", "audi"]}
# b = input("ведите ключ для проверки")
#
#
# if a in b:
#     print(f"slovo:{a[b]}")
# else:
#     print("not faund")



# weekday ={
#     "понедельник":1,
#     "вторник":2,
#     "среда":3,
#     "четверг":4,
#     "пятница":5,
#     "субота":6,
#     "воскресенье":7,
#
# }
#
# print(weekday)
""""""""




# a = {1:2, 3:4, 5:6}
#
# a.clear()
# print(a)
#
#
# a = {1:2, 3:4, 5:6}
# valuest = list (a.values())
# print(valuest)
#
#
#
# a = {"Dima":40, "Uson": 15, "Esentur":17}
#
# for key in a:
#     a[key]+=5
#     print(a)

########################### ПРАКТИЧЕСКИЕ ЗАДАНИЯ ######################
# numbers = [1, 2, 3, 4, 5, 6]
# odd_numbers = []
# for number in numbers:
#  if number % 2 != 0:
#     odd_numbers.append(numbers)
# print (odd_numbers)



# a = {"Alice":25, "Bob":30, "Charlie":35}
# for key in a:
#     a[key]+=1
#     print(a)


# for i in range(1,99+2,1):
#     print(i)

# str1 = "Hello"
# str2 = "World"
# "str1 + str2"
# print(str1 +  str2)



# text = "banana"
# count_a = text.count("a")
# print(count_a)


# words = ["apple", "dog", "banana", "cat", "elephant"]
#
# long_words = []
# for  word in words:
#     if len(word) > 4:
#         long_words.append(word)
# print (long_words)


# number = int(input("ведите число:"))
# if number % 2 == 0 and number > 10:
#     print(f"число четное  и больше 10")
# elif number % 2 == 0:
#     print("число не четное")
# else:
#     print(f"число четное но меньше или  10 ")




# age = int(input("ведите ваш возраст:"))
# if not age< 18:
#     print("вы взрослый чел")
# else:
#     print("вы слишом молоды")




# sum = 0
# i = 1
# while i <= 10:
#     sum += i
#     i += 1
# print("сумма чисел от 1 до 10:",sum)

# my_list  = []
# for i in range(1,11):
#     my_list.append(i)
# print(my_list)




# a = []
# a.append("привет")
# a.append("меня зовут эсентур")
# print(a)



# my_list = [1,4,3]
# my_list.append(5)
# total_sum = sum(my_list)
# print(f"выводим сумму чисел,{total_sum}")
# print(my_list)


#############################





# ########################## DEF ###################
#
# # def artur(name):
# #     return f'{name} hello'
# #
# # print(artur('name'))









# # def add_number(a,b):
# #     return a+b
# # result = add_number(5,5)
# # print(result)
#
# def ss(name,age,surneim):
#     return f'{name,age,surneim} ваше имя и возраст '
#
# print(ss('esentur' , 16,'токтогуов'))




# a = int(input("Введите число: "))
# if a % 2 == 0:
#     print(f"Чётное число: {a}")
# else:
#     print(f"Нечётное число: {a}")



# a = [2,4,45,67,7]


# def num():
#     for  result in a:
#         if result < 60:
#            a.append(result)
#            return a
#         print(result)
# num()







# a = [1, 2, 3, 4, 5, 6, 5, 4]
#
# def num (a):
#     result = a[0] +a [-1]
#     return result
# result = num(a)
# print(result)




# age = int(input("Введите : "))
#
#
# if age < 13:
#     print("вы малелеьнкий")
# elif 13 <= age <= 19:
#     print("Ты подросток")
# elif 20 <= age <= 64:
#     print("Ты взрослый")
# else:
#     print("Ты пожилой человек")
#

# number = int(input("ведите четное число :"))
#
#
# if number % 2 == 0 :
#     print(f"число четное")
#
# else:
#     print("число не четное побробуйте еще")



# i = int(input("введите число"))
#
#     if i % 2 == 0:
#         print(f"{i} четное число")
#
#     else:
#         print(f"{i} не четное число")





# a =  input("введите пароль")
# if  len(a)<8:
#     print("пароль должен состоять не менее 8 символов")
# else:
#     print("ваш пароль принят ")
#






# name = str(input("ведите слово"))
# if  name == "python":
#     print("правильно")
# else :
#    print("ведите правильное слово")
#
#
#
# def num (numbers):
#     return max(numbers)
# print(num([1,2,3,4,2,43,54,96]))




# num = int(input("введите число "))
# if num % 3 == 0:
#     print("правильно")
# else:
#     print(f"повторите еще ")






#########################  повторение python   #######################

# a = int(input("number a "))
# oper = input("operation o")
# b = int(input("number b "))
#
# if oper == "+":
#     print (a+b)
#
# elif oper == "-":
#     print(a-b)
#
# elif oper == "*":
#     print(a*b)
#
# elif oper == "/":
#     print(a/b)
#
# else:
#     print("туура амал эмес")
#
#
# i = 2
# while i <= 100:
#     print(i)
#     i = i + 2


# for i in range(1,100):
#     if i% 2 !=0:
#         print(f"не четные числа {i}")






# age = int(input("введите ваш возраст "))
# if age >= 25 :
#     print("совершенно  летний ")
# else:
#     print("не совршенно летний ")





# name = input("введите ")
# print(f"привет {name }")





# def name(a,b):
#     return a + b
# print(name(2,3,))



# for i  in range(1,10+1):
#     print(i)




# my_list = [1,2,3,4,5,6,7,8,10]
# print(my_list)
#
#
# a = "hello"
# for i in a :
#     print(i)

# #
# a = int(input("ведите "))
# b = int(input("ведите "))
# print(a+b)


#
# def print_list(items):
#     for item in items:
#         print(item)
#
# my_list = ["яблоко","banan","вишня"]
# print_list(my_list)








# import hashlib
#
# # Функция для хеширования строки
# def hash_string(input_string):
#     # Создаем хэш-объект с алгоритмом SHA-256
#     hash_object = hashlib.sha256()
#     # Преобразуем строку в байты и обновляем хэш-объект
#     hash_object.update(input_string.encode('utf-8'))
#     # Возвращаем хэш в виде шестнадцатеричной строки
#     return hash_object.hexdigest()
#
# # Пример использования
# if __name__ == "__main__":
#     user_input = input("Введите строку для хеширования: ")
#     hashed = hash_string(user_input)
#     print(f"Хэш (SHA-256): {hashed}")



#
# num = int(input("ведите число "))
# if num  % 2 == 0:
#     print("число четное ")
# else:
#     print("число не четное ")


# def chek(num):
#     if num % 2  == 0 :
#         return  "число четное"
#     else:
#         return ("число не четное ")
#
# num = int(input("введите число:"))
#
# result = chek(num)
# print(result)



# num = 7
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


# temp = 30
# if temp > 40:
#     print ("hot ")
# elif temp > 20:
#     print ("warm")
# else:
#     print("cold ")
#





# x = "10"
# y = 5
# print(x * y )





#
# x = 3
# y = "3"
# print(x + int(y))



# def al (a):
#     return f"privet:{a}"
# print(al("esentur" ))
#
#
# for i in range (1,20):
#     if i % 2 == 0:
#         print(i)

# i =1
# while i <= 20 :
#     print(i)
#     i += 1
#





####################### практические ########################





#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range (2,int(num**0.5)+1):
#         if num % i == 0 :
#             return False
#         return True
#
#
#
# number = int(input("введите число:"))
# if is_prime(number):
#     print(f"{number}-простое число")
# else:
#     print(f"{number}-составное число")



# def is_palindrome(s):
#     s =  s.lower().replace("","")
#     return s == s [::-1]
#
#
# text = input("введите строку:")
# if is_palindrome(text):
#     print("это палиндром!")
# else:
#     print("это не палиндром.")

















































