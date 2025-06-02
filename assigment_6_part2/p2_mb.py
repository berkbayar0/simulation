import numpy as np
import pandas as pd
import scipy.stats as stats

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

results_part2b = []

for name, dist in distributions_to_try.items():
    try:
        params = dist.fit(generated_data)

        loglik = np.sum(dist.logpdf(generated_data, *params))

        ks_stat, ks_p = stats.kstest(generated_data, name, args=params)
        
        results_part2b.append({
            "distribution": name,
            "log_likelihood": loglik,
            "ks_statistic": ks_stat,
            "ks_pvalue": ks_p,
            "params": params
        })
    except Exception as e:
        print(f"{name} dağılımı hata verdi: {e}")
        continue

df_results = pd.DataFrame(results_part2b)
df_sorted = df_results.sort_values(by="log_likelihood", ascending=False).reset_index(drop=True)

print("Top 3 fitted distributions based on log-likelihood:")
print(df_sorted[['distribution', 'log_likelihood', 'ks_statistic', 'ks_pvalue']].head(3))
