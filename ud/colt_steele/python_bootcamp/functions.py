# define product below:
from typing import Counter


def product(a, b):
    return a * b


def return_day(num):
    daydict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",

    }
    return daydict.get(num, None)


print(return_day(41))


def last_element(alist):
    try:
        return alist[-1]
    except IndexError:
        return None


print(last_element([1, 2, 3]))
print(last_element([]))


def single_letter_count(words, letter):
    return list(words.lower()).count(letter.lower())


print(single_letter_count("Hello", "h"))  # 1
print(single_letter_count("Hello", "z"))  # 0
print(single_letter_count("HelLo", "l"))  # 3

'''

'''

# flesh out multiple_letter count:


def multiple_letter_count(word):
    return {k: word.count(k) for k in word}


# {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
print(multiple_letter_count("helloooo"))


def list_manipulation(lis, com, loc, val=None):
    if com == "remove":
        if loc == "end":
            return lis.pop()
        else:
            return lis.pop(0)
    elif com == "add":
        if loc == "end":
            lis.append(val)
            return lis
        else:
            lis.insert(0, val)
            return lis


print(list_manipulation([1, 2, 3], "remove", "end"))  # 3
print(list_manipulation([1, 2, 3], "remove", "beginning"))  # 1
print(list_manipulation([1, 2, 3], "add", "beginning", 20))  # [20,1,2,3]
print(list_manipulation([1, 2, 3], "add", "end", 30))  # [1,2,3,30]``


def is_palindrome(input):
    input = str(input).lower().replace(" ", "")
    return input[::-1] == input


print(is_palindrome('testing'))  # False
print(is_palindrome('tacocat'))  # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False
print(is_palindrome('amanaplanacanalpanama'))  # True
print(is_palindrome('A man a plan a canal Panama'))  # True


def frequency(lst, term):
    counter = 0
    for l in lst:
        if term == l:
            counter += 1
    return counter


print(frequency([1, 2, 3, 4, 4, 4], 4))
print(frequency([True, False, True, True], False))

# BETTER SOLUTION!!!!


def frequency(collection, searchTerm):
    return collection.count(searchTerm)


def multiply_even_numbers(lst):
    res = 1
    for l in lst:
        if l % 2 == 0:
            res *= l
    return res


print(multiply_even_numbers([2, 3, 4, 5, 6]))  # 48


def capitalize(word):
    res = word[0].upper() + word[1::]
    return res


capitalize("tim")  # "Tim"
capitalize("matt")  # "Matt"


def compact(alist):
    return [a for a in alist if a]


compact([0, 1, 2, "", [], False, {}, None, "All done"])  # [1,2, "All done"]


# flesh out intersection pleaseeeee
def intersection(alist, blist):
    return [a for a in alist if a in blist]


print(intersection([1, 2, 3], [3, 4, 5]))
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z']))

# BETTER SOLUTION!!!!


def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]


def isEven(num):
    return num % 2 == 0


def partition(ilist, afunc):
    alist = []
    blist = []
    reslist = []
    for i in ilist:
        if afunc(i):
            alist.append(i)
        else:
            blist.append(i)
    reslist.append(alist)
    reslist.append(blist)
    return reslist


print(partition([1, 2, 3, 4], isEven))  # [[2,4],[1,3]]

# BETTER VERSION!!!


def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

 # Define combine_words below:


def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]

    return word

# print(combine_words("work", preefix="er"))

# NO TOUCHING! =================================================================


def count_sevens(*args):
    return args.count(7)


nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 54, 34, 76, 8, 23, 34, 45, 56, 67, 78, 12, 23, 34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17,
        11, 7, 11, 8, 4, 6, 2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7, 7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1, 4, 7)

result2 = count_sevens(*nums)

print(result1, result2)


def calculate(make_float, operation, first, second, message=None):
    res = 0
    if make_float:
        res = float(res)
    if operation == "add":
        res = first + second
    elif operation == "subtract":
        res = first - second
    elif operation == "multiply":
        res = first * second
    elif operation == "divide":
        res = first / second
    if not message:
        return "The result is {}".format(res)
    else:
        return "{} {}".format(message, res)


calculate(make_float=False, operation='add', message='You just added',
          first=2, second=4)  # "You just added 6"
calculate(make_float=True, operation='divide',
          first=3.5, second=5)  # "The result is 0.7"

# Official solution:
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), int(operation_value))
    return final
