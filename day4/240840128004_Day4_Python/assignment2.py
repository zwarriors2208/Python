#assignment 2
# filtering and modifying dictionaries

d = {'Alice': 85, 'Bob': 92,'Charlie': 78, 'David': 65}

d1 = {keys : (values + 5)  for keys, values in d.items() if (values > 80) }

print(d1)