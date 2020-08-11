numbers = []
n = int(input("Введите количество элементов в списке - "))
for i in range(n):
    new_element = str(input("Вводи элемент списка - "))
    numbers.append(new_element)

for key in numbers:
    i = numbers.index(key)
    if i + 1 == len(numbers):
        break
    if i % 2 == 0:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)