# Calculus Visualizer: Integration & Differentiation

This repository contains Python scripts that provide interactive and animated visualizations of fundamental calculus concepts. Built with `matplotlib` and `numpy`, these tools are designed to help conceptualize how integration and differentiation work under the hood.

##  Features

* **Integration Animation (`Integration.py`)**: 
    * Animates the process of approximating the area under a curve using Riemann sums.
    * Dynamically increases the number of slices (rectangles) to demonstrate how the approximation converges to the true area.
    * Visualizes the function f(x) = cos(x) + 1.5 with real-time updates of the calculated area.

* **Interactive Differentiation (`diffrentiation.py`)**: 
    * Provides an interactive slider to explore the derivative of f(x) = x^2 at various points.
    * Dynamically plots the tangent line at a selected point in real-time.
    * Displays the exact mathematical calculation of the derivative at the chosen coordinate using the limit definition of a derivative.

##  Requirements

To run these scripts, you will need Python installed along with the following libraries:

* `numpy`
* `matplotlib`

You can install the required dependencies using pip:

pip install numpy matplotlib

##  How to Run

Clone the repository and run the scripts directly from your terminal or command prompt:

1. **For the Integration Animation:**
   python Integration.py

2. **For the Interactive Derivative Tool:**
   python diffrentiation.py

##  Future Improvements

* Implement a Graphical User Interface (GUI) using Tkinter or PyQt5 to allow users to input custom mathematical functions natively.
* Add features to visualize physics concepts, such as velocity and acceleration derived from position graphs.