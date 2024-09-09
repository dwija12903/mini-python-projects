import random

class TicTacToe(object):
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    )

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self, board=[]):
        # Initialize the tic tav toe board
        # :param board: 1-D list of board positions
        if len(board) == 0:
            self.board = [0 for i in range(9)]
        else:
            self.board=board
        
    def print_board(self):
        # Printing Tic Tac Toe board
        for i in range(3):
            print(
                "|" + str(self.board[i * 3]) + 
                "|" + str(self.board[i * 3 + 1]) + 
                "|" + str(self.board[i * 3 + 2]) + "|"
            )

    def check_game_over(self):
        # Check if the game is over or there is a winner 
        if 0 not in [element for element in self.board]:
            return True
        if self.winner() != 0:
            return True
        return False
    
    def available_moves(self):
        # to check what all possible moves are remaining for a player 
        return [index for index, element in enumerate(self.board) if element == 0]
    
    def available_combos(self, player):
        # to check what all possible places to play for winning the game 
        return self.available_moves() + self.get_acquired_places(player)
    
    def X_won(self):
        return self.winner() == 'X'
    
    def O_won(self):
        return self.winner() == '0'
    
    def is_tie(self):
        return self.winner() == 0 and self.check_game_over()
    
    def winner(self):
        # Check the winner of the game
        # :return: 'X' or 'O' or 0 whoever wins else returns 0

        for player in ('X', 'O'):
            positions = self.get_acquired_places(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return 0
    
    def get_acquired_places(self, player):
        # to get the position alreast acquired by a particular player
        # :param player: 'X' or 'O'
        return [index for index, element in enumerate(self.board) if element == player]
    
    def make_move(self, position, player):
        self.board[position] = player

    def minimax(self, node, player):
        # Minimax algorithm for choosing the best possible move towards winning the game 
        if node.check_game_over():
            if node.X_won():
                return -1
            elif node.is_tie():
                return 0
            elif node.O_won():
                return 1
        best = 0
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.minimax(node, get_enemy(player))
            node.make_move(move, 0)
            if player == 'O':
                if val > best:
                    best = val
            else:
                if val < best:
                    best = val
        return best
    
def determine(board,player):
        # driver function to apply minimax algorithm
        a=0
        choices=[]
        if len(board.available_moves())==9:
            return 4
        for move in board.available_moves():
            board.make_move(move,player)
            val=board.minimax(board,get_enemy(player))
            board.make_move(move,0)
            if val>a:
                a=val
                choices=[move]
            elif val==a:
                choices.append(move)
        try:
            return random.choice(choices)
        except IndexError:
            return random.choice(board.available_moves())
        
def get_enemy(player):
    if player == 'X':
        return 'O'
    return 'X'

if __name__ =='__main__':
    board = TicTacToe()
    print("Board Positions are like this: ")
    for i in range(3):
        print(
            "|" + str(i * 3) + 
            "|" + str(i * 3 + 1) + 
            "|" + str(i * 3 + 2) + "|"
            )
    print("Type in the position where you want to play...")
    while not board.check_game_over():
        player='X'
        player_move=int(input("Enter your move: "))
        if player_move not in board.available_moves():
            print("Invalid Move, Check your move!")
            continue
        board.make_move(player_move,player)
        board.print_board()
        print()
        if board.check_game_over():
            break
        print("Computer is playing...")
        player = get_enemy(player)
        computer_move=determine(board,player)
        board.make_move(computer_move,player)
        board.print_board()
    if board.winner() != 0:
        if board.winner() == 'X':
            print("Congratulations You Win!")
        else:
            print("Computer Wins!")
    else:
        print("It's a Draw!")