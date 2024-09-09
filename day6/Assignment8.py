import re
file=open('start.txt','r')
# f=file.read().split()
# print(f)
#
# for i in f:
#     s = re.match(r'^[aeiou].*[qwrtypsdfghjklmnbvczx]$', i)
#     if s:
#         print(i)
#
f = file.read()
s = re.findall(r'\b[aeiouAEIOU]\w*[qwrtypsdfghjklmnbvczx]\b', f)

# print (s)
y = []

s1 = re.findall(r'[0-9]+[a-zA-Z]', f)
# s1 = re.findall(r'[0-9]+([a-z]|[A-Z]', f)
# s1 = re.findall(r'[0-9]+[^\d,a]', f)

print(s1)
file.close()
file=open('start.txt','r')
l3 = file.readlines()
for i in range(len(l3)):
    s9 = re.match(r'^Note.*[!]$', l3[i])
    if s9:
        print(l3[i])
