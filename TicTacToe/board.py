# Assignment: Programming Assignment 2
# Author: Raghav Singh
# Date: 28/4/2023
class Board:
    def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
    def get_size(self):
          return self.size
               # optional, return the board size (an instance size)
    def get_winner(self):
          return self.winner
            # return the winner's sign O or X (an instance winner)     
    def set(self, cell, sign):
        cell_list = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        index = cell_list.index(cell)
        # check if the cell is empty
        self.board[index] = sign
            
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you 
    def isempty(self, cell):
        cell_list = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        index = cell_list.index(cell)
        if self.board[index] == " ":
             return True
        else:
             return False
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        done = False
        self.winner = ''
        for i in range(0,7,3):# for checking horizontal rows
             if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                done = True
                self.winner = self.board[i]
        for i in range(0,3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                done = True
                self.winner = self.board[i]
        if (self.board[0] == self.board[4] == self.board[8] != " " ) or (self.board[2] == self.board[4] == self.board[6] != " "):
                done = True
                self.winner = self.board[4]
        elif " " not in self.board:
            done = True
            self.winner = ""
        return done       
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
    def show(self):
            # draw the board
            # need to complete the code
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
            print(' +---+---+---+')
