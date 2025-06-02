import numpy as np
import scipy.stats as stats
import pandas as pd

np.random.seed(42)
alpha = 1.2
beta = 0.8
size = 100
generated_data = 2.3 + np.random.weibull(alpha, size) * beta

dist_names = ['lognorm', 'weibull_min', 'gamma']
params_list = [stats.lognorm.fit(generated_data),
               stats.weibull_min.fit(generated_data),
               stats.gamma.fit(generated_data)]


ks_results = []

for name, params in zip(dist_names, params_list):
    dist = getattr(stats, name)
    try:
        ks_stat, p_value = stats.kstest(generated_data, name, args=params)
        ks_results.append({
            "distribution": name,
            "ks_statistic": round(ks_stat, 5),
            "p_value": round(p_value, 5)
        })
    except Exception as e:
        print(f"{name} için hata: {e}")
        continue

df_ks = pd.DataFrame(ks_results)
df_ks_sorted = df_ks.sort_values(by="p_value", ascending=False).reset_index(drop=True)
print(df_ks_sorted)
