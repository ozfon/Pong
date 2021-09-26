#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game import play
from titlescreen import start

if __name__ == "__main__": #only runs main function if this file is ran directly
    #initialize
    playing = True
    
    stop = start()
    
    if stop == False:
 
        play()