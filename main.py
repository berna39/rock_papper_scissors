import random

#main method
def play():
    computer = random.choice(['r', 'p', 's'])
    player = input("Choose between 'r, 'p' and 's : \n")

    if player == compile:
        return 'it\'  a tie'
    if is_win(player, computer): #testing if th user wins
        return 'yay ! you  won'
    return 'you lost'

#the is_win method
def is_win(player, computer):
    if (player == 'r' and computer == 's') or ( player == 's' and computer == 'p' ) or (player == 'p' and computer =='r' ):
        return True
    return False
 

print(play())