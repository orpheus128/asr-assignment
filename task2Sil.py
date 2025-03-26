# from matplotlib import pyplot as plt
# import numpy as np

# y = [172.57, 74.55, 79.14, 49.08]

# plt.title("Effect of Self-Loop Probability on WER")
# plt.bar(x_pos, y)
# plt.xticks(x_pos, x)
# plt.yticks(np.arange(0, 200, 20))
# plt.ylabel("Word Error Rate (%)")
# plt.xlabel("Self Loop Probability (%)")
# plt.grid()
# plt.show()

# data from https://allisonhorst.github.io/palmerpenguins/

import matplotlib.pyplot as plt
import numpy as np

x_labels = ("Baseline Parameters", "Best Parameters")
y_values={
    "Without Silence": (172.57, 79.14),
    "With Silence": (74.55, 49.08)
}

x = np.arange(len(x_labels))
width = 0.35  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in y_values.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Word Error Rate (%)')
ax.set_title('Effects of Silence on WER')
ax.set_xticks(x + (width/2), x_labels)
ax.legend(loc='upper right')
ax.set_ylim(0, 200)

plt.show()