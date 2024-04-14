student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for x in student_scores:
  if student_scores[x] > 90:
    student_scores[x] = "Outstanding"
  elif student_scores[x] > 80 and student_scores[x] < 91:
    student_scores[x] = "Exceeds Expectations"
  elif student_scores[x] > 71 and student_scores[x] < 81:
    student_scores[x] = "Acceptable"
  else:
    student_scores[x] = "Fail"
  student_grades[x] = student_scores[x]

print(student_grades)