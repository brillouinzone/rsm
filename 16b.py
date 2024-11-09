import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x=np.linspace(-10,10,100)


plt.plot(x,(x+5)/x)
plt.ylim([-10,10])

plt.show()
