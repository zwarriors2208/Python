fn = input("first name: ")
ln = input("last name: ")
# .format method?
print(f'My first name is {fn} and my last name is {ln}')

print("My first name is {1} and my last name is {0}".format(fn, ln))