import random
import csv
import time
from datetime import datetime
import os

csv_file = "color_history.csv"
interval = 10  # secondes

# Création du fichier si non présent
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "R", "G", "B"])

# Boucle principale
print("Démarrage du générateur de couleurs...")
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timestamp = datetime.utcnow().isoformat()

    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, r, g, b])

    print(f"[{timestamp}] RGB: ({r}, {g}, {b})")
    time.sleep(interval)
