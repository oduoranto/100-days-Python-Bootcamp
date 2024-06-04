import random


print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

print("Welcome to the Hangman game")

stages = ['''
       ______
     |/      |
     |      (_)
     |       |
     |       
     |   
     |
    _|___
          ''','''
       ______
     |/      |
     |      (_)
     |      \|
     |       
     |  
     |
    _|___
          ''','''
       ______
     |/      |
     |      (_)
     |      \|/
     |       
     |    
     |
    _|___
          ''','''
       ______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
    _|___
          ''',
          '''
       ______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
          ''','''
       ______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
          ''']

word_list = ["wolf", "chicken","lion"]
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
print (display)

end_of_game = False
while not end_of_game:
   guess = input("Choose a letter: ").lower()
   

   for position in range(word_length):
      letter =  chosen_word[position]
     
      if letter == guess:
           display[position] = letter

   if guess not in chosen_word:
       
       print(f"your {guess}, is not i the chosen word.You lose a life")
       lives -= 1
       if(lives == 0):
           end_of_game = True
           print("you lose")
           
           
   
   print(display)   

   if "_" not in display:
       end_of_game = True
       print("you win") 
       
   print(stages[lives -1])