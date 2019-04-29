#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Juan E. Rolon
https://github.com/juanerolon
"""

from bet import Bet

class Player:
    """
    Defines a Player object.
    Class member functions determine when player can continue
    hitting, the betting process, card update process and under
    which conditions he/she busts or gets blackjack
    """
    
    def __init__(self):
        """
        Initializes member attributes:
        hand_value: total value of cards in hand
        hand: list containing cards
        hand_ct: counts cards in hand
        aces_ct: counts aces in hand
        ace_flag: is True when hand contains an ace
        sysbet: Private attribute instantiates a Bet object
        """
        
        self.hand_value = 0
        self.hand = []
        self.hand_ct = 0
        self.aces_ct = 0
        self.ace_flag = False
        self.__sysbet = Bet()
        
    
    def can_bet(self,amount):
        return self.__sysbet.can_bet(amount)
    
    def make_bet(self,amount):
        """
        Player places a bet by calling Bet object make_bet method
        :param amount:
        :return:
        """
        self.__sysbet.make_bet(amount)
        
    def get_balance(self):
        """
        :return: the Player current balance
        """
        return self.__sysbet.balance

    def blnc_up_won(self,upamt):
        """
        Updates balance after Player wins
        :param upamt: amount by which balance gets increased
        :return:
        """
        self.__sysbet.balance += upamt
        
    
    def update_hand(self, card):
        """
        Updates the Players hand with the card being drawn from the deck
        :param card:
        :return: None
        """

        #chekcs whether drawn card is an ace
        if card[2] == 11:
            self.ace_flag = True
            self.aces_ct +=1

        #updates hand value
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]

        #determine below whether an ace in hand can be useful in case
        #dealer busts.
        if self.hand_value > 21 and self.ace_flag:
            self.hand_value = self.hand_value - 10
            self.ace_flag = False
            print("Player got a soft hand")
            
        self.hand_ct +=1
        
    def blackjack(self):
        """
        :return: Returns True if Player gets Blackjack or 21
        """
        if self.hand_value == 21:
            return True
        else:
            return False
        
    def busted(self):
        """
        :return: Returns True if Dealer busts
        """

        if self.hand_value > 21:                
            return True
        else:
            return False
        
    def clear_hand(self):
        """
        Clears all attributes representing a hand.
        Reset switch after game round
        :return: None
        """
        del self.hand[:]
        self.hand_value = 0
        self.hand_ct = 0
        self.aces_ct = 0
        self.ace_flag = False
        