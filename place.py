import random
import time 
from time import sleep
'''
class dice:
    def __init__(self):
        self.num_dice = 0
        self.total = 0
        self.new_turn = False
    
    def add_dice(self):
        if self.new_turn == True:
            self.num_dice += 1
    
    def use_dice(self):
        if self.num_dice != 0:
            for x in range(self.num_dice):
                num = random.randint(1,6)
                print ("you roled a: ",num)
                self.total+= num
                num = 0
'''



class Place():
    def __init__(self, given_name, total = 0, got_item = False):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.location_name = given_name
        self.items = []
        self.got_item = got_item
        self.num_dice = 0
        self.total = total
    
    def roll(self,new_turn):
        self.new_turn = new_turn
        if self.new_turn == True:
            self.num_dice += 1
            num = random.randint(1,6)
            print ("you rolled a: ",num)
            self.total += num
            print ("you are now on square: ",self.total)
            time.sleep(3)
            self.num_dice -= 1
            self.new_turn = False
            



    
    def wildcard(self):
        self.item_instance = ""
        if self.total in [1 , 4 , 9 , 14 , 19 , 24 , 29 , 34 , 39 , 44 , 49 , 54 , 59 , 64, 69 , 74 , 79]:
            print ("YOU GOT A WILDCARD")
            print ("generating card...")
            time.sleep(3)
            num = random.randint(1,10)
            if num == "1":
                print ("bad luck")
                print ("you fell of a cliff and lost 20 health")
                self.health -= 20 
                time.sleep(3)
            elif num == "2":
                print ("bad luck")
                print ("rats ate your food")
                if "food" in self.inventory:
                    self.inventory.append("food")
                time.sleep(3)
            elif num == "3":
                print ("bad luck")
                print ("you ran away from a spider, and lost energy")
                self.hunger -= 20
                time.sleep(3)
            elif num == "4":
                print ("bad luck")
                print ("you fell into a pit and encounterd trivia master...")
                self.playing_trivia = True 
                time.sleep(3)
            elif num == "5":
                print ("bad luck")
                print ("you fell into a pit and encounterd trivia master...")
                self.playing_trivia = True 
                time.sleep(3)
            elif num == "6":
                print ("good luck")
                print ("you found food")
                self.item_instance = "food"
                self.got_item = True
                time.sleep(3)
            elif num == "7":
                print ("good luck")
                print ("you found medicine")
                self.item_instance = "medicine"
                self.got_item = True
                time.sleep(3)
            elif num == "8":
                print ("good luck")
                print ("move forward 2 spaces")
                self.total += 2
                time.sleep(3)
            elif num == "9":
                print ("good luck")
                print ("you got a clue")
                self.item_instance = "clue"
                self.got_item = True
                time.sleep(3)
            else:
                print ("good luck")
                ("move forward 3 spaces")
                self.total += 3
                time.sleep(3)
    
    def interact_npc(self):
        self.item_instance= ""
        if self.total in [2,12,22,32,42,52,62,72]:
            if self.total == 2:
                print ("you encountered a fellow traveler...")
                choice = input("would you like to hear his message? yes/no")
                if choice.lower() == "yes":
                    print ("watch out for the theives trying to steal your items")
            elif self.total in [12,42,72]:
                print ("you encountered a theif...")
                print ("""rolling a dice...
                           if it is 3 or less then 3, yoy get set back a couple squares
                           if it is 4 or above you win an item""")
                num = random.randint(1,6)
                if num <= 3:
                    self.total -= 2
                    print ("you lost")
                    print ("you go set back by 2 squared")
                    print ("your currrent square is: ",self.total)
                    time.sleep(3)
                        

                else:
                        print ("you won the fight against the theif")
                        print ("you recieved a...")
                        num = random.randint(1,5)
                        if num == "1":
                            print ("sheild")
                            self.item_instance = "sheild"
                            self.got_item = True
                            time.sleep(3)
                        if num == "2":
                            print ("medicine")
                            self.item_instance = "medicine"
                            self.got_item = True
                            time.sleep(3)
                        if num == "3":
                            print ("food")
                            self.item_instance = "food"
                            self.got_item = True
                            time.sleep(3)
                        if num == "4":
                            print ("clue")
                            self.item_instance = "clue"
                            self.got_item = True
                            time.sleep(3)
                        if num == "5":
                            print ("sword")
                            self.item_instance = "sword"
                            self.got_item = True
                            time.sleep(3)
            elif self.total == 32:
                print ("you encountered another traveler...")
                choice = input("would you like to interact with npc? yes/no")
                if choice.lower() == "yes":
                    print ("watch out! you almost entered the deadly maze, watch out next time...")
                    time.sleep(3)
            
            elif self.total in [22,52]:
                print ("well done traveller...")
                print ("we wish you luck as you move on to a scary reigon...")
                print ("generating an item...")
                num = random.randint(1,5)
                if num == 1:
                    print ("you recieved a sheild...")
                    self.item_instance = "sheild"
                    self.got_item = True
                    time.sleep(3)
                elif num == 2:
                    print ("you recieved some medicine...")
                    self.item_instance = "medicine"
                    time.sleep(3)
                    self.got_item = True
                elif num == 3:
                    print ("you recieved some food...")
                    self.item_instance = "food"
                    time.sleep(3)
                    self.got_item = True
                elif num == 4:
                    print ("you recieved a clue...")
                    self.item_instance = "clue"
                    time.sleep(3)
                    self.got_item = True
                else:
                    print ("you recieved a sword...")
                    self.item_instance = "sword"
                    time.sleep(3)
                    self.got_item = True
            elif self.total == 62:
                print ("you encountered a fellow traveler...")
                choice = input("would you like to hear his message? yes/no")
                if choice.lower() == "yes":
                    choice2 = ("would you like to trade? i have a special mystery item...")
                    if choice2.lower() == "yes":
                        print ("this is your current inventory...", self.inventory)
                        item_removed = input("what item do you want to give in exchange for this mystery item")
                            
                        if item_removed not in self.inventory:
                                print ("item is not in inventory...")
                        if item_removed =="sheild":
                                amount = 10
                                self.total_weight -= amount
                                self.inventory.remove("sheild")
                        elif item_removed == "medicine":
                                amount = 2
                                self.total_weight -= amount
                                self.inventory.remove("medicine")
                        elif item_removed =="food":
                                amount = 2
                                self.total_weight -= amount
                                self.inventory.remove("food")
                        else:
                                print ("item does not have a weight, or doesnt exist")
                        
                        message = ("""you recieved a sword
                                  you can use this item to defeat trivia boss before game starts")
                                  keep in mind that you will have to defeat trivia level 8
                                  to get the final treasure
                                  the weight of the sword is 5 kg
                                  your maximum weight that you inventory can withstand is 20 kg""")
                        for x in message:                     
                            print(x, end='', flush=True)  
                            sleep(0.05)
                        print(message) 
                        self.item_instance = "sword"
                        self.got_item = True
                        choice = input("do you want to pick up the sword? yes/no")
    def safespace(self):
        if self.total in [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]:
            print ("you landed on a safe square, nothing happend, you can role thr dice again")
    
    def trivia(self):
        if self.total in [3,13, 23, 33, 43, 53, 63, 73, 6, 16, 26, 36, 46, 56, 66, 76]:
            if self.total in [3,13,6,16]:
                triv_txt = ("""this is trivia level 1
                               to pass this minigameyou need to answer 1 of 3 questions correctly
                                i) what is 1 - 5 x 3
                                ii) what is the literature technique? to compare something using the words 'like' or 'as'?
                                iii)what is 4'o'clock in military time(in the format 00:00)
                            """)
                points = 0
                for x in triv_txt:                     
                    print(x, end='', flush=True)  
                    sleep(0.05)
                print(triv_txt)
                a = input("what is you answer to i?")
                b = input("what is your answer to ii?")
                c = input("what is your answer to iii")
                if a == -14:
                    points +=1
                if b.lower() == "simile":
                    points += 1
                if c == "16:00":
                    points += 1
                print ("the right answers are: i)-14 ii)simile iii)16:00")
                if points == 0:
                    print ("you got every answer wrong")
                    self.total -= 1
                    print ("you moved back a square (you will not have to complete the action on the square)")
                if points > 0:
                    print ("you passed the trivia game")
            
            elif self.total in [23,33,26,36]:
                triv_txt2 = ("""this is trivia level 2
                               to pass this minigame you need to answer atleast 1 of these 3 questions correctly
                                i) what is 13*13*13?
                                ii) who is the author of the book titled: A christmas Carol?(full name)
                                iii) what blood vessel carries blood from the heart to the lungs?
                            """)
                points = 0
                for x in triv_txt2:                     
                    print(x, end='', flush=True)  
                    sleep(0.05)
                print(triv_txt2) 

                a2 = input("what is you answer to i?")
                b2 = input("what is your answer to ii?")
                c2 = input("what is your answer to iii")
                if a2 == 2197:
                    points +=1
                if b2.lower() == "charles dickens":
                    points += 1
                if c2 == "pulmonary artery":
                    points += 1
                print ("the right answers are: i)2197 ii)charles dickens iii)pulmonary artery")
                if points == 0:
                    print ("you got every answer wrong")
                    self.total -= 2
                    print ("you moved back two squares (you will not have to complete the action on the square)")
                if points >0:
                    print ("you passes the trivia game")
            
            elif self.total in [43,53,46,56]:
                triv_txt3= ("""this is trivia level 3
                               to pass this minigame you need to answer atleast 1 of these 3 questions correctly
                                i) differenctiate : y = 3x^2 + 2x^-1
                                ii) what is the literature technique: persuasive use of a short past story 
                                iii) what is the capital of malaysia?
                            """)
                points = 0
                for x in triv_txt3:                     
                    print(x, end='', flush=True)  
                    sleep(0.05)
                print(triv_txt3) 

                a3 = input("what is you answer to i?")
                b3 = input("what is your answer to ii?")
                c3 = input("what is your answer to iii")
                if a3 == "6x -2x^-2":
                    points +=1
                if b3.lower() == "anecdote":
                    points += 1
                if c3.lower() == "kuala lumpur":
                    points += 1
                print ("the right answers are: i)6x -2x^-2 ii)anecdote iii)kuala lumpur")
                if points == 0:
                    print ("you got every answer wrong")
                    self.total -= 3
                    print ("you moved back three squares (you will not have to complete the action on the square)")
                if points > 0:
                    print ("you passed the trivia game")
            
            elif self.total in [63,73,66,76]:
                triv_txt4= ("""this is trivia level 4
                               to pass this minigame you need to answer atleast 1 of these 3 questions correctly
                                i) the election system the UK currently uses is:
                                ii) what is the exact date of Kristallnacht(the first day not the second)(in the form 00/00/0000)
                                iii) what is the legislative capital of sri lanka? (full name)
                            """)
                points = 0
                for x in triv_txt4:                     
                    print(x, end='', flush=True)  
                    sleep(0.05)
                print(triv_txt4) 

                a4 = input("what is you answer to i?")
                b4 = input("what is your answer to ii?")
                c4 = input("what is your answer to iii")
                if a4.lower() == "first past the post":
                    points +=1
                if b4.lower() == "09/11/1938":
                    points += 1
                if c4.lower() == "sri jayawardenepura kotte":
                    points += 1
                print ("the right answers are: i)first past the post ii)09/11/1938 iii)sri jayawardenepura kotte")
                if points == 0:
                    print ("you got every answer wrong")
        
                    self.total -= 4
                    print ("you moved back four squares (you will not have to complete the action on the square)")
                if points > 0:
                    print ("you passed trivia")
    
    def maze(self):
        import pygame
        if self.total in [11, 21, 31, 41, 51, 61, 71]:
            WIDTH, HEIGHT = 1500, 1500
            pygame.init()
            sc =pygame.display.set_mode(WIDTH, HEIGHT)
            run = True 
            
            while run == True:
                sc.fill(pygame.Color("black"))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                
                pygame.display.flip()
            





                
                
                 
                             



    





                

