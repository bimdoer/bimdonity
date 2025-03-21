---
title: "Grundlagen-Import"
date: "2021-12-07"
author: "Manuel Emmenegger | bimdo.ch"
original: "Deutsch"
tags: 
  - "Archicad"
  - "Freiflaeche"
  - "Grasshopper"
  - "Rhino"
  - "Studie"
  - "Swisstopo"
  - "Terrain"
  - "Workflow"
  - "xyz"
---

Die Beschaffung und Verarbeitung von Grundlagendaten für Architekturstudien kann zeitaufwändig sein. Verschiedene Datenquellen, Formate und große Datenmengen erschweren den effizienten Workflow. Mit der richtigen Methodik lässt sich dieser Prozess jedoch deutlich vereinfachen.

Der Schlüssel liegt darin, nur die benötigten Daten gezielt zu importieren und direkt am Projektnullpunkt zu positionieren. Als Grundlagen dienen:

- Kataster-DWG (LV95)
- [Gebäudedaten von SwissTopo](https://www.swisstopo.admin.ch/de/geodata/landscape/buildings3d2.html)  
- [Terrain-XYZ-Daten von SwissTopo](https://www.swisstopo.admin.ch/de/geodata/height/alti3d.html)

**Der Workflow:**

1. Import des Katasters und der Gebäudedaten in Rhino
2. Import der Terrain-XYZ-Daten via Grasshopper
3. Verbindung aller Daten in Grasshopper
4. Begrenzung auf den relevanten Bereich
5. Definition des Versatzes zum Nullpunkt
6. Import in ArchiCAD über die Grasshopper-Verbindung

<div class="video-container">
  <iframe src="https://www.youtube.com/embed/irmRQJ-8-YA?si=AUGPiorBAVAcIzcQ" 
          allowfullscreen>
  </iframe>
</div>


---
**Veröffentlicht am:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Autor:** {{ page.meta.author }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}