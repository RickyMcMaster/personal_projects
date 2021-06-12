import math


def decrement_list(alist):
    return list(map(lambda x: x - 1, alist))


print(decrement_list([1, 2, 3]))


def remove_negatives(alist):
    return list(filter(lambda x: x >= 0, alist))

# print(remove_negatives([-2,-5,5,7,-8,-3]))

# print(all(type(x) == str for x in blah))


def extremes(iter):
    return (min(iter), max(iter))

# print(extremes("alcatrax"))


def max_magnitude(alist):
    return max(abs(l) for l in alist)

# print(max_magnitude([2, 89, -700]))


def sum_even_values(*args):
    return sum(l for l in args if l % 2 == 0)


# print(sum_even_values(1, 2, 3, 4, 5, 6))
# print(sum_even_values(4, 2, 1, 10))
# print(sum_even_values(1))


def sum_floats(*args):
    res = sum(a for a in args if type(a) == float)
    # if res:
    return res
    # return 0


print(sum_floats(1.5, 2.4, 'awesome', [], 1))
print(sum_floats(1, 2, 3, 4, 5))


def interleave(a, b):
    x = [''.join(u) for u in zip(a, b)]
    return ''.join(x)


# print(interleave("hi", "ha"))
# print(interleave("super", "cali"))


def triple_and_filter(args):
    return list(map(lambda x: x * 3, filter(lambda x: x % 4 == 0, args)))


print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))


def extract_full_name(xl):
    # print(list(zip(xl)))
    return ["{} {}".format(x["first"],x["last"]) for x in xl]
    # pass


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']