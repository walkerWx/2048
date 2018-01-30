import numpy
import random


def start_game():

    game_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    while True:
        key = input()
        if key == 'h':
            move_left_board(game_board)

        elif key == 'j':
            game_board = numpy.rot90(game_board, k=3)
            move_left_board(game_board)
            game_board = numpy.rot90(game_board, k=1)

        elif key == 'k':
            game_board = numpy.rot90(game_board, k=1)
            move_left_board(game_board)
            game_board = numpy.rot90(game_board, k=3)

        elif key == 'l':
            game_board = numpy.rot90(game_board, k=2)
            move_left_board(game_board)
            game_board = numpy.rot90(game_board, k=2)

        else:
            break

        generate(game_board)
        display(game_board)


def generate(game_board):
    candidates = []
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                candidates.append((i, j))
    choice = random.choice(candidates)
    game_board[choice[0]][choice[1]] = 2


def move_left_board(game_board):
    for i in range(len(game_board)):
        move_left_line(game_board[i])


def move_left_line(line):

    for i in range(len(line)):
        if line[i] == 0:
            for j in range(i, len(line)):
                if line[j] != 0:
                    line[i] = line[j]
                    line[j] = 0
                    break

    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            line[i] *= 2
            for j in range(i+1, len(line)-1):
                line[j] = line[j+1]
            line[-1] = 0


def display(game_board):
    for line in game_board:
        for cell in line:
            print(cell, end='\t')
        print('\n')


start_game()

