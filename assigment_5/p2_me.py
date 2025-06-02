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

sorted_data = np.sort(generated_data)
ecdf_y = np.arange(1, len(sorted_data)+1) / len(sorted_data)

plt.figure(figsize=(10, 6))

for name, params in zip(dist_names, params_list):
    dist = getattr(stats, name)
    try:
        cdf_theoretical = dist.cdf(sorted_data, *params)
        plt.plot(cdf_theoretical, ecdf_y, 'o', markersize=3, label=name)
    except Exception as e:
        print(f"{name} çizilemedi: {e}")
        continue

plt.plot([0, 1], [0, 1], 'k--', label='45° line')

plt.xlabel('Theoretical CDF')
plt.ylabel('Empirical CDF')
plt.title('Part 2.e: P–P Plot (Top 3 Distributions)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("part2e_pp_plot.png", dpi=300)
plt.show()
