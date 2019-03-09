"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""
lenLine1 = int(input("Укажите длину первого отрезка в мм: "))
lenLine2 = int(input("Укажите длину второго отрезка в мм: "))
lenLine3 = int(input("Укажите длину третьего отрезка в мм: "))

#проверка: существование треугольника возможно, когда сумма длинн двух отрезков больше длины третьего отрезка
if (lenLine1 + lenLine2 <= lenLine3) or (lenLine1 + lenLine3 <= lenLine2) or (lenLine2 + lenLine3 <= lenLine1):
    print("При заданных условиях существование треугольника не возможно.")

#определяем тип треугольника
else:
    if (lenLine1 != lenLine2) and (lenLine1 != lenLine3) and (lenLine2 != lenLine3):
        print("Треугольник - разносторонний.")
    elif lenLine1 == lenLine2 == lenLine3:
        print("Треугольник - равносторонний.")
    else:
        print("Треугольник - равнобедренный.")




