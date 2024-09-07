def convert(a,u,c):
    #a is the magnitude of current value
    # u is the current unit of value
    # c is the unit in which we want out initial value to convert
    match u.lower():
        # conversion from inch to other unit
        case "inches":
            match c.lower():
                case "meters":
                    a /= 39.37
                case "feet":
                    a /= 12
                case "centimeters":
                    a *= 2.54
        # conversion from meter to another unit
        case "meters":
            match c.lower():
                case "inches":
                    a *= 39.37
                case "feet":
                    a *= 3.281
                case "centimeters":
                    a *= 100

        # conversion from centimeter to another unit
        case "centimeters":
            match c.lower():
                case "inches":
                    a /= 2.54
                case "feet":
                    a /= 30.48
                case "meters":
                    a /= 100
        # conversion from centimeter to another unit
        case "feet":
            match c.lower():
                case "inches":
                    a *= 12
                case "meters":
                    a /= 3.281
                case "centimeters":
                    a *= 30.48
    return a

n=float(input("Enter the value:"))
u=input("Enter the unit:")
c=input("Enter the unit in which to convert:")
while True:
    new_val = convert(n,u,c)
    print(f"The converted value of {n} {u} =", new_val, c)
    ip = input("Do you want to continue calculation:")
    if ip.lower() == "no":
        break
    else:
        u = c
        n = new_val
        c = input("Enter the unit in which to convert:")
