print ("Welcome to the tip calculator!!")

bill = float (input("What is the total bill: $"))
tip = int(input("How much tip would you like to give? 10,12 or 15: "))
split = int(input("How many people to split the bill? : "))
total = bill - tip
totaSplit = round(total/split,2)
print (f"Everyone will contribute: ${totaSplit}")