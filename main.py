from game import play
from titlescreen import start

if __name__ == "__main__": #only runs main function if this file is ran directly
    #initialize

    stop = start()
    
    if stop == False:     
        stop = play()

    #End  Screen