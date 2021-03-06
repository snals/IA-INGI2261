'''
Created on Sep 28, 2012

@author: inekar, Florentin Rochet
'''

import WrongDirectionException
import copy

class State:
    """
        This class encapsule a representation of a state of the sliding puzzle.
        This state is a matrix and the representation is a list.
    """
    def __init__(self, state):
        self.state = state
        self.representation = self.make_representation()

    def __hash__(self):
       
        return self.representation
    
    def __eq__(self,other):
        return self.representation == other.representation
     
    def make_representation(self):
        
        """ Horiz == 2
            Vert == 3
            square == 4
            unique == 1
            None == 0"""
        list = []
        for line in self.state:
            list += line
        hashedlist = list[:]
        i = 0
        while i < len(list):
            if list[i] != "0":
                if list.count(list[i]) == 1:
                    hashedlist[i] = 1
                elif list.count(list[i]) == 4:
                    hashedlist[i] = 4
                elif list.count(list[i]) == 2:
                    if i == 0:
                        if list[i] == list[i+1]:
                            hashedlist[i] = 2
                    elif i == 19:
                        if list[i] == list[i-1]:
                            hashedlist[i] = 2
                    else:
                        if list[i] == list[i-1] or list[i] == list[i+1]:
                            hashedlist[i] = 2
                    if i < 4:
                        if list[i] == list[i+4]:
                            hashedlist[i] = 3
                    elif i > 15:
                        if list[i] == list[i-4]:
                            hashedlist[i] = 3
                    else:
                        if list[i] == list[i-4] or list[i] == list[i+4]:
                            hashedlist[i] = 3
            i += 1
            
        result = ""
        for elem in hashedlist:
            result += str(elem)

        return hash(result)
                    
    def move_vertical(self, x, y, direction, i):
        if direction == "north":
            dirmul = -1
            isInBound = x > 1
        elif direction == "south":
            dirmul = 1
            isInBound = x < 3
        else:
            raise WrongDirectionException(x,y,direction,"move_vertical")
        if i == 10:
            if isInBound and self.state[x+dirmul][y] == self.state[x+2*dirmul][y]:
                #Test if the piece is a vertical 2bloc piece
                diff = 2
            else:
                #Il s'agit d'une piece 1*1
                diff = 1
            self.state[x][y], self.state[x+dirmul*diff][y] = \
            self.state[x+dirmul*diff][y], self.state[x][y]
        else:            
            if i == -1:
                mul = -1
            elif i == 1:
                mul = 1
            if isInBound and self.state[x+dirmul][y] == self.state[x+2*dirmul][y] \
            and self.state[x+dirmul][y] == self.state[x+2*dirmul][y+mul]:
                #Case in which it is the square 2*2
                diff = 2
            else:
                #Case in which it is an horizontal 2*1
                diff = 1
            self.state[x][y], self.state[x+dirmul*diff][y] = \
            self.state[x+dirmul*diff][y], self.state[x][y]
            self.state[x][y+mul], self.state[x+dirmul*diff][y+mul] = \
            self.state[x+dirmul*diff][y+mul], self.state[x][y+mul]
            
            
    def move_horizontal(self, x, y, direction, i):
        if direction == "west":
            dirmul = -1
            isInBound = y > 1
        elif direction == "east":
            dirmul = 1
            isInBound = y < 2
        else:
            raise WrongDirectionException(x,y,direction,"move_horizontal")

        if i == 10:
            if isInBound and self.state[x][y+dirmul] == self.state[x][y+2*dirmul]:
                #Test if the piece is a vertical 2bloc piece
                diff = 2
            else:
                #Il s'agit d'une piece 1*1
                diff = 1
            self.state[x][y], self.state[x][y+dirmul*diff] = \
            self.state[x][y+dirmul*diff], self.state[x][y]
        else:            
            if i == -1:
                mul = -1
            elif i == 1:
                mul = 1
            if isInBound and self.state[x][y+dirmul] == self.state[x][y+2*dirmul] \
            and self.state[x][y+dirmul] == self.state[x+mul][y+2*dirmul]:
                #Case in which it is the square 2*2
                diff = 2
            else:
                #Case in which it is an horizontal 2*1
                diff = 1
            self.state[x][y], self.state[x][y+dirmul*diff] = \
            self.state[x][y+dirmul*diff], self.state[x][y]
            self.state[x+mul][y], self.state[x+mul][y+dirmul*diff] = \
            self.state[x+mul][y+dirmul*diff], self.state[x+mul][y]
            
            

    def move(self, x, y, direction):    
        """Return a new  state which represent the move. if the
        move is impossible, move return false"""  
        i = self.is_possible(x, y, direction)
        if i:
            localState = State(copy.deepcopy(self.state))
            if direction == "north" or direction == "south":
                localState.move_vertical(x, y, direction, i)
                return State(copy.deepcopy(localState.state))
            elif direction == "west" or direction == "east":
                localState.move_horizontal(x, y, direction, i)
                return State(copy.deepcopy(localState.state))
            else:
                raise WrongDirectionException(x,y,direction,"in move")
        else:
            return False
 
    
    def is_possible(self, x, y, direction):
        """Return False if the move is impossible, then
        -1 means that the >= 2bloc piece is towards the top or left
        +1 means that the >= 2bloc piece is towards the bottom or right
        10 means that it is a piece with width = 1 in the direction
        Remind : x is vertical coordonate, y is horizontal"""
        if direction == "north" or direction == "south":
            if direction == "north":
                isInBound = x == 0
                dirmul = -1
            elif direction == "south":
                isInBound = x == 4
                dirmul = 1
            if isInBound or self.state[x+dirmul][y] == "0":
                #Il ne peux pas y avoir de piece au dessus d'une case vide 
                #qui est en haut de la grille ou une piece en dessous d'une 
                #case vide en bas de la grille
                return False
            else:
                if y != 0 and self.state[x+dirmul][y] == self.state[x+dirmul][y-1]:
                    #Cas ou c'est une piece de deux (ou quatre) 
                    #en (x-1,{y-1, y})
                    if self.state[x][y-1] == "0":
                        return -1
                    else:
                        return False
                elif y != 3 and self.state[x+dirmul][y] == self.state[x+dirmul][y+1]:
                    #Cas ou c'est une piece de deux (ou quatre) 
                    #en (x-1,{y, y+1})
                    if self.state[x][y+1] == "0":
                        return +1
                    else:
                        return False
                else:
                    #La piece dans ce cas fait seulement 1 de large
                    #(1*1) ou (2*1) vertical
                    return 10
                         
        elif direction == "west" or direction == "east":
            if direction == "west":
                isInBound = y == 0
                dirmul = -1
            elif direction == "east":
                isInBound = y == 3
                dirmul = 1
            if isInBound or self.state[x][y+dirmul] == "0":
                return False
            else:
                if x != 0 and self.state[x][y+dirmul] == self.state[x-1][y+dirmul]:
                    #Cas ou c'est une piece de deux (ou quatre) 
                    #en ({x-1, x}, y+1)
                    if self.state[x-1][y] == "0":
                        return -1
                    else:
                        return False
                elif x != 4 and self.state[x][y+dirmul] == self.state[x+1][y+dirmul]:
                    #Cas ou c'est une piece de deux (ou quatre) 
                    #en ({x, x+1}, y+1)
                    if self.state[x+1][y] == "0":
                        return +1
                    else:
                        return False
                else:
                    #La piece dans ce cas fait seulement 1 de large
                    #(1*1) ou (2*1) vertical
                    return 10
        
        else:
            #Mauvaise direction entrée.
            raise WrongDirectionException(x,y,direction,"in is_possible")
    
    #
    # GETTERS AND SETTERS
    #
    
    def _get_state(self):
        return self._state
    
    def _set_state(self,state):
        self._state = state
        

    state = property(_get_state,_set_state)
    
