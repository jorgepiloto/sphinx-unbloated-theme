# # Heat Equation with Finite Differences
#
# The 1-D heat equation describes how temperature diffuses through a
# material over time:
#
# $$\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}$$
#
# where ``α`` is the thermal diffusivity (m²/s). This example solves the
# equation on a finite rod using an explicit Euler finite-difference scheme
# and plots how an initial temperature spike diffuses over time.
#
# This example uses NumPy and Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# ## Domain and Numerical Parameters
#
# The explicit scheme is stable when the Courant-Friedrichs-Lewy (CFL)
# condition ``r = α·Δt/Δx² ≤ 0.5`` is satisfied.

L      = 1.0       # rod length, m
alpha  = 1e-4      # thermal diffusivity of steel, m²/s
T_ends = 0.0       # fixed temperature at both ends (Dirichlet BC), °C

Nx   = 100          # number of spatial grid points
dx   = L / (Nx - 1)
r    = 0.45         # CFL number (< 0.5 for stability)
dt   = r * dx**2 / alpha
t_end = 500.0       # total simulation time, s
Nt   = int(t_end / dt)

x = np.linspace(0, L, Nx)

# ## Initial Condition
#
# Start with a Gaussian temperature profile centered at the rod midpoint.

T = np.exp(-200 * (x - 0.5)**2) * 100.0   # °C
T[0]  = T_ends
T[-1] = T_ends

# ## Time Integration
#
# Explicit Euler: ``T[i,n+1] = T[i,n] + r*(T[i+1,n] - 2*T[i,n] + T[i-1,n])``.
# Snapshots are saved at fixed intervals for plotting.

save_times = [0, 50, 100, 200, 500]   # seconds
snapshots  = {}

T_curr = T.copy()
t = 0.0
snapshots[0] = T_curr.copy()

for n in range(Nt):
    T_new = T_curr.copy()
    T_new[1:-1] = T_curr[1:-1] + r * (T_curr[2:] - 2*T_curr[1:-1] + T_curr[:-2])
    T_new[0]  = T_ends
    T_new[-1] = T_ends
    T_curr = T_new
    t += dt
    for ts in save_times[1:]:
        if ts not in snapshots and t >= ts:
            snapshots[ts] = T_curr.copy()

# ## Plotting
#
# Left panel: temperature profiles at each saved time. Right panel: heatmap
# showing the temperature over time, subsampled to limit the array size.

subsample   = max(1, Nt // 300)
T_history   = np.empty((Nt // subsample + 1, Nx))
T_curr      = T.copy()
T_history[0] = T_curr
step = 0
for n in range(Nt):
    T_new = T_curr.copy()
    T_new[1:-1] = T_curr[1:-1] + r * (T_curr[2:] - 2*T_curr[1:-1] + T_curr[:-2])
    T_new[0]  = T_ends
    T_new[-1] = T_ends
    T_curr = T_new
    if (n + 1) % subsample == 0:
        step += 1
        if step < T_history.shape[0]:
            T_history[step] = T_curr

fig, (ax_prof, ax_heat) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("1-D heat equation — diffusion of a Gaussian hot-spot", fontsize=14, fontweight="bold")
# Profiles panel.
cmap_lines = plt.cm.YlOrRd
n_snaps    = len(save_times)
for idx, ts in enumerate(save_times):
    if ts in snapshots:
        color = cmap_lines(0.2 + 0.8 * idx / (n_snaps - 1))
        ax_prof.plot(x * 100, snapshots[ts], color=color, linewidth=1.8, label=f"t = {ts} s")
ax_prof.set_xlabel("Position (cm)")
ax_prof.set_ylabel("Temperature (°C)")
ax_prof.set_title("Temperature profiles")
ax_prof.legend(fontsize=8)
ax_prof.grid(True, linestyle="--", alpha=0.5)
# Heatmap panel.
t_axis = np.linspace(0, t_end, T_history.shape[0])
im = ax_heat.imshow(T_history, origin="lower", aspect="auto",
                    extent=[0, 100, 0, t_end],
                    cmap="YlOrRd", vmin=0)
ax_heat.set_xlabel("Position (cm)")
ax_heat.set_ylabel("Time (s)")
ax_heat.set_title("Space–time evolution")
plt.colorbar(im, ax=ax_heat, label="Temperature (°C)")
plt.tight_layout()
plt.show()

# ## Grid and Temperature Statistics

print(f"Grid points   : {Nx}")
print(f"Time step dt  : {dt:.4f} s  (CFL r = {r})")
print(f"Total steps   : {Nt}")
print(f"Peak T at t=0 : {T.max():.1f} °C")
print(f"Peak T at t={t_end:.0f}s: {T_curr.max():.4f} °C")
