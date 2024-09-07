
name = input("Enter your name: ")
home_work = float(input("Enter your homework score: "))
quizzes = float(input("Enter your quizzes score: "))
mid_term = float(input("Enter your mid term: "))
final_exam = float(input("Enter your final_exam score: "))

avg= 0.2*(home_work+ quizzes)+ 0.3*(mid_term+final_exam)

percentage= (avg*100)/100

print("Name of the student:", name, "\nFinal percentage:",percentage)

if percentage > 90:
    print("Grade A")
elif percentage > 80:
    print("Grade B")
elif percentage > 70:
    print("Grade C")
elif percentage > 60:
    print("Grade D")
else:
    print("Grade F")
