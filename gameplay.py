#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:03:22 2019

@author: juanerolon
"""


from deck import Deck
from player import Player
from dealer import Dealer

class Blackjack():
    
    def __init__(self):
        
        self.gD = Deck()
        self.P1 = Player()
        self.Dl = Dealer()
        
        self.roundFlag = True
        self.gameFlag = True
        self.bamt = 0
        
        self.pwins_ct = 0
        self.ngmes_ct = 0
        self.ties_ct = 0
      
          
    #--X--
    
    def get_amount(self):
        fx=True
        while fx:
            amt = input("Enter amount: ").strip().replace(" ", "")
    
            if amt.isdigit():
                amt = eval(amt)
                fx = False
            else:
                print("Not a number. Re-enter amount")
        return amt
    
    def make_bets(self):
        
        flag = True
        while flag:
            self.bamt = 0
            if self.P1.can_bet(self.bamt):
                ans = input("Make bet (y/n)? Enter y for Yes, n for No: ")
                if ans.strip().lower() == "y":
                    flag = False
                    self.bamt = self.get_amount()
                    
                    fx = True
                    while fx:
                        if self.P1.can_bet(self.bamt):
                            self.P1.make_bet(self.bamt)
                            fx = False
                        else:
                            print("Bet exceeds your balance. Re-enter your bet")
                            self.bamt = self.get_amount()
                                          
                elif ans.strip().lower() == "n":
                    ans2 = input("Stop the game (y/n)? Enter y for Yes, n for No: ")
                    if ans2.strip().lower() == "y":
                        self.roundFlag = False
                        self.gameFlag = False
                        break
                    elif ans2.strip().lower() == "n":
                        continue
                    else:
                        continue
                else:
                    continue
            else:
                print("Not enough funds to play")
                flag = False
                self.gameFlag = False
                
                
    #--X--
    
    def deal(self):
        
        flag = True
        while flag:
            
            ans = input("Deal (y/n)? Enter y for Yes, n for No: ")
            if ans.strip().lower() == "y":
                flag = False
                self.Dl.update_hand(self.gD.draw_card())
                self.Dl.update_hand(self.gD.draw_card())
                self.P1.update_hand(self.gD.draw_card())
                self.P1.update_hand(self.gD.draw_card())             
                face_up_card = self.Dl.getFace_up_card()
                print("")
                print("Dealer's hand (one card face-up): {}".format(face_up_card))
                print("Dealer's hand value (one card face-up): {}".format(face_up_card[2]))
                print("")
                #set to True for testing
                if False:
                    print("Dealer's full hand: {}".format(self.Dl.hand))
                    print("Dealer's full hand value: {}".format(self.Dl.hand_value))
                    
                print("")
                print("Player's hand: {}".format(self.P1.hand))
                print("Player's hand value: {}".format(self.P1.hand_value))
                print("")
                if self.P1.blackjack():
                    print("Player gets blackjack! Player wins!")               
                    self.roundFlag=False
                    self.pwins_ct +=1
                    self.ngmes_ct +=1
                    self.P1.blnc_up_won(2.0 * self.bamt)
                    break
            elif ans.strip().lower() == "n":
                ans2 = input("Stop the game (y/n)? Enter y for Yes, n for No: ")
                if ans2.strip().lower() == "y":
                    self.P1.blnc_up_won(self.bamt)
                    self.roundFlag = False
                    self.gameFlag = False
                    break
                elif ans2.strip().lower() == "n":
                    continue
                else:
                    continue
            else:
                continue
            
    #--X--
            
    def main_loop(self):
        flag = True
        fflo = True
        dealerDraws = 0
        while flag:
            ans = input("Hit (y/n)? Enter y for Yes (Hit), n for No (Stand): ")
            if ans.strip().lower() == "y":
                self.P1.update_hand(self.gD.draw_card())
                print("")
                print("Player's hand: {}".format(self.P1.hand))
                print("Player's hand value: {}".format(self.P1.hand_value))
                print("")
                if self.P1.busted():
                    print("Player busted! Player Loss!")
                    print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                    print("Dealer's hand value: {}".format(self.Dl.hand_value))
                    flag = False
                    self.roundFlag = False
                    self.ngmes_ct +=1
                    break
                elif self.P1.blackjack():
                    print("")
                    print("Player gets blackjack! Player wins!")
                    print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                    print("Dealer's hand value: {}".format(self.Dl.hand_value))
                    self.P1.blnc_up_won(2.0 * self.bamt)
                    flag = False
                    self.roundFlag = False
                    self.pwins_ct +=1
                    self.ngmes_ct +=1
                    break            
                else:
                    pass
                    
            elif ans.strip().lower() == "n":
                print("Player stands")
                flag = False
                while fflo:
                    if self.Dl.blackjack():
                        fflo = False
                        print("")
                        print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                        print("Dealer's hand value: {}".format(self.Dl.hand_value))
                        print("Dealer gets Blackjack! Player Loss!")
                        self.roundFlag = False
                        self.ngmes_ct +=1
                        break
                        
                    elif self.Dl.busted():
                        fflo = False
                        self.roundFlag = False
                        print("")
                        print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                        print("Dealer's hand value: {}".format(self.Dl.hand_value))
                        print("Dealer Busted! Player Wins!")
                        self.P1.blnc_up_won(2.0 * self.bamt)
                        self.pwins_ct +=1
                        self.ngmes_ct +=1
                        break
                    elif self.Dl.can_hit():
                        #dealer keeps drawing card from deck until h17 rule kicks in
                        dealerDraws += 1
                        self.Dl.update_hand(self.gD.draw_card())
                        print("")
                        print("Dealer has drawn a card... counting: {}".format(dealerDraws))
                        if False:
                            print("Dealer'a hand in draw {}: {}".format(dealerDraws, self.Dl.hand))
                            print("Dealer'a hand value: {}".format(self.Dl.hand_value))
                        print("")
                        if False:
                            print("Dealer can hit?: {}".format(self.Dl.can_hit()))
                        
                        if self.Dl.blackjack():
                            fflo = False
                            flag = False
                            self.roundFlag = False
                            print("")
                            print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                            print("Dealer'a hand value: {}".format(self.Dl.hand_value))
                            print("Dealer gets Blackjack! Player Loss!")
                            self.ngmes_ct +=1
                            break
                        
                        if self.Dl.busted():
                            fflo = False
                            flag = False
                            self.roundFlag = False
                            print("")
                            print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                            print("Dealer's hand value: {}".format(self.Dl.hand_value))
                            print("Dealer Busted! Player Wins!")
                            self.P1.blnc_up_won(2.0 * self.bamt)
                            self.pwins_ct +=1
                            self.ngmes_ct +=1
                            break
                            
                        if  self.Dl.hand_value > self.P1.hand_value:
                            print("")
                            print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                            print("Dealer's hand value: {}".format(self.Dl.hand_value))
                            print("Dealer has greater hand value! Player Loss!")
                            fflo = False
                            flag = False
                            self.roundFlag = False
                            self.ngmes_ct +=1
                            break                       
                    elif self.P1.hand_value > self.Dl.hand_value:
                        print("")
                        print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                        print("Dealer's hand value: {}".format(self.Dl.hand_value))
                        print("Player has greater hand value! Player Wins!")
                        self.P1.blnc_up_won(2.0 * self.bamt)
                        fflo = False
                        flag = False
                        self.roundFlag = False
                        self.pwins_ct +=1
                        self.ngmes_ct +=1
                        break
                    elif self.Dl.hand_value > self.P1.hand_value:
                        print("")
                        print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                        print("Dealer's hand value: {}".format(self.Dl.hand_value))
                        print("Dealer has greater hand value! Player Loss!")
                        fflo = False
                        flag = False
                        self.roundFlag = False
                        self.ngmes_ct +=1
                        break
                    elif self.Dl.hand_value == self.P1.hand_value:
                        print("")
                        print("Dealer's revealed full hand: {}".format(self.Dl.hand))
                        print("Dealer's hand value: {}".format(self.Dl.hand_value))
                        print("Push! Tied round!")
                        self.ties_ct +=1
                        self.P1.blnc_up_won(self.bamt)
                        fflo = False
                        flag = False
                        self.roundFlag = False
                        self.ngmes_ct +=1
                        break                        
                    else:
                        print("Unknown condition")
                        self.ngmes_ct +=1
                        break
            else:
                break
       