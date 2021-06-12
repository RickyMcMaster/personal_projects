from datetime import date


def week():
    weekDays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")
    # count = 0
    # while count < 7:
    #     yield weekDays[count]
    #     count += 1
    # Colt's solution - better:
    for d in weekDays:
        yield d


days = week()

# print(next(week()))
# print(next(week()))
print(next(days))
print(next(days))
print(next(days))


# def yes_or_no():
#     yn = ("yes", "no")
#     while True:
#         for x in yn:
#             yield x

def yes_or_no():
    while True:
        yield "yes"
        yield "no"


gen = yes_or_no()
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
print(next(gen))  # 'yes'
print(next(gen))  # 'no'

'''

next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(count=99, bev="soda"):
    while count > 1:
        yield "{} bottles of {} on the wall.".format(count, bev)
        count -= 1
    yield "Only 1 bottle of {} left!".format(bev)
    yield "No more {}!".format(bev)


kombucha_song = make_song(5, "kombucha")
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '4 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '3 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
# print(next(kombucha_song)) # 'No more kombucha!'
# print(next(kombucha_song)) # StopIteration

'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration


'''

def get_multiples(num=1, count=10):
    ctr = 1
    for x in range(ctr, count+1):
        yield num * ctr
        ctr += 1

default_multiples = get_multiples(2, 3)
print(list(default_multiples)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_unlimited_multiples(num=1):
    ctr = 1
    while True:
        yield num * ctr
        ctr += 1

sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
print([next(ones) for i in range(20)])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
