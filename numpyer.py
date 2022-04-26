import random
import numpy as np
from sys import getsizeof as sizeof
import matplotlib.pyplot as plt
%matplotlib inline

data = [random.uniform(2, 50) for x in range(5)]
ndata = np.array(data)
print(ndata)
print(f"Size of data sequence: {sizeof(data)}. Size of numpy sequence: {sizeof(ndata)}")

plt.plot(ndata)
plt.show()
