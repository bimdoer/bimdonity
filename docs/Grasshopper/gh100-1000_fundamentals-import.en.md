---
title: "Fundamentals Import"
date: "2021-12-07"
author: "Manuel Emmenegger | bimdo.ch"
original: "German"
tags: 
  - "Archicad"
  - "Open Space"
  - "Grasshopper"
  - "Rhino"
  - "Study"
  - "Swisstopo"
  - "Terrain"
  - "Workflow"
  - "xyz"
---

Acquiring and processing base data for architectural studies can be time-consuming. Various data sources, formats, and large amounts of data make an efficient workflow difficult. With the right methodology, however, this process can be significantly simplified.

The key is to import only the required data in a targeted manner and position it directly at the project zero point. The following serve as a foundation:

- Cadastral DWG (LV95)
- [Building data from SwissTopo](https://www.swisstopo.admin.ch/de/geodata/landscape/buildings3d2.html)  
- [Terrain XYZ data from SwissTopo](https://www.swisstopo.admin.ch/de/geodata/height/alti3d.html)

**The workflow:**

1. Import the cadastral and building data into Rhino
2. Import the terrain XYZ data via Grasshopper
3. Connect all data in Grasshopper
4. Limit to the relevant area
5. Define the offset to the zero point
6. Import into ArchiCAD via the Grasshopper connection

<div class="video-container">
  <iframe src="https://www.youtube.com/embed/irmRQJ-8-YA?si=AUGPiorBAVAcIzcQ" 
          allowfullscreen>
  </iframe>
</div>


---
**Published on:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Author:** {{ page.meta.author }}

**Tags:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}