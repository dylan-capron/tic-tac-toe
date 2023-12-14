# ia.py

import random

def ia_facile(board, signe):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    if empty_positions:
        return random.choice(empty_positions)
    else:
        return False

def ia_moyen(board, signe):
    # Priorité à gagner ou bloquer l'adversaire
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = signe
                if check_winner(board, signe):
                    board[i][j] = ''
                    return i, j
                board[i][j] = ''

    # Si aucune opportunité n'est disponible, jouer au hasard
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    if empty_positions:
        return random.choice(empty_positions)
    else:
        return False

def ia_difficile(board, signe):
    # Implémenter un algorithme plus avancé (Minimax par exemple)
    # Pour cet exemple, on utilise l'IA de niveau moyen
    return ia_moyen(board, signe)

def check_winner(board, signe):
    for i in range(3):
        # Vérifier les lignes
        if board[i][0] == board[i][1] == signe and board[i][2] == signe:
            return True
        # Vérifier les colonnes
        if board[0][i] == board[1][i] == signe and board[2][i] == signe:
            return True

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == signe and board[2][2] == signe:
        return True
    if board[0][2] == board[1][1] == signe and board[2][0] == signe:
        return True

    return False
