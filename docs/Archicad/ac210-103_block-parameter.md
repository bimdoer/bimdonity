---
title: "BLOCK-Parameter"
date: "2021-09-22"
categories: 
  - "archicad"
  - "start-mit-gdl"
tags: 
  - "archicad"
  - "gdl"
---

Im letzten Artikel „[Bock auf BLOCK](https://bimdo.ch/bock-auf-block/)“ haben wir uns mit dem Befehl “[block](https://www.selfgdl.de/3d-elemente/grundkoerper/block/)“ auseinandergesetzt, welcher einen Quader erzeugt. Weiter haben wir uns den Befehl “[project2](https://www.selfgdl.de/2d-elemente-2/projektionen/project2/)“ zu nutze gemacht, damit wir eine einfache Grundriss-Projektion erzeugen konnten. Nun geht es darum dieses Element zu parametrisieren, hierfür schauen wir uns zuerst ein paar Standardparameter an. Öffne dazu in unserem bereits erstellten Element auf der linken Seite das Register “Parameter“, hier sollten bei dir ebenfalls drei Standardparameter vorhanden sein. Der Parameter A steht für die X-Achse, Parameter B für die Y-Achse und der Parameter ZZYZX für die Z-Achse.

Ersetzen wir nun unsere Zahlen im Script mit den Standardparametern und prüfen die Veränderung in der 3D-Ansicht. Nun können wir im Register Parameter die Parameter A, B und ZZYZX verändern und unser Block verändert sich in der 3D-Ansicht und dank des “project2“-Befehls auch in der 2D-Ansicht.

Speichern wir nun das Element und schliessen den GDL-Editor, anschliessend klicken wir auf der linken Seite auf das Objekt-Werkzeug und platzieren das entsprechende Element.

```
!Bock auf Block
!20210903
!Manuel Emmenegger
!3D-Script

block A,B,ZZYZX

end !Ende des Scripts
```

Wenn wir uns mit dem Tastenanschlag “T“ in die Einstellungen des Objekts begeben, sehen wir das gewohnte Übersichtsfenster und hier haben wir ebenfalls die Parameter A, B und ZZYZX. Diese befinden sich im oberen Bereich neben dem Vorschaubild. Somit hast du nun dein erstes parametrisiertes GDL-Objekt erstellt und wir wollen uns nun die Parameter Oberfläche, Stift und Schatten anschauen. Klicke dazu auf das platzierte GDL-Objekt und mit dem Kürzel ctrl+Shift+O gelangst du direkt in den Editor des selektierten Elements.

<figure>

[![](images/AC-GD2104_T-1-1024x534.png)](https://bimdo.ch/wp-content/uploads/2021/10/AC-GD2104_T-1.png)

<figcaption>

Einstellungsdialog aufgerufen durch den Tastenkürzel T mit den Parametern A, B und ZZYZX.

</figcaption>

</figure>

Als erstes wollen wir nun die zwei Parameter erstellen und entsprechend einordnen, anschliessend bauen wir diese dann ins Script ein. Im Register Parameter kannst du im oberen Bereich auf „neuer Parameter“ erstellen klicken und dir drei neue Parameter erstellen. Für die Namensgebung der Parameter empfehle ich dir ein gewisses Konzept für dich zu fixieren, hierzu kann dir der [Standard von Graphisoft](https://gdl.graphisoft.com/gdl-style-guide/naming-conventions) eventuell schon ein bisschen Abhilfe schaffen. Ich arbeite vorwiegend mit englischen Begriffen und kürze diese jeweils noch ein bisschen zusammen. Eine Liste mit den bereits vergebenen Parametern von Graphisoft findest du [hier](https://gdl.graphisoft.com/gdl_reference_guide_chapter/global-variables). Es macht in meinen Augen Sinn etwas längere Namen zu verwenden, damit man direkt ableiten kann um welchen Parameter es sich handelt. Dadurch wird das Script zwar etwas länger, aber man muss nicht eine zusätzliche Legende mit den Abkürzungen erstellen. Am wichtigsten ist jedoch eine durchgängige Logik, damit du auch später noch Parameter ergänzen kannst und mit automatischen Suchen-/ Ersetzen-Funktionen arbeiten kannst.

<figure>

[![](images/AC-GD2104_Parameter-1.png)](https://bimdo.ch/wp-content/uploads/2021/10/AC-GD2104_Parameter-1.png)

<figcaption>

Erklärung zu den neu erstellten Parametern.

</figcaption>

</figure>

<figure>

[![](images/AC-GD2104_GIF-1.gif)](https://bimdo.ch/wp-content/uploads/2021/10/AC-GD2104_GIF-1.gif)

<figcaption>

Veränderung der Parameter A, B und ZZYZX.

</figcaption>

</figure>

Schauen wir uns nun unsere drei erstellten Parameter etwas genauer an. In der obersten Zeile finden wir von links nach rechts Display, Variable, Typ, Name und Wert. In der ersten Spalte Display können wir Einfluss aufs User-Interface nehmen, heisst wir können den Namen der Variable fett darstellen oder die Variable ausblenden (Kreuz), etc. In der zweiten Spalte Variable definieren wir die Variable selber, diese wird dann auch im Script verwendet. Beim Typ definieren wir die Art der Variable in unserem Fall also Stift und Oberfläche, mehr dazu findest du [hier](https://help.graphisoft.com/AC/25/ger/_AC25_Help/140_UserInterfaceDialogBoxes/140_UserInterfaceDialogBoxes-66.htm#XREF_66121_GDL_Master_Window) sehr gut erklärt. Die Spalte Namen wird dem User schlussendlich angezeigt, heisst er muss deine Bezeichnungen der Variablen nicht verstehen, da er nur den Namen zu Gesicht bekommt. In der letzten Spalte definierst du dann noch den Standardwert für deinen Parameter.

Genug Theorie, begeben wir uns wieder in unser Script und ergänzen die entsprechenden Zeilen Code. Für den Konturstift verwenden wir den Befehl „[pen](https://www.selfgdl.de/attribute/allgemein/pen/)“ und für die Parametrisierung der Oberfläche den Befehl “[set material](https://www.selfgdl.de/attribute/materialien/set-material/)“. Anschliessend kannst du das Element wieder speichern und das Ergebnis in den Einstellungen des vorherig platzierten Elements prüfen.

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

Bis hierhin haben wir ein dreidimensionales Objekt erstellt, welches sowohl geometrische Parameter als auch Attribute enthält. Aktuell fehlt uns aber noch ein parametrisiertes 2D-Script, denn wir nutzen zur Zeit den Befehl “project2“, welcher nur ein Abbild des 3D-Scripts generiert. Wie ein solches 2D-Script aussehen kann und was für Befehle hierzu zur Auswahl stehen, erfährst du im nächsten Artikel [Back to 2D](https://bimdo.ch/ac-gd2105_back-to-2d/).

<figure>

[![](images/AC-GD2104_BoxGruen-1024x574.png)](https://bimdo.ch/wp-content/uploads/2021/10/AC-GD2104_BoxGruen.png)

<figcaption>

Endergebnis in den Objekt-Einstellungen des platzierten Elements in ArchiCAD.

</figcaption>

</figure>

---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
