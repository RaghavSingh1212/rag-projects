# Assignment: Programming Assignment 2
# Author: Raghav Singh
# Date: 28/4/2023

from random import choice
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign
            # return an instance sign
      def get_name(self):
            return self.name
            # return an instance name
      def choose(self, board):
            end = False
            while end == False:
                input1 = str(input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n")).upper()
                if len(input1) != 2:
                    print("You did not choose correctly.")
                    continue
                if input1[0] not in ["A","B","C"]:
                    print("You did not choose correctly.")
                    continue
                if input1[1] not in ["1","2","3"]:
                    print("You did not choose correctly.")
                    continue
                if not board.isempty(input1):
                    print("You did not choose correctly.")
                    continue
                board.set(input1, self.sign)
                break
                        # prompt the user to choose a cell
                        # if the user enters a valid string and the cell on the board is empty, update the board
                        # otherwise print a message that the input is wrong and rewrite the prompt
                        # use the methods board.isempty(cell), and board.set(cell, sign)
class AI(Player):
    def __init__(self, name, sign, board):
        self.name = name  # player's name
        self.sign = sign
        self.board = board.board
    def get_sign(self):
            return self.sign
            # return an instance sign
    def get_name(self):
            return self.name
    def choose(self, board):
        while True:
            colum_choice = choice(["1","2","3"])
            row_choice = choice(["A","B","C"])
            cell = (f'{row_choice}{colum_choice}')
            if board.isempty(cell):
                board.set(cell, self.sign)
                return cell  



class MiniMax(AI):
    def choose(self, board):
        if self.sign == "X":
            self.oponent = "O"
        else:
            self.oponent = "X"
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)
    def minimax(self, board, self_player, start):
        # check the base conditions

        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == "":
                return 0
            # self is a looser (opponent is a winner)
            else: 
                return -1
        max_score = float("-inf")
        min_score = float("inf")
        space = " "
        cell_list =  ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        for i in range(0,9):
            cell = cell_list[i]
            if board.isempty(cell):
                if self_player:
                   board.set(cell,self.sign)
                   score = self.minimax(board,False, False)
                   if score >= max_score:
                       max_score=score
                       space = cell
                else:
                   board.set(cell,self.oponent)
                   score = self.minimax(board, True, False)
                   if score <= min_score:
                       min_score=score
                       space = cell
                board.set(cell, " ")

        if start:
            return space
        elif self_player:
            return max_score
        else:
            return min_score
        


class SmartAI(AI):
    def choose(self, board):
        if self.sign == "X":
            self.oponent = "O"
        else:
            self.oponent = "X"
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)
    def minimax(self, board, self_player, start):
        # check the base conditions

        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == "":
                return 0
            # self is a looser (opponent is a winner)
            else: 
                return -1
        max_score = float("-inf")
        min_score = float("inf")
        space = " "
        cell_list =  ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        for i in range(0,9):
            cell = cell_list[i]
            if board.isempty(cell):
                if self_player:
                   board.set(cell,self.sign)
                   score = self.minimax(board,False, False)
                   if score >= max_score:
                       max_score=score
                       space = cell
                else:
                   board.set(cell,self.oponent)
                   score = self.minimax(board, True, False)
                   if score <= min_score:
                       min_score=score
                       space = cell
                board.set(cell, " ")

        if start:
            return space
        elif self_player:
            return max_score
        else:
            return min_score





