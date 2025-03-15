---
title: "Rect2 vs. Poly2"
date: "2021-12-08"
categories: 
  - "archicad"
  - "start-mit-gdl"
tags: 
  - "archicad"
  - "gdl"
---

Im Artikel [Back to 2D](https://bimdo.ch/ac-gd2105_back-to-2d/) haben wir uns intensiv mit den Darstellungsmöglichkeiten im 2D-Script beschäftigt und die entsprechenden Linienwerkzeuge in einem Beispiel angewendet, nun wollen wir uns mit dem Befehl “[poly2](https://www.selfgdl.de/2d-elemente-2/polygone/poly2/)“ die Schraffur anschauen. Weiter benötigen wir für die Parametrisierung der Schraffur den Befehl “[set fill](https://www.selfgdl.de/attribute/schraffuren/set-fill/)“, damit wir auch den Schraffurtyp steuern können.

Starten wir mit der Erstellung einiger Parameter gemäss nebenstehendem Screenshot. Anschliessend ergänzen wir den Schraffurtyp mit entsprechendem Befehl auch in unserem Script direkt nach der Definition von Stift und Linientyp.

<figure>

[![](images/AC-GD2106_Parameter-1024x576.png)](https://bimdo.ch/wp-content/uploads/2021/10/AC-GD2106_Parameter.png)

<figcaption>

Parameterübersicht mit den neu erstellten Parametern.

</figcaption>

</figure>

Den bestehenden rect2-Befehl ersetzen wir nun mit dem Befehl „poly2“ und ergänzen vor den xy-Werten die Anzahl Ecken (4) sowie die Darstellungsart (1+2+4+0) jeweils mit einem Komma getrennt. (Hinweis: Die Punkte entsprechen den gleichen Endpunkten der Linien, die wir im vorherigen Beitrag mit line2 benutzt haben) Es spielt dabei keine Rolle, ob ein Leerschlag oder ein Absatz zwischen den einzelnen Werten vorhanden ist, ich mache dies hier nur zum besseren Verständnis.

Der Befehl „poly2“ unterscheidet sich zum Befehlt „rect2“ in den folgenden Punkten:

- poly2 hat n Ecken

- poly2 kann eine Schraffur darstellen oder nur die Kontur wie rect2

- poly2 kann ein offenes Polygon darstellen, was rect2 nicht kann, hierfür wären wiederum einzelen line2-Befehle nötig

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

Der poly2-Befehl hat noch einige Steigerungsformen, damit die einzelnen Kanten sowie Vorder-& Hintergrundstift differenzierter gesteuert werden können. Wenn du den poly2-Befehl verstehst, wirst du später auch relativ einfach den Sprung zu den komplexeren 3D-Befehlen machen können, da diese auf dem gleichen Prinzip aufbauen. Wir werden nun den poly2-Befehl Schritt für Schritt ausbauen, bis wir Vorder-& Hintergrundstift steuern können.

Starten wir mit dem Befehl [poly2\_](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_/) und ergänzen hinter jedem xy-Wert den entsprechenden Status der ausgeführten Kante. Mehr zu diesem Status findest du sehr gut erklärt auf [selfgdl.de](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_/). Mit dem Wert 1 ist die Linie sichtbar, mit dem Wert -1 signalisieren wir den Endpunkt eines Polygonzuges.

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

Mit dem Befehl [poly2\_A](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_a/) können wir nun auch Einfluss auf den Schraffurstift nehmen, wichtig dabei ist, dass wir hier nur den Vordergrundstift der Schraffur steuern können. Wenn du den Schraffurtyp auf “nur Vordergrund-Stift“ eingestellt hast, bzw. wenn die Schraffur massiv sein soll, ist dieser Befehl die optimale Wahl.

Ich empfehle dir auch hier immer kurz einen Blick in die 2D-Ansicht zu werfen und das Ergebnis zu prüfen.

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

Kommen wir nun zum Endresultat mit dem Befehl „[poly2\_B](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_b/)“, welcher uns die Möglichkeit bietet auch den Hintergrundstift zu steuern. Noch komplexere poly2-Befehle findest du ebenfalls auf [selfgdl.de](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_b2/) sehr gut erklärt. Auch bei diese letzten Beispiel gilt, die Absätze können so angelegt werden, wie es für dich am leserlichsten ist.

Speichere dein Element nun ab und platziere es im Grundriss. Nun solltest du mal einen vollumfänglichen Test vornehmen. Dazu kannst du die bisherig erstellten Parameter testen.

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

Ich freue mich darauf dir in meinem nächsten Artikel den add-Befehl etwas näher zu bringen. Wir tasten uns anhand eines Tisches an unser erstes praxistaugliches GDL-Element heran;)


---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
