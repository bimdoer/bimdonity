---
title: "Importation des Données Fondamentales"
date: "2021-12-07"
author: "Manuel Emmenegger | bimdo.ch"
original: "Allemand"
tags: 
  - "Archicad"
  - "Espace Ouvert"
  - "Grasshopper"
  - "Rhino"
  - "Étude"
  - "Swisstopo"
  - "Terrain"
  - "Workflow"
  - "xyz"
---

L'acquisition et le traitement des données de base pour les études architecturales peuvent prendre beaucoup de temps. Différentes sources de données, formats et grandes quantités de données rendent un flux de travail efficace difficile. Avec la bonne méthodologie, cependant, ce processus peut être considérablement simplifié.

La clé est d'importer uniquement les données requises de manière ciblée et de les positionner directement au point zéro du projet. Les éléments suivants servent de base :

- DWG cadastral (LV95)
- [Données de bâtiments de SwissTopo](https://www.swisstopo.admin.ch/de/geodata/landscape/buildings3d2.html)  
- [Données XYZ du terrain de SwissTopo](https://www.swisstopo.admin.ch/de/geodata/height/alti3d.html)

**Le workflow :**

1. Importer les données cadastrales et de bâtiments dans Rhino
2. Importer les données XYZ du terrain via Grasshopper
3. Connecter toutes les données dans Grasshopper
4. Limiter à la zone pertinente
5. Définir le décalage par rapport au point zéro
6. Importer dans ArchiCAD via la connexion Grasshopper

<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/irmRQJ-8-YA?si=AUGPiorBAVAcIzcQ" 
          allowfullscreen>
  </iframe>
</div>


---
**Publié le:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Auteur:** {{ page.meta.author }}

**Tags:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}