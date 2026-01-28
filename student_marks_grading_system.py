name = input("Enter student name: ")
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]

total = sum(marks)
percentage = total / 3

if percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'E'

print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")