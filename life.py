#!/usr/bin/env python
#
#
# Program name:         life.py
# Written by:           Laurens Houben
# Date:                 20130416
#
# Description:
# The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
# The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
# each of which is in one of two possible states, alive or dead.
# Every cell interacts with its eight neighbours, which are the cells that are
# horizontally, vertically, or diagonally adjacent.
# At each step in time, the following transitions occur:
#
# 1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overcrowding.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#
# The initial pattern constitutes the seed of the system.
# The first generation is created by applying the above rules simultaneously
# to every cell in the seed-births and deaths occur simultaneously,
# and the discrete moment at which this happens is sometimes called a tick
# (in other words, each generation is a pure function of the preceding one).
# The rules continue to be applied repeatedly to create further generations.
#
# Dependencies:
# None

from time import sleep
from modGrid import Grid
from optparse import OptionParser

# blinker()
# toad()
# glider()
# random()
# laurens()

def main():
    parser = OptionParser()
    parser.add_option("-c", "--horizontal", type="int", dest="hcount", metavar="COLS", default=75, help="number of colums (int)")
    parser.add_option("-r", "--vertical", type="int", dest="vcount", metavar="ROWS", default=22, help="number of rows (int)")
    parser.add_option("-t", "--revolutions", type="int", dest="rcount", metavar="REVS", default=43, help="number of revolutions (int)")
#    parser.add_option("-f", "--figure", type="str", dest="figure". metavar="BEACON|BLINKER|TOAD|GLIDER|RANDOM", default="RANDOM", help="type of figure (str)")
    (options, args) = parser.parse_args()
    g = Grid(options.hcount,options.vcount,options.rcount)
    #g.beacon()
    #g.blinker()
    #g.toad()
    #g.glider()
    g.random()
    #g.laurens()
    for i in range(g.returnmaxgenerations()):
        g.clear()
        print "Generation %3i:" % ( i, )
        g.printgrid()
        sleep(0.2)
        g.nextgeneration()

if __name__ == '__main__':
    main()
