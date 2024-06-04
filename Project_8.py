alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', 't','u','v','w', 'x', 'y', 'z',
            'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', 't','u','v','w', 'x', 'y', 'z']


def caeser(choice_1, text, shift):
   word = ""
   if(choice_1 == "decode"):
    
      shift *= -1

 
   for char in text:
    if char in alphabet :
      position = alphabet.index(char)
      new_position = position + shift
      word += alphabet[new_position]


    else:
      word += char  
    
   print(f"The {choice_1}d text is {word}")  


cont = False
while  not cont:
  choice_1 = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
  text = input("Type your text here:\n")
  shift = int(input("Type the shift number:\n")) 

  shift = shift % 26
  caeser(choice_1,text,shift)
  choice =input("Do you want to conitinue type 'yes' to conituie and 'no' to  exit: ").lower()
  if choice ==  "no":
    break
  elif choice != "yes":
    while choice != "yes":
      print("Incorrect input")
      choice =input("Do you want to conitinue type 'yes' to conituie and 'no' to  exit: ").lower()
      if (choice == "no"):
        break


   

