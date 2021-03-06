#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Debroux Léonard - Rochet Florentin
'''
import random

from sarena import *
import minimax
import time


class AlphaBetaPlayer(Player, minimax.Game):

    """Sarena Player.

    A state is a tuple (b, p) where p is the player to make a move and b
    the board.

    """
#    count = 0
#    depthCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    
    def successors(self, state):
        board, player = state 
        for action in board.get_actions():
            yield (action,(board.clone().play_action(action), -player))
    
    def cutoff(self, state, depth):
        board, player = state
#        return board.is_finished()
        if board.is_finished():
            return True
        elif depth == 2:
            return True
#        self.depthCount[depth] += 1
#        self.count += 1

#        if self.count % 1000000 == 0:
#            print("% noeud totaux", self.count)
#            print("% par depth", self.depthCount)
#            print("% secondes", time.time()-self.start)
        board, player = state
        return board.is_finished()

    def evaluate(self, state):
        board, player = state
        return board.get_score()
    
    def play(self, percepts, step, time_left):
        if step % 2 == 0:
            player = -1
        else:
            player = 1
#        start = time.time()
        state = (Board(percepts), player)
        m = minimax.search(state, self)

#        print("nombre de noeuds explorés : ", self.count)
#        print("nombre de noeuds explorés par depth : ", self.depthCount)
#        self.count = 0
#        depthCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#        print("temps elapsed : ", format(time.time()-start))
        return m


if __name__ == "__main__":
    player_main(AlphaBetaPlayer())
