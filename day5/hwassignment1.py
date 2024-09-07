def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

def celsius_to_kelvin(celsius):
    return celsius + 273.15


l = input("enter the temperature in unit separated by space:").split()
l1 = 0
if len(l) == 2:
    try:
        l1 = float(l[0])
        ut = l[1]
    except ValueError:
        print("Please enter a number(temprature):")

else:
    print("invalid input")
    raise ValueError




if ut.lower() == "celsius":
    i1 = input("enter the unit in which you want to convert:")
    if i1.lower() == 'fahrenheit':
        print(celsius_to_fahrenheit(l1), "fahrenheit" )
    elif i1.lower() == 'kelvin':
        print(celsius_to_kelvin(l1), "kelvin" )
    else:
        print("invalid input")

elif ut.lower() == "fahrenheit":
    print(fahrenheit_to_celsius(l1), "celsius")
else:
    print("invalid input")

