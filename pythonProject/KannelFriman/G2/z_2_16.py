"""Напишите класс, который принимает с клавиатуры целое число и выводит
на экран два новых числа (каждое в отдельное строке): число,
больше введенного с клавиатуры на 6, и число, меньше введенного с
клавиатуры на 12."""

number = int(input('Введите число...'))
min_num = number-6
max_num = number+12
print(min_num)
print(max_num)