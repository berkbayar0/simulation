import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(42)
alpha = 1.2
beta = 0.8
size = 100
generated_data = 2.3 + np.random.weibull(alpha, size) * beta

dist_names = ['lognorm', 'weibull_min', 'gamma']
params_list = [stats.lognorm.fit(generated_data),
               stats.weibull_min.fit(generated_data),
               stats.gamma.fit(generated_data)]


def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y

x_emp, y_emp = ecdf(generated_data)

plt.figure(figsize=(10, 6))

for name, params in zip(dist_names, params_list):
    dist = getattr(stats, name)
    try:
        y_theo = dist.cdf(x_emp, *params)
        diff = np.abs(y_emp - y_theo)
        plt.plot(x_emp, diff, label=name, linewidth=2)
    except Exception as e:
        print(f"{name} çizilemedi: {e}")
        continue

plt.title("Part 2.d: |ECDF - CDF| Differences for Top 3 Distributions")
plt.xlabel("Value")
plt.ylabel("Absolute Difference")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("part2d_ecdf_cdf_diff.png", dpi=300)
plt.show()
