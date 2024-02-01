import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Path to the new JSON file
json_file_path_2 = '/content/101043661.3D.json'

# Load particles data from the new JSON file
with open(json_file_path_2, 'r') as file:
    data_2 = json.load(file)

# Extract particles from the first entry in the data
particles_2 = data_2[0]['particles']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize variables to track the min and max values for the axes for the new building
min_x_2, max_x_2 = float('inf'), float('-inf')
min_y_2, max_y_2 = float('inf'), float('-inf')
min_z_2, max_z_2 = float('inf'), float('-inf')



# Iterate over particles to plot them for the new building
for particle in particles_2:
    # Extract vertices (assuming triangles for simplicity)
    vertices = [
        [particle['x0'], particle['y0'], particle['z0']],
        [particle['x1'], particle['y1'], particle['z1']],
        [particle['x2'], particle['y2'], particle['z2']],
    ]

    # Update the min and max values for axes
    x_values = [vertex[0] for vertex in vertices]
    y_values = [vertex[1] for vertex in vertices]
    z_values = [vertex[2] for vertex in vertices]
    min_x_2, max_x_2 = min(min_x_2, min(x_values)), max(max_x_2, max(x_values))
    min_y_2, max_y_2 = min(min_y_2, min(y_values)), max(max_y_2, max(y_values))
    min_z_2, max_z_2 = min(min_z_2, min(z_values)), max(max_z_2, max(z_values))

    # Determine color based on height
    z_difference = particle['z2'] - particle['z0']
    color = 'green'

    # Create and add the polygon with the determined color
    poly = Poly3DCollection([vertices], color=color, alpha=0.5)
    ax.add_collection3d(poly)

# Setting the limits on axes
ax.set_xlim([min_x_2 - 10, max_x_2 + 10])
ax.set_ylim([min_y_2 - 10, max_y_2 + 10])
ax.set_zlim([min_z_2 - 5, max_z_2 + 5])

# Setting a view angle to reflect the building's shape
ax.view_init(elev=20, azim=45)  # Adjust as needed

# Show the plot
plt.show()
