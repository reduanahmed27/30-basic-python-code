"""Write a program that takes the integer number of a student and finds out 
the grade using a switch case statement following the grading system.
A = 90-100
B+ = 87-89
B = 84-86
B- = 80-83
C+ = 77-79
C = 74-76
C- = 70-73
D+ = 65-69
D = 60-64
F = Below 60"""

def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 87 <= score < 89:
        return "B+"
    elif 84 <= score < 86:
        return "B"
    elif 80 <= score < 83:
        return "B-"
    elif 77 <= score < 79:
        return "C+"
    elif 74 <= score < 76:
        return "C"
    elif 70 <= score < 73:
        return "C-"
    elif 65 <= score < 69:
        return "D+"
    elif 60 <= score < 64:
        return "D"
    elif score < 60:
        return "F"
    else:
        return "Invalid score"
try:
    student_score = int(input("Enter the student's score: "))
    grade = get_grade(student_score)
    print(f"The student's grade is: {grade}")
except ValueError:
    print("Invalid input. Please enter a valid integer score.")