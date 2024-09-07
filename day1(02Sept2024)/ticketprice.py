age = int(input('enter age: '))
if(age > 0):
    if (age < 5):
        print("Ticket is free")
    elif (age >= 5 and age <= 12):
        print("Ticket price is Rs.5")
    elif (age >= 13 and age <= 60):
        print("Ticket price is Rs. 10")
    else:
        print("Ticket price is Rs. 7")
else:
    print("Invalid age")