# Secret Auction Program

Welcome to the **Secret Auction Program**! This Python-based auction system allows multiple auctioneers to place bids, and it determines the winner based on the highest bid for each round. The program also provides an option to save auction history and view the leaderboard with the top auctioneers.

## Features

- **Countdown Timer**: A countdown before the auction starts, customizable by the user.
- **Auction Rounds**: Multiple auction rounds where auctioneers place bids.
- **Auction Summary**: After each round, the program shows the summary of bids placed.
- **Leaderboard**: Displays the top 3 auctioneers based on the number of wins and total bids.
- **Auction History**: Keeps track of auction history (winners and bid amounts).
- **Export to CSV**: Allows exporting the auction history to a CSV file.
  
## Installation

### Requirements

- Python 3.x
- Required Python libraries (can be installed via pip):
  - `pyfiglet`
  - `termcolor`
  - `tqdm`

You can install the necessary libraries by running:

```bash
pip install pyfiglet termcolor tqdm
