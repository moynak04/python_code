def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ₹{highest_bid}")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid amount: ₹"))

    bids[name] = price

    more_bidders = input("Are there more bidders? Type 'yes' or 'no': ").lower()

    if more_bidders == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 20)  # Clears screen (simple trick)