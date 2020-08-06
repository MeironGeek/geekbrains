proceeds = int(input("Введите значение выручки фирмы - "))
costs = int(input("Введите значение ваших издержек - "))
profit = proceeds - costs

if(proceeds > costs):
    print("Наша прибыль =", profit)
    print('Вы большие молодцы, отработали как надо, так держать!!!')
    rent = profit / proceeds * 100
    print("Наша рентабильность = {} %".format(round(rent, 1)))
    count = int(input("Сколько человек у вас работает? - "))
    print("Прибыль на каждого сотрудника =", profit / count)

elif(proceeds < costs):
    print("{}. Вижу отрицательное число, это плохо".format(profit))
    print('У вас не получилось. В следующем месяце справимся лучше!!!')

