# Error test
def add(a, b):
    return a+b


# add(1)

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Please do not divide by zero"
    except TypeError:
        return "Please provide two integers or floats"


print(divide(4, 2))
print(divide([], "1"))
print(divide(1, 0))
print()