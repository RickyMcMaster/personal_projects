def reverse_string(str):
    # l =
    # for r in reversed(l):
    #     print(r)
    return ''.join(list(str)[::-1])
    pass

print(reverse_string('sausages'))





def list_check(list_):
    res = True
    for l in list_:
        if type(l) != list:
            res = False
            break
    # print(res)
    return res


list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True