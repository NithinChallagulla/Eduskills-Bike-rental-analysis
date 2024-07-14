import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Draw the highway
highway = plt.Rectangle((0, 4), 10, 2, fc='grey')
ax.add_patch(highway)

# Draw a car on the highway
car, = ax.plot([2, 2.5], [5, 5], 'black', lw=3)

# Initial position of the drone
drone_pos = [0, 9]
drone, = ax.plot(drone_pos[0], drone_pos[1], 'bo', markersize=10)  # Blue drone

# The position of the first aid kit
first_aid, = ax.plot([], [], 'ro', markersize=5)  # Red first aid kit

# Function to initialize the animation
def init():
    drone.set_data([], [])
    first_aid.set_data([], [])
    return drone, first_aid

# Function to animate each frame
def animate(i):
    # Update the drone position
    if drone_pos[1] > 5:
        drone_pos[1] -= 0.1  # Move down
    else:
        drone_pos[0] += 0.1  # Move right
    
    drone.set_data(drone_pos[0], drone_pos[1])
    
    # Drop the first aid kit when the drone reaches the car
    if drone_pos[0] >= 2 and drone_pos[1] <= 5:
        first_aid.set_data(2.25, 5.2)
    
    return drone, first_aid

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
