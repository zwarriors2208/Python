ip = input("enter the name of file:")
try:
    f1=open(ip,'r')
    s = f1.read()
    print(s)
    s = s.split()
    for i in range(0,len(s)):
        if "after" in s[i].lower():
            s[i] = 'before'
        f1.close()
        f1 = open(ip, 'w')
        f1.write(" ".join(s))
        f1.close()
except FileNotFoundError:
    print("File Not Found")
