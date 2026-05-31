# The Project
This project simulates the tragectory and the rocket's velocity as a function of time by solving the differential equations describing the motion of the vehicle.
The user can  type in the console the initial velocity and the initial launch angle(in degrees).
The physics of the rocket flight is expalined here: 
# Features
-Physics-based program
-The numerical solving of the equations is done by solve_ivp from scipy.integrate 
-The visualization of the trajectory and velocity graphs is doene by pyplot form matplotlib
-The graphs are animated via FucAnimation from matplotlib.animation using 'update' function
# How to Run
```bash
pip install matplotlib numpy scipy
python rocket_launch_simulator.py
