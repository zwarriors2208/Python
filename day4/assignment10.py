s1 = input("Enter the first word:")
s2 = input("Enter the second word:")

if sorted(s1.lower().replace(" ","")) == sorted(s2.lower().strip().replace(" ","")):
    print(f'yes \'{s1}\' and \'{s2}\' are anagrams')
else:
    print(f'No \'{s1}\' and \'{s2}\' are not anagrams')