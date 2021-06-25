fp = "/Users/ricky/Documents/personal_projects/ud/colt_steele/python_bootcamp/story.txt"

def copy(old, new):
    with open(old) as f:
        txt = f.read()
    with open(new, "w") as g:
        g.write(txt)
    # return g

# N.B. it is not necessary to return anything from this function

# the_story = copy(fp, "/Users/ricky/Documents/personal_projects/ud/colt_steele/python_bootcamp/story_copy.txt")

# print(the_story)


def copy_and_reverse(old, new):
    with open(old) as f:
        txt = f.read()
        txt = txt[::-1]
    with open(new, "w") as g:
        g.write(txt)

copy_and_reverse(fp, "/Users/ricky/Documents/personal_projects/ud/colt_steele/python_bootcamp/story_reversed.txt")

def statistics(txt):
    res = {}
    g = open(txt)
    glist = g.readlines()
    g.close()
    wc = 0
    cc = 0
    for i in glist:
        wc += i.count(" ") + 1
        cc += len(i)
    res['lines'] = len(glist)
    res['words'] = wc
    res['characters'] = cc
    return res
    # with open(txt) as f:
    #     txt = f.read()
    
    # return len(txt)
    # return txt.count("\n") +1

# Colt's solution - WAY better:
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

print(statistics(fp))    

'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(src, old, new):
    with open(src) as f:
        txt = f.read()
        txt = txt.replace(old, new)
    with open(src, "w") as g:
        g.write(txt)

find_and_replace(fp, "Alice", "Colt")

