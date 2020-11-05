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

# from bkcharts.attributes import color
class Board():


    def __init__(self):
        "Set up initial board configuration."
        
        self.pieces = [4,4,4,4,4,4, 0, 4,4,4,4,4,4, 0]
        


    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.
        if color==1:        
            for i in range(6):
                if self[i] != 0:
                    moves.add(i)
        else:
            for i in range(7,13):
                if self[i] != 0:
                    moves.add(i)
        return list(moves)
        
          

    def has_legal_moves(self, color):
        if color == 1:
            for i in range(6):                
                if self[i] != 0:
                    return True
            return False
        else:
            for i in range(7,13):
                if self[i] != 0:
                    return True
            return False
        

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """
        if color==1:
            #replay stores if the player should act again
            replay = False

            #if there is one stone
            if self[move] == 1:
                #increase the next hole by one and make the initial hole 0
                self.pieces[move] = 0
                self.pieces[move+1] += 1

                """if the next hole is not the score hole and the number of stones in the next hole was 0,
                take all stones from opposite hole and put the stone in the next hole to score hole
                """
                if (move+1) != 6 and self[move+1] == 1 and self.pieces[11-move]!=0:
                    self.pieces[6] += self[11-move] + 1
                    self.pieces[11-move] = 0
                    self.pieces[move+1] = 0
                elif (move+1) == 6:
                    replay = True

            #if there is more than one stone in the hole
            elif self[move] > 1:
                k = self[move]
                self.pieces[move] = 0
                final = (move+k-1)%14
                

                #put 1 stone in each hole going counter clockwise until the stones in the initial hole are finished
                m = 0
                for i in range(k):
                    if (move+m)%14==13:
                        m+=1
                    self.pieces[(move+m)%14] +=1
                    m+=1
                        

                #if final hole had 0 stones, take stones from opposite hole and put the stone in final hole to score hole
                if final >= 0 and final <= 5 and self[final] == 1 and self.pieces[12-final]!=0:
                    self.pieces[6] += self[12-final] + 1
                    self.pieces[12-final] = 0
                    self.pieces[final] = 0

                #if final hole is score hole, set replay to true which means player should play again
                elif final == 6:
                    replay = True

                elif final >= 7 and final <=12 and self[final]%2 == 0:
                    """if final hole was opponent's hole and it became an even number after you distribute stones
                    take all stones from the final hole
                    """
                    self.pieces[6] += self[final]
                    self.pieces[final] = 0


        else:
            #replay stores if the player should act again
            replay = False
            move = move + 7
            #if there is one stone
            if self[move] == 1:
                #increase the next hole by one and make the initial hole 0
                self.pieces[move] = 0
                self.pieces[move+1] += 1

                """if the next hole is not the score hole and the number of stones in the next hole was 0,
                take all stones from opposite hole and put the stone in the next hole to score hole
                """
                if (move+1) != 13 and self[move+1] == 1 and self.pieces[11-move]!=0:
                    self.pieces[13] += self[11-move] + 1
                    self.pieces[11-move] = 0
                    self.pieces[move+1] = 0
                elif (move+1) == 13:
                    replay = True

            #if there is more than one stone in the hole
            elif self[move] > 1:
                k = self[move]
                self.pieces[move] = 0
                final = (move+k-1)%14

                m = 0
                #put 1 stone in each hole going counter clockwise until the stones in the initial hole are finished
                for i in range(k):
                    if (move+m)%14==6:
                        m+=1
                    self.pieces[(move+m)%14] +=1
                    m+=1

                #if final hole had 0 stones, take stones from opposite hole and put the stone in final hole to score hole
                if final >= 7 and final <= 12 and self[final] == 1 and self.pieces[12-final]!=0:
                    self.pieces[13] += self[12-final] + 1
                    self.pieces[12-final] = 0
                    self.pieces[final] = 0

                #if final hole is score hole, set replay to true which means player should play again
                elif final == 13:
                    replay = True

                elif final >= 0 and final <=5 and self[final]%2 == 0:
                    """if final hole was opponent's hole and it became an even number after you distribute stones
                    take all stones from the final hole
                    """
                    self.pieces[13] += self[final]
                    self.pieces[final] = 0

        
        if not self.has_legal_moves(color):
            if color == 1:
                for i in range(7,13):
                    self.pieces[6]+=self.pieces[i]
                    self.pieces[i] = 0
            else:
                for i in range(0,6):
                    self.pieces[13]+=self.pieces[i]
                    self.pieces[i] = 0
            replay = False
        
        return replay
                    
                

