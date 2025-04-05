import numpy as np
import matplotlib.pyplot as plt


n_values = [1000, 2000, 3000, 4000, 5000]


mean_list = []
std_list = []

b_values = [0, 100, 200, 300, 400, 500, 600, 800]
c_values = [500, 600, 700, 800]
c_probs = [0.20, 0.30, 0.15, 0.35]

for n in n_values:
    A = np.random.exponential(scale=200, size=n)
    B = np.random.choice(b_values, size=n)
    C = np.random.choice(c_values, size=n, p=c_probs)
    D = np.random.normal(loc=100, scale=20, size=n)
    E = np.random.normal(loc=100, scale=20, size=n)

    
    F = (6*A*B + 10*C) / (4*D*E)

    mean_list.append(np.mean(F))
    std_list.append(np.std(F))

# Plotting
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(n_values, mean_list, marker='o')
plt.title('Estimated Mean of F vs. n')
plt.xlabel('n')
plt.ylabel('Mean of F')

plt.subplot(1, 2, 2)
plt.plot(n_values, std_list, marker='o', color='orange')
plt.title('Estimated Std Dev of F vs. n')
plt.xlabel('n')
plt.ylabel('Standard Deviation of F')

plt.tight_layout()
plt.show()
