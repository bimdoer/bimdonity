---
title: "Qualitätskontrolle IFC (Teil 1)"
date: "2022-04-04"
categories: 
  - "archicad"
  - "ifc-export"
tags: 
  - "archicad"
  - "export"
  - "ifc"
  - "qualitaetskontrolle"
---

Immer mehr Daten und immer weniger Zeit, so könnte man gewisse digitale Arbeitsprozesse wohl zusammenfassen. Deshalb gilt auch hier "less is more" und das erfordert eine genaue Auseinandersetzung mit dem geforderten Output. Damit du schlussendlich mit gutem Gewissen dein Modell weitergeben kannst, zeige ich hier einige Methoden auf, die mir meinen Alltag immer mal wieder vereinfachen. Dabei bleiben wir bei den einfachen Anwendungsfällen und arbeiten uns dann hoch bis zu komplexeren Prüfregeln.

- [Fehlermeldungen](#Fehler)

- [Export-Protokoll](#Export)

- [Begriffe](#begriffe)

#### Fehlermeldungen

Bereits beim Export wirst du auf gewisse Export-Fehler hingewiesen, dieser würde ich immer besondere Beachtung schenken. Ich weiss, Fehlermeldungen klickt man weg 😀, bei dieser würde ich aber eine Ausnahme machen und ihr die doppelte Aufmerksamkeit schenken. Aussagekraft gleich Null, aber wir wissen, dass fünf Elemente fehlen und dass wir für mehr Informationen das Protokoll aufsuchen sollten. Vorab kann ich schon mal sagen, dass ich hier den Export mit 0mm starken Elementen herausfordere, weil dies für gewisse Arbeitsmodelle sehr praktisch ist. Falls du dich gerade fragst, für was man 0mm starke Elemente nutzen kann, findest du im Abschnitt [Oberflächenmodell](#oberfla) bestimmt eine Antwort darauf.

<figure>

[![](images/IF-EX2201_Fehlermeldung-1024x569.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_Fehlermeldung.png)

<figcaption>

Fehlermeldung in ArchiCAD beim IFC-Export von Elementen mit 0mm Stärke.

</figcaption>

</figure>

#### Exportprotokoll

Ein Blick ins Protokoll lohnt sich immer, hier siehst du die verschiedenen Berechnungszeiten schön aufgelistet. Auch ohne IFC-Export findest du ab und an hier deine Antwort auf eine korrupte Geometrie oder doppelte GUIDs in deinem Projekt.

Wir wollen uns jetzt aber unserem letzten IFC-Export widmen und uns den Output der Fehlermeldung anschauen. Wir können im unteren Bereich entnehmen, dass beim letzten Export bei 5/21 Elementen ein Problem aufgetreten ist. Diese fünf Elemente sind mit ihrer GUID noch etwas weiter unten aufgelistet und jetzt geht es auf die Suche🔎.

<figure>

[![](images/IF-EX2201_protokoll-1024x573.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_protokoll.png)

<figcaption>

Protokoll-Auszug nach dem IFC-Export mit entsprechender Elementauflistung.

</figcaption>

</figure>

Dies ist wiederum eine tolle manuelle Arbeit, deshalb ist jeder Modell-Verantwortliche daran interessiert von Anfang an richtig zu modellieren. In ArchiCAD kann mit dem Tool "Suchen & Aktivieren" nach den entsprechenden GUIDs gesucht werden, solche Suchfunktionen gibt es aber nicht nur in ArchiCAD, du wirst etwas in dieser Art sogar in deinem IFC-Viewer finden.

<figure>

![](images/IF-EX2201_sa01-2-1024x569.png)

<figcaption>

Suchen & Aktivieren von einem Element mit der zugehörigen GUID.

</figcaption>

</figure>

Bestimmt wirst du dich gefragt haben, warum ich fünf Boxen exportiere. In der nebenstehenden Grafik siehst du, welche Einstellungen ich jeweils im entsprechenden Werkzeug vorgenommen habe. Dies ist natürlich sehr spezifisch auf die Software ArchiCAD zugeschnitten, es geht hierbei aber weniger um die Software sondern um das Bewusstsein, dass es eben darauf ankommt, mit welchem Werkzeug du welche Elemente modellierst. Das Werkzeug Morph in ArchiCAD ist vergleichbar mit einer Knetmasse in der realen Welt. Während bei Wand, Decke und Dach klare Parameter für Länge, Breite und Höhe zur Verfügung stehen, gibt es beim Morph keine klaren Parameter.

<figure>

[![](images/IF-EX2201_legende-1024x568.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_legende.png)

<figcaption>

Die verschiedenen Farben stehen für die verschiedenen Einstellungen in den entsprechenden Werkzeugen.

</figcaption>

</figure>

Beim Export mit dem Allgemeinen IFC-Übersetzer 2x3 in ArchiCAD 25 werden die markierten Elemente nicht mitgegeben, auch mit dem IFC-Schema 4 kriegen wir es nicht hin😟. Dann ist es an der Zeit mal den Übersetzer auf den Kopf zu stellen. Mit der Einstellung "Exakter Geometrieexport" in den Übersetzer-Einstellungen klappt es ohne Fehlermeldung, diese Einstellung hat dann jedoch wiederum andere Folgen. Diese können wir jedoch getrost ignorieren, wenn es uns nur um den Export eines [Oberflächenmodells](#oberfla) als Arbeitsmodell geht.

<figure>

![](images/IF-EX2201_sa02-1-1024x568.png)

<figcaption>

Suchen & Aktivieren von mehreren Elementen mit der zugehörigen GUID.

</figcaption>

</figure>

Das ist jetzt eine tolle Sache mit diesem Protokoll und den Fehlermeldungen, trotzdem lohnt sich eine Qualitätskontrolle in einer Viewer-Software immer! Wie du siehst, wurden noch ein paar weitere Elemente nicht exportiert und diese tauchen leider nicht im Protokoll auf. Aber keine Panik, im Normalfall verwendet man keine 0mm starken Elemente und wenn doch, dann nur in einem Arbeitsmodell mit überschaubarer Datenmenge. Mehr zu diesem Thema im nächsten Abschnitt Begriffe.

<figure>

[![](images/IF-EX2201_export2x3-1024x648.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_export2x3.png)

<figcaption>

Exportierte Elemente mit dem Standardübersetzer in einer Viewer-Software.

</figcaption>

</figure>

#### Begriffe

##### 0-Schicht

Gerade in Holzbau-Projekten kann man immer wieder in Versuchung kommen, Folien im Bauteil direkt zu modellieren. Ob das Sinn macht oder nicht, hängt ganz vom Anwendungsfall ab. Ich empfehle der Folie jedoch immer eine Stärke zu geben, da dies sonst beim Export und bei späteren Prüfungen immer wieder Fehler verursachen kann. Trotzdem macht es in gewissen Arbeitsmodellen Sinn mit 0mm starken Elementen zu arbeiten und genau darum geht es im nächsten Abschnitt [Oberflächemodell](#oberfla).

Ein relativ schnell ersichtliches Problem ist zum Beispiel die Überschreibung der Oberfläche, welche beim grünen Beispiel ganz rechts zu Problemen führt. Hier wurde ein mehrschichtiges Bauteil mit zwei Schichten erstellt, eine Schicht ist jedoch 0mm stark. Beim gesamtheitlichen Überschreiben der Oberfläche mit der Farbe grün wird die 0mm starke Schicht nicht überschrieben und deshalb bleibt ein Teil des Bauteils grau. Immer genau auf der Seite, wo die 0mm starke Schicht vorhanden ist. Sie existiert zwar im Aufbau, aber irgendwie doch nicht ganz oder eher korrupt💰. Ach ja und die rote Fläche die da irgendwie fehlt, das ist nicht etwa ästhetische Provokation, sondern in ArchiCAD schlichtweg nicht möglich. Mehrschichtige Decken mit 0mm Stärke lassen sich nicht modellieren, bei den einschichtigen klappt es.

<figure>

[![](images/IF-EX2201_ms02-1024x568.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_ms02.png)

<figcaption>

Einstellungen mehrschichtiges Bauteil mit 0mm starker Schicht.

</figcaption>

</figure>

<figure>

[![](images/IF-EX2201_ms01.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_ms01.png)

<figcaption>

Mehrschichtiges Bauteil rechts wird nicht komplett grün überschrieben.

</figcaption>

</figure>

##### Oberflächenmodell

Bei der Definition von schrägen Oberflächen, wie z.B. Rampen, Betondecken im Gefälle oder schrägen Brüstungen, ist es für den Austausch hilfreich, wenn ein sogenanntes Oberflächenmodell ausgetauscht wird. Dann arbeiten alle mit den gleichen Abzugskörpern und die Kongruenz der Modelle ist dadurch gewährleistet.

<figure>

[![](images/IF-EX2201_cut-1024x667.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_cut.png)

<figcaption>

CUT-Modell für Rampe und schräge Wände der Firma [Hunold Architekten AG](https://hunold-architekten.ch/) für ein laufendes BIM-Projekt.

</figcaption>

</figure>

##### GUID

Unter der [General Unique Identifier](https://de.m.wikipedia.org/wiki/Globally_Unique_Identifier) versteht man eine Art Identifikationsnummer, welche bei jedem Bauteil einzigartig vorhanden sein sollte. Mit dieser Nummer können dann verschiedene Softwares Informationen mit dem Bauteil referenzieren.

<figure>

[![](images/IF-EX2201_GUID-1024x768.png)](https://bimdo.ch/wp-content/uploads/2022/03/IF-EX2201_GUID.png)

<figcaption>

Die GUID lässt sich wohl am ehesten vergleichen mit deiner Passnummer und diese sollte nur einmal vorkommen.

</figcaption>

</figure>

In den meisten Fällen sitzt das Export-Problem schlussendlich zwischen Bildschirm und Bürostuhl😟, auch in allen oben genannten Beispielen ist das der Fall. "Falsch" modelliert oder die falschen Übersetzer-Einstellungen führen zu einem korrupten IFC-Export, da hat die Software leider nur bedingt Schuld (einzig beim Export-Protokoll🤕). Deshalb macht eine visuelle Qualitätskontrolle immer Sinn und genau um diese visuelle Kontrolle geht es in meinem nächsten Artikel.
---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
