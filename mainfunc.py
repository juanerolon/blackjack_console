#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:05:00 2019

@author: juanerolon
"""

import os

from disp_intro import disp_header, disp_instruct
from gameplay import Blackjack



if __name__ == "__main__":
   
   disp_header()
   input("Press Enter to read game instructions...")
   disp_instruct()
   input("Press Enter to start the game...")
   os.system("clear")
   disp_header()
    
   bgame = Blackjack()
   
   while bgame.gameFlag:
           
       print("Your balance is : {}".format(bgame.P1.get_balance())) 
        
       bgame.make_bets()
                
       if bgame.gameFlag : bgame.deal()
       if bgame.roundFlag : bgame.main_loop()
       
       if bgame.gameFlag and bgame.P1.get_balance() > 0: 
           ans = input("\n\n Play another round? (y/n)? Enter y for Yes, n for No: ")
           if ans.strip().lower() == "y":
               os.system("clear")
               disp_header()
               bgame.roundFlag = True
               bgame.P1.clear_hand()
               bgame.Dl.clear_hand()
               bgame.gD.shuffle()                         
           elif ans.strip().lower() == "n":
                bgame.gameFlag = False
           else:
                continue
              
   print("\nPlayer end balance: {}\n".format(bgame.P1.get_balance())) 
   print("\nGame stats:\n") 
   print("Number of rounds played : {}".format(bgame.ngmes_ct))
   print("Number of wins by player: {}".format(bgame.pwins_ct))
   print("Number of ties by player: {}".format(bgame.ties_ct))
   try:
       print("Winning percentage: {}".format(round(bgame.pwins_ct/bgame.ngmes_ct,2)))
   except:
       print("Winning percentage: Not Available")
       