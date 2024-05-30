import random

print("Hello  world")

def generate_random():
    return random_number

random_number = random.randint(1,100)
random_number = generate_random()
print(f"The random number is {random_number} ")    


def generate_random1():

    return random.randint(1,100)

random_number1 = generate_random1()
print(f"The  random number is {random_number1}")

def add_number(a, b):
    return a + b

sum = add_number(12, 90)
print(f"The sum = {sum}")


def calculate_area(length, width):
    return length * width

length = int(input("Enter the length: "))
width = int(input("Enter  your width: "))
area = calculate_area(length, width)
print(f"The area = {area}")

fruits = ["Banana", "Oranges", "Apples", "Grapes"]

for fruit in fruits:
    print(fruit) 



for index, fruit in enumerate(fruits):
    print(f"The index {index} : is {fruit}")    


messages = "Hello World"

for char in  messages:
    print(char)


for n in range(1,19):
    print(n)
