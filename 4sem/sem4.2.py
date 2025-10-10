import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

fig = plt.figure(figsize = (10, 15))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

plt.subplots_adjust(hspace=0.5)


n1 = 50
n2 = 500
n3 = 5000


values1 = np.random.normal(0, 1, n1)
values2 = np.random.normal(0, 1, n2)
values3 = np.random.normal(0, 1, n3)

ax1.hist(values1, bins = 50, density=True)
ax2.hist(values2, bins = 50, density=True)
ax3.hist(values3, bins = 50, density=True)

x = [-4 + i * (8 / 999) for i in range(1000)]
theoretical_pdf = norm.pdf(x, 0, 1)

ax1.plot(x, theoretical_pdf, linewidth=2)
ax2.plot(x, theoretical_pdf, linewidth=2)
ax3.plot(x, theoretical_pdf, linewidth=2)

ax1.set_title('Нориальное распределение для 50 точек')
ax2.set_title('Нориальное паспределение для 500 точек')
ax3.set_title('Нориальоное распределение для 5000 точек')

plt.show()
