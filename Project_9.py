print("Welcome to the secret auction program")


bids =  {}
def checker(name, bid):
  bids[name] = bid
  highest_bid = 0
  winner_name = ""
  for n in bids:
    if (bids[n] > highest_bid):
      bid_amount = bids[n]
      highest_bid = bid_amount
      winner_name = n
  print(f"The winner is {winner_name} with a bid record of ${highest_bid}")    
      

      
is_true = False
while not  is_true:
  name = input("What is your name :")
  bid = float(input("What is your bid: $"))
  
  should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if(should_continue == "no"):

    checker(name, bid)
    is_true = True



