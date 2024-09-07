ip1=input("Enter the values of the 1st tuple separated by comma : ")
ip2=input("Enter the values of the 2nd tuple separated by comma : ")
# make tuple of input1
t1=tuple(x for x in ip1.split(","))
# make tuple of input2
t2=tuple(x for x in ip2.split(","))
# selecting common elements frm tuple 1 and tuple2
t3=tuple(set(t1).intersection(set(t2)))a
print(t3)
