ip = input("enter the numbers seprated by comma")
t=tuple(int(x) for x in ip.split(","))
print(t[0],t[-1],t[1:-1], t[::2], t[::-1], sep="\n")

