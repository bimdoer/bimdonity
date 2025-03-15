---
title: "Einführung in GDL"
date: "2025-03-15"
tags: 
  - "Archicad"
  - "GDL"
---

## GDL in Archicad

In diesem Beitrag werden häufig gestellte Fragen rund um die Geometric Description Language (GDL) beantwortet – der Skriptsprache, die ArchiCAD zur Erstellung parametrischer Objekte nutzt. Wir erklären dir, was GDL ist, warum es sich lohnt, GDL zu lernen, und wie du deine ersten Schritte in der GDL-Welt machst.

---

### Was ist GDL?
GDL (Geometric Description Language) ist die Skriptsprache, mit der ArchiCAD-Bibliotheken parametrische Objekte definieren. Anders als ein simples "Hello World" liefert GDL bereits nach wenigen Codezeilen praxisnahe Ergebnisse. Dabei werden komplexe Werkzeuge wie Fenster oder Türen nicht als statische Elemente, sondern als dynamische, skriptbasierte Objekte erstellt.  
GDL wird in ArchiCAD in sogenannten LCF-Containern (mit dem GSM-Dateiformat) verpackt.

### Vorteile von GDL
- **Schneller Einstieg:** Bereits einfache Skripte zeigen visuelle Ergebnisse, was motivierend wirkt.  
- **Parametrik verstehen:** Mit GDL erhältst du ein grundlegendes Verständnis für parametrische Modellierung in CAD-Software.  
- **Praxisnahe Anwendungen:** Du kannst tägliche Arbeitsabläufe optimieren, da viele Objekte und Werkzeuge in ArchiCAD auf GDL basieren.  
- **Visuelles Scripten:** Neuere Tools wie [Param-O](https://graphisoft.com/downloads/param-o) ermöglichen ein visuelles Herangehen, wodurch der Einstieg erleichtert wird.

---

## Erste Schritte in GDL

Ein guter Startpunkt ist es, sich auf ein einfaches 2D- und 3D-Skript zu konzentrieren. In der Schweizer Version von ArchiCAD findest du den GDL-Editor unter _Ablage → GDL-Objekte → GDL-Objekte erstellen_.   

  - **Tipp:** Beschränke dich anfangs auf grundlegende Befehle, etwa das Erzeugen eines Quaders mit dem Befehl `block`.  
  - **Visualisierung:** Nutze die 2D- und 3D-Ansicht, um die Auswirkungen deines Skripts unmittelbar zu überprüfen.
[![Uebersicht-Editor](assets/ac210-1000_01_Uebersicht-Editor.png)](assets/ac210-1000_01_Uebersicht-Editor.png)
---

docs\assets\images\ac210-1000_02_Referenzhandbuch.png

## Nützliche Ressourcen

- Das [GDL Referenzhandbuch](https://help.graphisoft.com/AC/24/GER/GDL.pdf) bietet eine umfangreiche Übersicht der Befehle.
[![Referenzhandbuch](assets/ac210-1000_02_Referenzhandbuch.png)](assets/ac210-1000_02_Referenzhandbuch.png)
- Seiten wie [SelfGDL.de](https://www.selfgdl.de/) und das [GDL-Kochbuch](https://issuu.com/dnicholsoncole/docs/gdlcookbook3_01) von David Nicholson-Cole liefern praxisnahe Beispiele.

**Weitere Ressourcen:**   
Hier eine Zusammenstellung hilfreicher Plattformen, auf denen du bereits fertige GDL-Elemente und weiterführende Informationen findest:   

- [idc.ch](https://www.idc.ch/archicad/ueber-archicad/zusatzprodukte/zusatzbibliotheken/)   
- [bimobject.com](https://www.bimobject.com/de-ch/product?sort=trending)    
- [bimcomponents.com](https://bimcomponents.com/)   
- [cadswift.com.au](https://cadswift.com.au/)   
- [arroway-textures.ch](https://www.arroway-textures.ch/)   
- [mtextur.com](https://www.mtextur.com/)   
- [bimbakery.co](http://bimbakery.co/)    
- [turbosquid.com](https://www.turbosquid.com/)   
- [b-prisma.de](https://www.b-prisma.de/)   
- [concepsysbim.com](http://www.concepsysbim.com/)    
- [prodlib.com](https://www.prodlib.com/?lang=en)   
- [3dwarehouse.sketchup.com](https://3dwarehouse.sketchup.com/)   
- [archive3d.net](https://archive3d.net/)   
- [velux.at](https://www.velux.at/fachkunden/tools-technik/3d-bim-objekte)    
- [eptar.hu](https://www.eptar.hu/)   
- [poliigon.com](http://www.poliigon.com/)    

Zusätzlich ist der Austausch in Foren (wie dem [ArchiCAD-Talk](https://archicad-talk.graphisoft.com/)) hilfreich, um von den Erfahrungen anderer Nutzer zu profitieren.

---


**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}