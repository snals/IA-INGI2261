'''
Created on 11 oct. 2012

@author: Florentin
'''
from IO import IO
from Case import *
import sys

class Board:
    
    '''
        Represent the static game board, with wall, goal and normal cases.
    '''


    def __init__(self, filename):
        """
            This constructor take the filename where the initial board representation is
            writting. It will make a representation in a matrix, containing Cases.
        """
        self.Io = IO(filename)
        self.Io.init_reader()
        self.board = []
    
        for line in self.Io.file :
            boardLine = []
            for char in line :
                if char == "#" :
                    boardLine.append(Case.WALL)
                elif char == " " :
                    boardLine.append(Case.NORMAL)
                elif char == ".":
                    boardLine.append(Case.GOAL)
            self.board.append(boardLine)
    
    def print_board(self):
        for line in self.board :
            for char in line :
                sys.stdout.write(str(char))
            print("\n")
    
    def getUp(self,x,y):
        assert y > 0 and y < len(self.board)
        assert x >= 0 and x < len(self.board[y])
        return self.board[y-1][x]
        
    def getRight(self,x,y):
        assert y >= 0 and y < len(self.board)
        assert x < len(self.board[y]-1) and x >= 0
        return self.board[y][x+1]
 
    def getLeft(self,x,y):
        assert y >= 0 and y < len(self.board)
        assert x > 0 and x < len(self.board[y]-1)
        return self.board[y][x-1]
    
    def getDown(self,x,y):
        assert y >= 0 and y < len(self.board-1)
        assert x >= 0 and x < len(self.board[y])
        return self.board[y-1][x]
    

# TEST 
    
if __name__ == "__main__" :
    plateau = Board("../benchs/sokoInst01.goal")
    plateau.print_board()
                    