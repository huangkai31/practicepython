# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

# Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

# 0: no winner, 1: player 1 wins, 2: player 2 wins
def getWinner(game):
    for row in game :
        if row[0]== row[1] and row[0] == row[2] and row[0] >0:
            return row[0]
    
    for i in range(0,3):
        if game[0][i] == game[1][i] and game[0][i]== game[2][i] and game[0][i] >0 :
            return game[0][i]

    if game[0][0] >0 and game[0][0]==game[1][1] and game[0][0]==game[2][2] :
        return game[0][0]

    return 0

print (getWinner(winner_is_1))
print (getWinner(winner_is_2))
print (getWinner(winner_is_also_1))
print (getWinner(no_winner), getWinner(also_no_winner))