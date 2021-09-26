from game import play
from titlescreen import start
import time

if __name__ == "__main__": #only runs main function if this file is ran directly
    #initialize
    playing = True

    stop = start()
    
    if stop == False:
 
        play()