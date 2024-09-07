# assignment 1
# Develop a python program extract all unique words, and print them in alphabetical order
s = input("Enter a paragraph containing multiple lines of dataset: ").lower().split()
l = len(s)
for i in range(l):
    for j in s[i]:
        if not(j.isidentifier()):
          s[i] = s[i].replace(j,"")
        else:
            continue
s1 = sorted(set(s))

print(s1)
