





#############################  constructor ####################


#
# class Car:
#
#     def __init__(self,model , marka , color ):
#         self.__model = model
#         self.__marka = marka
#         self.__color = color
#
#
#
#
#     def get_model(self):
#         return self.__model
#
#     def set_model(self,new_model):
#         self.__model = new_model
#
#     def set_color(self,new_color):
#         self.__color = new_color
#
#
#
#
#     def start(self):
#         print(f'{self.__model} Car is starting ')
#
#     def move(self):
#         print(f"{self.__model} Car is moving")
#
#     def stop(self):
#         print(f"{self.__model} Car is stoping")
#
#     def display_info(self):
#         print(f"model: {self.__model}\n"
#         f'marka: {self.__marka}\n'
#         f'color: {self.__color}\n'
#         )
#
#
# mers = Car('mers','cls amg','black',)
# mers.set_color('yellow')
# mers.set_model('mazda ')
# mers.display_info()
# mers.get_model()




# class Human:
#     def __init__(self,name , age, gender):
#         self.name = name
#         self.age = age
#         self._gender = gender
#
#
#     def get_gender(self):
#         return self._gender
#
#
#     def get_age(self):
#         return self.age
#
#
#
#     def introduce(self):
#         print(f'Привет, меня зовут:{self.name}')
#
#     def add_age(self):
#         print(f'Мне:{self.age} лет ')
#
#     def add_gender(self):
#         print(f'я:{self._gender}')
#
#
#     def display_info(self):
#         print(f"name:{self.name}\n"
#         f'age:{self.age}\n'
#         f'gender:{self._gender}\n'
#
#         )
#
# add = Human('Дима','25','мужчина')
# add.name = 'aleks'
# add.gender = 'женский'
# add.display_info()
# add.get_gender()
# print(add.get_gender())
# print(add.add_age())



# class Smartphone:
#     def __init__(self, brand, model, price, os):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.__os = os
#
#
#     def get_model(self):
#         return self.model
#
#     def get_info(self):
#
#         return f"{self.brand} {self.model} на {self.__os} - ${self.price}"
#
#
# smartphone = Smartphone("OPPO", "Find X5", 799, "Android")
#
# smartphone.brand = ('redmi')
# smartphone.os = ('ios')
#
# print(smartphone.get_info())
# print(smartphone.get_model())






class Smart_home:
    def __init__(self,name_home,start , year , ):
        self.name_home = name_home
        self.start =  start
        self.year = year


    def add_name_home(self):
        print(f"имя умного дома {self.name_home}")


    def add_start(self):
        print({self.start})

    def add_year(self):
        print(f"год выпуска умного дома{self.year}")













#
# class Animals:
#
#     def __init__(self,name ,age , color ):
#         self.name = name
#         self.age = age
#         self.color = color
#
#
#
#     def run(self):
#         print(f'{self.name},лев бежать ' )
#
#     def stop(self):
#         print(f'{self.name}:остановись')
#
#     def to_hunt(self):
#         print(f'{self.name}добывай еду охоться ')
#
# lev  =Animals ('leon','4','black')
#
#
# lev.run()
# lev.stop()




# class Home:
#     def __init__(self,adress,tv,fridge):
#         self.adress = adress
#         self.tv = tv
#         self.fridge = fridge
#
#
#
#     def add_adress(self):
#         print(f'Дом по адресу:{self.adress}')
#
#     def add_tv(self, color):
#         print(f'телевизор {self.tv}:дюймов{color}')
#
#     def add_fridge(self):
#         print(f'холодильник:{self.fridge}литров')
#
# my_home = Home('ул, патриса лумумбы 86','55','300')
#
# my_home.add_adress()
# my_home.add_tv('black')
# my_home.add_fridge()



# class Sport :
#     def __init__(self,age ,otkuda , spots,name  ):
#         self.name = name
#         self.age = age
#         self.otkuda = otkuda
#         self.sports = spots
#
#     def add_name (self):
#         print(f'имя:{self.name}')
#
#
#     def add_age (self):
#         print(f'ему {self.age}')
#
#     def talas (self):
#         print(f'он родился в :{self.otkuda}')
#
#     def add_sports (self,prizer):
#         print(f'чемпион по :{self.sports},{prizer}')
#
# sportic = Sport('27','талас','грекоримcкой  борьбе','Акжол Махмудов')
#
#
# sportic.add_name()
# sportic.add_age()
# sportic.talas()
# sportic.add_sports(2024)
# sportic.add_sports(f'призер 2024 года франция ')






# class Meal:
#     def __init__(self,drinks,food, bludo):
#         self.drinks = drinks
#         self.food = food
#         self. bludo = bludo
#
#
#     def add_drinks(self,price ):
#         print(f'есть такие напитки как: {self.drinks}{price}')
#
#     def add_food(self,price):
#         print(f'фастфуды на выбор:{self.food}{price}')
#
#     def add_bludo(self,price ):
#         print(f'любые вид блюд блюда на выбор:{self.bludo}{price}')
#
# add_fud = Meal('coca cola,fanta,sprite:','гамбургерб,ход-дог,сендвич,донер:','блины ,пельмени , и др:')
#
# add_fud.add_drinks  ('цена от:3$')
# add_fud.add_food("цена от:5$:до 5$")
# add_fud.add_bludo("цена от 2$:до 3$")



# class Student:
#     def __init__(self,name,age  ,uroki,):
#         self.name =  name
#         self.age = age
#         self.uroki = uroki
#
#     def add_name(self):
#         print(f'имя : {self.name}')
#
#     def add_age(self):
#         print(f'ему: {self.age} лет он студент ')
#
#
#     def add_uroki(self,a):
#         print(f'сегодня он получил по матеметике:{self.uroki} и по истории:{a}','хороший результат ')
#
# add = Student('Максим','17','4',)
# add.add_name()
# add.add_age()
# add.add_uroki('5')


# class Car:
#     def __init__(self,brand , model):
#         self.brand = brand
#         self.model = model
#
#     def start_engine(self):
#         return f'машина {self.brand}{self.model} завелась.'
#
# my_car = Car("toyota",'corolla')
#
# print(my_car.start_engine())







# class Meal:
#     def __init__(self, drinks, food, bludo, drinks_price, food_price, bludo_price):
#         self.drinks = drinks
#         self.food = food
#         self.bludo = bludo
#         self.drinks_price = drinks_price
#         self.food_price = food_price
#         self.bludo_price = bludo_price
#
#     def add_drinks(self):
#         print(f'Есть такие напитки как: {self.drinks} | Цена от: {self.drinks_price}')
#
#     def add_food(self):
#         print(f'Фастфуды на выбор: {self.food} | Цена от: {self.food_price}')
#
#     def add_bludo(self):
#         print(f'Любые блюда на выбор: {self.bludo} | Цена от: {self.bludo_price}')
#
# # Создание объекта Meal с указанием цен
# add_fud = Meal('Coca Cola, Fanta, Sprite', 'Гамбургер, Хот-дог, Сендвич, Донер', 'Блины, Пельмени и др.', '3$', '5$', '2$')
#
# # Вызов методов с выводом информации о ценах
# add_fud.add_drinks()
# add_fud.add_food()
# add_fud.add_bludo()




######################### DZ #######################

# class Bus:
#     def __init__(self,brand,model,year,mesta,topliva):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.mesta = mesta
#         self.topliva = topliva
#
#
#     def add_brand(self):
#         print(f'Марка автобуса:{self.brand}')
#
#     def add_model(self):
#         print(f'Модель автобуса:{self.model}')
#
#     def add_year(self):
#         print(f'Год выпуска:{self.year}')
#
#     def add_mesta(self,):
#         print(f'Количество мест:{self.mesta}')
#
#     def add_topliva(self):
#         print(f'Тип топлива:{self.topliva}')
#
#
# transport = Bus('Лотос','Лотос 216','2016','27','Газ')
#
# transport.add_brand()
# transport.add_model()
# transport.add_year()
# transport.add_mesta()
# transport.add_topliva()


#
#
# class Animals:
#     def __init__(self,name ,width , color, country):
#
#         self.name = name
#         self.width =  width
#         self.color = color
#         self.country = country
#
#     def golos(self):
#         print("Animals голос")
#
#     def spat(self,name):
#         print(f"{name} спать ")
#     def food(self):
#         print("Animals  кушать")
#
# class Dog(Animals):
#     def __init__(self,name , width , color , country , poroda , pol):
#         self.name = name
#         self.width = width
#         self.color = color
#         self.country = country
#         self.poroda = poroda
#         self.pol = pol
#
#
#     def fas(self):
#         print(f"{self.name} fas")
#
#     def ohrana(self):
#         print(f"{self.name} protect the house")
#
#
#
# animals = Dog('reks',30,'black',' Kyrgyzstan','taygan','mun')
#
# animals.ohrana()
# Animals.golos("reks")



# class Home:
#     def __init__(self,adress ,vnutri,fridje,tv):
#         self.adress = adress
#         self.vnutri = vnutri
#         self.fridje = fridje
#         self.tv = tv
#
#
#     def add_adress(self):
#         print(f'адрес:{self.adress}')
#
#     def add_vnutri(self):
#         print(f'в доме внутри имеется:{self.vnutri}')
#
#     def add_fride(self):
#         print(f'{self.fridje}')
#
#     def add_tv(self):
#         print(f'модель:{self.tv}')
    
    
        
# class Add_home(Home):
#
#     def __init__(self,adress,vnutri,fridje,tv,kv,komnata,zerkala):
#         self.adress = adress
#         self.vnutri = vnutri
#         self.fridje = fridje
#         self.tv = tv
#         self.kv = kv
#         self.komnata = komnata
#         self.zerkala = zerkala
#
#
#     def add_kv(self):
#         print(f' тип дома :{self.kv} дома')
#
#     def add_komnat(self):
#         print(f'внутри дома:{self.komnata}комнат')
#
#     def add_zerkala(self):
#         print(f'в доме находятся:{self.zerkala}')
#
# red = Add_home('садыгалиева','комфортно','300 литров','samsung','этажка','3','5')
#
# red.add_adress()




###########################################


# Родительский класс
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} издаёт звук."
#
# # Дочерний класс
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} гавкает."
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} мяукает."
#
# # Использование
# dog = Dog("Барсик")
# cat = Cat("Мурзик")
#
# print(dog.speak())  # Барсик гавкает.
# print(cat.speak())  # Мурзик мяукает.



##################################################3






















