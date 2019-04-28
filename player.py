#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:02:23 2019

@author: juanerolon
"""

from bet import Bet

class Player:
    
    def __init__(self):
        
        self.hand_value = 0
        self.hand = []
        self.hand_ct = 0
        self.aces_ct = 0
        self.ace_flag = False
        self.__sysbet = Bet()
        
    
    def can_bet(self,amount):
        return self.__sysbet.can_bet(amount)
    
    def make_bet(self,amount):
        self.__sysbet.make_bet(amount)
        
    def get_balance(self):
        return self.__sysbet.balance

    def blnc_up_won(self,upamt):
        self.__sysbet.balance += upamt
        
    
    def update_hand(self, card):
        
        if card[2] == 11:
            self.ace_flag = True
            self.aces_ct +=1
        
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]
                
        if self.hand_value > 21 and self.ace_flag:
            self.hand_value = self.hand_value - 10
            self.ace_flag = False
            print("Player got a soft hand")
            
        self.hand_ct +=1
        
    def blackjack(self):
        if self.hand_value == 21:
            return True
        else:
            return False
        
    def busted(self):
        if self.hand_value > 21:                
            return True
        else:
            return False
        
    def clear_hand(self):
        del self.hand[:]
        self.hand_value = 0
        self.hand_ct = 0
        self.aces_ct = 0
        self.ace_flag = False
        