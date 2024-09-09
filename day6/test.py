import re
f1=open('start.txt','r')
s1=f1.readlines()
# print(s1)
for i in range(0,len(s1)):
    s=re.findall(r'^Start',s1[i])
    e=re.findall(r'end.$',s1[i])
    if s== ["Start"] and e== ["end."]:
        print(s1[i])
