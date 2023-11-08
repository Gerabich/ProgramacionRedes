'''
 Nombre: Gerardo Antonio Garcia Vazquez
 Fecha: 08 de Octubre de 2023 
 Descripcion: Laboratorio 4.7.2.1
'''

import random

def display_board(board):
    print("+---+---+---+")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n+---+---+---+")

def enter_move(board):
    free_cells = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1-9): "))
            if move in free_cells:
                make_move(board, move, 'O')
                break
            else:
                print("Movimiento no válido. Inténtalo de nuevo.")
        except ValueError:
            print("Ingresa un número válido.")

def make_list_of_free_fields(board):
    return [cell for row in board for cell in row if isinstance(cell, int)]

def make_move(board, move, player):
    for row in board:
        for i, cell in enumerate(row):
            if cell == move:
                row[i] = player

# Función para verificar si alguien ha ganado
def victory_for(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def draw_move(board):
    free_cells = make_list_of_free_fields(board)
    move = random.choice(free_cells)
    make_move(board, move, 'X')

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

print("¡Bienvenido al juego de Tic-Tac-Toe!\n")
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("¡Has Ganado!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("¡Es un empate!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("¡La máquina ha ganado!")
        break