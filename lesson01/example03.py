number = int(input("Введите число "))
degree2 = '{}{}'.format(number, number)
degree3 = '{}{}'.format(degree2, number)
sum = number + int(degree2) + int(degree3)

print(sum)