def dynam_sum(*args):
    sm = 0
    for i in args:
        if i > 0:
            sm += i

    return sm

print(dynam_sum(1,2,3,4,5,-5,-6,-3))