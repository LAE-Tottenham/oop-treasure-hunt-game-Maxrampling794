'''
import time
seconds = time.time()
name = input("what is your name?")
time_since_epoch =  1735731730.71
time_taken = seconds - time_since_epoch
print ("it took you: ", time_taken ,"seconds to input your name")




import time

second,minute,hours = 0,0,0

while(True):
    print (hours ,":", minute, ":",second)
    time.sleep(1)
    second += 1
    if (second == 60):
        second = 0
        minute += 1
    if (minute == 60):
        minute= 0
        hours += 1
'''
import time
import numpy as np 
import math 

class stopwatch:
    def __init__(self, start):
        self.isRunning = False
        self.timeElapsed = 0
        self.startTime = None
        self.startStopwatch = start
    
    def start_time(self):
        if not self.isRunning:
            if self.startStopwatch == "yes":
                self.startTime = time.time()
                self.isRunning = True
        
    def stop_time(self):
        if self.isRunning:
            self.timeElapsed = time.time() - self.startTime
            self.isRunning = False
    
    def show_time(self):
        minutes = 0
        hours = 0
        seconds = np.around(self.timeElapsed)
        print (seconds)
        if (seconds > 60):
            minutes = seconds / 60
            type = isinstance(minutes, float)
            if type == True:
                difference = (math.floor(minutes))
                seconds = minutes - difference 
                minutes= np.around(minutes)
                seconds =np.around(seconds)
            else:
                seconds = 0 
        
        if (minutes > 60):
            hours = minutes/60
            type = isinstance(hours, float)
            if type == True:
                difference = (math.floor(hours))
                minutes = hours - difference
            else:
                minutes = 0
        
        print ("it took you: ", hours,":", minutes,":", seconds, "to complete the game")
            



from time import sleep

def print_slow(txt):
    for x in txt:                     
        print(x, end='', flush=True)  
        sleep(0.05)
    print() 



        
        
        



        
        
    

