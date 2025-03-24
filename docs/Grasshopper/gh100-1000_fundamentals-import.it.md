---
title: "Importazione dei Dati Fondamentali"
date: "2021-12-07"
author: "Manuel Emmenegger | bimdo.ch"
original: "Tedesco"
tags: 
  - "Archicad"
  - "Spazio Aperto"
  - "Grasshopper"
  - "Rhino"
  - "Studio"
  - "Swisstopo"
  - "Terreno"
  - "Workflow"
  - "xyz"
---

L'acquisizione e l'elaborazione dei dati di base per gli studi architettonici possono richiedere molto tempo. Diverse fonti di dati, formati e grandi quantità di dati rendono difficile un flusso di lavoro efficiente. Con la giusta metodologia, tuttavia, questo processo può essere notevolmente semplificato.

La chiave è importare solo i dati necessari in modo mirato e posizionarli direttamente al punto zero del progetto. I seguenti elementi servono come base:

- DWG catastale (LV95)
- [Dati degli edifici da SwissTopo](https://www.swisstopo.admin.ch/de/geodata/landscape/buildings3d2.html)  
- [Dati XYZ del terreno da SwissTopo](https://www.swisstopo.admin.ch/de/geodata/height/alti3d.html)

**Il workflow:**

1. Importare i dati catastali e degli edifici in Rhino
2. Importare i dati XYZ del terreno tramite Grasshopper
3. Collegare tutti i dati in Grasshopper
4. Limitare all'area rilevante
5. Definire l'offset rispetto al punto zero
6. Importare in ArchiCAD tramite la connessione Grasshopper

<div class="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/irmRQJ-8-YA?si=AUGPiorBAVAcIzcQ" 
          allowfullscreen>
  </iframe>
</div>


---
**Pubblicato il:** {{ page.meta.date }} | **Codice:** {{ page.file.name[:10] }}  | **Autore:** {{ page.meta.author }}

**Tag:** {{ page.meta.tags | join(', ') }} | **Originale:** {{ page.meta.original }}