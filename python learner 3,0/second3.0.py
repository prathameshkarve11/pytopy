from numpy import random
import numpy as np
import math

x = random.randint(10 , size=(4,4))
print(x)

y=np.floor(random.rand(4) *6)
print(y)

random.shuffle(x)