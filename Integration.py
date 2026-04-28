import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return np.cos(x) + 1.5

a, b = 0, 20
x_curve = np.linspace(a, b, 1000)
y_curve = f(x_curve)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_curve, y_curve, 'b', lw=2)
ax.set_title("Approximating Area Under f(x) with Riemann Sums", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylim(0, 3)
ax.grid(True, alpha=0.5)

fill_area = ax.fill_between([], [], color='cyan', alpha=0.5, step='pre')
text_disp = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontfamily='monospace')

def animate(frame):
    n = int(1.1**frame) + 1 if int(1.3**frame) + 1 < 10000 else 10000
    
    dx = (b - a) / n
    x_steps = np.linspace(a, b, n + 1)
    y_steps = f(x_steps)
    
    global fill_area
    fill_area.remove()
    fill_area = ax.fill_between(x_steps, y_steps, step='mid', color='black', alpha=0.9)
    
    current_area = np.sum(y_steps[:-1] * dx)
    text_disp.set_text(f"Slices: {n}\nArea:   {current_area:.4f}")
    
    return fill_area, text_disp

ani = animation.FuncAnimation(fig, animate, frames=150, interval=60, blit=False)
plt.show()