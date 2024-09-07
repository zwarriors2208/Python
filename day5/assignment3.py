sm=0
def s_m(*args):
    global sm
    sm = sum(args)
def re_set():
    global sm
    sm = 0

print(sm)
s_m(1,2,3,4,5)
print(sm)
re_set()
print(sm)
