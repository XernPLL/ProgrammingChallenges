from threading import Thread
import random
import time
from queue import Queue

queue = Queue(10)
nums = [i for i in range(0,5)]
print(nums)

class Producer(Thread):
    def run(self):
        while True:
            num = random.choice(nums)
            queue.put(num)
            print("Producer put {}".format(num))
            time.sleep(random.random())


class Consumer(Thread):
    def run(self):
        while True:
            num = queue.get()
            print("Consumer get {}".format(num))
            time.sleep(random.random()*5)

Producer().start()
Consumer().start()



