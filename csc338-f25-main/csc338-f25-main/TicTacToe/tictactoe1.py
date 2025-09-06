import sys

WIN_LINES = [
    [(0,0),(0,1),(0,2)],  # rows
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0)],  # cols
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
    [(0,0),(1,1),(2,2)],  # diagonals
    [(0,2),(1,1),(2,0)]
]

class GameBoard:

    def __init__(self):

        self.entries = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.state = 0
        # State 0: Game playing
        # State 1: Player 1 wins
        # State 2: Player 2 wins
        # State 3: Draw

    def print_bd(self):

        for i in range(3):
            for j in range(3):
                print(self.entries[i][j], end = '')
            print('')

    def checkwin(self) -> int:

        for line in WIN_LINES:
            vals = [self.entries[r][c] for r,c in line]
            if vals == [1, 1, 1]:
                return 1
            if vals == [2, 2, 2]:
                return 2
        if any(0 in row for row in self.entries):
            return 0
        
        return 3





class TicTacToeGame:

    def __init__(self):
        
        self.gameboard = GameBoard()
        self.turn = 1
        self.turnnumber = 1

    def playturn(self):
        print("Turn number: ", self.turnnumber)
        self.turnnumber += 1

        self.gameboard.print_bd()

        if self.turn == 1:
            print("Human, please choose a space!")
            validinput = False

            user_input = input("Enter two numbers separated by a comma: ")
            humanrow, humancol = map(int, map(str.strip, user_input.split(',')))
            self.gameboard.entries[humanrow][humancol] = 1
            self.turn = 2
        else:
            print("AI is thinking...")
            move, score = self.gameboard.minmax(self.gameboard.entries)
            print("AI chooses move: ", move, " with score: ", score)
            self.gameboard.entries[move[0]][move[1]] = 2
            self.turn = 1



game = TicTacToeGame()

while game.gameboard.state == 0:
    game.playturn()
    game.gameboard.state = game.gameboard.checkwin()
    print('')

game.gameboard.print_bd()
if game.gameboard.state == 1:
    print("Player 1 Wins!")
elif game.gameboard.state == 2:
    print("Player 2 Wins!")
else:
    print("The game is a draw!")