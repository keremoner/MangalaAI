from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .tictactoeLogic import Board
import numpy as np

"""
Game class implementation for the game of TicTacToe.
Based on the OthelloGame then getGameEnded() was adapted to new rules.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the OthelloGame by Surag Nair.
"""
class tictactoeGame(Game):
    def __init__(self):
        pass
        

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board()
        return np.array(b.pieces)

    def getBoardSize(self):
        # hole number
        return (3,3)

    def getActionSize(self):
        # return number of actions
        return 9

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        
        b = Board()
        b.pieces = np.copy(board)
        move = action
        b.execute_move(move, player)
        return b.pieces, -player

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board()
        b.pieces = np.copy(board)
        legalMoves =  b.get_legal_moves(player)
        #print(legalMoves)
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for i in legalMoves:
            valids[i] = 1
        return np.array(valids)
        
    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board()
        b.pieces = np.copy(board)
        if b.is_win(player):
            return 1
        if b.is_win(-player):
            return -1
        if b.has_legal_moves(player):
            return 0
        # draw has a very little value 
        return 1e-4
              

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1

        b = Board()
        b.pieces = np.copy(board)
        return player*b.pieces


    def getSymmetries(self, board, pi):
        # mirror, rotational
        assert(len(pi) == self.n**2+1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return np.array(board).tostring()

    @staticmethod
    def display(board):
        newBoard = np.reshape(board, (3,3))
        for row in newBoard:
            for i in row:
                if i == 0:
                    print("_", end = " ")
                elif i==1:
                    print("X", end = " ")
                elif i==-1:
                    print("O", end = " ")
            print("\n", end = "")
            
