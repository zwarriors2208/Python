# l = [x**2 for x in range(1,11) if x%2 ==0 else x**3 for x in range(1,11)]

l = [x**2 if x%2 == 0 else x**3 for x in range(1,11)]
print(l)