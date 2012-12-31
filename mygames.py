#!/bin/sh

#  mygames.py
#  PYPoker
#
#  Created by Charles Dowd on 12/30/12.
#  Copyright (c) 2012 Charles Dowd. All rights reserved.



#card
#suit
#rank
#value

import random
# ranks = ["A", "2","3","4","5","6","7","8","9","T","J","Q","K"]
# suits = ["C","D","H","S"]
# longRanks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# longSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]


class Card:
    
    def __init__(self, theGame, rankID, suitID):
        self.game = theGame
        self.suitID = suitID
        self.rankID = rankID
        self.suit = self.game.suits[suitID-1]
        self.rank = self.game.ranks[rankID-1]
        self.shortName = self.rank + "" + self.suit
        self.longName = self.game.longRanks[rankID-1] + " of " + self.game.longSuits[suitID-1]
    
    def printCard(self):
        print "|" + self.shortName + "|" + " (" + self.longName +")"


class Hand:

    def __init__(self, theGame, numCards):
        self.game = theGame
        self.numCards = numCards
        self.hand = []
        self.numOfCardsDealt = 0
        self.deck = self.game.deck

    def dealOneCard(self, deck):
        self.deck = deck
        if self.numOfCardsDealt < self.numCards:
            self.pickedCard = random.choice(self.deck)
            self.deck.remove(self.pickedCard)
            self.hand.append(self.pickedCard)
            self.numOfCardsDealt = self.numOfCardsDealt + 1

    def dealHand(self, deck):
        self.deck = deck
        if self.numOfCardsDealt < self.numCards:
            for index in range(0, self.numCards):
                self.dealOneCard(deck)
        print len(deck)

    def printHand(self):
        for index in range(0, self.numOfCardsDealt):
            self.hand[index].printCard()

    def returnCardsToDeck(self):
        for index in range(0, self.numCards):
            self.deck.append(Card(self.game, self.hand[index].rankID, self.hand[index].suitID))
            self.numOfCardsDealt = self.numOfCardsDealt - 1
        self.hand = []

    def __len__(self):
        return self.numOfCardsDealt




class Player:
    def __init__(self, theGame, handle):
        self.handle = handle
        self.game = theGame
        self.hand = Hand(self.game, self.game.numCards)

    def returnCardsToDeck(self):
        if len(self.hand) > 0:
            self.hand.returnCardsToDeck()

    def printPlayer(self):
        print self.handle
        self.hand.printHand()

    def deal(self):
        self.hand.dealHand(self.game.deck)

    def returnAll(self):
        self.returnCardsToDeck()



class Game:
    def __init__(self, numCards, maxPlayers):
        self.ranks = ["A", "2","3","4","5","6","7","8","9","T","J","Q","K"]
        self.suits = ["C","D","H","S"]
        self.longRanks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.longSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.maxPlayers = maxPlayers
        self.numPlayers = 0
        self.numRanks = len(self.ranks)
        self.numSuits = len(self.suits)
        self.players = []
        self.numCards = numCards
        self.deck = []
        self.selectedPlayers = []
        for rank in range(1,14):
            for suit in range(1,5):
                self.deck.append(Card(self, rank, suit))

    def addPlayer(self):
        if self.numPlayers < self.maxPlayers:
            gamerHandle = raw_input("Enter a gamer handle:")
            self.players.append(Player(self, gamerHandle))
            self.players[self.numPlayers].printPlayer()
#		self.players[self.numPlayers].startHand()
            self.numPlayers = self.numPlayers + 1

        #    def createDeck(self):
        # self.deck = DeckOfCards(self)

    def dealAll(self):
        for index in range(self.numPlayers):
            self.players[index].deal()

    def printPlayers(self):
        for index in range(self.numPlayers):
            self.players[index].printPlayer()

    def printPlayerOptions(self):
        for index in range(self.numPlayers):
            print str(index) + " - " + self.players[index].handle
            self.players[index].printPlayer()

    def returnAll(self):
        for index in range(self.numPlayers):
            self.players[index].returnAll()

    def isSelected(self, aPlayer):
        retBool = 0
        if aPlayer in self.selectedPlayers:
            retBool = 1
        return retBool

    def printPlayerSelection(self):
        for index in range(self.numPlayers):
            print str(index) + " - " + self.players[index].handle + ": " + str(self.isSelected(self.players[index]))

    def selectPlayer(self, code):
        retPlayer = None
        if self.numPlayers > 0 and int(code) < self.numPlayers:
            self.selectedPlayers.append(self.players[int(code)])
            retPlayer = self.players[int(code)]
        return retPlayer


