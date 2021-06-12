from keyword import iskeyword


def contains_keyword(*args):
    for a in args:
        if iskeyword(a):
            return True
    return False


print(contains_keyword("cra", "yarr", "def"))
