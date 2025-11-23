class TicTacToe:
    def __init__(self):
        """
        Initializes an empty Tic-Tac-Toe board and sets the starting player to X.
        """
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):
        """
        Prints the current board state with position numbers for empty spots.
        """
        # create a board display with position numbers for empty spots
        b = [str(i) if spot == " " else spot
             
        for i, spot in enumerate(self.board)]

        print("\nBOARD POSITION & CURRENT BOARD:")
        print(f"{b[0]} | {b[1]} | {b[2]}")
        print("--+---+--")
        print(f"{b[3]} | {b[4]} | {b[5]}")
        print("--+---+--")
        print(f"{b[6]} | {b[7]} | {b[8]}\n")
        
        # b = self.board

        # # display board positions
        # print("BOARD POSITION GUIDE:")
        # print("0 | 1 | 2")
        # print("--+---+--")
        # print("3 | 4 | 5")
        # print("--+---+--")
        # print("6 | 7 | 8\n")

        # # show current board state
        # print("CURRENT BOARD:")
        # print(f"{b[0]} | {b[1]} | {b[2]}")
        # print("--+---+--")
        # print(f"{b[3]} | {b[4]} | {b[5]}")
        # print("--+---+--")
        # print(f"{b[6]} | {b[7]} | {b[8]}")

        

    def available_moves(self):
        """
        Keeps track of available moves remaining on the board

        RETURN VALUE:
        - Returns a list of available moves on the board.
        """
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position):
        """
        Places the current player's mark on the board at the given position.

        PARAMETERS:
        - position (int): The board position (0-8) where the player wants to place their mark.

        RETURN VALUE:
        - True if move was made
        - False if position was already occupied
        """
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        """
        Switches the current player from X to O or O to X.
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def winner(self):
        """
        Checks if there is a winner on the board.

        RETURN VALUE:
        - Returns "X" or "O" if there is a winner
        - Returns None if there is no winner yet
        """
        # all possible winning combinations
        win_conditions = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a] 
        return None

    def is_full(self):
        """
        Checks if the board is full (no available moves left).
        
        RETURN VALUE:
        - Returns True if the board is full
        - Returns False otherwise
        """
        return " " not in self.board # if no empty spaces, board is full
