n=input("Enter name: ")
a=int(input("Enter age: "))
t1 = tuple(x for x in input('Enter city and country separated by coma: ').split(','))
t = (n, a, t1)
print( 'packed tuple: ' , t)

x, y, z = t
z1, z2 = z
print('unpacked tuple: ')
print(f"name : {x}, age : {y}, city : {z1}, country : {z2}")
