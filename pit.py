import Arena
from MCTS import MCTS
from mangala.MangalaGame import MangalaGame
from mangala.MangalaPlayers import *
from mangala.pytorch.NNet import NNetWrapper as NNet
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""


g = MangalaGame()

# all players
rp = RandomPlayer(g).play
gp = GreedyMangalaPlayer(g).play
hp = HumanMangalaPlayer(g).play


iterateAll = True;

#set player2
player2 = rp
gameNum = 2

if iterateAll:

    winrates = []
    for file in os.listdir('./temp/'):
        if file.endswith(".pth.tar") and not(file == "temp.pth.tar" or file == "best.pth.tar"):
          
            n1 = NNet(g)
            n1.load_checkpoint('./temp/', file)
            args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
            mcts1 = MCTS(g, n1, args1)
            n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
            arena = Arena.Arena(n1p, player2, g, display=MangalaGame.display)
            onewon, twowon, draws = arena.playGames(gameNum, verbose=False)
            winrates.append(onewon/gameNum)
    t = range(1, len(winrates)+1)
    print(winrates)
    fig, ax = plt.subplots()
    ax.plot(t, winrates)

    ax.set(xlabel='Iteration', ylabel='Win Rate (Win Num/Total)',
    title='Iteration vs Win Rate')
    ax.grid()

    fig.savefig("test.png")
    plt.show()
    

else:
    n1 = NNet(g)
    n1.load_checkpoint('./temp/','best.pth.tar')
    args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
    mcts1 = MCTS(g, n1, args1)
    n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
    arena = Arena.Arena(n1p, player2, g, display=MangalaGame.display)
    print(arena.playGames(gameNum, verbose=True))
    
    



