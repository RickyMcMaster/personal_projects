from typing import List


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0, len(list1))}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {x[0]: x[1] for x in person}
answer = {k:v for k,v in person}
answer = dict(person)

answer = {}.fromkeys("aeiou", 0)
answer = {i:chr(i) for i in range(65,91)}

print(answer)

print(print.__doc__)