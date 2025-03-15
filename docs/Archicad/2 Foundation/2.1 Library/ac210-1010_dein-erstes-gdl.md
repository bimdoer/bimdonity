---
title: "Dein erstes GDL"
date: "2025-03-15"
tags: 
  - "Archicad"
  - "GDL"
---

## Allgemeine Tipps

Bevor du mit deinem ersten Skript beginnst, hier einige hilfreiche Tipps:

1. **Ideen skizzieren**: Halte deine Ideen kurz fest, um wichtige Parameter zu identifizieren.
2. **Anforderungen definieren**: Unterteile die Anforderungen in grundlegende Funktionen und "nice to have"-Funktionen.
3. **Prototyping**: Experimentiere mit verschiedenen Ansätzen, um Lösungswege zu finden. Prototyping kann dir helfen, deine Ideen zu testen und zu verfeinern.

4.  **Strukturierung des Skripts**: Kommentiere dein Skript und verwende Überschriften, um die Lesbarkeit zu verbessern. Ein klar strukturierter Code erleichtert die Zusammenarbeit im Team.

```
!Beginne dein Script mit ein paar Infos
    !Objekttitel
    !Datum
    !Dein Name
    !Script-Name z.B. 3D-Script

Strukturiere
    deine
        Arbeit
    mit
Tabstops.

"G R O S S  & klein" dient nur der besseren Übersicht
    >>Graphisoft scriptet fast alles klein
    >>GDL-Kochbuch empfiehlt Befehle   "GROSS"
                             Attribute "klein"

END !--------------- Beende dein Script mit END.
```
---
## Strukturierung Script

- Kommentiere das Skript mit `!` und füge Überschriften hinzu.
- Verwende Tabstops für eine klare Struktur.
- Nutze Großbuchstaben für Befehle und Kleinbuchstaben für Attribute.
- Setze Subroutinen ein, um komplexe Skripte zu organisieren.
- Beende jedes Skript mit dem `END`-Befehl.
- Erstelle ein neues GDL und überprüfe das Ergebnis in der 3D-Ansicht.
- Weitere Informationen findest du im [Graphisoft GDL Style Guide](http://gdl.graphisoft.com/gdl-style-guide).

---
## Erstellung GDL
### 3D-Script
**1. Neues GDL erstellen:**

- Öffne ArchiCAD und gehe zum Menü "Ablage".
- Wähle "Neu" und dann "GDL-Objekt", um ein neues GDL-Skript zu erstellen.

**2. Block-Skript einfügen:**

- Öffne den 3D-Skript-Editor in deinem neuen GDL-Objekt.
- Kopiere und füge das folgende Block-Skript in den Editor ein.

**3. Prüfe das Ergebnis:**

- Öffne die 3D-Ansicht auf der linken Seite.


<div class="responsive-container">
  <div>
    <pre><code>
!Bock auf Block
!20210903
!Manuel Emmenegger
!3D-Script

block 1,2,3

end !Ende des Scripts
    </code></pre>
  </div>
  <div>
    <a href="/assets/images/ac210-1010_01_3D-Ansicht-300x278.png" target="_blank">
      <img src="/assets/images/ac210-1010_01_3D-Ansicht-300x278.png" alt="3D-Ansicht">
    </a>
  </div>
</div>

**4. Prüfe das Ergebnis:**

- Nach dem Befehl stehen die Eingaben _1,2,3_, welche für _x,y,z_ stehen. Spiele nun etwas mit diesen Werten und kontrolliere das Ergebnis in der 3D-Ansicht. Weitere Informationen zu diesem Befehl findest du unter [selfgdl.de](https://www.selfgdl.de/3d-elemente/grundkoerper/block/).

---

### 2D-Script
Im nächsten Schritt überarbeiten wir die 2D-Darstellung. Öffne das 2D-Script und ergänze die entsprechenden Zeilen, um eine automatische Projektion vom 3D-Script zu erzeugen. Verwende den Befehl nur zur Kontrolle, da er bei komplexer Geometrie den Grundrissaufbau verlangsamen kann. Weitere Informationen findest du auf [selfgdl.de](https://www.selfgdl.de/2d-elemente-2/projektionen/project2/).


<div class="responsive-container">
  <div>
    <pre><code>
!Bock auf Block
!20210903
!Manuel Emmenegger
!2D-Script

project2 3,270,1

end !Ende des Scripts
    </code></pre>
  </div>
  <div>
    <a href="/assets/images/ac210-1010_02_2D-Ansicht-300x273.png" target="_blank">
      <img src="/assets/images/ac210-1010_02_2D-Ansicht-300x273.png" alt="2D-Ansicht">
    </a>
  </div>
</div>

---

### Speichern
Speichere dein erstes GDL in der eingebetteten Bibliothek über "Ablage/sichern" und speichere die ArchiCAD-Datei als .pln, um das GDL zu integrieren.

---

## 3D Parameter
### Geometrie
Nun geht es darum, dieses Element zu parametrisieren. Wir beginnen mit einigen Standardparametern. Öffne in unserem bereits erstellten Element das Register "Parameter" auf der linken Seite. Hier sollten drei Standardparameter vorhanden sein: Parameter A für die X-Achse, Parameter B für die Y-Achse und Parameter ZZYZX für die Z-Achse.

Ersetze die Zahlen im Script durch die Standardparameter A, B und ZZYZX und überprüfe die Änderungen in der 3D-Ansicht. Diese Parameter beeinflussen auch die 2D-Ansicht dank des "project2"-Befehls.

Speichere das Element, schließe den GDL-Editor und platziere das Element mit dem Objekt-Werkzeug.

```
!Bock auf Block
!20210903
!Manuel Emmenegger
!3D-Script

block A,B,ZZYZX

end !Ende des Scripts
```

Drücke "T", um die Objekteinstellungen zu öffnen, wo du die Parameter A, B und ZZYZX findest. Dein parametrisiertes GDL-Objekt ist nun erstellt.
[![Parameter](/assets/images/ac210-1010_03_Einstellungsdialog.png)](/assets/images/ac210-1010_03_Einstellungsdialog.png)

---

### Darstellung
Um weitere Parameter zu erkunden, wähle das GDL-Objekt aus und drücke Strg+Shift+O.

Erstelle zwei neue Parameter im Register "Parameter". Für die Namensgebung empfiehlt sich ein konsistentes Konzept, eventuell basierend auf dem [Graphisoft Standard](https://gdl.graphisoft.com/gdl-style-guide/naming-conventions). Längere Namen sind hilfreich, um die Parameter direkt zu erkennen, ohne eine Legende zu benötigen.

[![Parameter](/assets/images/ac210-1010_04_Parameter.png)](/assets/images/ac210-1010_04_Parameter.png)

Die Parameter-Tabelle enthält folgende wichtige Spalten:

- Display: Steuert die Darstellung im Interface (z.B. fett, ausgeblendet)
- Variable: Name der Variable für das Script
- Typ: Art der Variable (z.B. Stift, Oberfläche)
- Name: Angezeigter Name für den Benutzer
- Wert: Standardwert des Parameters

Weitere Details zu den Parametertypen findest du in der [Dokumentation](https://help.graphisoft.com/AC/25/ger/_AC25_Help/140_UserInterfaceDialogBoxes/140_UserInterfaceDialogBoxes-66.htm#XREF_66121_GDL_Master_Window).

Ergänzen wir nun die Befehle "pen" für den Konturstift und "set material" für die Oberfläche im Script. Speichere anschließend das Element und prüfe das Ergebnis.

```
!Bock auf Block
!20210903
!Manuel Emmenegger
!3D-Script

pen            penContour3D
set material   matCover

block A,B,ZZYZX

end !Ende des Scripts
```
---
## Individuelles 2D-Script
### 2D Parameter
Nun wollen wir uns die zweidimensionale Darstellung von unserem Block etwas genauer anschauen. Dazu beschäftigen wir uns mit den Befehlen [line2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/line2/) und [rect2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/rect2/) sowie den Attributen [pen](https://www.selfgdl.de/attribute/allgemein/pen/) und [set line\_type](https://www.selfgdl.de/attribute/linien/set-line_type/).

Ein separates 2D-Script bietet zwei wichtige Vorteile:

1. Bei komplexen 3D-Elementen ist die Grundrissdarstellung schneller, da nicht alles projiziert werden muss.

2. Grundrisse verwenden oft Symbole statt reiner Projektionen, z.B. bei Steckdosen und Schaltern.

Um die project2-Linien von unseren eigenen unterscheiden zu können, erstellen wir zunächst neue Parameter wie im Screenshot gezeigt.
[![Parameter](/assets/images/ac210-1010_05_Parameter.png)](/assets/images/ac210-1010_05_Parameter.png)


Die Befehle "pen" und "line_type" werden nach project2 eingefügt, sodass die project2-Linien mit Stift 1 und Linientyp 1 gezeichnet werden und alle weiteren Linien die neuen Attribute erhalten.

---

### line2
Mit dem Befehl line2 zeichnen wir die vier Linien unseres Blocks von oben gesehen. Der Befehl verwendet zwei Koordinatenpaare (x1,y1,x2,y2) und zieht eine Linie zwischen diesen Punkten. Die vier Linien bilden ein Rechteck, das in der 2D-Ansicht kongruent zur project2-Darstellung sein sollte.

```
!Bock auf Block
!20210903
!Manuel Emmenegger
!2D-Script

project2 3,270,1

pen            penContour2D
set line_type  ltContour2D
   !line2 x1,y1,x2,y2
    line2 0,0,A,0
    line2 A,0,A,B
    line2 A,B,B,0
    line2 0,B,0,0

end !Ende des Scripts
```
---

### rect2
Der Befehl [rect2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/rect2/) ermöglicht es, die vier Linien durch eine einzige Rechteck-Definition zu ersetzen. Dabei wird ein Rechteck zwischen zwei Punkten (x1,y1) und (x2,y2) aufgezogen.

```
!rect2 x1,y1,x2,y2
 rect2 0,0,A,B
```

Wie du sicherlich bemerkt hast, funktionieren die beiden Befehle „line2" und „rect2" nicht gleich wie der Befehl „block". Beim Befehl "block" konnten wir nämlich den Startpunkt des Blocks, also den Objektursprung (Startpunkt im Raum), nicht bestimmen, wir starteten automatisch immer beim Punkt 0,0,0. Mit dem Befehl "[add](https://www.selfgdl.de/1_ko_trafos/3d_komplex/add/)" lässt sich diese Einschränkung später umgehen. Die 2D-Befehle bieten hier also mehr Flexibilität bei der Positionierung der Elemente.

---

### poly2
Nachdem wir die Linienwerkzeuge kennengelernt haben, wollen wir nun mit dem Befehl "[poly2](https://www.selfgdl.de/2d-elemente-2/polygone/poly2/)" Schraffuren erstellen. Dafür benötigen wir auch den Befehl "[set fill](https://www.selfgdl.de/attribute/schraffuren/set-fill/)" zur Steuerung des Schraffurtyps.

Erstelle die Parameter wie im Screenshot gezeigt und ergänze den Schraffurtyp im Script nach den Stift- und Linientyp-Definitionen.

[![Parameter](/assets/images/ac210-1010_06_Parameter.png)](/assets/images/ac210-1010_06_Parameter.png)


Ersetze den rect2-Befehl durch poly2 und füge die Anzahl Ecken (4) sowie die Darstellungsart (1+2+4+0) vor den xy-Werten ein. Die Punkte entsprechen den gleichen Endpunkten wie bei line2.

Der Befehl „poly2" unterscheidet sich von „rect2" durch:

- Variable Anzahl Ecken
- Schraffur- oder Konturdarstellung 
- Möglichkeit offener Polygone

```
!Bock auf Block
!20210903
!Manuel Emmenegger
!2D-Script

project2 3,270,1

pen            penContour2D
set line_type  ltContour2D
set fill       fillType2D
   !poly2 n,Konturfüllung,
   !      x1,y1,
   !      ..
   !      Xn,yn
    poly2 4,1+2+4+0,
          0,0,
          A,0,
          A,B,
          0,B

end !Ende des Scripts
```
---

### poly2_
Der poly2_ Befehl bietet erweiterte Steuerungsmöglichkeiten für Kanten und Stifte. Wir beginnen mit [poly2_](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_/), bei dem jeder xy-Wert einen Status erhält: 1 für sichtbare Linien, -1 für Polygonzug-Endpunkte. Details zum Status findest du auf [selfgdl.de](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_/).

```
!poly2_ n,Konturfüllung,
!       x1,y1,Status,
!       ..
!       x2,y2,Status
 poly2_ 4,1+2+4+0,
        0,0,1,
        A,0,1,
        A,B,1,
        0,B,1
```
---

### poly2_A
Mit [poly2_A](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_a/) steuern wir den Vordergrundstift der Schraffur - ideal für massive Schraffuren.

```
!poly2_A n,Konturfüll,Schraffurstift,
!        x1,y1,Status,
!        ..
!        x2,y2,Status
 poly2_A 4,1+2+4+0,penFront2D,
         0,0,1,
         A,0,1,
         A,B,1,
         0,B,1
```
---

### poly2_B
Der Befehl [poly2_B](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_b/) bietet die umfangreichsten Steuerungsmöglichkeiten, da sowohl Vorder- als auch Hintergrundstift definiert werden können. Nach dem Speichern und Platzieren des Elements im Grundriss können alle erstellten Parameter getestet werden.

```
!poly2_B n,Konturfüll,Schraffurstift,
!        Hintergrundstift,
!        x1,y1,Status,
!        ..
!        x2,y2,Status
 poly2_B 4,1+2+4+0,penFront2D,
         penBack2D,
         0,0,1,
         A,0,1,
         A,B,1,
         0,B,1
```

---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}

