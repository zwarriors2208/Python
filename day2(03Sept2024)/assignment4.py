for n in range(1, 6):
    for i in range(0, 5):
                                            # print(i+1, 'X', n, '=', (i+1) * n, end=((5 - len(str((i+1) * n)))*" "))
        print(f"{i+1} X {n} = {(i+1) * n}  ", end=((5 - len(str((i+1) * n)))*" "))
    print("")


# n=1
# while n<=5:
#     print("\n Table of ",n,"\n")
#     i=1
#     while(i<=10)
#         print