












# import re
# import sys
#
#
# def extract_attributes(html_fragment):
#     tags_attributes = {}
#
#     tag_pattern = re.compile(r'<([^\s>/]+)(.*?)>')
#     matches = re.finditer(tag_pattern, html_fragment)
#
#     for match in matches:
#         tag = match.group(1)
#         attributes_str = match.group(2)
#
#         attribute_pattern = re.compile(r'(\S+?)\s*=\s*["\'](.*?)["\']')
#         attribute_matches = re.finditer(attribute_pattern, attributes_str)
#
#         attributes = [match.group(1) for match in attribute_matches]
#
#         tags_attributes[tag] = attributes
#
#     return tags_attributes
#
#
# if __name__ == "__main__":
#     html_fragment = sys.stdin.read()
#
#     tags_attributes = extract_attributes(html_fragment)
#
#     for tag, attributes in sorted(tags_attributes.items()):
#         print(f"{tag}: {', '.join(sorted(attributes))}")







# import re
#
#
# def abbreviate(phrase):
#     pattern = r'(\b[A-Za-z]|[A-Z])'
#     match1 = re.findall(pattern, phrase)
#     return ''.join(match1).upper()
#
#
# print(abbreviate('javaScript object notation'))
# print(abbreviate('frequently asked questions'))
# print(abbreviate('JS game sec'))











# import re
# import sys
#
# data = [s.strip() for s in sys.stdin]
# pattern = r'beegeek'
#
# count = 0
#
# for i in data:
#     if re.search(pattern, i, flags=re.IGNORECASE):
#         count += 1
#
# print(count)







# import re
# import sys
#
# pattern1 = r'^(beegeek).*(beegeek)$'
# pattern2 = r'^beegeek|beegeek$'
# pattern3 = r'.+beegeek.+'
#
# data = [word.strip() for word in sys.stdin]
# power = 0
#
# for string in data:
#     if re.search(pattern1, string):
#         power += 3
#     elif re.search(pattern2, string):
#         power += 2
#     elif re.search(pattern3, string):
#         power += 1
#
# print(power)





# import re
# import sys
#
# pattern1 = r'((bee).*){2,}'
# pattern2 = r'\bgeek\b'
#
# data = [word.strip() for word in sys.stdin]
# match1 = [re.search(pattern1, word).group() for word in data if re.search(pattern1, word)]
# match2 = [re.search(pattern2, word).group() for word in data if re.search(pattern2, word)]
#
# print(len(match1))
# print(len(match2))





# {n}	ровно n повторений
# {m,n}	от m до n повторений включительно
# {m,}	не менее m повторений
# {,n}	не более n повторений
# ?	ноль или одно вхождение, синоним {0,1}
# *	ноль или более, синоним {0,}
# +	одно или более, синоним {1,}

# regex = r'\+7\d{10}|\+7\(\d{3}\)\d{7}|\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}|\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}'





# import re
# import sys
#
#
# pattern = r'_\d+[A-Za-z]*_?'
# data = [text.strip() for text in sys.stdin]
# for i in data:
#     if re.fullmatch(pattern, i):
#         print(True)
#     else:
#         print(False)





# import itertools as it
# from string import ascii_uppercase, digits
#
# n, m = int(input()), int(input())
# symbols = (digits + ascii_uppercase)[:n]
#
# print(*map("".join, it.product(symbols, repeat=m)))






# from string import ascii_lowercase
# from itertools import product
#
# letters = ascii_lowercase[:8]
# digits = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for i in product(letters, digits):
#     print(*i, sep='', end=' ')








# from itertools import product
#
# for time in product(range(24), range(60), range(60)):
#     print(*time, sep=' : ')







# from collections import namedtuple
# import itertools
#
# Item = namedtuple('Item', ['name', 'mass', 'price'])
#
# items = [Item('Обручальное кольцо', 7, 49_000),
#          Item('Мобильный телефон', 200, 110_000),
#          Item('Ноутбук', 2000, 150_000),
#          Item('Ручка Паркер', 20, 37_000),
#          Item('Статуэтка Оскар', 4000, 28_000),
#          Item('Наушники', 150, 11_000),
#          Item('Гитара', 1500, 32_000),
#          Item('Золотая монета', 8, 140_000),
#          Item('Фотоаппарат', 720, 79_000),
#          Item('Лимитированные кроссовки', 300, 80_000)]
#
# def bag(power_mass):
#     cur_tuple = None
#     cur_power_price = 0
#     m = all(map(lambda x: x.mass > power_mass, items))
#     if m:
#         return ['Рюкзак собрать не удастся']
#
#     for n in range(1, len(items) + 1):
#         for i in itertools.combinations(items, n):
#             if sum(j.mass for j in i) <= power_mass and sum(j.price for j in i) > cur_power_price:
#                 cur_power_mass = sum(j.mass for j in i)
#                 cur_tuple = [k.name for k in i]
#                 cur_power_price = sum(j.price for j in i)
#     return sorted(cur_tuple)
#
# print(*bag(int(input())), sep='\n')





# from itertools import permutations
#
# numbers = [1, 2, 3, 4]
# letters = 'cba'
#
# all_num_permutations = permutations(numbers)
# all_let_permutations = permutations(letters)
#
# print(list(all_num_permutations))
# print(list(all_let_permutations))



# from itertools import groupby
#
# def group_anagrams(words: list) -> list:
#     words_sorted = sorted(words, key=lambda x: sorted(list(x)))
#     g = groupby(words_sorted, key=lambda x: sorted(list(x)))
#     s = []
#     for key, val in g:
#         s.append(tuple(val))
#     return s
#
# groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
#
# print(*groups)






# from itertools import groupby
#
# tasks = [('Отдых', 'поспать днем', 3),
#         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
#         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
#         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
#         ('Отдых', 'погулять вечером', 4),
#         ('Курс по ооп', 'обсудить темы', 1),
#         ('Урок по groupby', 'добавить задачи на программирование', 3),
#         ('Урок по groupby', 'написать конспект', 1),
#         ('Отдых', 'погулять днем', 2),
#         ('Урок по groupby', 'добавить тестовые задачи', 2),
#         ('Уборка', 'убраться в ванной', 2),
#         ('Уборка', 'убраться в комнате', 1),
#         ('Уборка', 'убраться на кухне', 3),
#         ('Отдых', 'погулять утром', 1),
#         ('Курс по ооп', 'обсудить задачи', 2)]
#
# s = sorted(sorted(tasks, key=lambda x: x[-1]), key=lambda x: x[0])
# g = groupby(s, key=lambda x: x[0])
# for key, val in g:
#     print(f'{key}:')
#     for i in val:
#         print(f'    {i[-1]}. {i[-2]}')
#     print()










# from itertools import groupby
#
# s = sorted(input().split(), key=len)
# g = groupby(s, key=len)
# for key, val in g:
#     print(f'{key} -> {", ".join(sorted(list(val)))}')









# from itertools import zip_longest
#
# def grouper(iterable, n, fillvalue=None):
#     args = [iter(iterable)] * n
#     return zip_longest(*args, fillvalue=fillvalue)
#
#
# iterator = iter([1, 2, 3, 4, 5, 6, 7])
#
# print(*grouper(iterator, 3))


# from itertools import tee, chain
#
# def ncycles(iterable, times=1):
#     tee_object = tee(iterable, times)
#     for i in chain.from_iterable(tee_object):
#         yield i
#
#
# iterator = iter('bee')
#
# print(*ncycles(iterator, 4))


# from itertools import pairwise, starmap
#
# def max_pair(iterable):
#     pairwise_object = pairwise(iterable)
#     res = starmap(lambda x, y: x + y, pairwise_object)
#     return max(res)


# import itertools
#
# def roundrobin(*args):
#     iterators = [iter(arg) for arg in args]
#     return (i for a in itertools.zip_longest(*iterators, fillvalue='') for i in a if i != '')
#
# print(*roundrobin('abc', 'd', 'ef'))
# print(*roundrobin([1, 2, 3], iter('beegeek')))
# print(list(roundrobin()))


# import itertools as it
# import time
#
# symbols = ['.', '-', "'", '"', "'", '-', '.', '_']
#
# for c in it.cycle(symbols):
#     print(c, end='')
#     time.sleep(0.05)


# def stop_on(iterable, obj):
#     it = iter(iterable)
#     return iter(lambda: next(it), obj)


# def flatten(nested_list):
#     for i in nested_list:
#         if isinstance(i, list):
#             yield from flatten(i)
#         else:
#             yield i
#
#
# generator = flatten([[1, 2], [[3]], [[4], 5]])
#
# print(*generator)


# def palindromes():
#     n = 0
#     while True:
#         n += 1
#         if str(n) == str(n)[::-1]:
#             yield n


# class Xrange:
#     def __init__(self, start, end, step=1):
#         self.start = start
#         self.end = end
#         self.step = step
#         self.current = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if (self.step > 0 and self.current < self.end) or (self.step < 0 and self.current > self.end):
#             result = self.current
#             self.current += self.step
#             return result
#         else:
#             raise StopIteration


# class Cycle:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index == len(self.iterable):
#             self.index = 0
#         return self.iterable[self.index]


# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.degree = -1
#
#     def __iter__(self):
#         return iter
#
#     def __next__(self):
#         self.degree += 1
#         return self.number ** self.degree


# class Fibonacci:
#     def __init__(self):
#         self.n1 = 0
#         self.n2 = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.n1, self.n2 = self.n2, self.n1 + self.n2
#         return self.n1
#
# fibonacci = Fibonacci()
#
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))


# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index == self.times:
#             raise StopIteration
#         return self.obj
#
#
# geek = BoundedRepeater('geek', 3)
#
# print(next(geek))
# print(next(geek))
# print(next(geek))
#
# try:
#     print(next(geek))
# except StopIteration:
#     print('Error')


# from random import randint
#
#
# def random_numbers(left, right):
#     rand_num = randint(left, right)
#     return iter(lambda: rand_num, 'hi')


# def get_min_max(iterable):
#     try:
#         iterable = iter(iterable)
#         min_el = next(iterable)
#         max_el = min_el
#         for i in iterable:
#             if i < min_el:
#                 min_el = i
#             if i > max_el:
#                 max_el = i
#         return (min_el, max_el)
#     except:
#         return None
#
#
# data = list(range(1, 101))[::-1]
#
# print(get_min_max(data))


# def transpose(matrix):
#     return [list(row) for row in zip(*matrix)]


# import functools
#
#
# class MaxRetriesException(Exception):
#     pass
#
#
# def retry(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception:
#                     pass
#             raise MaxRetriesException()
#         return wrapper
#     return decorator
#
#
# @retry(3)
# def no_way():
#     raise ValueError
#
#
# try:
#     no_way()
# except Exception as e:
#     print(type(e))


# import functools
#
#
# def ignore_exception(*exceptions):
#     def inner(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as err:
#                 if err.__class__ in exceptions:
#                     print(f'Исключение {err.__class__.__name__} обработано')
#                 else:
#                     raise err
#         return wrapper
#     return inner
#
#
# @ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())


# import functools
#
#
# def add_attrs(**kwargs):
#     def inner(func):
#         for k, v in kwargs.items():
#             setattr(func, k, v)
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return inner
#
#
# @add_attrs(attr1='bee', attr2='geek')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)


# import functools
#
#
#
# def takes(*argss):
#     def checker(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             f = func(*args, **kwargs)
#             flag = False
#             for i in (*args, *kwargs.values()):
#                 if type(i) in argss:
#                     flag = True
#                     return f
#                 else:
#                     raise TypeError
#         return wrapper
#     return checker


# import functools
#
#
# def returns(datatype):
#     def decor(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             f = func(*args, **kwargs)
#             if isinstance(f, datatype):
#                 return f
#             else:
#                 raise TypeError
#         return wrapper
#     return decor


# import functools
#
#
# def repeat(times=1):
#     def decor(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 f = func(*args, **kwargs)
#             return f
#         return wrapper
#     return decor
#
#
# @repeat(3)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
#
# say_beegeek()


# import functools
#
#
# def make_html(tag):
#     def inner(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             f = func(*args, **kwargs)
#             return f'<{tag}>{f}</{tag}>'
#         return wrapper
#     return inner


# import functools
#
# def prefix(string, to_the_end=False):
#     def decor(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             r = func(*args, **kwargs)
#             if to_the_end:
#                 return r + string
#             else:
#                 return string + r
#         return wrapper
#     return decor


# import functools
#
# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         f = func(*args, **kwargs)
#         print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
#         print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(f)}')
#         return f
#     return wrapper
#
#
# @trace
# def sub(a, b, c):
#     '''прекрасная функция'''
#     return a - b + c
#
#
# print(sub.__name__)
# print(sub.__doc__)
# sub(20, 5, c=10)


# import functools
#
#
# def returns_string(func):
#     @functools.wraps(func)
#     def revisor(*args, **kwargs):
#         val = func(*args, **kwargs)
#         if type(val) == str:
#             return val
#         else:
#             raise TypeError
#     return revisor


# import functools
#
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         f = func(*args, **kwargs)
#         return f ** 2
#     return wrapper
#
# @square
# def add(a, b):
#     return a + b
#
# print(add(3, 7))


# import functools
# import time
#
#
# def slow_down(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @slow_down
# def countdown(number):
#     if number < 1:
#         print('Конец!')
#     else:
#         print(number)
#         countdown(number - 1)
#
#
# countdown(5)


# import functools
#
# def counter(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.num += 1
#         print(f'Вызов {func.__name__}: {wrapper.num}')
#         val = func(*args, **kwargs)
#         return val
#     wrapper.num = 0
#     return wrapper
#
# @counter
# def greet(name):
#     return f'Hello {name}!'
#
# print(greet('Timur'))
# print(greet('Ruslan'))
# print(greet('Arthur'))
# print(greet('Gvido'))


# import functools, time
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         val = func(*args, **kwargs)
#         end = time.perf_counter()
#         work_time = end - start
#         print(f'Время выполнения {func.__name__}: {round(work_time, 4)} сек.')
#         return val
#     return wrapper
#
# @timer
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])
#
# @timer
# def sleep(n):
#     time.sleep(n)
#
# res1 = test(10000)
# res2 = sleep(4)
#
# print(f'Результат функции test = {res1}')
# print(f'Результат функции sleep = {res2}')


# import functools
#
# def bold(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper
#
# @bold
# def greet(name):
#     '''Function greet user.'''
#     return f'Hello {name}!'
#
# print(greet.__name__)
# print(greet.__doc__)


# замыкание — это особый вид функции. Она определена в теле другой функции и создаётся каждый раз во время её выполнения
# def closure():
#    count = 0
#    def inner():
#        nonlocal count
#        count += 1
#        print(count)
#    return inner

# start = closure()
# another = closure()  # другое замыкание, со своими локальными значениями
# third = closure()

# start()  # выводит 1
# start()  # выводит 2
# another()  # выводит 1
# start()  # выводит 3


# Реализуйте функцию polynom(), которая принимает один аргумент: x, должна возвращать значение выражения x**2+1
# Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции, которые уже были вычислены.
# def polynom(x):
#     # Вычисляем значение выражения
#     result = x ** 2 + 1
#
#     # Используем атрибут __dict__ для доступа к атрибуту values
#     # и метод setdefault() для добавления значения в множество values
#     polynom.__dict__.setdefault('values', set()).add(result)
#
#     return result


# мы можем использовать методы как обычные функции. Для этого нужно указать название типа, затем точку и название метода: type.method
# text = 'hello'
# numbers = [1, 2, 3]
#
# text_upper = str.upper(text)
# list.append(numbers, 4)
#
# print(text_upper)
# print(numbers)


# последовательность Фибоначчи при помощи обычной функции
# def fib(n):
#     if n < 3:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# последовательность Фибоначчи при помощи анонимной функции
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
