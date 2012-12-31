#!/bin/sh

#  mypoker.py
#  PYPoker
#
#  Created by Charles Dowd on 12/30/12.
#  Copyright (c) 2012 Charles Dowd. All rights reserved.

from mygames import Game


theGame = Game(13, 4)

print "-- start -- (y/n)"
x = raw_input()


print "Let's go..."

while True:
    print "--- Select an option ---"
    print "Deck size: " + str(len(theGame.deck))
    if theGame.numPlayers > 0:
        print "Players:"
        theGame.printPlayerOptions()
        print "--- Select a player ---"
        theGame.printPlayerSelection()

    print "--- Select an option ---"
    print "x - Exit"
    print "p - Add player"
    print "r - Return all cards!"
    print "d - Deal!"


    x = raw_input()
    if x.strip() in "xpdr":
        if x.strip() == 'x':
            break
        if x.strip() == 'p':
            theGame.addPlayer()
        if x.strip() == 'd':
            theGame.dealAll()
        if x.strip() == 'r':
            theGame.returnAll()
    #   Or select player number x
    elif x.strip() in "0123456789":
        theGame.selectPlayer(int(x.strip()))

print "Good bye!"