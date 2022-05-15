from replit import clear
from art import logo
print(logo)

bids = {}
finsh_bidd = False

def find_highest_bidd(bidd_recods):
  highest_bidder_amount =  0
  winner = " "
  for bidder in bidd_recods:
    bidder_amount = bidd_recods[bidder]
    if bidder_amount > highest_bidder_amount:
      highest_bidder_amount = bidder_amount
      winner = bidder
  print(f"The winner is {winner} and the highest bid is {highest_bidder_amount}")

while not finsh_bidd:
  name = input("Enter your name: ")
  price =int(input("Enter your bid price: $"))
  bids[name]=price
  should_continue = input("There are other user who want to bid ? type 'Yes' or 'No'")
  if should_continue == 'no':
    finsh_bidd = True 
    find_highest_bidd(bids)
  elif should_continue == 'yes'  :
    clear()















  

