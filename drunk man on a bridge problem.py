import random
import time
chance = [-1,1]
# calculate the probablilty of reaching 0 or 100
starttime = time.time()

def walkingman():
    position = 17
    number_of_steps = 0
    while 0 < position < 100:
        step = random.choice(chance)
        position += step
    if position >= 100:
        return 1
x = 0
for i in range(10000):
    if walkingman() == 1:
        x += 1

print (x/10000)
print('Single Core took {} seconds'.format(time.time() - starttime))