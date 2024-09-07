ip = input("Enter numbers separated by space:")
t = tuple(int(x) for x in ip.split())
s = 0
for i in t:
    s += i
avg = s / len(t)

print(f"sum of all elements:{s}\naverage:{avg}\nmaximum value of tuple: {max(t)}\nminimum value of tuple: {min(t)}\nNumber of elements in tuple: {len(t)}")