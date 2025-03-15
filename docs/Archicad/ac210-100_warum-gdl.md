---
title: "Warum GDL?"
date: "2021-07-28"
categories: 
  - "archicad"
  - "start-mit-gdl"
tags: 
  - "archicad"
  - "bibliotheken"
  - "gdl"
  - "gsm"
  - "lcf"


---

Wer mit ArchiCAD gearbeitet hat, wird sich dies schon öfters gefragt haben. GDL ([Geometric Description Language](https://en.wikipedia.org/wiki/Geometric_Description_Language)) ist die Scriptsprache der ArchiCAD-Bibliotheken, welche bei der ArchiCAD-Installation pro Version mitinstalliert werden. Diese sind jeweils in einem [LCF-Container](https://help.graphisoft.com/AC/24/ger/_AC24_Help/020_Configuration/020_Configuration-95.htm#XREF_11055_Library_Container) verpackt und haben das Dateiformat GSM. Alle komplexeren Werkzeuge in ArchiCAD, wie das Fenster- oder Tür-Werkzeug basieren auf diesem Format. Man kann die Möglichkeiten mit GDL wohl mit den Revit-Familien oder AutoCAD-Blöcken vergleichen, wobei in ArchiCAD Ein Script erforderlich ist, sobald es ums Thema Parametrik geht. Mit dem neuen Tool [Param-O](https://graphisoft.com/downloads/param-o), welches direkt in ArchiCAD 24 implementiert ist, entschärft Graphisoft den Einstieg in GDL etwas. Mit Param-O ermöglicht Graphisoft visuelles Scripten, ähnlich wie man dies aus [Grasshopper](https://en.wikipedia.org/wiki/Grasshopper_3D) oder [Dynamo](https://blogs.autodesk.com/bimblog/visuelle-programmierung-mit-dynamo/) bereits kennt.

Doch macht es überhaupt Sinn GDL zu lernen? Für ArchiCAD-User, die noch nie ein Script gesehen haben, ist GDL sicherlich ein spannender Einstieg. Bereits nach wenigen Codezeilen ist ein Ergebnis ersichtlich und dieses beschränkt sich nicht nur auf ein "[Hello World](https://de.wikipedia.org/wiki/Hallo-Welt-Programm)", wie man dies aus anderen Sprachen kennt. Mit wenigen Schritten können praxisnahe Elemente erstellt werden und so die tägliche Arbeit optimieren. Ausserdem bekommt man ein Gefühl für Parametrik und den Aufbau von CAD-Software. Wichtige Elemente wie Subroutinen, Loops und Macros erfordern dann schon etwas fundiertere Kenntnisse. Die Sprache hat aber auch so ihre Tücken, denn man kann sie nur für ArchiCAD nutzen und auch da ist man beschränkt auf gewisse Anwendungsbereiche. Bevor man sich da in die Untiefen von GDL begibt, sollte man daher Ausschau halten nach Elementen die es schon gibt. Darum hier eine Zusammenstellung von Plattformen, welche GDL-Elemente zur Verfügung stellen.

<figure>

![](images/AC-GD2101_GDL-Symbol.png)

<figcaption>

Programme/GRAPHISOFT/ArchiCAD 24/Bibliotheken 24

</figcaption>

</figure>

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

Für komplexere Anwendungen solltest du einige Punkte beachten. In ArchiCAD programmierst du in einer Autorensoftware und die Kommunikation von Graphisoft bezüglich Veränderungen oder Neuerungen in der Software ist etwas schwer voraus zu sagen. In diesem Zusammenhang ist der Migration von Projektdateien besondere Beachtung zu schenken. Weiter beschränken sich komplexere Elemente nicht nur auf ein einfaches 3D-Script, schlussendlich sollen auch Auswertungen und der IFC-Export barrierefrei funktionieren. Sobald ein Element in mehreren Projekten Anwendung finden soll, spielen Themen wie Struktur, Updates von Scripts sowie Standards von Graphisoft eine wichtige Rolle. Dabei ist die Definition von Anforderungen besonders wichtig und sicherlich mit dem Endnutzer abzusprechen.  
Falls du dich entscheidest deine ersten Schritte in GDL zu machen, findest du alle wichtigen Infos in meinem nächsten Artikel [GDL für Dummies](https://bimdo.ch/ac-gd2102_gdl-fuer-dummies/).

---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
