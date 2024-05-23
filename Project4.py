import random

print("Welcome to Rock, Paper, Scissors game")

rock = '''                                             
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a'''

scissors = '''
           ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.'''

paper = ''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| '''

ans = [rock, paper, scissors]
choice = int(input("What do you choose: Type 0 for rock, 1 for paper and 2 for scissors: "))
randomNumber = random.randint(0,2)

if (choice ==0) and (randomNumber == 0):
    print("You chose"+ ans[0])
    print("The computer choose " + ans[0])
    print("Its a draw")
elif (choice == 1 ) and (randomNumber == 1):
    print("You chose "+ ans[1])
    print("The computer choose " + ans[1])
    print("Its a draw")
elif (choice == 2) and (randomNumber == 2):
    print("You chose"+ ans[2])
    print("The computer choose " + ans[2])
    print("Its a draw")
elif (choice == 0) and (randomNumber == 1):
    print("You chose"+ ans[0])
    print("The computer choose " + ans[1])
    print("You lose")
elif (choice == 0 ) and (randomNumber == 2):
    print("You chose"+ ans[0])
    print("The computer choose " + ans[2])
    print ("You win")  

elif (choice == 1) and (randomNumber == 0):
    print("You chose"+ ans[1])
    print("The computer choose " + ans[0])
    print("You win ")    
elif (choice == 1) and (randomNumber == 2):
    print("You chose"+ ans[1])
    print("The computer choose " + ans[2])
    print ("You lose")
elif (choice == 2) and (randomNumber  == 0):
    print("You chose"+ ans[2])
    print("The computer choose " + ans[0])
    print ("you losee")
elif (choice == 2) and (randomNumber == 1):
    print("You chose"+ ans[2])
    print("The computer choose " + ans[1])
    print("You win")
else:
    print("Incorrect input. Try again")                            