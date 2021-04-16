# -*- coding: utf-8 -*-
"""easyAI_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17n_WGpr5EqpkeDQC7iOgTDMDw30sUNSr
"""

!pip install easyAI

from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player

class TicTacToe( TwoPlayersGame ):
  
    def __init__(self, players):
        self.players = players
        self.grid = int(input("Choisir votre grille : 3(3x3), 5(5x5) ou 7(7x7): "))
        self.board = [0 for i in range(self.grid * self.grid)]
        self.nplayer = 1 # player 1 starts.
    
    def possible_moves(self):
        return [i+1 for i,e in enumerate(self.board) if e==0]
    
    def make_move(self, move):
        self.board[int(move)-1] = self.nplayer

    def unmake_move(self, move): # optional method (speeds up the AI)
        self.board[int(move)-1] = 0
    
    def lose(self):
        win_state = []
        if self.grid == 3:
            """ Has the opponent "three in line ?" """
            is_win =  any( [all([(self.board[c-1]== self.nopponent)
                          for c in line])
                          for line in [[1,2,3],[4,5,6],[7,8,9], # horiz.
                                       [1,4,7],[2,5,8],[3,6,9], # vertical
                                       [1,5,9],[3,5,7]]]) # diagonal
            if is_win:
              print('here')               
              if self.nplayer == 1:
                print('IA a gagné')
              elif self.nplayer == 2:
                print('Humain a gagné')


            return is_win

        if self.grid == 5:
            """ Has the opponent "five in line ?" """
            is_win =  any( [all([(self.board[c-1]== self.nopponent)
                          for c in line])
                          for line in [[1,2,3,4],[2,3,4,5],[1,6,11,16],
                                       [6,11,16,21],[6,7,8,9],[7,8,9,10],
                                       [11,12,13,14],[12,13,1,15],[16,17,18,19],
                                       [17,18,19,20], [21,22,23,24], [22,23,24,25],
                                       [2,7,12,17],[7,12,17,22],[3,8,13,18],[8,13,18,23],
                                       [4,9,14,19],[9,14,19,24],[5,10,15,20],[10,15,20,25],
                                       [2,8,14,20],[7,13,19,25],[6,12,18,24],[1,7,13,19],
                                       [16,12,8,4],[21,17,13,9],[17,13,9,5],
                                       [22,18,14,10]
                                      ]])
            if is_win:
              print('here')               
              if self.nplayer == 1:
                print('IA a gagné')
              elif self.nplayer == 2:
                print('Humain a gagné') 

            return is_win
        
    def is_over(self):
        is_over = (self.possible_moves() == []) or self.lose()

        #if is_over == True:
          #print(self.nplayer)

        return is_over
        
    def show(self):
        print ('\n'+'\n'.join([
                        ' '.join([['.','O','X'][self.board[self.grid*j+i]]
                        for i in range(self.grid)])
                 for j in range(self.grid)]) )
                 
    def scoring(self):
        return -100 if self.lose() else 0

if __name__ == "__main__":
    
    from easyAI import AI_Player, Negamax
    ai_algo = Negamax(1)
    TicTacToe( [Human_Player(),AI_Player(ai_algo)]).play()