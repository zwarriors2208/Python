i = 76
for r in range(10):
    g = int(input("guess the secret number:"))
    if g == i:
        print("correct guess")
        break
    elif(r == 9):
        print("you have exhausted all the tries available")
    else:
        print("wrong try again")
