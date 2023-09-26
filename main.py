



# функция Фибоначчи при помощи анонимной функции
# def fib(n):
#     if n < 3:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# fib = lambda x: 1 if x < 3 else fib(x - 1) + fib(x - 2)
#
# print(fib(2))
# print(fib(5))


# Итераторы, которые возвращают функции map() и filter(), можно обойти только один раз.
# То есть при вторичной итерации мы будем получать уже пустой итератор.
# squares = map(lambda x: x ** 2, range(1, 10))
# print(*squares)
# print(*squares)


# Напишите программу, которая определяет минимальное и максимальное значения функции на отрезке в целых точках.
# f, a, b = input(), *map(int, input().split())
# row_f = []
# for x in range(a, b + 1):
#     row_f.append(eval(f))
#
# print(f'''Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(row_f)}
# Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(row_f)}
# ''')




# Напишите программу, которая принимает на вход произвольное количество строк, содержащих корректные математические выражения, и выводит значение наибольшего из них.
# print(max(map(eval, open(0))))
# Она может принимать в качестве аргумента не только абсолютный/относительный путь к файлу, но и дескриптор файла
# Под stdin (стандартный вход) в системе зарезервирован дескриптор 0



# если введен список, выводит его последний элемент
# если введен кортеж, выводит его первый элемент
# если введено множество, выводит количество его элементов
# def fff(l):
#     if isinstance(l, list):
#         return l[-1]
#     elif isinstance(l, tuple):
#         return l[0]
#     elif isinstance(l, set):
#         return len(l)
#
#
# data = [[1, 2], [3, 4], [5, 6]]
# print(fff(data))


# Функция exec(), в отличие от eval(), принимает блок кода и выполняет его, возвращая значение None.
# code = '''a = 10
# b = 20
# print(a + b)'''
#
# exec(code)
# выводит: 30

# Функция eval() выполняет строку-выражение, переданную ей в качестве обязательного аргумента, и возвращает результат выполнения этой строки.
# С помощью функции eval() можно парсить объекты, то есть преобразовывать из строки в реальные Python объекты.
# expression = '7 + 10.1'
#
# result = eval(expression)
# print(type(result))
# print(result)
#
# expression1 = "print('Привет из функции eval()')"
# expression2 = "len([1, 1, 1, 1, 1])"
#
# result1 = eval(expression1)
# result2 = eval(expression2)
#
# print(result1)
# print(result2)
#
# list_data = eval("['Python', 'C#', 'Java']")
# tuple_data = eval('(1, 2, 3, 4, 5)')
# dict_data = eval("{1: 'January', 2: 'February'}")
#
# print(type(list_data), len(list_data))
# print(type(tuple_data), max(tuple_data))
# print(type(dict_data), dict_data[2])

# Функция должна возвращать словарь, ключом в котором является хеш-значение объекта из списка objects, а значением — сам объект. Если хеш-значения некоторых объектов совпадают, их следует объединить в список.
# def hash_as_key(objects):
#     d = {}
#     for i in objects:
#         if hash(i) in d:
#             if isinstance(d[hash(i)], list):
#                 d[hash(i)].append(i)
#             else:
#                 d[hash(i)] = [d[hash(i)], i]
#         else:
#             d[hash(i)] = i
#     return d
#
# data = [1, 2, 3, 4, 5, 5]
#
# print(hash_as_key(data))


# Функция callable() принимает в качестве аргумента некоторый объект и возвращает True, если переданный объект является вызываемым, или False в противном случае.
# print(callable(int))
# print(callable(100))

# Функция hasattr() используется для проверки существования атрибута.
# print(hasattr([1, 2, 3], 'sort'))
# print(hasattr(13, 'to_str'))

# Функция hash() принимает в качестве аргумента некоторый объект и возвращает целое число, представляющее хеш-значение переданного объекта.
# print(hash(9999))
# print(hash('Robert'))
# print(hash([1, 2, 3])) # unhashable type: 'list' - Изменяемые коллекции, такие как списки, множества и словари, не имеют хеш-значений.

# Функция help() используется для получения документации по указанному модулю, функции или другому объекту.
# help(print)
# help(sorted)

# Функция repr() принимает в качестве аргумента некоторый объект и возвращает строку, содержащую формальное (понятное интерпретатору) представление переданного объекта.
# from datetime import date
#
# print(repr('stepik'))
# print(repr([1, 2, 3, 4]))
# print(repr(date(2022, 1, 16)))



# программа, которая сортирует символы в строке согласно следующим правилам:
# все отсортированные строчные буквы стоят перед заглавными буквами
# все отсортированные заглавные буквы стоят перед цифрами
# все отсортированные нечетные цифры стоят перед отсортированными четными
# v1:
# def sort_trash(string: str):
#     l = list(string)
#     l.sort()
#     little_alph = [i for i in l if i.isalpha() and i == i.lower()]
#     big_alph = [i for i in l if i.isalpha() and i == i.upper()]
#     odd_numb = [i for i in l if i.isdigit() and int(i) % 2 != 0]
#     even_numb = [i for i in l if i.isdigit() and int(i) % 2 == 0]
#     res = little_alph + big_alph + odd_numb + even_numb
#     return ''.join(res)
#
#
# s = input()
# print(sort_trash(s))

# v2:
# def comparator(char):
#     if char.isalpha():
#         return 0, char.isupper(), char
#     digit = int(char)
#     return 1, digit % 2 == 0, digit
#
# string = input()
#
# print(''.join(sorted(string, key=comparator)))



# Функция должна объединять элементы переданных последовательностей в кортежи, аналогично функции zip(), и возвращать в
# виде списка, но если последовательности имеют различную длину, недостающие элементы последовательностей меньшей длины должны принимать значение fill
# def zip_longest(*args, fill=None):
#     max_len = max(map(len, args))
#     lst = [i + [fill] * (max_len - len(i)) for i in args]
#     return list(zip(*lst))
#
#
# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))



# Нужно чтобы он определил, какую прибыль принес каждый мультфильм, и вывел названия мультфильмов, указав для каждого соответствующую прибыль
# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
#
# for name, budgets, box_offices in sorted(zip(names, budgets, box_offices)):
#     print(f'{name}: {box_offices - budgets}$')



# Функция должна возвращать сумму, состоящую из цифр числа, возведенных в степень их порядкового номера. 1^1 + 3^2 + 9^3 = 739
# def my_pow(number):
#     return sum(int(c )* *i for i, c in enumerate(str(number) ,1))
#
#
# print(my_pow(139))



# Доступен список numbers. Он должен вывести индекс максимального элемента в этом списке.
# numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
#
# print(numbers.index(max(numbers)))
# # или
# print(max(enumerate(numbers), key=lambda x: x[1])[0])


# Функция должна возвращать единственное число — количество объектов из списка objects, которые принадлежат типу typeinfo или одному из типов, если был передан кортеж.
# def custom_isinstance(objects, typeinfo):
#     return sum(isinstance(i, typeinfo) for i in objects)
#
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, (int, float)))



# Функция должна возвращать True, если хотя бы в одном вложенном списке из списка lists сумма всех элементов больше number, или False в противном случае.
# def is_greater(lists, number):
#     return any(sum(i) > number for i in lists)
#
#
# data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
#
# print(is_greater(data, 10))



# Функция должна возвращать True, если все числа в списке numbers являются четными и неотрицательными, или False в противном случае.
# def non_negative_even(numbers):
#     return all(i % 2 == 0 and i >= 0 for i in numbers)
#
#
# print(non_negative_even([0, 2, 4, 8, 16]))
# print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
# print(non_negative_even([64, 78, 4454, 234, 90, 78, 67676]))
#
#
# def main():
#     pass
#
#
# if __name__ == '__main__':
#     main()
