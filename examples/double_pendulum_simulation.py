# # Double Pendulum Simulation
#
# A double pendulum has two bobs connected in series. A coupled pair of
# nonlinear ordinary differential equations derived from the Lagrangian
# describes their motion. In chaotic motion, small differences in initial
# conditions lead to exponentially diverging trajectories.
#
# Integrate the equations with a fourth-order Runge-Kutta method.
# This example uses NumPy and Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# ## System Parameters

L1, L2 = 1.0, 1.0    # rod lengths, m
m1, m2 = 1.0, 1.0    # bob masses, kg
g       = 9.80665     # gravitational acceleration, m/s²

# ## Equations of Motion
#
# State vector: ``[θ₁, ω₁, θ₂, ω₂]`` where θ are angles from the vertical
# and ω = dθ/dt are angular velocities.

def derivatives(state):
    t1, w1, t2, w2 = state
    dt = t2 - t1
    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(dt)**2
    den2 = (L2 / L1) * den1
    dw1 = (m2 * L1 * w1**2 * np.sin(dt) * np.cos(dt)
           + m2 * g * np.sin(t2) * np.cos(dt)
           + m2 * L2 * w2**2 * np.sin(dt)
           - (m1 + m2) * g * np.sin(t1)) / den1
    dw2 = (- m2 * L2 * w2**2 * np.sin(dt) * np.cos(dt)
           + (m1 + m2) * g * np.sin(t1) * np.cos(dt)
           - (m1 + m2) * L1 * w1**2 * np.sin(dt)
           - (m1 + m2) * g * np.sin(t2)) / den2
    return np.array([w1, dw1, w2, dw2])


def rk4_integrate(state0, dt, n_steps):
    states = np.empty((n_steps + 1, 4))
    states[0] = state0
    s = state0.copy()
    for i in range(n_steps):
        k1 = derivatives(s)
        k2 = derivatives(s + 0.5 * dt * k1)
        k3 = derivatives(s + 0.5 * dt * k2)
        k4 = derivatives(s + dt * k3)
        s  = s + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        states[i + 1] = s
    return states

# ## Simulation
#
# Integrate two trajectories starting from almost identical initial conditions
# to compare their sensitivity to initial conditions.

dt      = 0.005   # time step, s
T_total = 25.0    # total simulation time, s
n_steps = int(T_total / dt)

eps = 1e-6   # Perturbation in θ₁, rad.
state_A = np.array([np.pi / 2, 0.0, np.pi / 2, 0.0])
state_B = state_A + np.array([eps, 0.0, 0.0, 0.0])

traj_A = rk4_integrate(state_A, dt, n_steps)
traj_B = rk4_integrate(state_B, dt, n_steps)
time   = np.linspace(0, T_total, n_steps + 1)

# Cartesian positions of the two bobs for trajectory A
x1 =  L1 * np.sin(traj_A[:, 0])
y1 = -L1 * np.cos(traj_A[:, 0])
x2 =  x1 + L2 * np.sin(traj_A[:, 2])
y2 =  y1 - L2 * np.cos(traj_A[:, 2])

# Angular separation between the two trajectories
separation = np.sqrt((traj_A[:, 0] - traj_B[:, 0])**2 +
                     (traj_A[:, 2] - traj_B[:, 2])**2)

# ## Plotting
#
# Three panels: Cartesian trace of the lower bob, phase portrait (θ₁, ω₁),
# and exponential growth of the angular separation.

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
fig.suptitle("Double pendulum — chaotic dynamics", fontsize=14, fontweight="bold")
# Cartesian trace.
axes[0].plot(x2, y2, linewidth=0.6, color="tab:blue", alpha=0.8)
axes[0].plot(x2[0], y2[0], "go", markersize=7, label="start")
axes[0].plot(x2[-1], y2[-1], "rs", markersize=7, label="end")
axes[0].set_aspect("equal")
axes[0].set_xlabel("x (m)")
axes[0].set_ylabel("y (m)")
axes[0].set_title("Trace of lower bob")
axes[0].legend(fontsize=8)
axes[0].grid(True, linestyle="--", alpha=0.4)
# Phase portrait.
axes[1].plot(traj_A[:, 0], traj_A[:, 1], linewidth=0.5, color="tab:purple", alpha=0.7)
axes[1].set_xlabel("θ₁ (rad)")
axes[1].set_ylabel("ω₁ (rad/s)")
axes[1].set_title("Phase portrait — upper bob")
axes[1].grid(True, linestyle="--", alpha=0.4)
# Sensitivity to initial conditions.
valid = separation > 0
axes[2].semilogy(time[valid], separation[valid], color="tab:red", linewidth=1.4)
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Angular separation (rad)")
axes[2].set_title(f"Sensitivity (Δθ₁₀ = {eps:.0e} rad)")
axes[2].grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

# ## Energy Conservation Check

KE = 0.5*(m1+m2)*L1**2*traj_A[:,1]**2 + 0.5*m2*L2**2*traj_A[:,3]**2 \
   + m2*L1*L2*traj_A[:,1]*traj_A[:,3]*np.cos(traj_A[:,0]-traj_A[:,2])
PE = -(m1+m2)*g*L1*np.cos(traj_A[:,0]) - m2*g*L2*np.cos(traj_A[:,2])
E  = KE + PE
E_drift = E[-1] - E[0]
print(f"Initial energy : {E[0]:.6f} J")
print(f"Final energy   : {E[-1]:.6f} J")
print(f"Absolute drift : {abs(E_drift):.6f} J")
