# https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
# This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.

# In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

#     Draw the Tic Tac Toe game board
#     Checking whether a game board has a winner
#     Handle a player move from user input

# The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

# Here are a few things to keep in mind:

#     You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
#     If there are no more moves left, don’t ask for the next player’s move!

# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.


def row(size):
    for i in range(0, size):
        print(' ---', end='')
    
    print('')
def column(size, game):
    for i in range(0, size):
        print ('|', end='')
        if game[i] == 0:
            print('   ', end='')
        elif game[i] ==  1:
            print(' X ', end='')
        else:
            print(' O ', end='')
    print('|')
    
def gameboard(game):
    size = 3
    for i in range(0, size):
        row(size)
        column(size,game[i])
    row(size)

def hasMove(game):
    for r in game:
        if 0 in r:
            return True
    return False

def hasWinner(game):
    for row in game :
        if row[0]== row[1] and row[0] == row[2] and row[0] >0:
            return row[0]
    
    for i in range(0,3):
        if game[0][i] == game[1][i] and game[0][i]== game[2][i] and game[0][i] >0 :
            return game[0][i]

    if game[0][0] >0 and game[0][0]==game[1][1] and game[0][0]==game[2][2] :
        return game[0][0]

    return 0

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

while True:
    

    gameboard(game)
    

    if hasWinner(game) != 0 :
        winner = hasWinner(game)
        print ("Player ", winner, "wins!")
        break

    if hasMove(game) == False:
        print("Game over!")
        break

    player1 = input("Player 1, what's your move?")
    x = int(player1[0]) 
    y = int(player1[2])
    game[x-1][y-1]=1

    gameboard(game)
    if hasWinner(game) != 0 :
        winner = hasWinner(game)
        print ("Player ", winner, "wins!")
        break
        
    if hasMove(game) == False:
        print("Game over!")
        break

    player2 = input("Player 2, what's your move?")
    x = int(player2[0]) 
    y = int(player2[2])
    game[x-1][y-1]=2