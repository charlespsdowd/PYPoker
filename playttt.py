#!/bin/sh

#  playttt.py
#  PYPoker
#
#  Created by Charles Dowd on 12/31/12.
#  Copyright (c) 2012 Charles Dowd. All rights reserved.

from tictactoe import CPDTicTacToe


theGame = CPDTicTacToe()
theGame.createGrid()
theGame.resetWins()

print "Do you want to play a game? (y/n)"
x = raw_input()


print "Let's go..."

while True:
    print "--- Select an option ---"
    print "Scores:"
    print "X: " + str(theGame.xwins)
    print "O: " + str(theGame.owins)
    print "x - Exit"
    print "c - Concede"
    print "r - Reset wins"
 
    theGame.displayGrid()

    if theGame.isGameOver():
        print "*********** Game Over!!!! *************"
        if theGame.checkWinner() != 0:
            winnerMark = str(theGame.checkWinner())
            theGame.saveWin(winnerMark)
            print "*********** Winner: " + winnerMark + " ***************cd..**"
        else:
            print "----------- It's a draw! --------------"
        theGame.reset()
    #        theGame.displayGrid()
        continue

    x = raw_input()
    if x.strip() in "xcr":
        if x.strip() == 'x':
            break
        if x.strip() == 'c':
            theGame.reset()
            #            theGame.displayGrid()
            continue
        if x.strip() == 'r':
            theGame.resetWins()
            continue

    #   Or select player number x
    elif x.strip() in "123456789":
        theGame.playMark(int(x.strip()))


# print "Winner: " + str(theGame.checkWinner())

print "Good bye!"