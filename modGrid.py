import random
from os import system
from collections import defaultdict

# default values
celltable = defaultdict(int, {
                       (1, 2): 1,
                       (1, 3): 1,
                       (0, 3): 1,
                       } ) # Only need to populate with the keys leading to life
cellcount = ''
cell0 = ''
cell1 = ''
nextgeneration = ''
maxgenerations = 1
printdead = '.'
printlive = 'o'
universe = ''

class Grid(object):
    def __init__(self, hcount, vcount, maxgen):
        global cellcount
        global maxgenerations
        global cell0
        global cell1
        cellcount = hcount,vcount
        cell0 = int(cellcount[0])
        cell1 = int(cellcount[1])
        maxgenerations = maxgen

    def returnmaxgenerations(self):
        return maxgenerations

    def printgrid(self):
        for row in range(cellcount[1]):
            print "  ", ''.join(str(universe[(row,col)])
            for col in range(cellcount[0])).replace(
                '0', printdead).replace('1', printlive)

    def nextgeneration(self):
        global nextgeneration
        global celltable
        global universe
        nextgeneration = defaultdict(int)
        for row in range(cellcount[1]):
            for col in range(cellcount[0]): 
                nextgeneration[(row,col)] = celltable[
                    ( universe[(row,col)],
                      -universe[(row,col)] + sum(universe[(r,c)]
                                                 for r in range(row-1,row+2)
                                                 for c in range(col-1, col+2) )
                    ) ]
        universe = nextgeneration

    # Start States
    def beacon(self):
        global universe
        u = universe = defaultdict(int)
        u[(cell1/2-2,cell0/2-2)], u[(cell1/2-2,cell0/2-1,)] = 1,1
        u[(cell1/2-1,cell0/2-2)] = 1
        u[(cell1/2,cell0/2+1)] = 1
        u[(cell1/2+1,cell0/2)], u[(cell1/2+1,cell0/2+1)] = 1,1

    def blinker(self):
        global universe
        u = universe = defaultdict(int)
        u[(cell1/2,cell0/2-1)], u[(cell1/2,cell0/2)], u[(cell1/2,cell0/2+1)] = 1,1,1

    def toad(self):
        global universe
        u = universe = defaultdict(int)
        u[(cell1/2,cell0/2-1)], u[(cell1/2,cell0/2)], u[(cell1/2,cell0/2+1)] = 1,1,1
        u[(cell1/2-1,cell0/2-2)], u[(cell1/2-1,cell0/2-1)], u[(cell1/2-1,cell0/2)] = 1,1,1

    def laurens(self):
        global universe
        u = universe = defaultdict(int)
        u[(cell1/2,cell0/2-1)], u[(cell1/2,cell0/2)], u[(cell1/2,cell0/2+1)] = 1,1,1
        u[(cell1/2-1,cell0/2+1)], u[(cell1/2-1,cell0/2+2)], u[(cell1/2-1,cell0/2+3)] = 1,1,1


    def glider(self):
        global maxgenerations
        global universe
        u = universe = defaultdict(int)
        maxgenerations = cell1*2+1
        u[(cell1/2,cell0/2-1)], u[(cell1/2,cell0/2)], u[(cell1/2,cell0/2+1)] = 1,1,1
        u[(cell1/2+1,cell0/2-1)] = 1
        u[(cell1/2+2,cell0/2)] = 1

    def random(self):
        global universe
        universe = defaultdict(int,
        # array of random start values
        ( ((row, col), random.choice((0,1)))
            for col in range(cellcount[0])
            for row in range(cellcount[1])
        ) ) # returns 0 for out of bounds

    def clear(self):
        system('clear')
