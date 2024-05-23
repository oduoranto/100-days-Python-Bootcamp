students_Height = input().split()

for x in range(0, len(students_Height)):
 students_Height[x] = int(students_Height[x])

total = 0

for n in students_Height:
  total += n
print(f"Total height = {total}")  

numberOfStudent = 0
for student in students_Height:
  numberOfStudent += 1

print(f"The number of students = {numberOfStudent}")  

avarage = round(total/numberOfStudent)
print (f"The avarageee height = {avarage}")