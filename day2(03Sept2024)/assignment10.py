i = input("Enter a number to be add in list separated by space: ")
l=[]
s,e=0,0
c = 0
while(e <= len(i)):
    for j in range(e + 1, len(i)):
        if c + 1 == len(i):
            l.append(i[e + 2 :] )
            e = c
        if i[j] == " " or j == len(i):
            s, e = e, j
            l.append(i[s : e])
            break
        else:
            c = j

print(l)



# ip = input("Enter a number to be add in list separated by space: ").split()
# p = int(input("rotation by:"))
# l = len(ip)
#
# c = ip.copy()
#
# for i in range(l):
#     c[i] = ip[(i + (p % l)) % l]
#
# print(c, ip, sep = "\n")










