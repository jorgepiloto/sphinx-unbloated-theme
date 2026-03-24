# # Projectile motion with drag
#
# This example simulates the trajectory of a projectile launched at different
# angles under gravity and quadratic air drag. The equations of motion are
# integrated with a simple 4th-order Runge-Kutta scheme — no external solver
# required.
#
# Only NumPy and Matplotlib are needed.

import numpy as np
import matplotlib.pyplot as plt

# ## Physical parameters
#
# All quantities are in SI units. The drag coefficient combines the air
# density, cross-sectional area, and drag coefficient into a single constant
# ``b`` so that the drag force is ``F_drag = -b * v * |v|``.

g   = 9.80665   # gravitational acceleration, m/s²
v0  = 60.0      # launch speed, m/s
b   = 0.003     # drag constant, kg/m  (≈ baseball-sized sphere)
m   = 0.145     # projectile mass, kg

# ## RK4 integrator
#
# The state vector is ``[x, y, vx, vy]``.  The equations of motion are
# ``ax = -(b/m)*v*vx`` and ``ay = -g - (b/m)*v*vy``.

def derivatives(state):
    x, y, vx, vy = state
    v  = np.sqrt(vx**2 + vy**2)
    ax = -(b / m) * v * vx
    ay = -g - (b / m) * v * vy
    return np.array([vx, vy, ax, ay])


def rk4_step(state, dt):
    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)
    return state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)


def simulate(angle_deg, dt=0.01):
    """Simulate until the projectile hits the ground (y ≤ 0 after launch)."""
    theta = np.radians(angle_deg)
    state = np.array([0.0, 0.0, v0 * np.cos(theta), v0 * np.sin(theta)])
    xs, ys = [state[0]], [state[1]]
    while True:
        state = rk4_step(state, dt)
        xs.append(state[0])
        ys.append(state[1])
        if state[1] < 0 and len(xs) > 2:
            break
    return np.array(xs), np.array(ys)

# ## Computing trajectories
#
# Simulate for seven launch angles from 15° to 75°.

angles = [15, 25, 35, 45, 55, 65, 75]
trajectories = {a: simulate(a) for a in angles}

# Vacuum trajectories for comparison (b = 0 ⟹ parabolic arc)
def simulate_vacuum(angle_deg, dt=0.01):
    theta = np.radians(angle_deg)
    vx0, vy0 = v0 * np.cos(theta), v0 * np.sin(theta)
    t_flight = 2 * vy0 / g
    t = np.linspace(0, t_flight, 500)
    return vx0 * t, vy0 * t - 0.5 * g * t**2

vacuum = {a: simulate_vacuum(a) for a in angles}

# ## Plotting
#
# Left panel: trajectories with drag. Right panel: range comparison.

cmap   = plt.cm.plasma
colors = [cmap(i / (len(angles) - 1)) for i in range(len(angles))]

fig, (ax_traj, ax_range) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Projectile motion with quadratic air drag", fontsize=14, fontweight="bold")
# --- trajectories panel ---
for (angle, color) in zip(angles, colors):
    x, y = trajectories[angle]
    xv, yv = vacuum[angle]
    ax_traj.plot(x, y, color=color, linewidth=1.8, label=f"{angle}°")
    ax_traj.plot(xv, yv, color=color, linewidth=0.8, linestyle="--", alpha=0.5)
ax_traj.set_xlabel("Horizontal distance (m)")
ax_traj.set_ylabel("Height (m)")
ax_traj.set_title("Trajectories (solid = drag, dashed = vacuum)")
ax_traj.set_ylim(bottom=0)
ax_traj.grid(True, linestyle="--", alpha=0.5)
ax_traj.legend(title="Launch angle", fontsize=8)
# --- range comparison panel ---
ranges_drag   = [trajectories[a][0][-1] for a in angles]
ranges_vacuum = [vacuum[a][0][-1] for a in angles]
ax_range.plot(angles, ranges_drag,   "o-", color="tab:blue",   linewidth=1.8, label="With drag")
ax_range.plot(angles, ranges_vacuum, "s--", color="tab:orange", linewidth=1.8, label="Vacuum")
ax_range.set_xlabel("Launch angle (°)")
ax_range.set_ylabel("Range (m)")
ax_range.set_title("Range vs. launch angle")
ax_range.grid(True, linestyle="--", alpha=0.5)
ax_range.legend()
plt.tight_layout()
plt.show()

# ## Key results

opt_drag   = angles[np.argmax(ranges_drag)]
opt_vacuum = angles[np.argmax(ranges_vacuum)]
print(f"Optimal angle (drag)   : {opt_drag}°  →  range = {max(ranges_drag):.1f} m")
print(f"Optimal angle (vacuum) : {opt_vacuum}°  →  range = {max(ranges_vacuum):.1f} m")
