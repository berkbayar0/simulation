import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(42)
alpha = 1.2
beta = 0.8
size = 100
generated_data = 2.3 + np.random.weibull(alpha, size) * beta

dist_names = ['lognorm', 'weibull_min', 'gamma']
params_list = [stats.lognorm.fit(generated_data),
               stats.weibull_min.fit(generated_data),
               stats.gamma.fit(generated_data)]


num_bins = 10
observed_counts, bin_edges = np.histogram(generated_data, bins=num_bins)

chi_square_results = {}

for name, params in zip(dist_names, params_list):
    dist = getattr(stats, name)
    expected_counts = []
    try:
        for i in range(len(bin_edges)-1):
            prob = dist.cdf(bin_edges[i+1], *params) - dist.cdf(bin_edges[i], *params)
            expected = prob * len(generated_data)
            expected_counts.append(expected)

        expected_counts = np.array(expected_counts)
        expected_counts *= (np.sum(observed_counts) / np.sum(expected_counts))

        # Chi-square testi
        chi2_stat, p_val = stats.chisquare(f_obs=observed_counts, f_exp=expected_counts)
        chi_square_results[name] = (round(chi2_stat, 4), round(p_val, 6))
    except Exception as e:
        print(f"{name} için hata: {e}")
        continue

for dist_name, (chi2, pval) in chi_square_results.items():
    print(f"{dist_name} -> Chi2: {chi2}, p-value: {pval}")
