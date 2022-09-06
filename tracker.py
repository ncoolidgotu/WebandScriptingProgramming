
from pynput.mouse import Button, Controller
import time

class Activity:
    def __init__(self):
        self.time = 0
    
    def tracker(self):
        while True:
            time.sleep(10)
            if mouse.get_focused() == False:
                print("no")
            else:
                print("yes")
    
    def position(self):
        return mouse.get_rel()
                

session = Activity()