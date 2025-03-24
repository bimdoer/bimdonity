---
title: "Erste Schritte mit Bonsai"
date: "2024-03-20"
author: "Manuel Emmenegger"
original: "Deutsch"
tags:
  - "Blender"
  - "Bonsai"
---

## Einleitung
Als Teil einer Bonsai Interview-Reihe von [Petru Conduraru](https://www.linkedin.com/in/petruc/) sind folgende Inhalte entstanden, welche dir helfen sollen mit Bonsai zu starten. Möchtest du dein Wissen auch teilen? Dann melde dich direkt bei Petru und werde Teil der Interview-Reihe.
Das zugehörige Interview findest du [hier](https://www.youtube.com/watch?v=bp3uZyTVqpk).

<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/bp3uZyTVqpk?si=ZIHVXgTVxoe754So" frameborder="0" allowfullscreen></iframe>
</div>


---
## Hilfreiche Links
### Software
- [Blender herunterladen](https://www.blender.org/download/)
- [Bonsai Add-on herunterladen](https://blenderbim.org/download.html)

### Community & Support
- [Bonsai GitHub Repository](https://github.com/IfcOpenShell/IfcOpenShell)
- [IFC Architect - Bonsai Dokumentation](https://ifcarchitect.com/)
- [IFC Architect YouTube Kanal](https://www.youtube.com/@ifcarchitect)
- [BIMvoice YouTube Kanal](https://www.youtube.com/@BIMvoice)
- [Bonsai Community Forum](https://community.osarch.org/)

---
## Funktionsübersicht
Bonsai ist ein leistungsstarkes Open-Source BIM-Tool für Blender, das vielfältige Funktionen bietet:

### Hauptfunktionen die ich aktiv nutze

- **BIM Viewer & Koordination**
    - Schnelle Navigation und Visualisierung von IFC-Modellen
    - Flexible Filteroptionen zur gezielten Analyse von Bauteilen

- **Informationsmanagement**
    - Einfacher Zugriff auf alle IFC-Eigenschaften und -Attribute
    - Strukturierte Darstellung der Gebäudehierarchie

- **Visualisierung**
    - Anpassbare Farbschemata für unterschiedliche Eigenschaften

- **Modellmodifikation**
    - Anpassung von Eigenschaften und Attributen

### Weitere verfügbare Funktionen

- **Modellierung**: Erstellung von nativen BIM-Elementen
- **Kostenmanagement**: Verknüpfung mit Kostendaten
- **Ressourcenplanung**: Zeitliche und materielle Ressourcenverwaltung
- **Qualitätsprüfung**: Automatisierte Modellprüfungen
- **Kalkulation**: Mengen- und Massenermittlung
- **Facility Management**: Unterstützung des Gebäudebetriebs

[![Bonsai Overview](assets/bo100-1001_01_bonsai-overview.jpg)](assets/bo100-1001_01_bonsai-overview.jpg)

---
## Einstellungen Navigation
- **Depth**: Diese Checkbox optimiert das Scrollen und verhindert, dass die Navigation durch Objekte im Vordergrund blockiert wird.
- **Zoom to Mouse Position**: Diese Einstellung bewirkt, dass der Zoom-Vorgang direkt an der Mausposition erfolgt, anstatt vom Bildschirmmittelpunkt aus zu zoomen.

[![Blender Settings](assets/bo100-1001_02_bonsai-blender-settings.jpg)](assets/bo100-1001_02_bonsai-blender-settings.jpg)

---
## Navigator Filter Selected
Die Filterfunktion ermöglicht eine selektive Filterung der hierarchischen Baum-Struktur - besonders nützlich bei großen IFC-Modellen. Somit stellt die Baumstruktur dann nur Elemente dar, welche im Modell gerade selektiert sind.



[![Bonsai Navigator](assets/bo100-1001_03_bonsai-navigator.jpg)](assets/bo100-1001_03_bonsai-navigator.jpg)

---
## IfcStruktur und Shift
- **shift**: Eine nützliche Funktion ist das Halten der Shift-Taste während dem Öffnen und Schliessen der Baumstruktur, dies ermöglicht das Öffnen und Schliessen der Struktur inklusiv aller Unterordner.
- **IfcStruktur**: Im Vergleich mit anderen IfcViewer fällt auf, dass die Struktur irgendwie anders aussieht und z.B. auch die Geschosse geometrisch abgebildet sind. Dieses "anders" ist wohl die native und korrekt abgebildete IfcStruktur.


[![Bonsai Shift](assets/bo100-1001_04_bonsai-shift.jpg)](assets/bo100-1001_04_bonsai-shift.jpg)

---
## Darstellung Umgebung
Im folgenden Screenshot wird gezeigt, wie sich die visuellen Einstellungen wie Achsenfarben und das Arbeitsraster anpassen lassen. Zusätzlich können die Referenzkreuze für Geschosse und andere Elemente ein- oder ausgeblendet werden.

[![Bonsai Levels](assets/bo100-1001_05_bonsai-levels.jpg)](assets/bo100-1001_05_bonsai-levels.jpg)

---
## Speichern der Arbeitsumgebung
Wie du es vielleicht von anderen Tools kennst, kannst du auch in Blender deine vorgenommenen Einstellungen für deine Arbeitsumgebung speichern, wie zum Beispiel die Anordnung von verschiedenen Arbeitsbereichen.

[![Bonsai User Preferences](assets/bo100-1001_06_bonsai-userpref.jpg)](assets/bo100-1001_06_bonsai-userpref.jpg)

---
## Shortcuts
- **shift**: Shift ist sehr mächtig, so lassen sich Baumstrukturen mit Substrukturen öffnen und schliessen oder eben auch alle Subelemente in der Baumstruktur ein- und ausblenden.
- **Point**: Mit dem Kürzel "." oder je nach Spracheinstellungen "," lässt sich der Zoom zur Selektion optimieren. Man wählt das Element z.B. im Navigator aus und zoomt dadurch in 3D direkt zum Element.
- **Transparenz**: Zugegeben dies ist kein Shortcut, aber trotzdem sehr hilfreich für die Koordination.
- **H**: Ausblenden eins ausgewählten Elements
- **alt+H**: Blende alles ein
- **shift+H**: Ausblenden aller nicht ausgewählten Elemente

[![Bonsai Shortcuts](assets/bo100-1001_07_bonsai-shortcuts.jpg)](assets/bo100-1001_07_bonsai-shortcuts.jpg)

---
## Einfärben nach Eigenschaft
Eine sehr praktische Funktion für das Einfärben von Modell-Elementen. Wichtig zu wissen, wenn deine Eigenschaft, bzw. dein Property-Set nicht auftaucht, dann selektiere ein Element und probiere es noch einmal.
[![Bonsai Colorizing](assets/bo100-1001_08_bonsai-colorizing.jpg)](assets/bo100-1001_08_bonsai-colorizing.jpg)

### Bonsai vs. Solibri
In Bonsai existiert aktuell keine Liste, welche zugleich Farben enthält. Diese Funktionen sind getrennt, entweder Liste oder Farbe.
> Dies ist eine sehr praktische Funktion, um visuelle Prüfungen vorzunehmen und sich einen Überblick über die Daten machen möchte.

[![Bonsai Solibri](assets/bo100-1001_09_bonsai-solibri.jpg)](assets/bo100-1001_09_bonsai-solibri.jpg)

---
## Filter
Die Filterfunktion ist sehr mächtig, beachte dabei die Unterschiede zwischen Property und Attribute.
[![Bonsai Filters](assets/bo100-1001_10_bonsai-filters.jpg)](assets/bo100-1001_10_bonsai-filters.jpg)

---
## Schnitte im Modell
Die Benutzung von Section cutaways ist nicht die einfachste Methode und ist noch etwas unstabil. In der Version auf dem Screenshot funktioniert diese jedoch.
> Eine optimalere Anwendung ist die Auswahl des "Fetch-Tools" auf der linken Seite in der Werkzeugpalette von Bonsai (Symbol grüne Box mit weissem Cursor). Mit Shift+C kann anschliessend eine Clipping Plane beliebig platziert werden.

[![Bonsai Sections](assets/bo100-1001_11_bonsai-sections.jpg)](assets/bo100-1001_11_bonsai-sections.jpg)


---
**Veröffentlicht am:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Autor:** {{ page.meta.author }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}