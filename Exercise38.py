print("Welcome to love calulator")

name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

combineNames = name1 + name2
lowerCase = combineNames.lower()
t = lowerCase.count("t")
r = lowerCase.count("r")
u = lowerCase.count("u")
e = lowerCase.count("e")
firstDigit = t + r + u + e

l = lowerCase.count("l")
o = lowerCase.count("o")
v = lowerCase.count("v")
e = lowerCase.count("e")
secondDigit = l + o + v + e

score = int(str(firstDigit ) + str(secondDigit))

if ( score < 10 ) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif (score >= 40) and (score <= 60):
    print ("Your score is {score}, you are alright togther")    
else:
    print(f"Your score is {score}")    