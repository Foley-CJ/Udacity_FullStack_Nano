'''
What steps would you take to get to the the output of take a break:

We need a timer/sleep module as well as a video execute module.

1. wait for 2 hours
2. opens web browser -play youtube video
3. wrap 1&2 in a loop (3x)
'''
import webbrowser
import time

#time.sleep(10)
#webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")


#we want to take 3 breaks

for x in range(3):
    print "The current time is: " + time.ctime()
    time.sleep(60*60*2)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

