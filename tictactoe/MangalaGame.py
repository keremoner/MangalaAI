from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .MangalaLogic import Board
import numpy as np

"""
Game class implementation for the game of TicTacToe.
Based on the OthelloGame then getGameEnded() was adapted to new rules.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the OthelloGame by Surag Nair.
"""
class MangalaGame(Game):
    def __init__(self):
        pass
        

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board()
        return np.array(b.pieces)

    def getBoardSize(self):
        # hole number
        return (7,2)

    def getActionSize(self):
        # return number of actions
        return 6

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        
        b = Board()
        b.pieces = np.copy(board)
        move = action
        replay = b.execute_move(move, player)
        if replay:
            return (b.pieces, player)
        else:   
            return (b.pieces, -player)

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
    
    def getScore(self, board, player):
        if player==1:
            return (board[6]-board[13])
        else:
            return (board[13]-board[6])

        
    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board()
        b.pieces = np.copy(board)
       
        if not b.has_legal_moves(player) and not b.has_legal_moves(-player):
            #player wins
            if b[6]>b[13]:
                return 1
            #player loses
            elif b[6]<b[13]:
                return -1
            #tie, very little reward for draw
            else:
                return 1e-4
        else:
            return 0
              

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1

        b = Board()
        b.pieces = np.copy(board)
        if player == 1:
            return b.pieces
        
        for i in range(7):
            temp = b[i]
            b.pieces[i] = b[i+7]
            b.pieces[i+7] = temp
        return b.pieces


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
        n = board.shape[0]
        print(board[13], end = "| ")
        for i in range(12,6,-1):
            print(board[i], end = " ")
        print("\n   ", end="")
        for i in range(6):
            print(board[i], end = " ")
        print(" |", board[6])
