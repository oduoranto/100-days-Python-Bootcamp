print ("Welcome! Thank you for choosing Anto's Pizza Deliveries ")

size = input("Choose your pizza size: S, M ,L: ")
add_pepperoni = input("Would you like pepperoni; Y or N: ")
extra_cheese = input ('Would you like extra cheese; Y or N: ')
bill= 0

if size.lower() == "s": 

  bill += 15

elif size.lower() == "m":
   
   bill += 20


else :
    bill += 25

if (add_pepperoni.lower() == "y"):
   if size == 's':
      bill += 2

   else :
      bill += 3

if extra_cheese == "y":
   bill += 1   

print(f">>Total bill = $ {bill}")   

