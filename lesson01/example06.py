start = int(input("Сколько км бегаешь сейчас - "))
end = int(input("Сколько км хочешь достичь - "))
i = 1

while(start < end):
    start = start + start / 100 * 10
    i += 1
    if(start > end):
        print("Ты достигнешь желаемого результата в {} км, через {} дней".format(end,i))
        break