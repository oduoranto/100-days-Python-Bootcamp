print("Welcome  to the dictionary")
student_score = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

for key in student_score:
    if student_score[key] >=91 :
        student_score[key] = "outstanding"
    elif  student_score[key] >= 81 :
        student_score[key] = "Exceeds Expectations"
    elif student_score[key] >= 71:
        student_score[key] = "Acceptable"
    else :
        student_score[key] = "Fail"


print(student_score)        