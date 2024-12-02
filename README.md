# Secret Auction Program

A fun and interactive auction program where auctioneers can place bids, and the winner is declared based on the highest bid. It supports multiple rounds, leaderboard tracking, and a countdown timer before the auction begins.

## Features

- **Auction Countdown**: Users can set a countdown time before the auction begins.
- **Auction Process**: Multiple auctioneers can participate, and they place their bids. The auctioneer with the highest bid wins the round.
- **Multiple Winners**: If multiple auctioneers have the same highest bid, it's a tie.
- **Leaderboard**: Keeps track of the top 3 auctioneers based on wins and total bid amounts.
- **Auction History**: Displays all rounds, winners, and bid amounts.
- **Input Validation**: Ensures that user inputs (auctioneers' names and bid amounts) are valid.

## Requirements

Before running the program, ensure you have the following Python libraries installed:

- `pyfiglet`: For displaying fun ASCII art for the program title.
- `replit`: For clearing the terminal screen after each auction.
- `termcolor`: For colorizing terminal output (for a better user experience).
- `time`: For implementing the countdown timer.

To install the required libraries and use the application, run the following commands:

```bash
pip install pyfiglet replit termcolor
python auction_program.py
