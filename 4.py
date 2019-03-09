"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random

beginInt = int(input("Укажите начало границы диапазона целого числа: "))
endInt = int(input("Укажите конец границы диапазона целого числа: "))
print("Случайное целое число в диапазоне от <%d> до <%d>: %d;" %(beginInt, endInt, random.randint(beginInt, endInt)))

beginFloat = float(input("Укажите начало границы диапазона вещественного числа: "))
endFloat = float(input("Укажите конец границы диапазона вещественного числа: "))
print("Случайное вещественное число в диапазоне <%.3f> до <%.3f>: %.3f;" %(beginFloat, endFloat, random.uniform(beginFloat, endFloat)))

beginChar = input("Укажите начало границы диапазона случайного символа: ")
endChar = input("Укажите конец границы диапазона случайного символа: ")
print("Случайный символ в диапазоне от <%s> до <%s>: %s;" %(beginChar, endChar, chr(random.randint(ord(beginChar), ord(endChar)))))
