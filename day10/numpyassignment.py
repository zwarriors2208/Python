import numpy as np

a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13,14,15]
d = [16,17,18,19,20]

a1 = np.array(a+b)
a2 = np.array(c+d)
print("Add:",  a1+a2)
print("Subtraction:",  a1-a2)
print("Exponential:",  a1**a2)
print("Multi:",  a1*a2)
