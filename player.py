import random

class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.inventory_max_weight = 20
        self.total_weight= 0 
        self.inventory = []

        
    def pick_up(self, item_instance):
        self.item_instance = item_instance
        print ("the item infront of you is: ",self.item_instance)
        pick_up = input("would you like to pick up the item.yes/no?")
        if pick_up.lower() == "yes":
                self.inventory.append(self.item_instance)
                if self.item_instance == "sheild":
                    amount = 10
                if self.item_instance == "medicine":
                    amount = 2
                if self.item_instance == "food":
                    amount = 2
                if self.item_instance == "sword":
                    amount = 5
                self.total_weight += amount
                if self.total_weight > self.inventory_max_weight:
                    print ("your inventory is full...")
                    print("you cannot pick up this item")
                    self.inventory.remove(self.item_instance)
                    self.total_weight -= amount
                    
    
        def remove(self, item_instance):
            self.item_instance = item_instance
            if remove.lower() == "yes":
                    print ("this is your current inventory: ", self.inventory)
                    loop = int(input("how many items would you like to remove?"))
                    i = 0
                    while i > range(loop):
                        if self.item_instance not in self.inventory:
                            print ("item is not in inventory...")
                        elif self.item_instance =="sheild":
                            amount = 10
                            self.total_weight -= amount
                            self.inventory.remove("sheild")
                        elif self.item_instance == "medicine":
                            amount = 2
                            self.total_weight -= amount
                            self.inventory.remove("medicine")
                        elif self.item_instance =="food":
                            amount = 2
                            self.total_weight -= amount
                            self.inventory.remove("food")
                        elif self.item_instance == "sword":
                            amount = 5
                            self.total_wieght -= amount
                            self.inventory.remove("sword")
                        else:
                            print ("item does not have a weight(the clue or double dice), or doesnt exist")
                        i += 1
                        


    def use_item(self, item_instance):
        self.item_instnace= item_instance
        if self.item_instance.lower() == "shield":
                self.health += 20
        elif self.item_instance.lower() =="double_dice":
                self.num_dice += 1
        elif self.item_instance.lower() =="clue":
                num = random.randint(1,3)
                if num == 1:
                    print ("YOUR CLUE IS: try not to skip through the town. You might find some missing treause there")
                elif num == 2:
                    print ("YOUR CLUE  IS: try looking through the volcano more thoroughly, you might find some treasure...")
                else:
                    print ("YOUR CLUE IS: try looking in glaciers, in the frosty reigon, for some treasure...")
        elif self.item_instance.lower() == "medicine":
                self.health += 30
                if self.health > 100:
                    difference = self.health - 100
                    self.health -= difference
                    difference = 0
        elif self.item_instance.lower() == "food":
                self.hunger += 30
                if self.hunger > 100:
                    difference = self.hunger - 100
                    self.hunger -= difference
                    difference = 0
        elif self.item_instance.lower == "sword":
                print ("you killed the trivia master...")
                trivia_game = False
                
    

            

    
    

