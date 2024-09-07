ip = input("Enter a palindrome: ").split()
s = "".join(ip)
s1 = s[-1::-1]
if s.lower() == s1.lower():
    print('yes')
else:
    print('no')
