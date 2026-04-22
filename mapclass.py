import numpy as np

# 1. Definiere dein Mapping
# Key: Original-ID aus dem Datensatz (z.B. HePIC oder LAS-Standard)
# Value: Die Ziel-ID für dein RangeNet++ Training
class_map = {
    0: 0,     # Unclassified -> Background
    2: 1,     # Ground -> Floor
    7: 0,     # Low Noise -> Ignore
    17: 2,    # Bridge Deck (oder Wand im HePIC Kontext) -> Wall
    18: 3,    # High Vegetation/Obstacle -> Pillar/Object
    # ... ergänze weitere Klassen je nach Datensatz
}

def map_labels(labels, mapping):
    """
    Konvertiert Roh-Labels in Trainings-Labels.
    Punkte mit nicht definierten Klassen werden auf 0 gesetzt.
    """
    # Erstelle ein Array mit Nullen in der Größe der Labels
    mapped_labels = np.zeros_like(labels)
    
    for old_id, new_id in mapping.items():
        mapped_labels[labels == old_id] = new_id
        
    return mapped_labels

# 2. Anwendung
# raw_labels kommen direkt aus laspy
training_labels = map_labels(labels, class_map)