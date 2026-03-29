student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# We can get min and max value using built-in function
# print(max(student_scores))
# print(min(student_scores))
# But i wanna find using loops

min_value = student_scores[0]
max_value = student_scores[0]

for score in student_scores:
    if score > max_value:
        max_value = score
    if score < min_value:
        min_value = score
print(min_value)
print(max_value)