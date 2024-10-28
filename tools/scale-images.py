from PIL import Image
import os

# Durchsucht das aktuelle Arbeitsverzeichnis nach Bildern
for filename in os.listdir('.'):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        with Image.open(filename) as img:
            width, height = img.size

            # Prüft, ob die Breite des Bildes größer als 1920 Pixel ist
            if width > 1920:
                # Berechnet die neue Höhe, um das Seitenverhältnis beizubehalten
                new_height = int((1920 / width) * height)
                img = img.resize((1920, new_height), Image.LANCZOS)  # LANCZOS statt ANTIALIAS

                # Überschreibt das Originalbild mit der skalierten Version
                img.save(filename)
                print(f"{filename} wurde auf 1920 Pixel Breite skaliert.")
            else:
                print(f"{filename} ist bereits kleiner als 1920 Pixel.")