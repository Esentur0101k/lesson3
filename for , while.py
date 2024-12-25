





# while — это один из видов циклов в Python, который выполняет блок кода многократно, пока
# выполняется условие. То есть, цикл while продолжает выполняться до тех пор, пока условие остается
# истинным(True).



# x = 0
# while x < 5:
#     print(x)  # Выводим значение x
#     x += 1  # Увеличиваем x на 1



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

# i = 0
# j = 10
#
# while i < 10 and j >= 0:
#     print(f" i = {i} j = {j}")
#     i = i + 1 = 1:
#     j = i + 1 = 1:












###################################### for цикл ################################



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
#
#
# a = ['aple', 'banana', 'orahge']
#
# for i in a:
#     print(i)


# a = ["Python"]
# for i  in a:
#     print(i)






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



# for i in range(0,11):
#     print(i)







