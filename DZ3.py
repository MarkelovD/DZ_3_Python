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
nums = int(input("введите число в десятичном формате: "))
stroka=""
while nums>-1:
    a=nums%2
    nums=nums//2
    stroka+=str(a)
    if nums==0:
        break
reversSroka="".join(reversed(stroka))
print(reversSroka)