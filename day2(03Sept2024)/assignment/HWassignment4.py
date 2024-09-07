ip = input("Enter thr numbers separated by comma: ")
t1 = tuple(int(x) for x in ip.split(","))
v1 = int(input("enter the number which you want to repeat: "))
v2 = int(input("number of times you want to repeat it: "))
t2 = tuple([v1]) * v2

print(f"original tuple:- {t1} \n New tuple:- {t1 + t2}")a
