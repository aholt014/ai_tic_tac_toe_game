import math

class AIPlayer:
    """
    AI Player using Minimax algorithm for Tic-Tac-Toe.
    """

    def __init__(self, ai_letter):
        """
        Initializes the AI player with its letter (X or O).
        """
        self.ai_letter = ai_letter
        self.human_letter = "O" if ai_letter == "X" else "X"

    def minimax(self, board, maximizing):
        """
        Minimax algorithm to evaluate the best move.
        # NOTE: Minimax algorithm is a recursive algorithm used in decision-making and game theory.
        It provides an optimal move for the player assuming that the opponent also plays optimally.
        - maximizing: The AI player tries to maximize its score.
        - minimizing: The human player tries to minimize the AI's score.

        PARAMETERS:
        - board (list): Current state of the board.
        - maximizing (bool): True if the current layer is maximizing for AI, False for human.
        
        RETURN VALUE:
        - Score of the board state.
        """

        # Check terminal states
        winner = self.check_winner(board)

        if winner == self.ai_letter:
            return 1
        
        if winner == self.human_letter:
            return -1
        
        if " " not in board:
            return 0

        if maximizing:
            best_score = -math.inf

            for i in range(9):
                if board[i] == " ":
                    board[i] = self.ai_letter
                    score = self.minimax(board, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score

        else:
            best_score = math.inf

            for i in range(9):
                if board[i] == " ":
                    board[i] = self.human_letter
                    score = self.minimax(board, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def get_best_move(self, board):
        """
        Determines the best move for the AI using the Minimax algorithm.
        
        PARAMETERS:
        - board (list): Current state of the board. 
       
        RETURN VALUE:
        - The index (0-8) of the best move for the AI.
        """
        best_score = -math.inf
        move = None

        for i in range(9):
            if board[i] == " ":
                board[i] = self.ai_letter
                score = self.minimax(board, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def check_winner(self, board):
        """
        Checks if there is a winner on the board.

        PARAMETERS:
        - board (list): Current state of the board.
        
        RETURN VALUE:
        - Returns "X" or "O" if there is a winner
        - Returns None if there is no winner yet
        """
        win_conditions = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]

        for a, b, c in win_conditions:
            if board[a] == board[b] == board[c] != " ":
                return board[a]
        return None
