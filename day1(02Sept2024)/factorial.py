def factorial(i):
    c = 1
    r = 1
    while (c <= i):
        r = r*c
        c += 1

    return r


i = int(input("Number: "))
print(factorial(i))

# def fact(i):
#     if(i == 0):
#         return 1
#     return i * fact(i-1)
#
# print(fact(i))