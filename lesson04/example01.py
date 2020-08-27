def salary_employee():
    try:
        time = float(input("Выроботка в часах"))
        salary = id(input("Ставка"))
        bonus = int(input("Премия"))
        result = time * salary + bonus
        print(f'заработная плата сотрудника {result}')
    except ValueError:
        return print('Not a number')

salary_employee()