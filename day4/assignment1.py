l=[]
while True:
    i1 = tuple(x for x in input("Enter two elements for tuple separated by comma: ").split(','))
    l.append(i1)
    ip = input("Do you want to enter more tuple in list: ")
    if ip.lower() == "yes" or ip.lower() == "y":
        continue
    else:
        break

# D={}
# D={D[l[x][0]]:l[x][1] for x in range(len(l))}
# print(D)

d = {i[0]: i[1] for i in l}
print(d)


# d = {}
#
# for i in l:
#     d[i[0]] = i[1]
#
# print(d)


# D={}
# for i in range(len(l)):
#     D[l[i][0]]= l[i][1]
# print(D)
