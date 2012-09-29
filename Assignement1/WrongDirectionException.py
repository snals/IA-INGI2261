'''
Created on 29 sept. 2012

@author: Florentin
'''
class WrongDirectionException(Exception):
    """
        This class handle wrong move on the board
        
    """
    def __init__(self,x,y,direction):
        Exception.__init__(self)
        self.x = x
        self.y = y
        self.direction = direction
        
    def __str__(self):
        return "Direction :"+self.direction+", x :"+self.x+", y :"+self.y