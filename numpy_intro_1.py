import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # line plot
plt.plot(x, y, 'o')  # dot plot
plt.show()           # <-- shows the plot (not needed with Ipython)

# color map
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()

y = np.sin(x)
plt.legend = "Sinus"
plt.plot(x,y)
plt.show()
