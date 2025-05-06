subjects = 0
grades = 0

for _ in range(20):
    subject, grade, score = input().split()
    grade = float(grade)
    if score == 'A+':
        subjects += 4.5 * grade
    elif score == 'A0':
        subjects += 4 * grade
    elif score == 'B+':
        subjects += 3.5 * grade
    elif score == 'B0':
        subjects += 3 * grade
    elif score == 'C+':
        subjects += 2.5 * grade
    elif score == 'C0':
        subjects += 2 * grade
    elif score == 'D+':
        subjects += 1.5 * grade
    elif score == 'D0':
        subjects += 1 * grade
    elif score == 'F':
        subjects += 0 * grade

    if not score == 'P':
        grades += grade

print(f"{subjects/grades:.6f}")
