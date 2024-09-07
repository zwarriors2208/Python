#i = int(input("Enter a number:"))
# while(i<0):
    # i = int(input("Please enter a positive number: "))
# sum = 0
# for j in str(i):
#     sum += int(j)
# print('Sum of digits of given no. is : {}'.format(sum))

i=int(input("Enter a positive number: "))
while(i < 0):
    i = int(input("Please enter a positive number: "))
temp=i
s=0
while temp>0:
    d=temp%10
    s=s+d
    temp=temp//10
print('Sum of digits of given no. is : {}'.format(s))