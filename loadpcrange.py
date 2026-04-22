import numpy as np
import matplotlib.pyplot as plt

def do_range_projection(points, intensity, width=1024, height=64, fov_up=3.0, fov_down=-25.0):
    # 1. Parameter definieren
    fov_up_rad = (fov_up / 180.0) * np.pi
    fov_down_rad = (fov_down / 180.0) * np.pi
    fov_rad = fov_up_rad - fov_down_rad

    # 2. Distanz (Range) berechnen
    ranges = np.linalg.norm(points, axis=1)

    # 3. Winkel berechnen (Azimut & Neigung)
    yaw = -np.arctan2(points[:, 1], points[:, 0])
    pitch = np.arcsin(points[:, 2] / ranges)

    # 4. In Pixel-Koordinaten umrechnen (Normalisierung)
    proj_x = 0.5 * (yaw / np.pi + 1.0)          # 0..1
    proj_y = 1.0 - (pitch - fov_down_rad) / fov_rad  # 0..1

    # Skalieren auf Bildgröße
    proj_x *= width
    proj_y *= height

    # Runden auf Integer-Indizes
    proj_x = np.floor(proj_x).astype(np.int32)
    proj_x = np.clip(proj_x, 0, width - 1)

    proj_y = np.floor(proj_y).astype(np.int32)
    proj_y = np.clip(proj_y, 0, height - 1)

    # 5. Range-Image erstellen (Initialisierung mit -1)
    range_image = np.full((height, width), -1.0, dtype=np.float32)
    
    # Punkte in das Bild schreiben (nähere Punkte überschreiben weitere)
    indices = np.argsort(ranges)[::-1] # Von weit nach nah sortieren
    range_image[proj_y[indices], proj_x[indices]] = ranges[indices]

    return range_image
def do_label_projection(points, labels, proj_x, proj_y, width=1024, height=64):
    """
    Projiziert die semantischen Labels in das 2D-Gitter.
    proj_x und proj_y sind die bereits berechneten Pixel-Indizes.
    """
    # 1. Label-Image initialisieren (0 = unbeschriftet/Hintergrund)
    label_image = np.zeros((height, width), dtype=np.int32)

    # 2. Sortierung wie beim Range-Image (nähere Punkte haben Vorrang)
    ranges = np.linalg.norm(points, axis=1)
    indices = np.argsort(ranges)[::-1]

    # 3. Labels in das Bild schreiben
    label_image[proj_y[indices], proj_x[indices]] = labels[indices]

    return label_image
# Beispielanwendung (mit Daten aus dem vorherigen Schritt)
# range_img = do_range_projection(points, intensity)

def visualize_range_image(range_image, label_image, unique_labels):
    """Visualizes the range image with labels."""
    plt.figure(figsize=(20, 10))

    # Plot range image
    plt.subplot(1, 2, 1)
    plt.title("Range Image")
    plt.imshow(range_image, cmap="viridis")
    plt.colorbar(label="Range")

    # Plot label image
    plt.subplot(1, 2, 2)
    plt.title("Label Image")
    plt.imshow(label_image, cmap="tab10")
    plt.colorbar(ticks=range(len(unique_labels)), label="Labels")

    plt.tight_layout()
    plt.savefig('range_and_label_image.png', dpi=150, bbox_inches='tight')
    print("✓ Saved: range_and_label_image.png")
    plt.show()

# Load data from file
file_path = "data_for_debug/101.txt"
data = np.loadtxt(file_path, delimiter=",", dtype=str)

# Extract points, labels, and IDs
points = data[:, :3].astype(float)
labels = data[:, 3]

# Project range image
range_image = do_range_projection(points, None)

# Compute projection coordinates
proj_x = 0.5 * (-np.arctan2(points[:, 1], points[:, 0]) / np.pi + 1.0) * 1024
proj_y = 1.0 - ((np.arcsin(points[:, 2] / np.linalg.norm(points, axis=1)) - (-25.0 / 180.0 * np.pi)) / ((3.0 / 180.0 * np.pi) - (-25.0 / 180.0 * np.pi))) * 64

# Convert to integer indices
proj_x = np.floor(proj_x).astype(np.int32)
proj_x = np.clip(proj_x, 0, 1024 - 1)
proj_y = np.floor(proj_y).astype(np.int32)
proj_y = np.clip(proj_y, 0, 64 - 1)

# Project label image
unique_labels = np.unique(labels)
label_to_color = {label: i for i, label in enumerate(unique_labels)}
label_indices = np.array([label_to_color[label] for label in labels])
label_image = do_label_projection(points, label_indices, proj_x, proj_y)

# Visualize the range and label images
visualize_range_image(range_image, label_image, unique_labels)
