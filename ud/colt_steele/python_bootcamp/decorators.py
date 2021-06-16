from time import sleep
from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("This is from the wrapper:")
        print("Here are the args: {}".format(args))
        print("Here are the kwargs: {}".format(kwargs))
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass


do_nothing(1, 2, 3, a="hi", b="bye")


def double_return(fn):
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return wrapper


@double_return
def add(x, y):
    return x + y


print(add(1, 2))  # [3, 3]


@double_return
def greet(name):
    return "Hi, I'm " + name


print(greet("Colt"))  # ["Hi, I'm Colt", "Hi, I'm Colt"]


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args):
        if len(args) >= 3:
            return "Too many arguments!"
        return fn(*args)
    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


print(add_all())  # 0
print(add_all(1))  # 1
print(add_all(1, 2))  # 3
print(add_all(1, 2, 3))  # "Too many argument)s!"
print(add_all(1, 2, 3, 4, 5, 6))  # "Too many argument)s!"


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args):
        for item in args:
            if type(item) != int:
                return "Please only invoke with integers."
        return fn(*args)
    return wrapper

# Colt's solution


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args):
        if any([a for a in args if type(a) != int]):
            return "Please only invoke with integers."
        return fn(*args)
    return wrapper


@only_ints
def add(x, y):
    return x + y


print(add(1, 2))  # 3
print(add("1", "2"))  # "Please only invoke with integers."


def ensure_authorized(fn):
    def wrapper(*args, **kwargs):
        if kwargs.get('role') != 'admin':
            return "Unauthorized"
        return fn(*args, **kwargs)
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

# print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
# print(show_secrets(role="nobody")) # "Unauthorized"
# print(show_secrets(a="b")) # "Unauthorized"


def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper():
            print("Waiting {}s before running {}".format(val, fn.__name__))
            sleep(val)
            return fn()
        return wrapper
    return inner


@delay(3)
def say_hi():
    return "hi"


say_hi()