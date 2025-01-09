import pyfiglet
from termcolor import colored
import time
import csv
from datetime import datetime
import warnings
from requests.exceptions import RequestsDependencyWarning
import os
from tqdm import tqdm

warnings.filterwarnings("ignore", category=RequestsDependencyWarning)

# Global variables for auction data
auction_history = []
leaderboard = {}
MIN_BID_INCREMENT = 10  # Default minimum bid increment

def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def get_valid_integer(prompt, error_message="Invalid input! Please enter a valid integer.", condition=None):
    """Prompt the user for a valid integer."""
    while True:
        try:
            value = int(input(prompt))
            if condition and not condition(value):
                print(colored(error_message, "red"))
                continue
            return value
        except ValueError:
            print(colored(error_message, "red"))

def countdown_timer(seconds):
    """Display a countdown timer using tqdm for a smoother experience."""
    for remaining in tqdm(range(seconds, 0, -1), desc="Starting Auction", unit="sec"):
        time.sleep(1)
    print(colored("\nAuction has started!", "green"))

def auction_summary(bids):
    """Display a summary of the current auction round."""
    print("\n--- Auction Round Summary ---")
    for name, bid in bids.items():
        print(f"{name} placed a bid of ${bid}")
    print("\n-----------------------------")

def update_leaderboard(winner_names, max_bid):
    """Update the global leaderboard with auction results."""
    for winner in winner_names:
        if winner not in leaderboard:
            leaderboard[winner] = {"wins": 0, "total_bids": 0}
        leaderboard[winner]["wins"] += 1
        leaderboard[winner]["total_bids"] += max_bid

def print_top_3():
    """Display the top 3 auctioneers from the leaderboard."""
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
    """Display the full auction leaderboard."""
    print("\n--- Auction Leaderboard ---")
    if auction_history:
        for idx, (winners, bid) in enumerate(auction_history, 1):
            winners_str = ', '.join(winners)
            print(f"Round {idx}: Winner(s) - {winners_str} | Bid: ${bid}")
    else:
        print("No auction history available.")
    print("\n--------------------------")

def export_history_to_file():
    """Export auction history to a CSV file."""
    if not auction_history:
        print(colored("\nNo auction history to export.", "yellow"))
        return

    filename = f"auction_history_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Round", "Winners", "Bid"])
            for idx, (winners, bid) in enumerate(auction_history, 1):
                writer.writerow([idx, ', '.join(winners), bid])
        print(colored(f"\nAuction history has been exported to {filename}", "cyan"))
        print(colored(f"File saved as: {os.path.abspath(filename)}", "cyan"))
    except Exception as e:
        print(colored(f"\nFailed to export auction history: {e}", "red"))

def auction_winner():
    """Conduct a single auction round and declare the winner."""
    print(pyfiglet.figlet_format("Secret Auction"))

    # Input validation for number of auctioneers
    n = get_valid_integer(
        "Enter the number of auctioneers (at least 2): ",
        "At least 2 auctioneers are required.",
        lambda x: x >= 2
    )

    bids = {}
    names_set = set()
    for i in range(n):
        while True:
            name = input(f"Enter the name of auctioneer {i+1}: ").strip()
            if name in names_set:
                print(colored("Auctioneer names must be unique! Please enter a different name.", "red"))
            else:
                names_set.add(name)
                break

        # Input validation for bid
        bid = get_valid_integer(
            f"Enter the bid value for {name} (minimum: ${max(bids.values(), default=0) + MIN_BID_INCREMENT}): $",
            f"Please enter a bid greater than ${max(bids.values(), default=0) + MIN_BID_INCREMENT}.",
            lambda x: x > max(bids.values(), default=0) + MIN_BID_INCREMENT
        )
        bids[name] = bid
        clear_screen()

    max_bid = max(bids.values())
    winner_names = [name for name, bid in bids.items() if bid == max_bid]

    auction_summary(bids)  # Display the bids of all auctioneers

    if len(winner_names) == 1:
        print(colored(f"The winner is {winner_names[0]} with a winning bid of ${max_bid}", "green"))
    else:
        print(colored(f"It's a tie! Winners: {', '.join(winner_names)} with a bid of ${max_bid}", "yellow"))

    # Update history and leaderboard
    auction_history.append((winner_names, max_bid))
    update_leaderboard(winner_names, max_bid)

    print_top_3()
    print_leaderboard()

def main():
    """Main function to run the auction program."""
    try:
        print(colored("Welcome to the Secret Auction Program!", "magenta"))

        countdown_time = get_valid_integer(
            "Enter the countdown time before auction begins (seconds): ",
            "Please enter a non-negative integer.",
            lambda x: x >= 0
        )
        countdown_timer(countdown_time)

        while True:
            auction_winner()

            print("\nWhat would you like to do next?")
            print("1. Continue with a new auction")
            print("2. Exit without saving")
            print("3. Exit and save auction history")
            choice = get_valid_integer("Enter your choice (1-3): ", "Invalid choice! Please enter 1, 2, or 3.", lambda x: 1 <= x <= 3)
            
            if choice == 1:
                clear_screen()
            elif choice == 2:
                print(colored("Thank you for using the Secret Auction Program!", "cyan"))
                break
            elif choice == 3:
                export_history_to_file()
                break
    except Exception as e:
        print(colored(f"\nAn unexpected error occurred: {e}", "red"))

if __name__ == "__main__":
    main()
