import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]


def ai_move(board, ai_symbol):
    moves = get_available_moves(board)
    return random.choice(moves) if moves else None


def tic_tac_toe():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        user_symbol = "X" if input("Do you want to be X or O? ").upper() == "X" else "O"
        ai_symbol = "O" if user_symbol == "X" else "X"

        current_player = "X"  
        print_board(board)

        while True:
            if current_player == user_symbol:
                move = None
                while move not in get_available_moves(board):
                    try:
                        row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
                        move = (row, col)
                    except ValueError:
                        print("Invalid input. Please enter two numbers between 0 and 2.")

                board[row][col] = user_symbol
            else:
                print("AI is making a move...")
                row, col = ai_move(board, ai_symbol)
                board[row][col] = ai_symbol

            print_board(board)

            if check_winner(board, current_player):
                print(f"{current_player} wins!")
                break
            elif not get_available_moves(board):
                print("It's a draw!")
                break

            current_player = user_symbol if current_player == ai_symbol else ai_symbol

        if input("Play again? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    tic_tac_toe()
