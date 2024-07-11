def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
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