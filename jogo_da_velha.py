# JOGO DA VELHA COM IA MINIMAX

import math

board = [" " for _ in range(9)]


def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")


def is_winner(board, player):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    return any(
        all(board[i] == player for i in cond)
        for cond in win_conditions
    )


def is_draw(board):
    return " " not in board and not is_winner(board, "X") and not is_winner(board, "0")


def minimax(board, depth, is_maximizing):

    if is_winner(board, "0"):
        return 1

    if is_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "0"

                score = minimax(board, depth + 1, False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, depth + 1, True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "0"

            score = minimax(board, 0, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def play():
    print("\n=== JOGO DA VELHA COM IA MINIMAX ===")
    print("Você é X, IA é 0.")
    print("Escolha uma posição de 0 a 8.\n")

    print("Posições:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8\n")

    print_board(board)

    while True:

        try:
            move = int(input("\nEscolha sua jogada (0-8): "))

            if move < 0 or move > 8:
                print("Jogada inválida, escolha entre 0 e 8.")
                continue

            if board[move] != " ":
                print("Espaço ocupado, tente novamente!")
                continue

        except ValueError:
            print("Digite apenas um número de 0 a 8.")
            continue

        board[move] = "X"

        if is_winner(board, "X"):
            print_board(board)
            print("\nVocê venceu!!")
            break

        if is_draw(board):
            print_board(board)
            print("\nEmpate!")
            break

        ia_move = best_move(board)
        board[ia_move] = "0"

        print(f"\nIA jogou na posição {ia_move}.\n")
        print_board(board)

        if is_winner(board, "0"):
            print("\nA IA venceu!")
            break

        if is_draw(board):
            print("\nEmpate!")
            break


# INICIAR JOGO
play()