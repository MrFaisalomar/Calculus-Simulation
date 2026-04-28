import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f(x):
    return x**2

def f_prime(x):
    return 2 * x

def calculate_derivative_at_point(func, point, h=1e-5):
    return (func(point + h) - func(point - h)) / (2 * h)

a, b = 0 , 10
x_curve = np.linspace(a, b, 1000) 
y_curve = f(x_curve) 

fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.15) 

ax.plot(x_curve, y_curve, 'r', lw=2.5)
ax.set_title("Function and Its Derivative", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("f(x)", fontsize=14)
ax.set_ylim(0, 100)
ax.set_xlim(a, b)
ax.grid(True, alpha=0.3)

x0 = 5 
y0 = f(x0) 
slope = f_prime(x0) 
tangent_line = slope * (x_curve - x0) + y0 
value = calculate_derivative_at_point(f, x0)

# The lines are stored in ax.lines in the order they are plotted:
# ax.lines[0] = the red curve
# ax.lines[1] = the green tangent line
# ax.lines[2] = the blue dot
ax.plot(x_curve, tangent_line, 'g', lw=1.5, label=f"Tangent at x={x0}")
ax.plot(x0, value, 'bo', label=f"Derivative at x={x0}, f(x)={y0}, f'(x)={value:.2f}")
ax.legend()


ax_slider = plt.axes([0.25, 0.05, 0.50, 0.03])
plt.slider = Slider(ax_slider, 'x0', a, b, valinit=x0)

def update(val):
    x0 = plt.slider.val
    y0 = f(x0)
    slope = f_prime(x0)
    tangent_line = slope * (x_curve - x0) + y0
    value = calculate_derivative_at_point(f, x0)
    
    
    ax.lines[1].set_ydata(tangent_line)
    ax.lines[1].set_label(f"Tangent at x={x0:.2f}") 
    
    
    ax.lines[2].set_data([x0], [value]) 
    ax.lines[2].set_label(f"Derivative at x={x0:.2f}, f(x)={y0:.2f}, f'(x)={value:.2f}")
    
    
    ax.legend() 
    
    
    fig.canvas.draw_idle() 

plt.slider.on_changed(update)
plt.show()