seconds = int(input("Введите количество секунд "))
minutes = seconds // 60
hours = minutes // 60

print("Время:","{:02d}:{:02d}:{:02d}".format(hours, minutes % 60, seconds % 60))