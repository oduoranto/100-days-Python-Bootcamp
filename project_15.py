print('Holla! Welcome to coffee machine!')

menu = {
    'espresso':{
        'ingredients': {
            'water':50,
            'coffee':18
        },
        'cost' : 1.5
    },
    'latte':{
        'ingredients':{
            'water': 200,
            'coffee': 24,
            'milk' : 150
        },
        'cost': 2.5
    },
    'cappuccino':{
        'ingredients' : {
            'water': 250,
            'coffee': 24,
            'milk': 100
        },
        'cost' : 3.0
    }
}
  

    
profit = 0
resources = {
    'water': 300,
    'milk' : 200,
    'coffee': 100,
    }


def is_resources_sufficient(ingredients):
  """returns True when order can be made and False when order cannot be made"""
  for item in ingredients:
    if ingredients[item] >=  resources[item]:
      print(f'Sorry there is no enough {item}')
      return False
  return True  
  
def process_coins():
  """Returns the total calculated of the coins inserted"""
  print('Please insert coins')
  try:
    total = int(input('How many quaterz? ')) * 0.25  
    total += int(input('How many dimes? ')) * 0.10 
    total += int(input('How many nickels? ')) * 0.05
    total += int(input('How many pennies? ')) * 0.01  
    return total
  except(ValueError):
    print('Numbers only!')
    

def is_transaction_successful(payment, drink_cost):
  """Returns True if payment is accepted and False when money is insufficient"""
  if payment >=  drink_cost:
    change = round(payment - drink_cost,2)
    print(f'Here is $ {change} in change')
    global profit
    profit += drink_cost
    return True 
  else:
    print('Sorry that is not enough money. Money refunded.')
    return False
  

def make_coffee(drink_name, order_ingredients):  
  """Deduct the ingredients used from the resources"""
  for items in order_ingredients:
    resources[items] -= order_ingredients[items]
  print('here is your {drink_name} ☕ enjoy!') 
is_on = True
while is_on:
 info = input('What would you like? (espresso / latte / cappucciono): ')
    
 #secret code to turn off the coffee machine
 if info == 'off':
   is_on = False

 elif info == 'report':
    print(f'water: {resources["water"]}ml')
    print (f'milk : {resources["milk"]}ml')
    print(f'coffee : {resources["coffee"]}g')
    print(f'money : ${profit}')


 else:
   drinks = menu[info] 
   try: 
    if is_resources_sufficient(drinks['ingredients']):
      payment = process_coins()
      if is_transaction_successful(payment, drinks['cost']):
       make_coffee(info,drinks['ingredients'])
   except TypeError:
     print('Invalid input')
