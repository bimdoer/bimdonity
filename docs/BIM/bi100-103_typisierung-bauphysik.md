---
title: "Typisierung Bauphysik"
date: "2022-09-14"
categories: 
  - "methodik"
  - "typisierung"
tags: 
  - "bauphysik"
  - "bim"
  - "ifc"
  - "typisierung"
  - "workflow"
---

In den letzten Projekten durfte ich mich immer wieder mit Typisierungen auseinandersetzen, dabei geht es um die Auseinandersetzung mit der Gebäudestruktur. Welche Elemente haben ähnliche oder gleiche Anforderungen? Aus diesen ähnlichen und gleichen Anforderungen entstehen dann wiederum Gruppen und genau um diese Gruppierungen geht es schlussendlich, wenn man das Gebäude als Datenbank verstehen möchte. Abgeleitet aus den Typisierungskonzepten von der Firma Pirmin Jung und meinen Erfahrungen aus den letzten Projekten, habe ich eine mögliche Typisierung in ein Modell eingepflegt. Dabei sind folgende zwei grafischen Darstellungen entstanden:

<figure>

<figure>

[![](images/MT-TY2201_Perimeter.png)](https://bimdo.ch/wp-content/uploads/2022/09/MT-TY2201_Perimeter.png)

<figcaption>

Perimetermodell

</figcaption>

</figure>

<figure>

[![](images/MT-TY2201_Typen.png)](https://bimdo.ch/wp-content/uploads/2022/09/MT-TY2201_Typen.png)

<figcaption>

Typenmodell

</figcaption>

</figure>

<figcaption>

Beide Modelle lassen sich im BIMx-Webviewer noch etwas genauer anschauen und entsprechende Informationen darstellen. Das Perimetermodell zeigt in rot die perimeterbildenden Elemente, in blau die Elemente im Kaltbereich und die transparenten Elemente liegen im warmen Innenbereich. Beim Typenmodell ist jeder Typ eingefärbt, mehr dazu im Abschnitt [Infos zum BIMx](#Infos).

</figcaption>



</figure>

Das Typenmodell geht genauer auf die Typisierung einzelner Bauteile ein, so dass diese schlussendlich deckungsgleich mit dem Bericht der Bauphysik sind. Natürlich ist die Typisierung nicht abschliessend, da gerade im Bereich des Unterlagsbodens oder Flachdachs durchaus sehr komplexe Bauteile entstehen. Mit etwas tricksen kriegt man aber auch diese Problematik geregelt. Bei dieser Typisierung geht es um ein Grundverständnis des Modells, wobei wir auch im Erdbereich noch eine Lücke in der Typisierung haben. Aktuell existiert nur eine WE und eine DE für "Wand gegen Erdreich" und "Decke gegen Erdreich". Um die Typisierung zu vervollständigen, wären auch hier getrennte Typen notwendig, damit man auch gleich den Dämmperimeter direkt rausziehen kann.

<iframe width="960" height="320" src="https://bimx-webviewer.graphisoft.com/?modelId=94c1dd96-9b8a-4770-a72c-321009c36b8b&amp;modelType=HyperModel&amp;auth=eyJhbGciOiJIUzI1NiIsImtpZCI6Ikc0MmdJR1ZzUWpLdGtpdk1YT0h5VmciLCJ0eXAiOiJKV1QifQ.eyJ0c19tb2RlbF9pZCI6Ijk0YzFkZDk2LTliOGEtNDc3MC1hNzJjLTMyMTAwOWMzNmI4YiIsInhfaWV2IjoiMCIsIm5iZiI6MTYyODUwMTU5NywiZXhwIjoyMTM2NTMzNTk3LCJpYXQiOjE2NjMxNDc5OTcsImlzcyI6Imh0dHBzOi8vYmlteC5ncmFwaGlzb2Z0LmNvbSIsImF1ZCI6Imh0dHBzOi8vYmlteC13ZWJ2aWV3ZXIuZ3JhcGhpc29mdC5jb20ifQ.lZXrN3Pobvo4OiCrp2rZTKzcpc9A-eXh43uaCEjeG1g&amp;linkVersion=2.0" frameborder="0" allowfullscreen></iframe>

Ein weiterer Punkt bei der Typisierung ist das Thema Sprache, diesen Punkt habe ich mit einigen meiner Kunden diskutiert. Je nachdem spricht man in der Planungsphase eine andere Sprache oder sogar zwei Sprachen als auf der Baustelle, geschweige dann in der Bewirtschaftung. Doch wie geht man mit solchen Problematiken um? Alles auf Englisch switchen ist dann leichter gesagt als getan. Ich habe die Typisierung versucht umzugestalten und so mit der deutschen Typisierung automatisiert auch eine englische Version mitzugeben. Können wir uns auf eine englische Variante einigen? Sobald wir uns für Deutsch, Französisch oder Italienisch entscheiden, haben wir das sogenannte "Röstigraben-Problem" und jemand fühlt sich benachteiligt. Wenn du mit der englischen Variante arbeitest, dann wirst du sofort einige Konflikte feststellen. Einige Sprachbarrieren habe ich hier aufgelistet, damit du siehst, weshalb es so schwer ist bei Typen von beispielsweise Deutsch auf Englisch zu wechseln. In einem Projekt sollte sicherlich nur eine Typisierung vorhanden sein, alles andere führt zu Missverständnissen! 💡Stimmt nicht ganz, dank einem Tipp aus der Community ([danke an Christoph Räss & Anne Nyffeler](https://www.linkedin.com/feed/update/urn:li:activity:6976159568741474304/)) habe ich diesen Satz weiter [unten](#Tipp) 💡 noch etwas konkretisiert.

- WE - Wall to exterior

- BE - Bottom slab to exterior

- WE - Wand gegen Erdreich

- BE - Boden gegen Erdreich

Solche Problemstellungen sind leider projektübergreifen vorhanden und in meinen Augen wäre hier ein Standard erforderlich. Auch wenn ich im jeweiligen Projekt eine Sprache durchziehe, ist es für den Endnutzer schwer in jedem Projekt wieder umzudenken. Aus Sicht der Automatisierung benötigen wir eine Typisierung, aber aus Sicht des Nutzers muss alles ausgeschrieben werden, weil sonst gerade bei Sprachbarrieren Missverständnisse entstehen.

#### Infos zum BIMx

Wie bereits erwähnt gibt es zwei verschiedene Modelle, welche jeweils separat geöffnet werden können. Dazu klickst du beim [obigen BIMx](#BIMx) auf den Play-Button. Danach siehst du am linken Rand beide Modell zu Auswahl, wähle eines der Modelle aus und klicke im unteren Bereich auf das Vorschaubild gemäss nebenstehendem Screenshot.

<figure>

[![](images/MT-TY2201_Anleitung1-1024x517.png)](https://bimdo.ch/wp-content/uploads/2022/09/MT-TY2201_Anleitung1.png)

<figcaption>

Anleitung zum Öffnen des BIMx-Modells.

</figcaption>

</figure>

Schauen wir uns nun das Typenmodell etwas genauer an, denn aktuell sehen wir einfach Farben, wissen jedoch nicht, was diese zu bedeuten haben. Mit einem Rechtsklick auf die entsprechenden Element kann man "Info" auswählen und entsprechend sieht man die beiden Typisierungen in Deutsch und Englisch.

<figure>

[![](images/MT-TY2201_info-1024x618.png)](https://bimdo.ch/wp-content/uploads/2022/09/MT-TY2201_info.png)

<figcaption>

Mit einem Rechtsklick auf ein Element lassen sich Elementinformationen abbilden.

</figcaption>

</figure>

Bestimmt wirst du dich gefragt haben, was diese roten und blauen Kugeln sollen? Diese stehen jeweils für den Status beheizt/ unbeheizt der Räumlichkeiten. Auch hier lassen sich mit einem Rechtsklick/ Info die entsprechenden Informationen abrufen. Natürlich lassen sich auch die Räume einblenden, welche wiederum klassifiziert sind als warm oder kalt. Auf dem nebenstehenden Screenshot siehst du wie das geht.

<figure>

[![](images/MT-TY2201_Zones-1024x517.png)](https://bimdo.ch/wp-content/uploads/2022/09/MT-TY2201_Zones.png)

<figcaption>

Über die Einstellungen lassen sich auch noch die verschiedenen Raumvolumen einblenden.

</figcaption>

</figure>

Typisieren und damit einhergehend Informationsgruppen existierten auch schon ohne Modell, rein theoretisch ist auch ein Leuchtstift-Plan eine Art Typisierung von Elementen. Mit Modellen lassen sich diese Informationen aber wirklich als konsistente Datenbank abbilden, die Auseinandersetzung mit den einzelnen Typen ist jedoch immer noch genau die gleiche. Das Modell gibt dir ein Tool an die Hand, wie du dies effizient und nachhaltig visualisieren kannst, damit alle Projektbeteiligten ein besseres Verständnis des zu Bauenden erlangen.

###### 💡 Eine Typisierung pro Projekt? 💡

Christoph Räss und Anne Nyffeler haben auf [Linkedin](https://www.linkedin.com/feed/update/urn:li:activity:6976159568741474304/) eine spannende Diskussion zu diesem Thema begonnen. Mit "nur eine Typisierung" pro Projekt, meine ich die Art von Typisierung. Für jede Phase, jeden Use-Case und jedes Fachgebiet gibt es jeweils eine Typisierung, quasi eine Teilansicht und die Schwierigkeit liegt bei der Koordination all dieser Informationen. Wenn jedoch im gleichen Projekt zwei Typisierungen vorhanden sind, aber abgeleitet aus zwei Sprachen, dann führt dies zu Missverständnissen. Es macht keinen Sinn den Bauphysik-Typ z.B. WA zweifach zu führen (einmal englisch und einmal deutsch), denn aus der englischen Sprache abgeleitet und aus der deutschen Sprache abgeleitet, bedeuten gewisse Abkürzungen nicht dasselbe. Aus diesem Grund nur eine Typisierung (der gleichen Funktion und Art) pro Projekt.
---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
