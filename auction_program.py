import pyfiglet
from replit import clear
from termcolor import colored
import time
import csv
from datetime import datetime

# Global variables for auction data
auction_history = []
leaderboard = {}
MIN_BID_INCREMENT = 10  # Minimum bid increment

def countdown_timer(seconds):
    print(colored(f"\nAuction will start in {seconds} seconds...", "blue"))
    for i in range(seconds, 0, -1):
        print(colored(f"Starting in {i}...", "yellow"))
        time.sleep(1)
    print(colored("\nAuction has started!", "green"))

def auction_summary(bids):
    print("\n--- Auction Round Summary ---")
    for name, bid in bids.items():
        print(f"{name} placed a bid of ${bid}")
    print("\n-----------------------------")

def update_leaderboard(winner_names, max_bid):
    for winner in winner_names:
        if winner not in leaderboard:
            leaderboard[winner] = {"wins": 0, "total_bids": 0}
        leaderboard[winner]["wins"] += 1
        leaderboard[winner]["total_bids"] += max_bid

def print_top_3():
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: (-x[1]["wins"], -x[1]["total_bids"]))
    print("\n--- Top 3 Auctioneers ---")
    if sorted_leaderboard:
        for i, (name, stats) in enumerate(sorted_leaderboard[:3], 1):
            print(f"{i}. {name} | Wins: {stats['wins']} | Total Bids: ${stats['total_bids']}")
    else:
        print("No auctioneers yet.")
    
    max_bid_ever = max([max_bid for _, max_bid in auction_history], default=0)
    print(f"\nMax Bid Ever: ${max_bid_ever}\n--------------------------")

def print_leaderboard():
    print("\n--- Auction Leaderboard ---")
    for idx, (winners, bid) in enumerate(auction_history, 1):
        winners_str = ', '.join(winners)
        print(f"Round {idx}: Winner(s) - {winners_str} | Bid: ${bid}")
    print("\n--------------------------")

def export_history_to_file():
    """Export auction history to file"""
    filename = f"auction_history_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Round", "Winners", "Bid"])
        for idx, (winners, bid) in enumerate(auction_history, 1):
            writer.writerow([idx, ', '.join(winners), bid])
    print(colored(f"\nAuction history has been exported to {filename}", "cyan"))

def auction_winner():
    print(pyfiglet.figlet_format("Secret Auction"))
    
    # Input validation for number of auctioneers
    while True:
        try:
            n = int(input("Enter the number of auctioneers: "))
            if n <= 0:
                print(colored("Please enter a valid number of auctioneers (greater than 0).", "red"))
                continue
            break
        except ValueError:
            print(colored("Invalid input! Please enter a valid integer.", "red"))
    
    bids = {}
    for i in range(n):
        name = input(f"Enter the name of auctioneer {i+1}: ")
        
        # Input validation for bid
        while True:
            try:
                bid = int(input(f"Enter the value of the bid for {name}: $"))
                if bid <= 0:
                    print(colored("Please enter a valid bid amount (greater than 0).", "red"))
                    continue
                if bids and bid <= max(bids.values()) + MIN_BID_INCREMENT:
                    print(colored(f"Bid must be at least ${MIN_BID_INCREMENT} higher than the current highest bid.", "red"))
                    continue
                break
            except ValueError:
                print(colored("Invalid input! Please enter a valid integer.", "red"))
        
        bids[name] = bid
        clear()

    max_bid = max(bids.values())
    winner_names = [name for name, bid in bids.items() if bid == max_bid]
    
    auction_summary(bids)  # Display the bids of all auctioneers

    if len(winner_names) == 1:
        print(colored(f"The winner is {winner_names[0]} with a winning bid of ${max_bid}", "green"))
    else:
        print(colored(f"It's a tie between {' and '.join(winner_names)} with a bid of ${max_bid}", "yellow"))
    
    # Update history and leaderboard
    auction_history.append((winner_names, max_bid))
    update_leaderboard(winner_names, max_bid)
    
    print_top_3()
    print_leaderboard()

def main():
    print(colored("Welcome to the Secret Auction Program!", "magenta"))
    
    # User-defined countdown timer before auction starts
    while True:
        try:
            countdown_time = int(input("Enter the countdown time before auction begins (seconds): "))
            if countdown_time < 0:
                print(colored("Please enter a non-negative value.", "red"))
                continue
            break
        except ValueError:
            print(colored("Invalid input! Please enter a valid integer.", "red"))
    
    countdown_timer(countdown_time)
    
    while True:
        auction_winner()
        
        opinion = input("Do you want to continue the auction program? (Yes/No/Exit): ").strip().lower()
        if opinion == 'yes':
            clear()  # Clear the screen for the next auction
        elif opinion == 'no':
            print(colored("Thank you for using our auction winner declaring application!", "cyan"))
            break
        elif opinion == 'exit':
            export_history_to_file()
            break
        else:
            print(colored("Invalid input! Please respond with 'Yes', 'No', or 'Exit'.", "red"))

if __name__ == "__main__":
    main()
