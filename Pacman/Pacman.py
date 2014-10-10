#!/usr/bin/env python
import random

class Trial(object):
    def __init__(self):
        self.coins = 0
        self.hcoins = 0
        self.score = 0
        self.board = []
        for i in xrange(15): 
            row = []
            for j in xrange(35):
                row.append(Point(i, j, "."))
            self.board.append(row)
    def pboard(self):
        print chr(27) +"[2J"
        for i in self.board:
            for j in i:
                print j,
            print '\n'
    def Score(self):
        self.hcoins += 1
        self.score += 1
    def wall(self):
        a = random.randint(0, 14)
        b = random.randint(0, 34)
        c = random.randint(0, 34)
        d = random.randint(0, 14)
        e = random.randint(0, 1)
        if e is 0:
            for i in self.board[a]: 	#range(min(a,d),max(a,d))) and (Point.y is b) :
                if self.board[a].index(i) < max(b, c) and self.board[a].index(i) > min(b, c):
                    i.val = 'X'
        else:
            for i in self.board:		#(Point.y in range(min(b,c),max(b,c))) and (Point.x is a) :
                if self.board.index(i) < max(a, d) and self.board.index(i) > min(a, d):
                    i[b].val = 'X'
    def coin(self):
        a = random.randint(0, 14)
        b = random.randint(0, 34)
        c = random.randint(0, 34)
        d = random.randint(0, 14)
        e = random.randint(0, 1)
        if e is 1:
            for i in self.board[a]: #range(min(a,d),max(a,d))) and (Point.y is b) :
                if self.board[a].index(i) < max(b, c) and self.board[a].index(i) > min(b, c):
                    i.val = 'C'
                    self.coins += 1
        else:
            for i in self.board:#(Point.y in range(min(b,c),max(b,c))) and (Point.x is a) :
                if self.board.index(i) < max(a, d) and self.board.index(i) > min(a, d):
                    i[b].val = 'C'
                    self.coins += 1
    def checkGhost(self, pac, ghost):
        if pac.position == ghost.position:
            return True
        return False
    def Start(self):
        for i in xrange(15):
            for j in xrange(35):
                self.board[i][j].val = '.'
        self.wall()
        self.wall()
        self.coin()
        pacman = Person('P')
        ghost = Person('G')
        self.board[pacman.x][pacman.y].val = pacman.val
        self.board[ghost.x][ghost.y].val = ghost.val
        self.pboard()
        while 1:
            inp = raw_input("Enter your move: ")#sys.stdin.read(1)
            if inp == 'q':
                print "Score : ", self.score
                break
            pacman.move(inp, self)
            arr = ['w', 'a', 's', 'd']
            ghost.move(arr[random.randint(0, 3 )], self)
            if self.checkGhost(pacman, ghost):
                print "Score : ", self.score
                print "Game Over !"
                break
            self.pboard()
            print "Score : ", self.score
            if self.hcoins == self.coins:
                self.Start()
                return



class Point(object):
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
    def __str__(self):
        return self.val
    def setter(self, p):
        self.val = p
class Person(Point):
    def __init__(self, tp):
        self.x = random.randint(0, 14)
        self.y = random.randint(0, 34)
        self.position = [self.x, self.y]
        self.val = tp
        print "Person Initiated", self.x, self.y, self.val
    def checkMove(self, obj, mv):
        pos = self.position
#-------------------check Wall------------------------
        if pos[0] is not 14 and obj.board[pos[0]+1][pos[1]].val is 'X' and mv is 's':
            return True
        if pos[0] is not 0 and obj.board[pos[0]-1][pos[1]].val is 'X' and mv is 'w':
            return True
        if pos[1] is not 0 and obj.board[pos[0]][pos[1]-1].val is 'X' and mv is 'a':
            return True
        if pos[1] is not 34 and obj.board[pos[0]][pos[1]+1].val is 'X' and mv is 'd':
            return True
#-------------if no wall then check edge---------------------
        if (pos[0] == 14 and mv is 's') or (pos[0] == 0 and mv is 'w') or (pos[1] == 34 and mv is 'd') or (pos[1] == 0 and mv is 'a'):
            return True
        return False
    def move(self, mv, obj):
        if not self.checkMove(obj, mv):
            pos = self.position
            tp = self.val
            if tp == 'G' and obj.board[pos[0]][pos[1]].val != 'P':
                obj.board[pos[0]][pos[1]].val = '.'
            elif tp == 'P':
                obj.board[pos[0]][pos[1]].val = '.'
            if mv is 'w':
                self.x = self.x-1
            elif mv is 's':
                self.x = self.x+1
            elif mv is 'a':
                self.y = self.y-1
            elif mv is 'd':
                self.y = self.y+1
            self.position = [self.x, self.y]
            pos = self.position
            if obj.board[pos[0]][pos[1]].val is 'C' and tp == 'P':
                obj.Score()
            elif obj.board[pos[0]][pos[1]].val is 'C' and tp == 'G':
                obj.coins -= 1
            obj.board[pos[0]][pos[1]].val = tp


if __name__ == "__main__":
    obj = Trial()
    obj.Start()
