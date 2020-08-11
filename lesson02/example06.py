products = []
n = int(input("Введите количество товаров которые хотите добавить в список - "))

for i in range(n):
    name = str(input("Введите название товара - "))
    price = int(input("Введите цену товара - "))
    quantity = int(input("Введите количество товара - "))
    product_type = str(input("Введите единицу измерения товара - "))
    product_dict = {"название" : name, 'цена' : price, 'количество' : quantity, 'единица измерения': product_type}
    cortage = (i+1, product_dict)
    products.append(cortage)

print(products)

analytics = {'название': [], 'цена': [], 'количество' : [], 'единица измерения' : []}
for value in products:
    for val in value:
        if type(val) is dict:
            for k,v in val.items():
                print(analytics[k])
                if k == 'единица измерения' and v in analytics[k]:
                    continue
                else:
                    analytics[k].append(v)


print(analytics)






