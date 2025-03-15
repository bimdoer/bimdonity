---
title: "Typisierung Bauphysik"
date: "2022-09-14"
tags: 
  - "Bauphysik"
  - "BIM"
  - "IFC"
  - "Typisierung"
  - "Workflow"
---
## Typisierung
Die Typisierung von Gebäudeelementen ist ein zentraler Aspekt der BIM-Methodik. Dabei werden Bauteile mit ähnlichen oder identischen Anforderungen in logische Gruppen zusammengefasst. Diese systematische Kategorisierung ermöglicht es, das Gebäude als strukturierte Datenbank zu verstehen und effizient zu verwalten.

Das folgende Modell wurde auf Basis bestehender Typisierungskonzepte (z.B. von Pirmin Jung AG) und Projekterfahrungen entwickelt, um die Gruppierung anschaulich darzustellen. Die folgenden zwei Visualisierungen zeigen die unterschiedlichen Aspekte der Typisierung:

<div class="responsive-container">
  <div>
    <img src="../assets/bi100-1003_01_perimter.png" alt="Perimetermodell" style="width:100%">
  </div>
  <div>
    <img src="../assets/bi100-1003_02_typen.png" alt="Typenmodell" style="width:100%">
  </div>
</div>

## BIMx Viewer
Im BIMx-Webviewer lassen sich beide Modelle detailliert untersuchen. Das Perimetermodell verwendet eine klare Farbcodierung:

- Rot: Perimeterbildende Elemente
- Blau: Elemente im Kaltbereich  
- Transparent: Elemente im warmen Innenbereich

Das Typenmodell klassifiziert die einzelnen Bauteile entsprechend dem bauphysikalischen Bericht. Die Typisierung deckt die wichtigsten Standardfälle ab, wobei komplexere Aufbauten wie Unterlagsböden oder Flachdächer gesondert behandelt werden müssen. Ein Hauptziel ist das Vermitteln des grundlegenden Typisierungskonzepts.

Verbesserungspotential besteht im Erdbereich: Aktuell existieren nur die Grundtypen WE ("Wand gegen Erdreich") und DE ("Decke gegen Erdreich"). Für eine vollständige Typisierung wären weitere Untertypen sinnvoll, besonders im Hinblick auf die Dämmperimeterberechnung.

<iframe width="960" height="320" src="https://bimx-webviewer.graphisoft.com/?modelId=94c1dd96-9b8a-4770-a72c-321009c36b8b&amp;modelType=HyperModel&amp;auth=eyJhbGciOiJIUzI1NiIsImtpZCI6Ikc0MmdJR1ZzUWpLdGtpdk1YT0h5VmciLCJ0eXAiOiJKV1QifQ.eyJ0c19tb2RlbF9pZCI6Ijk0YzFkZDk2LTliOGEtNDc3MC1hNzJjLTMyMTAwOWMzNmI4YiIsInhfaWV2IjoiMCIsIm5iZiI6MTYyODUwMTU5NywiZXhwIjoyMTM2NTMzNTk3LCJpYXQiOjE2NjMxNDc5OTcsImlzcyI6Imh0dHBzOi8vYmlteC5ncmFwaGlzb2Z0LmNvbSIsImF1ZCI6Imh0dHBzOi8vYmlteC13ZWJ2aWV3ZXIuZ3JhcGhpc29mdC5jb20ifQ.lZXrN3Pobvo4OiCrp2rZTKzcpc9A-eXh43uaCEjeG1g&amp;linkVersion=2.0" frameborder="0" allowfullscreen></iframe>

Die Sprachenwahl ist ein wichtiger Aspekt der Typisierung. Verschiedene Projektphasen und Stakeholder verwenden unterschiedliche Sprachen. Eine durchgängige Verwendung von Englisch wäre eine Lösung, bringt aber eigene Herausforderungen. Das entwickelte System enthält automatisch deutsche und englische Bezeichnungen, da die Wahl einer einzelnen Landessprache oft zum "Röstigraben-Problem" mit benachteiligten Sprachgruppen führt. Für ein Projekt empfiehlt sich eine einheitliche Typisierungssprache.

| Deutsch | Englisch |
|---------|----------|
| WE - Wand gegen Erdreich | WE - Wall to exterior |
| BE - Boden gegen Erdreich | BE - Bottom slab to exterior |

## BIMx Anleitung
### Modell öffnen
Um ein Modell zu öffnen, klicke beim BIMx auf Play. Wähle links eines der beiden Modelle und klicke unten auf das entsprechende Vorschaubild.

[![Parameter](../assets/bi100-1003_03_anleitung.png)](../assets/bi100-1003_03_anleitung.png)

### Bauteil-Informationen
Im Typenmodell können die Bedeutungen der Farben durch einen Rechtsklick auf ein Element und Auswahl von "Info" angezeigt werden. Dort sind die Typisierungen in Deutsch und Englisch hinterlegt.

[![Parameter](../assets/bi100-1003_04_anleitung.png)](../assets/bi100-1003_04_anleitung.png)

### Status beheizt
Die roten und blauen Kugeln zeigen den Heizstatus (beheizt/unbeheizt) der Räume an. Per Rechtsklick auf "Info" werden Details angezeigt. Die Räume selbst können ebenfalls eingeblendet und nach warm/kalt gefiltert werden, wie im Screenshot dargestellt.

[![Parameter](../assets/bi100-1003_05_anleitung.png)](../assets/bi100-1003_05_anleitung.png)

## Fazit
Typisierung gab es schon vor BIM - bereits ein markierter Plan gruppiert Elemente. Der Vorteil des digitalen Modells liegt in der konsistenten Datenhaltung und effizienten Visualisierung, wodurch alle Projektbeteiligten ein besseres Verständnis des Bauvorhabens entwickeln können.


---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
