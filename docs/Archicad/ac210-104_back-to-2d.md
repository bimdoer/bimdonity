---
title: "Back to 2D"
date: "2021-09-22"
categories: 
  - "archicad"
  - "start-mit-gdl"
tags: 
  - "archicad"
  - "gdl"
---

Im letzen Blog-Eintrag [Block-Parameter](https://bimdo.ch/?p=456) ging es um die Parametrisierung von unserem Block im 3D-Fenster. Nun wollen wir uns die zweidimensionale Darstellung von unserem Block etwas genauer anschauen. Dazu beschäftigen wir uns in diesem Artikel mit den Befehlen [line2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/line2/) und [rect2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/rect2/) sowie den Attributen [pen](https://www.selfgdl.de/attribute/allgemein/pen/) und [set line\_type](https://www.selfgdl.de/attribute/linien/set-line_type/).

Unser aktuelles Script enthält noch immer den Befehl “project2“ und dies ist zur Kontrolle durchaus gut so, aber warum machen wir uns überhaupt die Mühe ein separates 2D-Script zu schreiben? Nach meinem Verständnis gibt es hierzu zwei Gründe.

1. Je komplexer die dreidimensionalen Elemente, desto komplexer die zweidimensionale Projektion. Gerade wenn man mit runden Elementen arbeitet sollte man sich immer fragen, zu welchem Zeitpunkt welcher Detaillierungsgrad nötig ist. Dank einem separaten 2D-Script ist der Grundrissaufbau deshalb einiges schneller bei komplexeren Elementen.

3. Im Grundriss werden häufig Abstraktionen oder Symbolsprachen verwendet, nehmen wir als Beispiel eine Steckdose und einen Lichtschalter. Würde man hier im Grundriss einfach die Aufsicht darstellen, wäre der Unterschied nur schwer erkennbar und auf einen Blick festzustellen ob es sich um eine Einfach- oder Dreifachsteckdose handelt schlicht unmöglich.

Damit wir in der 2D-Ansicht sehr einfach unterscheiden können zwischen den generierten project2-Linien und unseren programmierten Linien, beginnen wir als erstes wieder mit dem Erstellen einiger Parameter. Ergänze die entsprechenden Parameter gemäss nebenstehendem Screenshot.

<figure>

[![](images/AC-GD2105_Parameter-1024x576.png)](https://bimdo.ch/wp-content/uploads/2021/10/AC-GD2105_Parameter.png)

<figcaption>

Ergänze die zwei neuen Parameter penContour2D & ltContour2D.

</figcaption>

</figure>

Ergänzen wir nun unser Script mit den neu erstellten Parametern und nutzen den bereits bekannten Befehl „pen“ sowie den neuen Befehl “line\_type“. Indem wir die beiden Attribute erst nach dem project2-Befehl ergänzen, werden dessen Linien immer noch Stift 1 und Linientyp 1 haben und alles was nach unseren Attributen kommt, wird in den Farben der neuen Attributierung dargestellt.

Von oben betrachtet besteht unser Block aus vier Linien und genau diese programmieren wir in einem ersten Schritt mit dem Befehl [line2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/line2/). Dieser Befehl funktioniert hat zwei Koordinaten, es wird also eine Linie von Punkt 1 (x1, y1) zu Punkt 2 (x2, y2) gezogen. In meinem Beispiel geht die erste Linie nach rechts, die zweite dann nach oben, die dritte nach links und die letze Linie schliesst das Rechteck von links oben zu meinem Startpunkt 0,0. Hier empfiehlt es sich immer kurz eine einfache Skizze zu machen, damit man sich vorstellen kann, wo man sich gerade befindet im Koordinatensystem. Das Ergebnis in der 2D-Ansicht sollten nun zwei kongruente Rechtecke sein.

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

In einem nächsten Schritt wollen wir den Befehl [rect2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/rect2/) anschauen, denn dieser ermöglicht es uns die vier Zeilen Script auf eine zu reduzieren. Wir ziehen also ein Reckteck vom Punkt 1 (x1, y1) zum Punkt 2 (x2, y2) auf.

```
!rect2 x1,y1,x2,y2
 rect2 0,0,A,B
```

Wie du sicherlich bemerkt hast, funktionieren die beiden Befehle „line2“ und „rect2“ nicht gleich wie der Befehl „block“. Beim Befehl “block“ konnten wir nämlich den Startpunkt des Blocks, also den Objektursprung (Startpunkt im Raum), nicht bestimmen, wir starteten automatisch immer beim Punkt 0,0,0. Dieser Thematik werden wir uns später im Zusammenhang mit dem Befahl “[add](https://www.selfgdl.de/1_ko_trafos/3d_komplex/add/)“ noch annehmen, im nächsten Artikel wollen wir uns aber zuerst noch etwas mit der zweidimensionalen Darstellung auseinandersetzen und uns den Befehl [poly2](https://www.selfgdl.de/2d-elemente-2/polygone/poly2/) etwas genauer anschauen.

---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
