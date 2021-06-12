# 110

def remove_every_other(alist):
    return alist[0::2]


print(remove_every_other([1, 2, 3, 4, 5]))  # [1,3,5]
print(remove_every_other([5, 1, 2, 4, 1]))  # [5,2,1]
print(remove_every_other([1]))  # [1]


def sum_pairs(alist, target):
    x = 0
    y = 1
    while x < len(alist):
        for r in range(y, len(alist)):
            if alist[x] + alist[y] == target:
                return [alist[x], alist[y]]
        x += 1
        y += 1
    return []


print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))

def vowel_count(word):
    return {w:word.lower().count(w) for w in "aeiou" if w in word}

# print("sequoia")

# for w in "aeiou":
#     print("awesome".count(w))
#     {w:}s

print(vowel_count("Elie"))
