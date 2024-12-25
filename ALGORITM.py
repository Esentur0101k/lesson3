from operator import length_hint


############################## АЛГОРИТМЫ ###########################




#
# def bsort(array):
#     length =  len (array)
#     for i in range (length):
#         for  j in range (0,length-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
# array = [3,4,5,6,7,8,8,6,4,3,2,2,4,5,6,1,2]
# bsort(array)
# print(array)

############# хд коды ################

num = [2,3,1,5,8,9,4]
print(num)

for i in range(len(num)):
    for j in range(len(num)-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1] =  num[j+1] , num[j]

            print(num)
###########







def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
    return arr

numbers = [8, 4, 3, 7, 6, 5, 2]
print("До сортировки:", numbers)
sorted_numbers = insertion_sort(numbers)
print("После сортировки:", sorted_numbers)

















#
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

