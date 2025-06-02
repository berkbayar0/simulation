import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib


np.random.seed(42)
alpha = 1.2
beta = 0.8
size = 100
generated_data = 2.3 + np.random.weibull(alpha, size) * beta

distributions_to_try = {
    'norm': stats.norm,
    'expon': stats.expon,
    'gamma': stats.gamma,
    'lognorm': stats.lognorm,
    'weibull_min': stats.weibull_min,
    'weibull_max': stats.weibull_max,
    'beta': stats.beta,
    'uniform': stats.uniform
}

results = []

for name, dist in distributions_to_try.items():
    try:
        params = dist.fit(generated_data)
        loglik = np.sum(dist.logpdf(generated_data, *params))
        ks_stat, ks_p = stats.kstest(generated_data, name, args=params)
        results.append({
            "distribution": name,
            "log_likelihood": loglik,
            "ks_statistic": ks_stat,
            "ks_pvalue": ks_p,
            "params": params
        })
    except Exception:
        continue

df_results = pd.DataFrame(results)
df_sorted = df_results.sort_values(by="log_likelihood", ascending=False).reset_index(drop=True)

# İlk 3 dağılım ve parametreleri
top3 = df_sorted.head(3)
dist_names = top3['distribution'].values
params_list = top3['params'].values

x = np.linspace(min(generated_data), max(generated_data), 1000)

plt.figure(figsize=(10, 6))
plt.hist(generated_data, bins=20, density=True, alpha=0.5, color='gray', label='Histogram')

for name, params in zip(dist_names, params_list):
    dist = getattr(stats, name)
    try:
        pdf_vals = dist.pdf(x, *params)
        plt.plot(x, pdf_vals, linewidth=2, label=f'{name}')
    except Exception as e:
        print(f"{name} çizilemedi: {e}")
        continue

plt.yscale("log")
plt.title("Histogram + Top 3 Fitted Distributions (Log Scale)")
plt.xlabel("Value")
plt.ylabel("Density (log scale)")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig("part2c_fit_plot.png", dpi=300)
plt.show()
