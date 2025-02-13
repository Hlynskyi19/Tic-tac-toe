class TicTacToe:
    def __init__(self):
        """Ініціалізуємо ігрове поле"""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        """Виводимо ігрове поле на екран"""
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row: int, col: int) -> bool:
        """Здійснюємо хід, якщо клітинка порожня"""
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        """Змінюємо активного гравця"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self) -> str:
        """Перевіряємо, чи є переможець"""
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return ""

    def is_draw(self) -> bool:
        """Перевіряємо, чи нічию"""
        return all(cell != " " for row in self.board for cell in row)

    def play(self):
        """Основний ігровий цикл"""
        while True:
            self.print_board()
            try:
                row, col = map(
                    int,
                    input(
                        f"Гравець {self.current_player}, введіть рядок і стовпчик (0-2): "
                    ).split(),
                )
                if row not in range(3) or col not in range(3):
                    raise ValueError("Некоректні координати. Спробуйте ще раз.")
                if not self.make_move(row, col):
                    print("Ця клітинка вже зайнята! Спробуйте ще раз.")
                    continue
            except ValueError as e:
                print(e)
                continue

            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Гравець {winner} виграв!")
                break
            elif self.is_draw():
                self.print_board()
                print("Нічия!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
