voters = {}
votees = {}
votes = {}

def add_votee():
    name = input("Enter the votee's name: ")
    symbol = input("Enter their symbol: ")
    
    if symbol not in votes:
        votes[symbol] = 0 
        votees[symbol] = name  
    else:
        print("Symbol already in use. Please choose a different symbol.")

def vote():
    voter_id = input("Enter the voter ID: ")
    
    if voter_id in voters:
        print("You have already voted.")
        return
    
    name = input("Enter your name: ")
    voters[voter_id] = name 
    
    print("Available symbols to vote for:")
    for symbol in votes:
        print(symbol)
    
    while True:
        vote_for = input("Enter the symbol you wish to vote for: ")
        if vote_for in votes:
            votes[vote_for] += 1
            print("Thank you for voting!")
            break
        else:
            print("Invalid symbol, please try again.")

while True:
    print("1. Add votee")
    print("2. Vote")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_votee()
    elif choice == 2:
        vote()
    elif choice == 3:
        break
    else:
        print("Invalid choice, please try again.")

print("\nVote Results:")
for symbol, count in votes.items():
    print(f"{symbol} ({votees[symbol]}): {count} votes")
