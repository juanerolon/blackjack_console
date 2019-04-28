#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Juan E. Rolon
https://github.com/juanerolon

"""

class Bet:
    """Defines a Bet object for a playing card game. """
    
    def __init__(self):
        """
        Constructor initializes balance
        """
        
        self.balance = 1000

    def make_bet(self,amount):
        """
        Returns the current players balance after bet is placed
        :param amount: represents the betted amound
        :return: Nothing. Updates member variable only
        """
        self.balance = self.balance - amount

    def can_bet(self,amount):
        """
        Returns True when amount betted is positive and less than
        current balance. Returns False otherwise
        :param amount:
        :return: Boolean
        """
        return (amount <= self.balance) and (self.balance > 0)