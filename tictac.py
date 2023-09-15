import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.root,
                    text=" ",
                    font=("Arial", 20),
                    width=8,
                    height=4,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in self.board:
            if len(set(row)) == 1 and row[0] != " ":
                return row[0]

        # Check columns
        for col in range(3):
            if len(set([self.board[row][col] for row in range(3)])) == 1 and self.board[0][col] != " ":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] ==self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" " , fg="red",bg="blue")

    def run(self):
        self.root.mainloop()

game = TicTacToe()
game.run()
