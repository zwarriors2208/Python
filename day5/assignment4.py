ip = [int(x) for x in input("Enter the list of numbers separated by space:").split()]
x = map((lambda x : 'positive' if x > 0 else 'negative' if x < 0 else 'zero'), ip)
print(list(x))