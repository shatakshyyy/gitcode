import matplotlib.pyplot as plt

x = [1, 2, 3, 6]
y = [4, 6, 2, 8]
m_s = ["^", "*", "s", "o"]

plt.plot(x, y, marker = m_s[0], markerfacecolor = "red", markeredgecolor = "white")

for i, marker in enumerate(m_s):
    plt.plot(x[i], y[i], marker = m_s[i])

plt.legend()
plt.show()    