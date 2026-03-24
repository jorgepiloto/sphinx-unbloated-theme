# # Fourier series approximation
#
# A **Fourier series** decomposes a periodic function into a sum of sines and
# cosines. This example approximates a square wave and a sawtooth wave with an
# increasing number of harmonics, illustrating both convergence and the
# **Gibbs phenomenon** — the persistent ~9 % overshoot near a discontinuity.
#
# Only NumPy and Matplotlib are needed.

import numpy as np
import matplotlib.pyplot as plt

# ## Target waveforms
#
# Both waveforms have period 2π, unit amplitude, and known Fourier series:
#
# * **Square wave**: ``f(t) = (4/π) Σₙ sin((2n−1)t) / (2n−1)``
# * **Sawtooth wave**: ``f(t) = (2/π) Σₙ (−1)^(n+1) sin(nt) / n``

t = np.linspace(-np.pi, np.pi, 2_000)

def square_wave(t, N):
    """Partial Fourier sum of a square wave with N harmonics."""
    result = np.zeros_like(t)
    for k in range(1, N + 1):
        n = 2 * k - 1
        result += np.sin(n * t) / n
    return (4 / np.pi) * result


def sawtooth_wave(t, N):
    """Partial Fourier sum of a sawtooth wave with N harmonics."""
    result = np.zeros_like(t)
    for n in range(1, N + 1):
        result += ((-1) ** (n + 1)) * np.sin(n * t) / n
    return (2 / np.pi) * result

# ## Computing approximations
#
# Evaluate partial sums for several values of N.

harmonics = [1, 3, 5, 11, 51]
square_approx   = {N: square_wave(t, N)   for N in harmonics}
sawtooth_approx = {N: sawtooth_wave(t, N) for N in harmonics}

# Exact waveforms (sign function)
square_exact   = np.sign(np.sin(t))
sawtooth_exact = t / np.pi   # normalised to [−1, 1] on (−π, π)

# ## Plotting
#
# Two rows (square / sawtooth), colour-coded by number of harmonics.

cmap   = plt.cm.viridis
colors = [cmap(i / (len(harmonics) - 1)) for i in range(len(harmonics))]

fig, axes = plt.subplots(2, 2, figsize=(13, 8))
fig.suptitle("Fourier series approximation", fontsize=14, fontweight="bold")
# --- square wave: approximation panel ---
axes[0, 0].plot(t, square_exact, "k--", linewidth=1.0, alpha=0.4, label="exact")
for N, color in zip(harmonics, colors):
    axes[0, 0].plot(t, square_approx[N], color=color, linewidth=1.4, label=f"N = {N}")
axes[0, 0].set_title("Square wave — partial sums")
axes[0, 0].set_xlabel("t (rad)")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].legend(fontsize=8, loc="upper right")
axes[0, 0].grid(True, linestyle="--", alpha=0.4)
# --- square wave: Gibbs phenomenon zoom ---
mask = (t > 0.0) & (t < 0.6)
axes[0, 1].plot(t[mask], square_exact[mask], "k--", linewidth=1.2, alpha=0.5, label="exact")
for N, color in zip(harmonics, colors):
    axes[0, 1].plot(t[mask], square_approx[N][mask], color=color, linewidth=1.4, label=f"N = {N}")
axes[0, 1].set_title("Square wave — Gibbs phenomenon (zoom)")
axes[0, 1].set_xlabel("t (rad)")
axes[0, 1].set_ylabel("Amplitude")
axes[0, 1].legend(fontsize=8)
axes[0, 1].grid(True, linestyle="--", alpha=0.4)
# --- sawtooth wave: approximation panel ---
axes[1, 0].plot(t, sawtooth_exact, "k--", linewidth=1.0, alpha=0.4, label="exact")
for N, color in zip(harmonics, colors):
    axes[1, 0].plot(t, sawtooth_approx[N], color=color, linewidth=1.4, label=f"N = {N}")
axes[1, 0].set_title("Sawtooth wave — partial sums")
axes[1, 0].set_xlabel("t (rad)")
axes[1, 0].set_ylabel("Amplitude")
axes[1, 0].legend(fontsize=8, loc="upper right")
axes[1, 0].grid(True, linestyle="--", alpha=0.4)
# --- error vs N ---
N_range = np.arange(1, 101)
rms_sq  = [np.sqrt(np.mean((square_wave(t, N) - square_exact)**2))   for N in N_range]
rms_saw = [np.sqrt(np.mean((sawtooth_wave(t, N) - sawtooth_exact)**2)) for N in N_range]
axes[1, 1].loglog(N_range, rms_sq,  color="tab:blue",   linewidth=1.8, label="Square")
axes[1, 1].loglog(N_range, rms_saw, color="tab:orange",  linewidth=1.8, label="Sawtooth")
axes[1, 1].set_title("RMS error vs. number of harmonics")
axes[1, 1].set_xlabel("N harmonics")
axes[1, 1].set_ylabel("RMS error")
axes[1, 1].legend(fontsize=9)
axes[1, 1].grid(True, which="both", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

# ## Gibbs overshoot

peak_sq = max(square_approx[harmonics[-1]])
jump    = 2.0   # total jump height of the square wave (from −1 to +1)
print(f"Peak amplitude (N={harmonics[-1]}) : {peak_sq:.4f}  (exact = 1.0)")
print(f"Gibbs overshoot                    : {(peak_sq - 1.0)/jump*100:.2f} % of jump height (theoretical ≈ 8.9 %)")
