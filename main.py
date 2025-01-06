import time 
from pyfiglet import Figlet 
from place import Place
from player import Player
from test import stopwatch
from time import sleep


class Game(Place, Player):
    def __init__(self):
        self.total = 0
        self.got_item = False
        self.play = "play" 
        self.new_turn = False
        self.inventory = []

    def start(self):
        name = input("Enter player name: ")
        player = Player(name)
        
        txt= ('''Welcome to my game
                 reach the end of the board, and find the missing treasure to win
                 items: 
                 shiled:use this item to gain health abpv ethe maxed 100 health
                 clue: read the clue, to help find the treasure
                 food: eat food to stay alive
                 medicine: use to recover health
                 sword: used to avoid playing risky minigames 
                 the player must complete the action on the square they are on
                 the player can only use there items after a turn, not during
                 there is some exceptions as you can use some items before a turn
                 good luck
                 the timer will start soon...
                 3... 2 ... 1
                 start!''')
        for x in txt:                     
            print(x, end='', flush=True)  
            sleep(0.05)
        print(txt) 
        time.sleep(3)
        self.got_item = False
        timer = stopwatch("yes")
        timer.start_time()
        island = Place("island",0)
        print ("start")
        f = Figlet(font='larry3d')
        print(f.renderText('welcome to the island...'))
        print (f)
       
        while self.total < 10:
            self.new_turn = True
            island.roll(self.new_turn)
            self.new_turn = False
            island.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(item_instance)
            self.got_item = False
            
            island.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(item_instance)
            self.got_item = False
            island.safespace()
            if len(self.inventory) != 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                    print ("this is your current inventory: ",self.inventory)
                    item_instance = input("what item would you like to use")
                    if item_instance not in self.inventory:
                        print ("item is not in inventory")
                    player.use_item(item_instance)
            island.trivia()


            
        volcano = Place("volcano")
        f = Figlet(font='larry 3d')
        print(f.renderText('welcome to the volcano'))
        print (f)

        while (self.total.palce < 20):
            self.new_turn = True
            volcano.rol()
            volcano.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            self.got_item = False
            volcano.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            self.got_item =False
            volcano.safespace()
            if len(self.inventory) != 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                    print ("this is your current inventory: ",self.inventory)
                    self.item_instance = input("what item would you like to use")
                    if self.item_instance not in self.inventory:
                        print ("item is not in inventory")
                    player.use_item(self.item_instance)
            volcano.trivia()

            

            

            
        sea = Place("sea")
        f = Figlet(font='larry 3d')
        print(f.renderText('welcome to the sea'))
        print (f)

        while (self.total < 30):
            self.new_turn = True
            sea.roll()
            sea.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            self.got_item = False
            sea.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            self.got_item =False
            sea.safespace()
            if len(self.inventory)!= 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                        print ("this is your current inventory: ",self.inventory)
                        self.item_instance = input("what item would you like to use")
                        if self.item_instance not in self.inventory:
                            print ("item is not in inventory")
                        player.use_item(self.item_instance)
            sea.trivia()
            
        desert = Place("desert")  
        f = Figlet(font='larry 3d')
        print(f.renderText('welcome to the desert'))
        print (f)
    
        while (self.total < 40):
            self.new_turn = True
            desert.roll()
            desert.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            self.got_item =False
            desert.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            self.got_item =False
            desert.safespace()
            if len(self.inventory)!= 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                        print ("this is your current inventory: ",self.inventory)
                        self.item_instance = input("what item would you like to use")
                        if self.item_instance not in self.inventory:
                            print ("item is not in inventory")
                        player.use_item(self.item_instance)
            desert.trivia()
            
            
            
        forest = Place("forest")
        f = Figlet(font='larry 3d')
        print(f.renderText('welcome to the forest'))
        print (f)

        while (self.total < 50):
            self.new_turn = True
            forest.roll()
            forest.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            forest.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            forest.safespace()
            if len(self.inventory)!= 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                    print ("this is your current inventory: ",self.inventory)
                    self.item_instance = input("what item would you like to use")
                    if self.item_instance not in self.inventory:
                        print ("item is not in inventory")
                    player.use_item(self.item_instance)
            forest.trivia()

            
        town = Place("town")   
        f = Figlet(font='larry 3d')
        print(f.renderText('welcome to the town'))
        print (f)

        while (self.total < 60):
            self.new_turn = True
            town.roll()
            town.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            town.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            town.safespace()
            if len(self.inventory)!= 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                    print ("this is your current inventory: ",self.inventory)
                    self.item_instance = input("what item would you like to use")
                    if self.item_instance not in self.inventory:
                        print ("item is not in inventory")
                    player.use_item(self.item_instance)
            town.trivia()
            
            
        snowy_reigon = Place("snowy_reigon")    
        f = Figlet(font='larry 3d')
        print(f.renderText('welcome to the snowy reigon'))
        print (f)

        while self.total <= 70:
            self.new_turn = True
            snowy_reigon.roll()
            snowy_reigon.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            snowy_reigon.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            snowy_reigon.safespace()
            if len(self.inventory)!= 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                    print ("this is your current inventory: ",self.inventory)
                    self.item_instance = input("what item would you like to use")
                    if self.item_instance not in self.inventory:
                        print ("item is not in inventory")
                    player.use_item(self.item_instance)
            snowy_reigon.trivia()
                
        city = Place("city")
        f = Figlet(font='larry 3d')
        print(f.renderText('welcome to the city'))
        print (f)

        while self.total <= 80:
            self.new_turn = True
            city.roll()
            city.wildcard()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            city.interact_npc()
            if self.got_item == True:
                choice = input("would you like to pickup the item")
                if choice.lower() == "yes":
                    player.pick_up(self.item_instance)
            city.safespace()
            if len(self.inventory)!= 0:
                choice = input("would you like ot use an item")
                if choice.lower() == "yes":
                    print ("this is your current inventory: ",self.inventory)
                    self.item_instance = input("what item would you like to use")
                    if self.item_instance not in self.inventory:
                        print ("item is not in inventory")
                    player.use_item(self.item_instance)
            city.trivia()
        

        show_message = True 
        while self.total > 80:
            while show_message == True:    
                print (" WELL DONE, for finihing the board game...")
                print ("but did you collect the 3 missing treasure peices?")
                timer.stop_time()
                timer.show_time()
                show_message = False 
            

new_game = Game()
new_game.start()

'''

    def trivia(self):
        if self.total in [3,13, 23, 33, 43, 53, 63, 73, 6, 16, 26, 36, 46, 56, 66, 76]:
    
    def maze(self):
        if self.total in [11,21,31,41,51,61,71, 7, 17, 27, 37, 47, 57, 67, 77]:
    
    def reward_item(self):
        if self.total in [8,18,28,38,48,58,68,78]:
        


                player.trivia()
                player.minigame()
                player.reward_item()
                player.safe_space()
        
                            ("you lost the fight agaist the thief")
                        x = self.inventory.count("sheilds")
                        y = self.inventory.count("double dice")
                        z = self.inventory.count("medicine")
                        q = self.inventory.count("food")
                        t = self.inventory.count("clue")
                        max = x + y + z + q + t
                        num = random.randint(0,(max-1))
                        if num == "0":
                            self.inventory.pop[0]
                        elif num == "1":
                            self.inventory.pop[1]
                        elif num == "2":
                            self.inventory.pop[2]
                        elif num == "3":
                            self.inventory.pop[3]
                        elif num == "4":
                            self.inventory.pop[4]
                        elif num == "5":
                            self.inventory.pop[5]
                        elif num == "6":
                            self.inventory.pop[6]
                        elif num == "7":
                            self.inventory.pop[7]
                        elif num == "8":
                            self.inventory.pop[8]
                        elif num == "9":
                            self.inventory.pop[9]
                        elif num == "10":
                            self.inventory.pop[10]
                        elif num == "11":
                            self.inventory.pop[11]
                        elif num == "12":
                            self.inventory.pop[12]
                        elif num == "13":
                            self.inventory.pop[13]
                        elif num == "14":
                            self.inventory.pop[14]
        
'''




            


        

        

        
        



        
        
        



        
        
        
        

            
