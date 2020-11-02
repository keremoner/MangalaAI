'''
Board class for the game of TicTacToe.
Default board size is 3x3.
Board data:
  1=white(O), -1=black(X), 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the board for the game of Othello by Eric P. Nichols.

'''
import numpy as np
# from bkcharts.attributes import color
class Board():


    def __init__(self):
        "Set up initial board configuration."
        self.n = 3
        self.pieces = [0,0,0, 0,0,0, 0,0,0]
        


    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.
        
        for i in range(9):
            if self[i] == 0:
                moves.add(i)
        return list(moves)
        
          

    def has_legal_moves(self, color):
        for i in range(9):
            if self[i] == 0:
                return True
        return False

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """
        if color==1:
            #replay stores if the player should act again
            self.pieces[move]=1

        else:
            #replay stores if the player should act again
            self.pieces[move]=-1
                    
    def is_win(self, color):
        """Check whether the given player has collected a triplet in any direction; 
        @param color (1=white,-1=black)
        """
        win = self.n
        newBoard = np.reshape(np.array(self.pieces), (3,3))
        
        # check y-strips
        for y in range(self.n):
            count = 0
            for x in range(self.n):
                if newBoard[x][y]==color:
                    count += 1
            if count==win:
                return True
        # check x-strips
        for x in range(self.n):
            count = 0
            for y in range(self.n):
                if newBoard[x][y]==color:
                    count += 1
            if count==win:
                return True
        # check two diagonal strips
        count = 0
        for d in range(self.n):
            if newBoard[d][d]==color:
                count += 1
        if count==win:
            return True
        count = 0
        for d in range(self.n):
            if newBoard[d][self.n-d-1]==color:
                count += 1
        if count==win:
            return True
        
        return False

