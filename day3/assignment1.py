l = []
while(True):
    ip1 = [input("Enter name of student: ")]
    ip2 = input("Enter age and score of three subjects separated by comma: ")
    t = tuple(ip1)
    t = t + tuple(int(x) for x in ip2.split(","))
    l.append(t)
    ip3 = input("Do you want to enter the data of another student (y/yes): ")
    if ip3.lower() == "yes" or ip3.lower() == "y":
        continue
    else:
        break

print(l[0])
len_th = len(l)
temp = 0
temp_index = None
for i in range(len_th):
    s_m = 0
    for j in range(2,5):
        s_m += l[i][j]
    s_m = s_m/3
    if(temp < s_m):
        temp = s_m
        temp_index = i
    a,b,c,d,e = l[i]
    l[i] =(a,b,c,d,e,s_m)
print(l)
print(f"the highest score is ---> {temp} scored by {l[temp_index][0]}")

ip4 = float(input("Enter the minimum average score: "))
for i in range(len_th):
    if l[i][5] >= ip4 :
        print(f"Name of student: {l[i][0]}\nAverage score of {l[i][0]} : {l[i][5]}")
