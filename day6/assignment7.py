import re
file  = open("start.txt", 'r')
f = file.readlines()
for i in range(0,len(f)):
    s = re.match(r'^Start', f[i])
    e = re.findall(r'end.$', f[i])
    if s and e == ["end."]:
        print(f[i])
    # try:
    #     if s[0] == "start" and e[0] == "end":
    #         print(f[i])
    # except Exception as e:
    #     None


file.close()