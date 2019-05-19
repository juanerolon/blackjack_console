#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Juan E. Rolon
https://github.com/juanerolon
"""

import random
class Dealer:
    """
    Defines a Dealers object for a blackjack game.
    Class member functions determine when dealer can continue
    hitting, how cards are dealt, updated and under which conditions
    dealer hits or gets blackjack
    """
    
    def __init__(self):
        """
        Initializes member attributes:
        hand_value: total value of cards in hand
        hand: list containing cards
        hand_ct: counts cards in hand
        aces_ct: counts aces in hand
        
        """
        self.hand_value = 0
        self.hand = []
        self.hand_ct = 0
        self.aces_ct =0
        
               
    def update_hand(self, card):
        """
        :param card: accepts a card object (list) as input and appends it
        to list representing a hand.
        :return: None. Updates member attributes only.

        """

        # chekcs whether drawn card is an ace
        if card[2] == 11:
           
            self.aces_ct +=1
            
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]

        #determine below whether an ace in hand can be useful in case
        #dealer busts.
        if self.hand_value > 21 and self.aces_ct > 0:
            self.hand_value = self.hand_value - 10
            self.aces_ct -= 1
            print("Dealer got soft hand")
            
        self.hand_ct +=1
               
    def getFace_up_card(self):
        """
        :return: randomly chosen card from Dealers hand. This card is
        representing the card shown faced-up on the table. It is understood
        that the second card remains hidden.
        """
        return self.hand[random.choice([0,1])]
        
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
        
        
    def can_hit(self):
        """
        Controls whethe Dealder can hit. Dealer hits only if
        its hand value is strictly less than 17.
        This rule varies from Casino to Casino.
        :return: Boolean. True if dealer can continue hitting.
        """

        if self.hand_value < 17:
            return True
        else:
            return False
        
    def blackjack(self):
        """
        :return: Returns True if Dealer gets Blackjack or 21
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