# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# a = [1,2,3,4,5,6,7]
# sum = 0
# for i in range (1,len(a),2):
#     sum+=a[i]
# print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# a = [1,2,3,7,4,3,8,4,8]
# b = []
# sum = 0
# for i in range(int(len(a)/2)):
#     b.append(a[i]*a[len(a)-1-i])
# if len(a)%2!=0:
#     b.append(a[int(len(a)/2)]**2)
# print(a)
# print(b)

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# nums = int(input("введите число в десятичном формате: "))
# stroka=""
# while nums>-1:
#     a=nums%2
#     nums=nums//2
#     stroka+=str(a)
#     if nums==0:
#         break
# reversSroka="".join(reversed(stroka))
# print(reversSroka)

# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# import random
# listNum = [round(random.uniform(0,20),2)for i in range (random.randint(5,10))]
# drobnayChast = []
# print(listNum)
# for i in listNum:
#     i=round((i%1),2)
#     drobnayChast.append(i)
# print(drobnayChast)
# raznica = round(max(drobnayChast)-min(drobnayChast),2)
# print(f"разница между минимальной дробной частью {max(drobnayChast)} и минимальной дробной частью {min(drobnayChast)} = {raznica}")

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
lenght = 8
positiv = [0,1]
negative = [0,1]
for i in range (lenght-1):
    positiv.append(positiv[-2]+positiv[-1])
print(positiv)
for i in range(lenght-1):
     negative.append((negative[-2]-negative[-1]))
print(negative)
print(negative[::-1]+positiv[1::])