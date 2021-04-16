fat_wallet = 100
video_game = 60
sales_tax = .08 * video_game
print("I want to buy a game")
print("how much money do I have? $" + str(fat_wallet))
video_game += sales_tax
print("It is going to be $" + str(video_game)) 
fat_wallet -= video_game
print("I have " +  str(fat_wallet) + " left")