#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:59:50 2019

@author: Juan E Rolon
       : rolon.math@gmail.com
"""

class Bet:
    
    def __init__(self):
        
        self.balance = 1000
        
                
    def make_bet(self,amount):
        self.balance = self.balance - amount

    def can_bet(self,amount):
       return (amount <= self.balance) and (self.balance > 0)