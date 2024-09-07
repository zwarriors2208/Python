def prime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
        else:
            continue
    return True


l = [x for x in range(2, 51) if prime(x)]

print(l)