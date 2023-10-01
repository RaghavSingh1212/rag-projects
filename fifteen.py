''' DO NOT FORGET TO ADD COMMENTS '''

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.adjacent = [
        [1, 4],              # 0
        [0, 2, 5],           # 1
        [1, 3, 6],           # 2
        [2, 7],              # 3
        [0, 5, 8],           # 4
        [1, 4, 6, 9],        # 5
        [2, 5, 7, 10],       # 6
        [3, 6, 11],          # 7
        [4, 9, 12],          # 8
        [5, 8, 10, 13],      # 9
        [6, 9, 11, 14],      # 10
        [7, 10, 15],         # 11
        [8, 13],             # 12
        [9, 12, 14],         # 13
        [10, 13, 15],        # 14
        [11, 14]             # 15
    ]


    def update(self, move):
        if self.is_valid_move(move):
            move_index = np.where(self.tiles == move)[0][0]
            for i in self.adjacent[move_index]:
                if self.tiles[i] == 0:
                    self.transpose(move_index,i)


        
    def transpose(self, i, j):
        self.tiles[i],self.tiles[j] = self.tiles[j],self.tiles[i]
        pass

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for _ in range(steps):
            move_index = choice (self.adjacent[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
        
    def is_valid_move(self, move):
        move_index = np.where(self.tiles == move)[0][0]
        for i in self.adjacent[move_index]:
            if self.tiles[i] == 0:
                return True
        return False


    def is_solved(self):
        target_tiles = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])
        return np.array_equal(self.tiles, target_tiles)


    def draw(self):
        print('+---+---+---+---+')
        for i in range(4):
            row = '|'
            for j in range(4):
                tile = self.tiles[i * 4 + j]
                if tile == 0:
                    row += '    |'
                else:
                    row += f' {tile:2d} |'
            print(row)
            print('+---+---+---+---+')



        
    def __str__(self):
        size = 4
        result = ''
        for i in range(size):
            for j in range(size):
                if self.tiles[i*size+j] == 0:
                    result += '   '
                else:
                    result += f'{self.tiles[i*size+j]:2d} '
            result += '\n'
        return result


    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False


    
    
    
    '''You should be able to play the game if you uncomment the code below'''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
    
    
        
