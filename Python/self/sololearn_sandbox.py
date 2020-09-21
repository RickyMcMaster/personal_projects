def func(x):
    res = 0
    for i in range(x):
        # print(i)
        res += i
    return res


# print('Now result')
# print(func(4))

#
# # Uncaught Exceptions
# try:
#    print(1)
#    print(10 / 0)
# except ZeroDivisionError:
#    print(unknown_var)
# finally:
#    print("This is executed last")


# num = input(":")
# if float(num) < 0:
#     print('Neg')
#     raise ValueError("Negative!")


# Assertions
# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)


def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


# print(apply_twice(add_five, 10))


def factorial(x):
    if x == 1:
        print(x)
        return 1
    else:
        print(x)
        return x * factorial(x - 1)


print(factorial(5))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))
print()


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(4))

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print('Union:')
print(first | second)
print('Intersection:')
print(first & second)
print('Difference:')
print(first - second)
print('Difference:')
print(second - first)
print('Symmetric difference:')
print(first ^ second)

print('Functional Programming Test')
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

print('Powers')


def power(x, y):
    if y == 0:
        print('y = {}'.format(y))
        return 1
    else:
        print('y = {}'.format(y))
        res = x * power(x, y - 1)
        print('res = {}'.format(res))
        return res


print(power(2, 3))

a = (lambda x: x * (x + 1))(6)

print(a)


class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color


fido = Dog("Fido", "brown")
print(fido.name)
print(fido.legs)
print(Dog.legs)
