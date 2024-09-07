p = input("password: ")
c = 0
if (len(p) >= 8):
    c += 1
b = True
c1= 0
for i in p:
    if i.islower():
        c1 += 1
        break
for i in p:
    if i.isupper():
        c1 += 1
        break
if(c1 == 2):
    c += 1
for i in p:
    if i.isnumeric():
        c += 1
        break
for i in p:
    if not(i.isalnum()):
        c+=1



if(c == 1):
    print("Weak password")
elif(c>=1 and c<4):
    print("Moderate password")
elif(c==4):
    print("strong password")
else:
    print("invalid password")
# --------------------------------------
# p = input("password: "))
# c = 0
# if (len(p) >= 8):
#     c += 1
# b = True
# c1= 0
# if p.islower():
#     c1 += 1
#
# if p.isupper():
#     c1 += 1
#
# if(c1 == 2):
#     c += 1
#
# if p.isnumeric():
#     c += 1
# for i in p:
#     if not(i.isalnum()):
#         c+=1
#         break
#
# if(c == 1):
#     print("Weak password")
# elif(c>=1 and c<4):
#     print("Moderate password")
# elif(c==4):
#     print("strong password")
# else:
#     print("invalid password")
