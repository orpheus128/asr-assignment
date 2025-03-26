from matplotlib import pyplot as plt
import numpy as np

sl_y_values = [172.57, 180.08, 95.22, 79.14]
sl_x_values = [10, 30, 50, 90]

plt.title("Effect of Self-Loop Probability on WER")
plt.plot(sl_x_values, sl_y_values)
plt.xticks(np.arange(10, 100, 10))
plt.yticks(np.arange(0, 200, 20))
plt.ylabel("Word Error Rate (%)")
plt.xlabel("Self Loop Probability (%)")
plt.grid()
plt.show()