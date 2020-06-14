import math
import random
import time

print("Pi value :"+str(math.pi))
print("Random  value :"+str(random.random()))
print("Random  INT value :"+str(random.randint(1,10)))
print("Random  CHOICE value :"+str(random.choices([1,10,25,12])))
print("Random  CHOICE value :{0}".format(random.choices([1,10,25,12])))

print(time.localtime())