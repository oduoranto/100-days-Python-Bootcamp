studentScore = input().split()

for n in range(0, len(studentScore)):
    studentScore[n] = int (studentScore[n])

highestScore = 0
for score in studentScore:
    if(score > highestScore):
        highestScore = score

print(f"The highest score = {highestScore}")          