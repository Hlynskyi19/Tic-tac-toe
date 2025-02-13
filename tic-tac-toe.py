def print_board(board):
    """Виводить ігрове поле у консоль."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Перевіряє, чи є переможець."""
    # Перевірка рядків і стовпців
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(
            board[j][i] == player for j in range(3)
        ):
            return True
    # Перевірка діагоналей
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True
    return False


def is_draw(board):
    """Перевіряє, чи є нічия."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def get_player_move(board):
    """Отримує хід гравця."""
    while True:
        try:
            row, col = map(
                int, input("Введіть рядок і стовпець (0-2 через пробіл): ").split()
            )
            if board[row][col] == " ":
                return row, col
            else:
                print("Ця клітинка вже зайнята. Спробуйте ще раз.")
        except (ValueError, IndexError):
            print("Некоректний ввід. Введіть два числа від 0 до 2.")


def main():
    """Головна функція гри."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        print(f"Хід гравця {players[turn]}")
        row, col = get_player_move(board)
        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Гравець {players[turn]} переміг!")
            break
        elif is_draw(board):
            print_board(board)
            print("Нічия!")
            break

        turn = 1 - turn  # Зміна гравця


if __name__ == "__main__":
    main()
