import art

print(art.logo)

def find_higher_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
data = {}

continue_bidding = True
while continue_bidding:
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? $"))
    data[user_name] = user_bid
    should_continue = input("Are there any other bidder? Type 'yes' or 'no' \n").lower()
    if should_continue == "no":
       continue_bidding = False
       find_higher_bidder(data)
    elif should_continue == "yes":
        print("\n" * 20)
        continue_bidding = True





