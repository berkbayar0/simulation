import numpy as np
import matplotlib.pyplot as plt


n = 5000

b_values = [0, 100, 200, 300, 400, 500, 600, 800]
c_values = [500, 600, 700, 800]
c_probs = [0.20, 0.30, 0.15, 0.35]

A = np.random.exponential(scale=200, size=n)
B = np.random.choice(b_values, size=n)
C = np.random.choice(c_values, size=n, p=c_probs)
D = np.random.normal(loc=100, scale=20, size=n)
E = np.random.normal(loc=100, scale=20, size=n)

F = (6*A*B + 10*C) / (4*D*E)

plt.figure(figsize=(8, 5))
plt.hist(F, bins=50, color='skyblue', edgecolor='black')
plt.title('Histogram of F (n = 5000)')
plt.xlabel('F values')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
