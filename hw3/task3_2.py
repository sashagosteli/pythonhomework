# #### 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине 
# элемент к заданному числу X.  Пользователь вводит это число с клавиатуры, 
# список можно считать заданным. 
# Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

# list_1 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# number = int(input('Введите число: '))
# min = 0
# temp = 0
# result = 0
# for i in list_1:
    # if number == i:
    #     print(f'Число {number} есть в списке')
    #     break

lst = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
num = int(input('Введите число: '))
dist = abs(num - lst[0])
find_el = lst[0]
for idx, el in enumerate(lst):
    if abs(el - num) < dist:
        dist = abs(el - num)
        find_el = lst[idx]
print(find_el)