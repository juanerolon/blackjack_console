#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Juan E. Rolon
https://github.com/juanerolon
"""

import random

   
class Deck:
    """
    Defines a 52-card playing deck for use in card games like Blackjack.
    Contains methods creating the deck representation, how cards are drawn
    and randomly shuffled.
    """
    
    def __init__(self):
        """
        Initializes private attributes:
        cardIndex: a list of integers representing each element on the deck.
        The list of integers get randomly shuffled upon calls to shuffle method.
        counter: counts the cards being drawn.
        drawnCards: a list that stores the cards being drawn.
        cards: a dictionary whose keys are integers and values are 3-element lists
        representing a card.
        """
    
        self.__cardIndex = []
        self.__counter = 0
        self.__drawnCards = []
        self.__cards = {}
        
        self.__n=0
        
        #this creates only a set of 52 integer indexes stored in a list
        while self.__n < 52:
            self.__cardIndex.append(self.__n+1)
            self.__n+=1
        
        #shuffle the index list
        random.shuffle(self.__cardIndex)
        
        self.create_deck()

    def create_deck(self):
        """
        Creates each one of the key-value pairs of the cards dictionary.
        Keys are integers and values are the list representation of cards.
        card[n] = ["Short name (str value)", "Description suit symbol", Numeric value]
        Note: the description of each card contains a unicode symbol that
        yields the symbol for each suit (Tested on Unix and OS X)
        :return: None
        """
      
        self.__cards[1] = ["Ace", u"Ace of Clubs \u2667", 11]
        self.__cards[2] = ["2", u"Two of Clubs  \u2667",2]
        self.__cards[3] = ["3", u"Three of Clubs \u2667",3]
        self.__cards[4] = ["4", u"Four of Clubs \u2667",4]
        self.__cards[5] = ["5", u"Five of Clubs \u2667",5]
        self.__cards[6] = ["6", u"Six of Clubs \u2667",6]
        self.__cards[7] = ["7", u"Seven of Clubs \u2667",7]
        self.__cards[8] = ["8", u"Eight of Clubs \u2667",8]
        self.__cards[9] = ["9", u"Nine of Clubs \u2667",9]
        self.__cards[10] = ["10", u"Ten of Clubs \u2667",10]
        self.__cards[11] = ["Jack", u"Jack of Clubs \u2667",10]
        self.__cards[12] = ["King", u"King of Clubs \u2667",10]
        self.__cards[13] = ["Queen", u"Queen of Clubs \u2667",10]
        
        #diamonds
        
        self.__cards[14] = ["Ace", u"Ace of Diamonds \u2662", 11]
        self.__cards[15] = ["2", u"Two of Diamonds \u2662",2]
        self.__cards[16] = ["3", u"Three of Diamonds \u2662",3]
        self.__cards[17] = ["4", u"Four of Diamonds \u2662",4]
        self.__cards[18] = ["5", u"Five of Diamonds \u2662",5]
        self.__cards[19] = ["6", u"Six of Diamonds \u2662",6]
        self.__cards[20] = ["7", u"Seven of Diamonds \u2662",7]
        self.__cards[21] = ["8", u"Eight of Diamonds \u2662",8]
        self.__cards[22] = ["9", u"Nine of Diamonds \u2662",9]
        self.__cards[23] = ["10", u"Ten of Diamonds \u2662",10]
        self.__cards[24] = ["Jack", u"Jack of Diamonds \u2662",10]
        self.__cards[25] = ["King", u"King of Diamonds \u2662",10]
        self.__cards[26] = ["Queen", u"Queen of Diamonds \u2662",10]
        
        
        #hearts
        
        self.__cards[27] = ["Ace", u"Ace of Hearts \u2661", 11]
        self.__cards[28] = ["2", u"Two of Hearts \u2661",2]
        self.__cards[29] = ["3", u"Three of Hearts \u2661",3]
        self.__cards[30] = ["4", u"Four of Hearts \u2661",4]
        self.__cards[31] = ["5", u"Five of Hearts \u2661",5]
        self.__cards[32] = ["6", u"Six of Hearts \u2661",6]
        self.__cards[33] = ["7", u"Seven of Hearts \u2661",7]
        self.__cards[34] = ["8", u"Eight of Hearts \u2661",8]
        self.__cards[35] = ["9", u"Nine of Hearts \u2661",9]
        self.__cards[36] = ["10", u"Ten of Hearts \u2661",10]
        self.__cards[37] = ["Jack", u"Jack of Hearts \u2661",10]
        self.__cards[38] = ["King", u"King of Hearts \u2661",10]
        self.__cards[39] = ["Queen", u"Queen of Hearts \u2661",10]
        
        
        #spades
        
        self.__cards[40] = ["Ace", u"Ace of Spades \u2664", 11]
        self.__cards[41] = ["2", u"Two of Spades \u2664",2]
        self.__cards[42] = ["3", u"Three of Spades \u2664",3]
        self.__cards[43] = ["4", u"Four of Spades \u2664",4]
        self.__cards[44] = ["5", u"Five of Spades \u2664",5]
        self.__cards[45] = ["6", u"Six of Spades \u2664",6]
        self.__cards[46] = ["7", u"Seven of Spades \u2664",7]
        self.__cards[47] = ["8", u"Eight of Spades \u2664",8]
        self.__cards[48] = ["9", u"Nine of Spades \u2664",9]
        self.__cards[49] = ["10", u"Ten of Spades \u2664",10]
        self.__cards[50] = ["Jack", u"Jack of Spades \u2664",10]
        self.__cards[51] = ["King", u"King of Spades \u2664",10]
        self.__cards[52] = ["Queen", u"Queen of Spades \u2664",10]
        
    def draw_card(self):
        """
        Draws a card from deck; after card return an element is
        removed from the dictionary of cards
        :return: card
        """
        num = self.__cardIndex[self.__counter]
        card = self.__cards[num]
        del self.__cards[num]
        self.__counter +=1
        return card
    
    def getCards_count(self):
        """
        :return: Number of elements in cards dictionary
        """
        return len(self.__cards)
    
    def shuffle(self):
        """
        Reshufles the indexes or integer keys of the list storing the cards
        After reshufling we recreate the deck with a new random rearrangment of the keys.
        :return: None
        """
        self.__counter = 0
        random.shuffle(self.__cardIndex)
        self.create_deck()