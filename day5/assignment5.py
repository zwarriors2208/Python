def fact(i):
    if i == 0:
        return 1
    else:
        return i * fact(i-1)

ip = int(input("Enter the number whose factorial you want to calculate:"))
print(fact(ip))

# def rec(n1):
#   if n1 == 0:
#     return 1
#     return n1* rec(n1-1)
#
#
# n=int(input("Enter a number: "))
# print(rec(n))
