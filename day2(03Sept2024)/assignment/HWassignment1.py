n = int(input("Enter the number of rows: "))

for i in range(1, n +1):
    # loop to print blank spaces
    for j in range(0, n - i):
        print(" ", end = "")
    # loop to print one half of pyramid
    for j in range(0, i + (i - 1)):
        print("*", end="")
    print()
