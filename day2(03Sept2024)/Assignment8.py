# n=int(input("Write a positive number"))
# while(n<0):
#     n=int(input("Please write a positive number"))
# l=[]
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         l.append(i)
#
# print(l)



n=int(input("Write a positive number"))
while(n<0):
    n=int(input("Please write a positive number"))
l=[]

for i in range(2,n+1):
    b = False
    for j in range(2,i):
        if i % j == 0:
            b = True
            break
    if not b:
        l.append(i)

print(l)
