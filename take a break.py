#Take a Break!  Take a break every 10 minutes.  Take x breaks.

import time
import webbrowser

breaks = input ("How many breaks would you like to take?  ")
break_tally = 0
breaktime = input ("how long before you take each break?  ")

while (break_tally < breaks) :  #run a break timer for as many breaks as the user specified.
    time.sleep(breaktime) #set the timer for a user specified amount of time.
    webbrowser.open("https://www.youtube.com/watch?v=Krgi3XUJz24&t=0s")
    break_tally = break_tally + 1

 
