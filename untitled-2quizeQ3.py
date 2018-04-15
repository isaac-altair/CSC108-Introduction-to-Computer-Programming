def rem_odd(lst):
    idx = 0
    while idx < len(lst):
        if len(lst[idx]) % 2 == 1:
            lst.pop(idx)
        idx = idx + 1