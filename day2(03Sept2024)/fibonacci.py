
num1=1
num2=2
next_num=num2



while next_num<100:
    print(next_num)
    next_num=num1+num2
    num1,num2=num2,next_num
