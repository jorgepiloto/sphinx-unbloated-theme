# # Central limit theorem
#
# The **Central Limit Theorem** (CLT) states that the normalised sum of
# independent, identically distributed random variables converges to a standard
# normal distribution as the sample size grows — regardless of the shape of
# the underlying distribution.
#
# This example draws samples from three very different distributions (uniform,
# exponential, and Poisson), forms running averages of increasing size ``n``,
# and shows the histograms of the standardised sums converging to ``N(0, 1)``.
#
# Only NumPy and Matplotlib are needed.

import numpy as np
import matplotlib.pyplot as plt

# ## Setup

rng     = np.random.default_rng(seed=0)
N_draws = 50_000    # number of independent sums per experiment
n_sizes = [1, 2, 5, 30]   # sample sizes to demonstrate

# ## Sampling functions
#
# Each returns an ``(N_draws, n)`` array of i.i.d. samples together with the
# population mean ``μ`` and standard deviation ``σ`` for standardisation.

def sample_uniform(n):
    X = rng.uniform(0, 1, size=(N_draws, n))
    return X, 0.5, np.sqrt(1 / 12)


def sample_exponential(n):
    lam = 1.0
    X = rng.exponential(scale=1 / lam, size=(N_draws, n))
    return X, 1 / lam, 1 / lam


def sample_poisson(n):
    lam = 3.0
    X = rng.poisson(lam=lam, size=(N_draws, n))
    return X, lam, np.sqrt(lam)

# ## Computing standardised sums
#
# For each distribution and each ``n``, compute ``Z = (X̄ - μ) / (σ / √n)``.

distributions = [
    ("Uniform [0, 1]",   sample_uniform),
    ("Exponential(λ=1)", sample_exponential),
    ("Poisson(λ=3)",     sample_poisson),
]

z_normal = np.linspace(-4, 4, 300)
pdf_normal = np.exp(-0.5 * z_normal**2) / np.sqrt(2 * np.pi)

# ## Plotting
#
# Grid: rows = distributions, columns = sample sizes n.

fig, axes = plt.subplots(len(distributions), len(n_sizes),
                         figsize=(14, 9), sharex=True, sharey=False)
fig.suptitle("Central Limit Theorem — convergence to N(0, 1)", fontsize=14, fontweight="bold")
for row, (dist_name, sampler) in enumerate(distributions):
    for col, n in enumerate(n_sizes):
        ax = axes[row, col]
        X, mu, sigma = sampler(n)
        Z = (X.mean(axis=1) - mu) / (sigma / np.sqrt(n))
        ax.hist(Z, bins=60, density=True, color="tab:blue", alpha=0.6, edgecolor="none")
        ax.plot(z_normal, pdf_normal, color="tab:red", linewidth=1.6)
        ax.set_xlim(-4, 4)
        ax.grid(True, linestyle="--", alpha=0.4)
        if row == 0:
            ax.set_title(f"n = {n}", fontsize=10)
        if col == 0:
            ax.set_ylabel(dist_name, fontsize=9)
        if row == len(distributions) - 1:
            ax.set_xlabel("Z")
plt.tight_layout()
plt.show()

# ## Normality check (n = 30)
#
# Verify that the standardised sums are close to N(0, 1) by checking that
# the sample mean and standard deviation match the theoretical values.

print("Standardised sum statistics at n=30 (expect mean≈0, std≈1):")
for dist_name, sampler in distributions:
    X, mu, sigma = sampler(30)
    Z = (X.mean(axis=1) - mu) / (sigma / np.sqrt(30))
    print(f"  {dist_name:<25}  mean = {Z.mean():+.4f}  std = {Z.std():.4f}")
