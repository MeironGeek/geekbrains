words = str(input("Введите предложение - "))
lst = words.replace('.', '').split()
i = 1
for val in lst:
    if(len(val) > 10):
        val = val[:10]
    print("Слово под номером", "{} {}".format(i, val))
    i += 1
