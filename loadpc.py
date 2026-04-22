import laspy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_pc_data(file_path): # LAS-Datei öffnen
    data = np.loadtxt(file_path, delimiter=',', dtype=str)
	
	# Extract coordinates (first 3 columns as float)
	points = data[:, :3].astype(float)
	
	# Extract labels (4th column)
	labels = data[:, 3]
	
	# Extract IDs (5th column)
	instance_ids = data[:, 4]

	# Berechnung der Distanz (Range) für jeden Punkt
	ranges = np.linalg.norm(points, axis=1)
	
	return points, labels, instance_ids, ranges


file_path = "data_for_debug/101.txt"
points, labels, instance_ids, ranges = load_pc_data(file_path)


# Visualize the point cloud with colors by label
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Get unique labels and create color mapping
unique_labels = np.unique(labels)
label_to_color = {label: i for i, label in enumerate(unique_labels)}
colors = np.array([label_to_color[label] for label in labels])

# Create scatter plot with small points
scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], 
                     c=colors, cmap='tab10', marker='.', s=10, alpha=0.9, edgecolors='none')

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title(f'Point Cloud - Colored by Label ({points.shape[0]} Punkte)', fontsize=14, fontweight='bold')

# Create legend for labels
legend_labels = [f'{label}' for label in unique_labels]
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', 
                             markerfacecolor=plt.cm.tab10(label_to_color[label]/len(unique_labels)), 
                             markersize=10, markeredgecolor='black', markeredgewidth=0.5) 
                  for label in unique_labels]
ax.legend(legend_handles, legend_labels, loc='upper left', fontsize=10)

plt.tight_layout()

# Save the figure
plt.savefig('pointcloud_view1.png', dpi=150, bbox_inches='tight')
print("✓ Saved: pointcloud_view1.png")

plt.show()
