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
