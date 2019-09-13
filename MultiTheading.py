import _thread
import time

def threadFunction(threadName, sleepTime):

    i = 0;
    while i < 5:
        time.sleep(sleepTime);
        i = i + 1
        print(threadName, i)
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
    # _thread.start_new_thread( threadFunction, ("Thread-1", 2, ) )
    # _thread.start_new_thread( threadFunction, ("Thread-2", 4, ) )
    threadFunction('thread 1: ', 2)
    threadFunction('thread 2: ', 2)
except:
    print ("Error: unable to start thread")

while 1:
    pass

# threadFunction('Thread 1', 5)
# threadFunction('Thread 2', 5)
#
