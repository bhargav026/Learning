import multiprocessing
import random 

def printsec(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())
    
if __name__ == '__main__':
    for n in range(3):
        seconds = random.randrange(1,5)
        proc = multiprocessing.Process(target=printsec, args=(seconds,))
        proc.start()