my_list = [7, 5, 3, 3, 2]

raiting = int(input("Нука дай оценку - "))
if raiting in my_list:
    my_list.insert(my_list.index(raiting), raiting)
elif raiting > max(my_list):
    my_list.insert(0, raiting)
elif raiting < min(my_list):
    my_list.append(raiting)

print(my_list)