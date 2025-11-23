from game import TicTacToe
from ai_agent import AIPlayer

def play():
    """
    Main function to play Tic-Tac-Toe between a human and an AI agent.
    """

    # Initialize game and AI agent
    game = TicTacToe() # create a new TicTacToe game instance
    ai = AIPlayer("O")  # AI plays O

    print("Welcome to Tic-Tac-Toe (Human vs AI)!")
    print("================================")
    print("You are X, AI is O. Select your moves by entering a number 0-8.")
    print("Board positions are numbered 0-8 as follows: \n")

    # TODO: create other game options for human vs human, ai vs ai, etc.
    # TODO: create option to choose X or O
    # TODO: create option to choose difficulty (depth limit for minimax)

    game.print_board()

    while True:
        # Human move
        if game.current_player == "X":
            move = int(input("Choose move (0-8): "))
            if move not in game.available_moves():
                print("Invalid move. Try again.")
                continue
            game.make_move(move)

        else:
            print("\nAI thinking...")
            move = ai.get_best_move(game.board)
            game.make_move(move)
            print(f"AI chose {move}\n")

        game.print_board()

        # Check winner
        if game.winner():
            print("Winner:", game.winner())
            break

        if game.is_full():
            print("It's a tie!")
            break

        game.switch_player()

if __name__ == "__main__":
    play()

