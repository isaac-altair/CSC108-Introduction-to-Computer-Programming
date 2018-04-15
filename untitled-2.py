b = 1
def change():
    return 1+b

a = 1
def new_change():
    global a
    a += 1

def mod_list(lst):
    lst[0] = lst[0] * 2
    return lst
