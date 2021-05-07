x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13, 8]

a = [14, 27, 1, 4, 2, 50, 3, 1]
b = [2, 4, -4, 3, 1, 1, 14, 27, 50]

def shift_sort(x, y):
    # return set(x) ^ set(y)
    return list(set(x).symmetric_difference(set(y)))[0]

print(shift_sort(a, b))