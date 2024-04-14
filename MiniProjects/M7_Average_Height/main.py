student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

heights_combined = 0
amount_of_students = 0
for student in student_heights:
  heights_combined += student
  amount_of_students+=1
average_height = round(heights_combined / amount_of_students)
print(f"total height = {heights_combined}\nnumber of students = {amount_of_students}\naverage height = {average_height}")