---
title: "Bock auf BLOCK?"
date: "2021-08-02"
categories: 
  - "archicad"
  - "start-mit-gdl"
tags: 
  - "archicad"
  - "gdl"
---

Mit Bock auf BLOCK legst du den Grundstein für den Einstieg in die Welt von GDL in ArchiCAD. Falls du noch nie etwas von GDL gehört hast, empfehle ich dir folgende zwei Artikel:

- [Warum GDL?](https://bimdo.ch/warum-gdl/)

- [GDL für Dummies](https://bimdo.ch/gdl-fuer-dummies/)

 Bevor wir mit dem ersten Script starten hier noch ein paar Tipps, welche dir den Einstieg sicherlich erleichtern werden. Skizziere deine Idee immer kurz auf, dies hilft enorm gewisse Parameter zu erkennen. Definiere die Anforderungen unter anderem für die Parametrik und unterteile diese Anforderungen in eine Art Stufenplan. Ich unterscheide jeweils zwischen grundlegenden Funktionen und Funktionen, die ein “nice to have“ sind. Durch diese Arbeitsweise werden dir schon etliche Lösungswege offenbart, jedoch wirst du gewisse zuerst ausprobieren müssen und da kommt das sogenannte [Prototyping](https://de.wikipedia.org/wiki/Prototyping_\(Softwareentwicklung\)) ins Spiel. Abschliessend noch ein paar Tipps zur Strukturierung des Scripts.

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

Es empfiehlt sich das eigene Script zu kommentieren und mit Überschriften zu versehen, so dass auch deine Team-Mitglieder eine Chance in deinem Script haben. Dazu schreibst du ein “!“ vor die entsprechende Zeile. Gerade, wenn in Teams an Scripts gearbeitet wird, sollte man sich auf einen Standard einigen. Schau doch mal in den [Standard von Graphisoft](http://gdl.graphisoft.com/gdl-style-guide) rein. Meine Scripts beginne ich immer mit einem Header, damit ich auch später noch weiss, wann ich dieses Script geschrieben oder geändert habe.

Je komplexer dein Script wird, desto mehr wirst du dieses strukturieren wollen, neben Subroutinen (zu denen kommen wir dann in einem weiteren Artikel noch) können schon Elemente wie Tabstobs, Gross-/ Kleinschreibung oder Kommentare eine grosse Hilfe sein.

Am Ende eines Scripts sollte immer ein END-Befehl kommen (Ausnahme im Masterscript), dies würde ich mir von Anfang angewöhnen, damit du es einfacher hast, wenn wir später mit Subroutinen arbeiten. Nun hast du hoffentlich genügend Bock auf BLOCK, na dann auf zu unserem ersten Script. Erstelle dazu ein neues GDL über das Menü Ablage und öffne das 3D-Script. Ergänze folgenden Code. Betrachte anschliessend das Ergebnis in der 3D-Ansicht.

```
block 1,2,3
```

<figure>

![](images/AC-GD2103_3D-Ansicht-300x278.png)

<figcaption>

Darstellung in der 3D-Ansicht

</figcaption>

</figure>

Ergänzen wir unser Script nun mit den bereits gelernten Inhalten, wobei hier das Ergebnis in der 3D-Ansicht immer noch das gleiche bleibt.

Nach dem Befehl stehen die Eingaben _1,2,3_, welche für _x,y,z_ stehen. Spiele nun etwas mit diesen Werten und kontrolliere das Ergebnis in der 3D-Ansicht. Weitere Informationen zu diesem Befehl findest du unter [selfgdl.de](https://www.selfgdl.de/3d-elemente/grundkoerper/block/).

```
!Bock auf Block
!20210903
!Manuel Emmenegger
!3D-Script

block 1,2,3

end !Ende des Scripts
```

```
!Bock auf Block
!20210903
!Manuel Emmenegger
!2D-Script

project2 3,270,1

end !Ende des Scripts
```

Im nächsten Schritt überarbeiten wir die 2D-Darstellung, denn zurzeit wird in der 2D-Ansicht noch nichts dargestellt. Dazu öffnen wir das 2D-Script und ergänzen die entsprechenden Script-Zeilen. Dieser Befehl erzeugt eine automatische Projektion vom 3D-Script. Ich verwende diesen jeweils zur Kontrolle des 2D-Scripts. Ich empfehle dir diesen Befehl nur zur Kontrolle zu benutzen, da je nach Komplexität der Geometrie, der Aufbau des Grundrisses verlangsamt wird. Auch hier empfehle ich dir wieder die Seite [selfgdl.ch](https://www.selfgdl.de/2d-elemente-2/projektionen/project2/)

Jetzt müssen wir dein erstes Element nur noch speichern, wir werden in den kommenden Artikeln dieses Script immer weiterentwickeln. Über das Menü Ablage/sichern lässt sich dein erstes GDL in der eingebetteten Bibliothek speichern, speichere danach deine ArchiCAD-Datei als pln und dein GDL wird in dieser Datei mit gespeichert. Wir werden uns später mit der ganzen Verwaltung von Bibliotheken auseinandersetzen.

![](images/AC-GD2103_2D-Ansicht-300x273.png)

[Im nächsten Artikel](https://bimdo.ch/ac-gd2104_block-parameter/) [](https://bimdo.ch/ac-gd2104_block-parameter/\(öffnet in neuem Tab\))beschäftigen wir uns mit den Parametern von unserem Block, damit dieser auch ohne das Bearbeiten vom Script verändert werden kann.

---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
