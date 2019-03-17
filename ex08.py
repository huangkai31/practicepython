# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock


# get player input
def player_input(name):
    i = input(name+ ": Pls input R/P/S:")
    while i not in ["R", "P", "S"]:
        i = input(name+": Wrong input, Pls input R/P/S:")
    return i

while True :
    player1 = player_input("Player1")
    player2 = player_input("Player2")
    if player1 == player2 :
        print ("tie")
    else:
        if player1 == "R" and player2 == "S" or player1 == "S" and player2 == "P" or player1 == "P" and player2 == "R":
            print("player1 wins")
        elif player1 == "S" and player2 == "R" or player1 == "P" and player2 == "S" or player1 == "R" and player2 == "P":
            print("player2 wins")
    
    continue_game = input("Do you want to play again? (y/n)")
    if continue_game == "y" :
        continue
    else: 
        break
    

    

