#Password generator
import random

letters = ['a','b', 'c', 'd','e', 'f', 'g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O','P','Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers =['0', '1', '2', '3', '4', '5', '6', '7','8','9']

symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']

print("Welcome to Password Generator")
#length =int(input("How long do you want your password: "))
numLetters = int(input("How many letters would you  like: "))
numNumbers =int(input("How many numbers would you like: "))
numSymbols = int(input("How many symbols would you like: "))


passwordList =[]
for char in range(1, numLetters +1):
   passwordList  +=  random.choice(letters)



for char in range(1,numNumbers+1):
  passwordList += random.choice(numbers)
   

for char  in range(1, numSymbols+1 ):
     passwordList += random.choice(symbols)

print(passwordList)   

random.shuffle(passwordList)
print(passwordList)

password = ""

for char in passwordList:
   password += char
   
print(f"Your password is : {password}")