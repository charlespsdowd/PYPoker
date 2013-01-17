#!/bin/sh

#  tictactoe.py
#  PYPoker
#
#  Created by Charles Dowd on 12/31/12.
#  Copyright (c) 2012 Charles Dowd. All rights reserved.


class CPDTicTacToe:

    def __init__(self):
        self.grid = []
        self.startMark = 'X'
        self.nextMark = 'O'
        self.currMark = self.startMark
        self.xCount = 0
        self.oCount = 0
        self.xwins = 0
        self.owins = 0

    
    def resetWins(self):
        self.owins = self.xwins = 0
        self.currMark = self.startMark
    
    def saveWin(self, winnerMark):
        if winnerMark == 'X':
            self.xwins = self.xwins + 1
        if winnerMark == 'O':
            self.owins = self.owins + 1
        self.currMark = self.startMark

    
    def createGrid(self):
        self.grid = []
        for i in range(0, 9):
            self.grid.append(0)
        self.currMark = self.startMark


    def reset(self):
        self.createGrid()

    def checkWinner(self):
        
        self.oCount = self.xCount = 0
        # check horizontals
        for i in range(0, 3):
            self.oCount = self.xCount = 0
            for j in range(0, 3):
                if self.grid[3*i+j] != 0:
                    if self.grid[3*i+j] == 'X':
                        self.xCount = self.xCount + 1
                    if self.grid[3*i+j] == 'O':
                        self.oCount = self.oCount + 1
            if self.xCount == 3:
                return 'X'
            if self.oCount == 3:
                return 'O'

        # check verticals
        for i in range(0, 3):
            self.oCount = self.xCount = 0
            for j in range(0, 3):
                if self.grid[i+3*j] != 0:
                    if self.grid[i+3*j] == 'X':
                        self.xCount = self.xCount + 1
                    if self.grid[i+3*j] == 'O':
                        self.oCount = self.oCount + 1
                if self.xCount == 3:
                    return 'X'
                if self.oCount == 3:
                    return 'O'

        # check diagonals
        self.oCount = self.xCount = 0

        for i in range(0,3):
            if self.grid[4*i] != 0:
                if self.grid[4*i] == 'X':
                    self.xCount = self.xCount + 1
                if self.grid[4*i] == 'O':
                    self.oCount = self.oCount + 1
        if self.xCount == 3:
            return 'X'
        if self.oCount == 3:
            return 'O'

        # check diagonals
        self.oCount = self.xCount = 0

        for i in range(1,4):
            if self.grid[2*i] != 0:
                if self.grid[2*i] == 'X':
                    self.xCount = self.xCount + 1
                if self.grid[2*i] == 'O':
                    self.oCount = self.oCount + 1
        if self.xCount == 3:
            return 'X'
        if self.oCount == 3:
            return 'O'
        
        return 0

    def displayGrid(self):
        self.line = ""
        k = 1
        for i in range(0, 3):
            self.line = self.line + " "
            for j in range(0, 3):
                if self.grid[k-1] == 0:
                    self.line = self.line + str(k)
                else:
                    self.line = self.line + self.grid[k-1]
                    if self.grid[k-1] == 'X':
                        self.xCount = self.xCount + 1
                    if self.grid[k-1] == 'O':
                        self.oCount = self.oCount + 1
                if j < 2:
                    self.line = self.line + " | "
                k = k + 1
            print self.line
            self.line = ""

    def playMark(self, gridspot):
        mark = self.currMark
        if self.grid[int(gridspot-1)] == 0:
            self.grid[int(gridspot-1)] = mark
            if mark == self.startMark:
                self.currMark = self.nextMark
            if mark == self.nextMark:
                self.currMark = self.startMark

    def isGameOver(self):
        if self.checkWinner():
            return 1
        fOver = 1
        for i in range(0,9):
            if self.grid[i] == 0:
                fOver = 0
        return fOver





