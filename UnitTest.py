import time
from threading import Thread

def printNumbers(lowEnd, highEnd):
    while(lowEnd <= highEnd):
        print(repr(lowEnd))
        lowEnd += 1


countTo = 100000

#Test using 1 thread.        
startSingleThread = time.clock()
printNumbers(0,countTo)
elapsedSingleThread = (time.clock() - startSingleThread)

#Test using 10 threads
numberOfThreads      = 10
countAmountPerThread = countTo/numberOfThreads

startTenThread = time.clock()
for i in range(numberOfThreads):
    threadLowEnd  = i*countAmountPerThread
    threadHighEnd = (i+1)*countAmountPerThread
    t = Thread(target=printNumbers, args=(threadLowEnd,threadHighEnd,))
    t.start()

#Join all existing threads to main thread.
for thread in Thread.enumerate():
    if thread is not Thread.currentThread():
        thread.join()

elapsedTenThread = (time.clock() - startTenThread)

print("Time for 1 thread: " + repr(elapsedSingleThread))
print("time for 10 threads: " + repr(elapsedTenThread))