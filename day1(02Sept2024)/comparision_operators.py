score = int(input("score"))

if (score > 95):
    print("grade is A++")
elif (score >= 90):
    print("grade is A++")
elif (score < 36):
    if (score > 30):
        print("grade is D")
    elif (score == 0):
        print("try next year")
    elif (score <= 30):
        print("grade is F")