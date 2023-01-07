import pyfiglet
from replit import clear
app_name=pyfiglet.figlet_format("Secret Auction")
print(app_name)
def auction_winner():
        n=int(input("Enter the number of auctioners: "))
        dict1={}
        for i in range(n):
                name=input("Enter the name of the auctioner: ")
                bid=int(input("Enter the value of the amount they are bidding: "))
                dict1.update({name:bid})
                clear()
        max1=max(dict1.values())
        name_list=list(dict1.keys())
        bid_list=list(dict1.values())
        position=bid_list.index(max1)
        winner=name_list[position]
        print(f"The winner is {winner} with a winning bid of ${max1}")
auction_winner()
while(True):
        opinion=input("Do you want to continue the auction program: ")
        if(opinion=="Yes" or opinion=="yes" or opinion=="YES"):
                auction_winner()
        elif(opinion=="No" or opinion=="no" or opinion=="NO"):
                print("Thank you for using our auction winner declaring application")
                break