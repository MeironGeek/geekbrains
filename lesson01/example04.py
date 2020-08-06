number = int(input("Введите целое положительное число "))
check = -1

while number > 10:
    d = number % 10
    number //= 10
    if d > check:
        check = d

if(check == -1) :
    print('Самое больше число =', number)
elif (check < number):
    print('Самое больше число =', number)
else:
    print('Самое больше число =', check)