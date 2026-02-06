import numpy as np
import matplotlib.pyplot as plt
# Parameters
k1 = 0.03
k2 = 0.01
dt = 0.1
steps = 30
# Initial concentrations
c1 = [50.0] # Reactant A
c2 = [25.0] # Reactant B
c3 = [0.0] # Product C
# Open a file to write the results
with open("output.txt", "w") as file:
# Write initial concentrations
    file.write(f"{c1[0]} {c2[0]} {c3[0]}\n")
# Time-stepping loop for concentration updates
    for i in range(steps):
# Calculate next concentrations based on the given equations
        c1_next = c1[i] + (k2 * c3[i] - k1 * c1[i] * c2[i]) * dt
        c2_next = c2[i] + (k2 * c3[i] - k1 * c1[i] * c2[i]) * dt
        c3_next = c3[i] + (2 * k1 * c1[i] * c2[i] - 2 * k2 * c3[i]) * dt
# Append the new concentrations to the lists
        c1.append(c1_next)
        c2.append(c2_next)
        c3.append(c3_next)

# Write concentrations to the file
        file.write(f"{c1_next} {c2_next} {c3_next}\n")
# Time points for plotting
time_points = np.arange(0, (steps + 1) * dt, dt)
# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(time_points, c1, label='Concentration of c1', color='blue')
plt.plot(time_points, c2, label='Concentration of c2', color='green')
plt.plot(time_points, c3, label='Concentration of c3', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (mol)')
plt.title('Concentration vs Time')
plt.legend()
plt.grid(True)
plt.show()