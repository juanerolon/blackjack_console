#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:39:41 2019

@author: juanerolon
"""
import os


def disp_header():
    print("\n"*2)
    print(u'\u2661 \u2667 \u2664 \u2662 '*12)
    print(" "*32 + "B L A C K J A C K")
    print(u'\u2661 \u2667 \u2664 \u2662 '*12)
    print("\n"*2)

def disp_instruct():
    
    
    instr = u"""
    
    The game follows the basic rules of blackjack. https://en.wikipedia.org/wiki/Blackjack
    
    \U0001F3B2 In this simulation, each playing card is represented by a list with three elements 
    e.g. ['6', 'Six of Hearts ♡', 6]. The first element is the string representation of the value, 
    the second is the card description and the last is the value itself.
    
    \U0001F3B2 A hand is represented by a list of cards, for example 
    [['7', 'Seven of Clubs ♧', 7], ['2', 'Two of Hearts ♡', 2], ['6', 'Six of Diamonds ♢', 6]].
    
    \U0001F3B2 The objective of the game for Player and Dealer is to reach a cumulative hand value of 21 
    or to reach a score higher than the dealer without exceeding 21.
    
    \U0001F3B2 Player has a starting balance of $1000. Player can play any number of rounds until he(she) decides
    to stop or gets insufficient funds to continue playing.
    
    \U0001F3B2 The player begins by placing a bet on the table and dealers deals two cards to the player.
    Kings, Queens and Jacks are counted as 10. Aces count as either 1 or 11. All other cards are counted their 
    numeric value.
    
    \U0001F3B2 Out of the first two cards dealt by the Dealer to itself, one is placed face-up while the other
    remains hidden. The player is dealt two cards face-up.
    
    \U0001F3B2 After the dealing stage, the player has the option of to get a hit to draw his desired number of 
    cards or at some point to stand (making the choice not to hit) to stop receiving more cards.
    
    \U0001F3B2 After player stands, the Dealer will draw the necessary number of cards as set by its internal algorithm.
    
    \U0001F3B2 The game ends when either Player or dealer busts its hand or if either reaches the highest score
    in the round; if in one round the both get the same score, the game is Pushed or Tied.
    
    \U0001F3B2 For the player, winning or losing the game means winning or losing the amount placed as bet.
 
    """
        
    os.system('clear')
    print("INSTRUCTIONS:\n")
    print(instr) 
    print("")
    
    
    
    
