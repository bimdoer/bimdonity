---
title: "Studie jetzt, nicht morgen"
date: "2021-12-07"
categories: 
  - "grasshopper"
tags: 
  - "archicad"
  - "freiflaeche"
  - "grasshopper"
  - "rhino"
  - "studie"
  - "swisstopo"
  - "terrain"
  - "workflow"
  - "xyz"
---

Nur noch kurz eine Studie und dann haben wir Feierabend, doch nur schon die Beschaffung der Grundlagen erstreckt sich über Stunden. Verschiedene Datenquellen und Datenformate führen immer wieder zu roten Köpfen, will man doch einfach nur Architektur machen und jetzt muss man sich zuerst mit Punktwolken, Vermessungssystemen und Modelldaten auseinandersetzen? Und wenn dann mal alle Daten am richtigen Ort sind, steigt der Computer dank den Unmengen an Geometrie-Daten aus.

Dabei ist die Lösung hierfür relativ simpel, wir importieren nur die benötigten Daten und zwar direkt an der richtigen Position. Wir entscheiden wie gross unser Terrain ist und wie detailliert dieses dargestellt wird. Die Suche nach Elementen im Koordinatensystem nach LV95 ersparen wir uns ebenfalls. Unsere Daten liegen direkt beim Projektnullpunkt, übereinander, lokal verortet und dies ohne Computer-Absturz. Klingt utopisch?

Als Grundlage dient uns das ganz konventionelle Kataster-DWG nach LV95. Weiter laden wir uns die [Gebäudedaten](https://www.swisstopo.admin.ch/de/geodata/landscape/buildings3d2.html) von SwissTopo runter sowie auch die [XYZ-Daten](https://www.swisstopo.admin.ch/de/geodata/height/alti3d.html) des Terrains. Wichtig dabei ist, dass alle Grundlage-Daten auf dem gleichen [Vermessungssystem](https://www.swisstopo.admin.ch/de/wissen-fakten/geodaesie-vermessung/bezugsrahmen/lokal/lv95.html) basieren.

Als erstes wird der Kataster in Rhino importiert und die entsprechenden Blöcke werden aufgehoben. Auch die Gebäude importieren wir direkt in Rhino. Im nächsten Schritt importieren wir das Terrain als XYZ-Datei mittels Grasshopper ebenfalls in Rhino. Jetzt sind alle Daten vorhanden und wir brauchen nur noch die Gebäudedaten sowie den Kataster mit Grasshopper zu verbinden.

<figure>

[![](images/GH-TE2101_Prozess.gif)](https://bimdo.ch/wp-content/uploads/2021/12/GH-TE2101_Prozess.gif)

<figcaption>

Vereinfachter Prozess für den Import der Geodaten in ArchiCAD.

</figcaption>

</figure>

Sobald alle Daten verbunden sind, können wir mit dem Datenspiel beginnen. Wir begrenzen die Geometrie auf den gewünschten Kataster-Bereich und definieren den Versatz zum Nullpunkt. Abschliessend müssen wir nur noch ArchiCAD öffnen, mit Grasshopper verbinden und wir erhalten die gewünschten Daten an der richtigen Position und mit reduzierter Polygon-Anzahl.

<figure>

https://www.youtube.com/watch?v=irmRQJ-8-YA

<figcaption>

Video mit den einzelnen Prozess-Schritten beim Import in Rhino, Grasshopper und ArchiCAD.

</figcaption>



</figure>
---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
