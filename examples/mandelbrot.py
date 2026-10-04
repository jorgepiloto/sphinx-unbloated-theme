# # Mandelbrot Set
#
# The Mandelbrot set contains complex numbers ``c`` for which the iteration
# ``zₙ₊₁ = zₙ² + c``, starting from ``z₀ = 0``, does not diverge.
# Color escaping points by their escape count to show the fractal boundary.
#
# Compute the iterations with NumPy complex arrays and plot them with
# Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# ## Grid Definition
#
# Build a complex-valued array whose real and imaginary parts sample the
# region of interest in the complex plane.

WIDTH, HEIGHT = 800, 600
MAX_ITER      = 256
ESCAPE_RADIUS = 2.0

x_min, x_max = -2.5,  1.0
y_min, y_max = -1.25, 1.25

x = np.linspace(x_min, x_max, WIDTH)
y = np.linspace(y_min, y_max, HEIGHT)
C = x[np.newaxis, :] + 1j * y[:, np.newaxis]

# ## Iteration
#
# Track the escape count for each point. Use fractional counts for smooth
# coloring to avoid bands from integer thresholds.

Z       = np.zeros_like(C)
counts  = np.zeros(C.shape, dtype=float)
escaped = np.zeros(C.shape, dtype=bool)

for i in range(MAX_ITER):
    mask      = ~escaped
    Z[mask]   = Z[mask] ** 2 + C[mask]
    newly_escaped = mask & (np.abs(Z) > ESCAPE_RADIUS)
    # Use a fractional escape count for smooth coloring.
    counts[newly_escaped] = i + 1 - np.log2(np.log2(np.abs(Z[newly_escaped])))
    escaped |= newly_escaped

# Leave points that did not escape within MAX_ITER at 0.
counts[~escaped] = 0.0

# ## Zoom into Seahorse Valley
#
# Zoom into Seahorse Valley to show its self-similar structure.

x2 = np.linspace(-0.76, -0.73, WIDTH)
y2 = np.linspace(0.10,  0.14,  HEIGHT)
C2 = x2[np.newaxis, :] + 1j * y2[:, np.newaxis]
Z2      = np.zeros_like(C2)
counts2 = np.zeros(C2.shape, dtype=float)
escaped2 = np.zeros(C2.shape, dtype=bool)

for i in range(MAX_ITER):
    mask       = ~escaped2
    Z2[mask]   = Z2[mask] ** 2 + C2[mask]
    newly      = mask & (np.abs(Z2) > ESCAPE_RADIUS)
    counts2[newly] = i + 1 - np.log2(np.log2(np.abs(Z2[newly])))
    escaped2 |= newly

counts2[~escaped2] = 0.0

# ## Plotting

fig, (ax_full, ax_zoom) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Mandelbrot set", fontsize=14, fontweight="bold")
# Full view.
ax_full.imshow(counts, origin="lower", extent=[x_min, x_max, y_min, y_max],
               cmap="inferno", interpolation="bilinear")
ax_full.set_title("Full view")
ax_full.set_xlabel("Re(c)")
ax_full.set_ylabel("Im(c)")
rect_x = [x2[0], x2[-1], x2[-1], x2[0], x2[0]]
rect_y = [y2[0], y2[0], y2[-1], y2[-1], y2[0]]
ax_full.plot(rect_x, rect_y, "w-", linewidth=1.2)
# Zoom.
ax_zoom.imshow(counts2, origin="lower", extent=[x2[0], x2[-1], y2[0], y2[-1]],
               cmap="inferno", interpolation="bilinear")
ax_zoom.set_title("Seahorse Valley (zoom)")
ax_zoom.set_xlabel("Re(c)")
ax_zoom.set_ylabel("Im(c)")
plt.tight_layout()
plt.show()

# ## Statistics

total_points    = WIDTH * HEIGHT
interior_points = int((~escaped).sum())
print(f"Grid size         : {WIDTH} × {HEIGHT} = {total_points:,} points")
print(f"Max iterations    : {MAX_ITER}")
print(f"Interior (set)    : {interior_points:,}  ({interior_points/total_points*100:.1f} %)")
print(f"Exterior (escaped): {total_points - interior_points:,}")
