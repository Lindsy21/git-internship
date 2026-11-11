
# Student Grade Calculator

student_name = input("Enter student name: ")

math_score = float(input("Enter Mathematics score: "))
english_score = float(input("Enter English score: "))
computer_score = float(input("Enter Computer Science score: "))

average = (math_score + english_score + computer_score) / 3

print("\n--- STUDENT REPORT ---")
print("Student:", student_name)
print("Average:", round(average, 2))

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
