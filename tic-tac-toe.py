# tic-tac-toe.py
import tkinter as tk
from tkinter import messagebox
import ia

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.user_scores = {'X': 0, 'O': 0, 'Draw': 0}
        self.user_history = []

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text='', font=('normal', 20), width=8, height=3,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Le joueur {self.current_player} gagne!")
                self.user_scores[self.current_player] += 1
                self.user_history.append(f"Le joueur {self.current_player} a gagné.")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "Match nul!")
                self.user_scores['Draw'] += 1
                self.user_history.append("Match nul.")
                self.reset_game()
            else:
                self.switch_player()
                self.perform_ia_move()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True

        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != '':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='')

        self.current_player = 'X'

    def perform_ia_move(self):
        move = ia.ia_moyen(self.board, 'O')

        if move is not False:
            row, col = move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", "L'ordinateur gagne!")
                self.user_scores['O'] += 1
                self.user_history.append("L'ordinateur a gagné.")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "Match nul!")
                self.user_scores['Draw'] += 1
                self.user_history.append("Match nul.")
                self.reset_game()
            else:
                self.switch_player()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
