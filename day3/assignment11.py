s="Quick brown fox jumps the lazy dog Quick brown fox jumps the lazy dog"
s = s.lower()
l=[x for x in s if x in 'aeiou']
# l=[x for x in s if x=='a' or x=='e' or x=='i' or x=='o' or x=='u']
print((set(l)))