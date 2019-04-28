#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:00:39 2019

@author: juanerolon
"""
import random
class Dealer:
    
    def __init__(self):
        
        self.hand_value = 0
        self.hand = []
        self.hand_ct = 0
        self.aces_ct =0
        self.ace_flag = False
               
    def update_hand(self, card):
        
        if card[2] == 11:
            self.ace_flag = True
            self.aces_ct +=1
            
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]
        
        if self.hand_value > 21 and self.ace_flag:
            self.hand_value = self.hand_value - 10
            print("Dealer got soft hand")
            
        self.hand_ct +=1
               
    def getFace_up_card(self):
        return self.hand[random.choice([0,1])]
        
    def clear_hand(self):
        del self.hand[:]
        self.hand_value = 0
        self.hand_ct = 0
        self.aces_ct = 0
        self.ace_flag = False
        
    def can_hit(self):
        """Controls when dealer should stand"""
        if self.hand_value < 17:
            return True
        else:
            return False
        
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