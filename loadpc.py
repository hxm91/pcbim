import laspy
import numpy as np

def load_pc_data(file_path): # LAS-Datei öffnen
with laspy.open(file_path) as fh:
	las = fh.read()
	
	# Koordinaten extrahieren (XYZ)
	points = np.vstack((las.x, las.y, las.z)).transpose()
	
	# Intensität extrahieren (wichtig für RangeNet-Input)
	intensity = np.array(las.intensity)
	
	# Falls vorhanden: Semantische Labels (oft im Feld 'classification')
	labels = np.array(las.classification)
	
	return points, intensity, labels

points, intensity, labels = load_pc_data("deine_datei.las") # Beispielaufruf

# Berechnung der Distanz (Range) für jeden Punkt
# Das ist der erste Schritt für das Range-Image
ranges = np.linalg.norm(points, axis=1)

print(f"Geladen: {points.shape[0]} Punkte.")
print(f"Maximale Distanz: {ranges.max():.2f}m")
