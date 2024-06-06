print(''' _____________________
|  _________________  |
| | Calculator   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')
print("Welcome to the calculator app")

def additional_calculation(results):
     another_number = float(input("Enter another number: "))  
     print("+\n-\n/\n*\n")
     operation = input("Pick an operation: ")  
     calculator(results,another_number,operation)


def calculator(first_number, second_number, operation):
    results = 0.0

    if (operation == "+"):
        results =first_number + second_number
    elif operation == "-":
        results = first_number - second_number
    elif operation == "*":
         results = first_number * second_number
    else: 
        results = first_number/second_number   

    choice = input(f"Type 'y' to continue calculating with {results} or 'n' to start new calculation: ")
    if (choice == 'n'):
       print(f"{first_number} {operation} {second_number} = {results}")    

    else :
        return additional_calculation(results)
    
first_number= float(input("What is your first number: "))
print("+\n-\n/\n*\n")
operation = input("Pick an operation: ")
second_number =float(input("What is your next number: "))
calculator(first_number, second_number,operation)