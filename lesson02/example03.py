input_month = int(input("Введи порядковый номер месяца - "))

#Решение с dict
seasons_dict = {'Зима':{11,12,1},'Весна':{2,3,4}, 'Лето':{5,6,7}, 'Осень':{8,9,10}}
for key,val in seasons_dict.items():
    if input_month in val:
        print(key)

#Решение с list
seasons_month = [
    [11, 12, 1],
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

for i,value in enumerate(seasons_month):
    if input_month in value:
        print(seasons_list[i])