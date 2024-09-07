ip = input("enter paragraph: ")
l = [x.lower() for x in ip.split()]
# s1 is set of all words in paragraph
s1 = set(l)
# s is set of all letters in para
s=set()
for i in ip:
    s.add(i.lower())
s.remove(' ')
s, s1=sorted(s), sorted(s1)

print("Sorted unique word in para is:", s1, "\nsorted unique letters in para is:", s)