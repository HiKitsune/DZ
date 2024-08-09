number = int(input("Введите число: "))
if number % 6 == 0 or number % 10 == 0:
    print('first')
elif number % 3 == 0:
    print('second')
elif number % 5 == 0:
    print('third')
else:
    print('Число не подходит')