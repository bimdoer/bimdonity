---
title: "Qualitätskontrolle IFC (Teil 2)"
date: "2022-05-19"
categories: 
  - "ifc-export"
tags: 
  - "bim"
  - "ifc"
  - "navisworks"
  - "solibri"
---

Im ersten Artikel haben wir uns vorwiegend der Kontrolle 🔎 direkt im IFC-Export gewidmet, in diesem Artikel wollen wir uns verschiedenen Möglichkeiten der visuellen 👓 Prüfung und der zusammenhängenden Datenvisualisierung 📊 annehmen. Dazu einige Beispiele mit BIMCollab Zoom, Solibri, Dalux, Excel und PowerBI.

- [Visuelle Geometrie-Prüfung](#visuell)

- [Visuelle Informations-Prüfung](#info)
    - [Geschosse](#geschosse)
    
    - [IFC-Entitäten](#enti)

- [Daten visualisieren](#data)
    - [Excel](#excel)
    
    - [PowerBI](#power)

#### Visuelle Geometrie-Prüfung 👓

Die visuelle Prüfung lohnt sich in jedem Fall, denn du wirst auf einen Blick sehen, wenn ein Geschoss fehlt. Besonders bei Teilmodellen schaue ich mir jeweils die heiklen Parts beim Export etwas genauer an. Für das Rohbaumodell aus dem Architekturmodell, müssen so einige Filter eingestellt werden für den Export und da gibt es Bauteile die besonders anfällig auf Fehler sind:

- Öffnungen (Fenster, Türen, etc.)

- Solid-Befehle (z.B. Deckengefälle)

- Verschnitte (Wandecken, Übergänge Geschoss, etc.)

- Umbau-Filter (ArchiCAD)

<figure>

[![](images/IF-EX2204_fenster-1024x712.png)](https://bimdo.ch/wp-content/uploads/2022/04/IF-EX2204_fenster.png)

<figcaption>

Nicht alles was im Grundriss toll aussieht, funktioniert auch im Modell, deshalb sollte man gerade bei Schichteinzügen zweimal hinschauen und sich überlegen, wie man diese modelliert.

</figcaption>

</figure>

Solche Elemente gilt es einfach am Anfang des Prozesses einmal zu prüfen, danach genügen Stichproben. Je früher eine solche Prüfung vorgenommen wird, desto eher kann man die Arbeitsweise des Teams in beispielsweise ArchiCAD noch lenken. Dies können Favoriten sein, Voreinstellungen im Template oder ganz einfach interne Schulungen, damit allen klar ist, weshalb wir etwas wie modellieren. Häufig ist es schwer, den ganzen Rattenschwanz an Abhängigkeiten kompakt aufzuzeigen, aber durch die Schulung, muss man sich selber immer wieder damit auseinandersetzen und Konzepte überarbeiten.

#### Visuelle Informations-Prüfung

###### Geschosse

Bei den Geschossen kontrolliere ich immer deren Bezeichnung, diese sollten immer gleich viele Stellen haben. (z.B. 08UG, 30OG und nicht 8UG, 10OG) Weiter sollte man sich hier angewöhnen die Geschosse durchgängig zu nummerieren. Die Untergeschosse sollten nicht mit einem -2UG angeschrieben werden, weil wir die Geschosse nach Name sortieren wollen. Weiter sollte die Zahl immer vorne sein, ansonsten werden die Geschosse wieder falsch sortiert. Hierzu ein paar “falsche Beispiele zur Veranschaulichung:

<figure>

[![](images/IF-EX2204_geschoss-1024x768.png)](https://bimdo.ch/wp-content/uploads/2022/04/IF-EX2204_geschoss.png)

<figcaption>

In rot die Namenskonvention für die Abbildung der Geschosse.

</figcaption>

</figure>

###### 1\. unsortiert

AT04  
OG03  
OG02  
OG01  
EG00  
UG01  
UG02

###### 1\. sortiert

AT04  
EG00  
OG01  
OG02  
OG03  
UG01  
UG02

###### 2\. unsortiert

04AT  
03OG  
02OG  
01OG  
00EG  
01UG  
02UG

###### 2\. sortiert

00EG  
01OG  
01UG  
02OG  
02UG  
03OG  
04AT

Bei beiden Varianten kommen wir nicht zu dem gewünschten Ziel und je nach Software wirst du immer wieder über dieses Thema stolpern. Und wenn du jetzt sagst, dass BIM zu kompliziert ist, dann brechen wir dies doch mal runter auf die 2D-Pläne, die wir als PDF auf dem Server ablegen. Spannend, dass wir da genau das gleiche Problem bekommen, aus diesem Grund hier ein mögliches Konzept, welches sowohl noch weitere Untergeschosse als auch Obergeschosse zulässt.

###### 3\. unsortiert

14AT  
13OG  
12OG  
11OG  
10EG  
09UG  
08UG

###### 3\. sortiert

14AT  
13OG  
12OG  
11OG  
10EG  
09UG  
08UG

Ich würde nicht mit einer Nummerierung von unten nach oben oder umgekehrt starten, sondern von der Mitte aus beim Erdgeschoss. Sonst haben wir plötzlich ein Problem, wenn während dem Arbeitsprozess ein weiteres Geschoss hinzukommt. Die zweite Zahl ist dann ja ab dem Erdgeschoss nach oben immer gleich dem Geschoss und Untergschosse haben wir ja nicht ganz so viele. Mit der dritten Variante haben wir also eine Variante, die bei der Sortierung nicht durcheinander gerät. Weiter würde ich bei dieser visuellen Prüfung Acht geben, dass die Elemente wirklich in dieser Geschoss-Struktur integriert sind. Hier kann man auch mal geschossweise Elemente ein-/ ausblenden und sieht so direkt, ob die Zugehörigkeit zu den Geschossen einigermassen stimmig ist.

###### IFC-Entitäten

Hier macht ein stichprobenartiges Verfahren sicher Sinn, sind die entsprechenden Psets vorhanden und haben diese auch einen Inhalt? Wurde die Information load bearing richtig geschlauft, wenn ja dann liegt sie nun auf dem Standard-Feld, wenn nein, dann haben wir schon den ersten Fehler gefunden. Besondere Beachtung ist dabei den verschiedenen Viewern zu geben, denn es liegt nicht immer an deinem Export, die verschiednen Viewer können dein IFC auch verschieden interpretieren und gewisse Tools haben Probleme mit IFC-Entitäten, welche nicht dem Standard IFC-Schema entsprechen.

<figure>

[![](images/IF-EX2204_load-1024x593.png)](https://bimdo.ch/wp-content/uploads/2022/04/IF-EX2204_load.png)

<figcaption>

Wenn die Standardeigenschaften, wie z.B. tragend/ nicht tragend, nicht auf dem Standardfeld liegen, funktionieren vordefinierte Prüfsystem nicht.

</figcaption>

</figure>

Eine weitere Möglichkeit besteht mit der Suchfunktion, mit dieser kannst du sehr simpel Information filtern. Noch einfacher geht dies aber mit entsprechenden Filter-Systemen oder automatischen Einfärbungen von Bauteilen. Hierzu wollen wir uns zwei sehr simple Beispiele mit BIMCollab Zoom und Solibri anschauen.

**BIMCollab Zoom:** Bei BIMCollab Zoom kannst du sogenannte SmartViews erstellen, diese sind vergleichbar mit der grafischen Überschreibung in ArchiCAD. Dabei kannst du entsprechende Modellinhalte filtern und auch einfärben. Im nebenstehenden Beispiel siehst du eine automatische Einfärbung der Fenster an Hand ihrer Typennummer. So kann visuell sehr schnell überprüft werden, wie viele Typen vorhanden sind oder ob die Fenster zum richtigen Typ gehören.

<figure>

[![](images/IF-EX2204_farbigefenster-1024x829.png)](https://bimdo.ch/wp-content/uploads/2022/04/IF-EX2204_farbigefenster.png)

<figcaption>

Fenster eingefärbt nach Typen mit den SmartViews von BIMCollab Zoom (Bildquelle Hunold Architekten AG)

</figcaption>

</figure>

**Solibri:** Eine ähnliche Option steht auch in Solibri mit der Auswertung zur Verfügung. Im nebenstehenden Beispiel werden Fassadenpaneele an Hand von ihrer Grösse in verschiedene Gruppen als Zeile in der Auswertung unterteilt und im Modell eingefärbt. So kann visuell noch sehr viel optimiert werden, weil man ein anderes Verständnis von den Informationen bekommt.

<figure>

![](images/IF-EX2204_GIF-final.gif)

<figcaption>

Variantenstudie im Projekt Hirtenhofring Luzern der Hunold Architekten AG.

</figcaption>

</figure>

#### Daten visualisieren

###### Excel

Mit Excel ist es sehr einfach gewisse Konventionen oder doppelte Werte zu prüfen, dafür brauchst du also nicht zwingend eine Prüfsoftware für deine ersten Schritte in diesem Bereich. Unter dem Reiter Daten & Daten prüfen lassen sich sehr simple Regeln für die ausgewählten Felder anlegen. Eine entsprechende Tabelle kannst du z.B. aus BIMCollab Zoom per CSV exportieren und in Excel öffnen. Je nach Prozess lassen sich so Informationen auch direkt anpassen und als Excel wieder in ArchiCAD importieren. Im nebenstehenden Beispiel werden in der ersten Spalte Namenskonventionen geprüft, in der zweiten Spalte visualisiert ein Balkendiagramm die verschiedenen Rahmenaussenmass-Breiten und in der Spalte ganz rechts werden die Rahmenaussenmass-Höhen in verschiedene Farbcodexe eingeteilt.

<figure>

[![](images/IF-EX2204_xls.png)](https://bimdo.ch/wp-content/uploads/2022/05/IF-EX2204_xls.png)

<figcaption>

Mit der bedingten Formatierung in Excel lassen sich Werte einfach visualisieren, in diesem Beispiel eine Auswertung der Fenster direkt aus ArchiCAD.

</figcaption>

</figure>

###### PowerBI

Die Möglichkeiten mit PowerBI sind praktisch unbeschränkt und es macht echt Spass interaktive Dashboards zu erstellen. Plötzlich lassen sich Abhängigkeiten von Daten visualisieren und gegenüberstellen, das sorgt für eine völlig neue Betrachtungsweise deiner Daten. Je nach Tool sind sogar direkte Schnittstellen vorhanden und sonst tut es hier auch wieder ein einfacher CSV-Export und wenn du diesen immer schön unter dem gleichen Pfad überschreibst, ist dein Dashboard immer auf dem aktuellsten Stand.

Im nebenstehenden Beispiel wurden verschiedene Projektstände (ca. 50 IFC-Dateien) in einem Modell zusammengeführt. Danach wurde eine Bauteilliste als CSV gespeichert und nun lassen sich die verschiedenen Projektstände an Hand Informationen, wie z.B. Volumenveränderung vergleichen. Dies kann enorme Mehrwerte bieten, wenn man aufzeigen kann, zu welchem Projektstand wie viel verändert wurde.

<figure>

[![](images/P-180PowerBI-1024x607.jpg)](https://bimdo.ch/wp-content/uploads/2022/04/P-180PowerBI-scaled.jpg)

<figcaption>

Ein Vergleich verschiedener Bauteile über eine lange Projektphase zeigt auf, was wann geändert wurde und welche Bauteile zusammenhängend verändert wurden.

</figcaption>

</figure>

Ich hoffe ich konnte dir mit diesem Artikel mögliche Herangehensweisen von Prüfungen am Modell etwas näher bringen, eigentlich ja wirklich keine Hexerei. Für welche Methode hast du dich entschieden oder wartest du noch auf meinen nächsten Artikel mit den automatisierten Prüfprozessen?
---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
