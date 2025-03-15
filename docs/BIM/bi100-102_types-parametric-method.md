---
title: "Parametrik & Typisierung als Methode"
date: "2022-10-17"
categories: 
  - "methodik"
  - "typisierung"
tags: 
  - "bim"
  - "event"
  - "workflow"
---

Anlässlich des letzten bimdo-Events zu den Themen Parametrik und Typisierung habe ich in diesem Artikel einige wichtige Punkte aufgelistet und in meinen Worten formuliert. Als erste Referentin durften wir Anne Nyffeler begrüssen, welche uns einen Einblick ins Forschungsprojekt BIMwood vermittelte und das Thema Parametrik & Typisierung auf methodischer Ebene präsentierte.

#### Parameter

Damit wir verstehen können, was einen Typen genau definiert, müssen wir über die Bedeutung von Parametern Bescheid wissen. Grundsätzlich besteht unser ganzes Leben aus mehr oder weniger einfachen Parametern, aber wir wollen uns doch Parametrik an Hand eines einfachen Beispiels anschauen. Nehmen wir einen Tisch, dann haben wir hier die Parameter Höhe, Länge und Breite auf geometrischer Ebene und z.B. das Material auf informativer Parametrikebene.

Etwas komplexer wird es, wenn Parameter wiederum Abhängigkeiten haben und dazu bleiben wir gleich beim Tisch. Das Material z.B. hat in Abhängigkeit mit der Dimensionierung von Tischbein und Plattendicke wiederum einen Einfluss auf Höhe, Länge und Breite des Tischs.

<figure>

[![](images/MT-TY2202_parameter-1024x684.png)](https://bimdo.ch/wp-content/uploads/2022/11/MT-TY2202_parameter.png)

<figcaption>

Beispiel Parametrik in der Mathematik: Parameter der Rechnung ergeben als Resultat einen Typen.

</figcaption>

</figure>

#### Typen

Damit man nun einen ersten Schritt in Richtung Typisierung gehen kann, muss man zuerst einmal aufräumen und strukturieren. Diesen Prozess kann man zum jetzigen Zeitpunkt nicht komplett einer Maschine überlassen, denn dafür brauchen wir sehr viel interdisziplinäres Know-How und sehr viele Abhängigkeiten entstehen durch den Prozess.

Nehmen wir erneut das Beispiel mit dem Tisch und stellen uns dabei einen Einkauf im Möbelgeschäft vor. Du suchst spezifisch einen Holztisch, also hast du alle Tische schon mal sortiert in Holz wahr/ falsch. Räumen wir noch weiter auf, denn du willst einen Esstisch und wiederum gibt es zwei Gruppen bei den Holztischen mit wahr/ falsch. Du vergibst also so lange Parameter, bis du den gewünschten Tisch gefunden hast.

<figure>

[![](images/MT-TY2202_tree.png)](https://bimdo.ch/wp-content/uploads/2022/10/MT-TY2202_tree.png)

<figcaption>

Beispiel Aufräumen und Strukturieren von der Bestellung bis zur Lieferung einer Tanne.

</figcaption>

</figure>

💡 Je klarer dein Ziel definiert ist, desto schneller findest du den gewünschten Tisch.

😎 Es macht keinen Sinn die Tische in Stein, Aluminium, Kunststoff und Holz zu unterteilen, wenn du ganz klar weisst, dass du einen Holztisch willst. Mit dieser klaren Zielvorstellung können wir den Aufwand massiv verkleinern, weil wir nur in Holz wahr/ falsch unterteilen müssen.

💡💡 Starte beim Aufräumen mit dem Parameter, welcher den grössten Impact hat.

😎😎 Du willst einen Esstisch aus Holz. Du hast 100 Tische, 80 davon sind aus Holz und nur 30 sind Esstische. Wenn du zuerst in Esstische wahr/ falsch unterteilst, dann muss du danach viel weniger Tische nach Holz wahr/ falsch einteilen.

Wenn man nun all diese Parameter strukturiert hat, kann man diese in eine Abhängigkeit zueinander setzen. Da es sehr viele verschiedene Abhängigkeiten gibt, muss man diese auch jeweils aus verschiedenen Blickwinkeln betrachten.

Bei unserem Einkauf im Möbelhaus haben wir bereits Typen generiert, diese Typen sind abhängig von den Eigenschaften Esstisch wahr/ falsch und Holz wahr/ falsch. Vielleicht bleiben uns am Schluss drei verschiedene Tische und wir müssen weitere Parameter hinzufügen, bis wir jeden einzelnen Tisch als Unikat identifizieren können. Dies könnten zum Beispiel Preis, Grösse, Herkunftland, Verfügbarkeit, Nachhaltigkeit, Standort im Laden, etc. sein.

<figure>

![](images/MT-TY2202_flower.png)

<figcaption>

Definition eines Typs als Schnittmenge der einzelnen Parameter.

</figcaption>

</figure>

💡💡💡 Typen bilden sich aus der Schnittmenge der ausgewählten Parameter.

😎😎😎 Was sich mit dem Tisch machen lässt, können wir mit jedem Bauteil im Gebäude machen. Wir unterstützen so die Kunden, die Planer und die Hersteller bei der Auswahl des richtigen Tisches sowie bei der weiteren Planung und Herstellung.

#### BIMwood

Mir persönlich ist das Dreischichtenmodell hängen geblieben und auch im Nachgang führte dieses Konzept zu Diskussionen, zuvor möchte ich aber noch das Thema Koordination auf der strategischen, koordinativen und operativen Ebene zu diesen Typen setzen.

E1 Prozesskoordination (strategisch): Bei unserem Tischbeispiel hatten wir die Anforderungen Holz und Esstisch. Das heisst auf strategischer Ebene wird definiert, welche Informationen überhaupt erforderlich sind. Zugleich findet auf strategischer Ebene auch eine Qualitätssicherung statt, dass genau diese zwei Anforderungen eingehalten werden.

E2 Gesamtkoordination (koordinativ): Jetzt geht es darum Lösungen für diese zwei Anforderungen zu entwickeln. Aspekte, die hier hinzukommen sind dann die Einhaltung eigener Normen. Zum Beispiel muss der Tisch natürlich statisch etwas aushalten können. Auch hier wiederum findet eine Qualitätskontrolle statt und die Ebene steht besonders für die Verbindung zwischen E1 und E3.

E3 Arbeitskoordination (operativ): Die Einbindung dieser Aspekte in die Ebene 2 ist elementar, denn hier haben wir das Know-How vom Handwerker, welcher nun das Geplante auf Baubarkeit prüft und den Tisch in seine Einzeltypen (Tischbeine, Tischplatte, Schrauben, etc.) zerlegt.

<figure>

![](images/MT-TY2202_overview.png)

<figcaption>

Verbindung der verschiedenen Ebenen mit der Typenthematik und dem damit zusammenhängenden Prinzip des Dreischichtenmodells.

</figcaption>

</figure>

Diese drei Ebenen haben zugleich Einfluss auf den Detaillierungsgrad vom Modell, welches wir in diesem Zusammenhang als Informationsgefäss verstehen. Für die Anforderung Esstisch wahr/ falsch und Holz wahr/ falsch brauchen wir genau einen Körper als Gesamtes. Der Tisch als Ganzes hat diese zwei Anforderungen, aus diesem Grund würde hier also eine rechteckige Box reichen. Somit existiert auf dieser Ebene nur ein Typ mit den Parametern Esstisch und Holz.

Für die Lösungsfinde auf koordinativer Ebene (Ebene 2) brauchen wir etwas mehr Detail und somit die Tischbeine für die Statik-Prüfung. Hierfür brauchen wir aber noch nicht alle Angaben zu jeder einzelnen Schraube, Filz und der Einölung. Wir unterscheiden hier aber z.B. zwischen den Typen Tischplatte und Tischbeine, weil sich diese z.B. auf Grund der Parameter Breite und Höhe unterscheiden.

Auf der operativen Ebene existieren alle Informationen aus den höheren Ebenen ebenfalls, diese werden hierarchisch übernommen. Hier sprechen wir von einem Produktionsmodell, so wird der Tisch schlussendlich gebaut. Wir müssen genau wissen, welche Schraube wo ist und in welche Richtung diese verschraubt wird. Die Parameter der Schrauben (Länge, Material, etc.) definieren somit den Typ der Schraube.

<figure>

[![](images/MT-TY2202_01-1024x768.png)](https://bimdo.ch/wp-content/uploads/2022/11/MT-TY2202_01.png)

[![](images/MT-TY2202_02-1024x768.png)](https://bimdo.ch/wp-content/uploads/2022/11/MT-TY2202_02.png)

[![](images/MT-TY2202_03-1-1024x768.png)](https://bimdo.ch/wp-content/uploads/2022/11/MT-TY2202_03-1.png)

[![](images/MT-TY2202_04-1024x768.png)](https://bimdo.ch/wp-content/uploads/2022/11/MT-TY2202_04.png)

<figcaption>

Abhängigkeiten der verschiedenen Informations-Gefässe auf den drei Ebenen.

</figcaption>

</figure>

Genau gleich funktioniert das auch bei einer Wand oder einer Decke, wir nutzen die Geometrie als Gefäss für unsere Informationen. Wir brauchen nicht immer den vollen Detaillierungsgrad des Bauteils um die entsprechende Information abzufüllen, denn manchmal ist die Information auf der Schichtebene Dämmung und manche Informationen sind hierarchisch gesehen auf der gesamten Wand.

#### Praxisbeispiel Dämmperimeter

- Ebene 1 - **Anforderungsmodell**: Verstehen wir den Dämmperimeter erstmal als Zone, dann entspricht dieser einem Volumenkörper, welcher die Räume innerhalb der thermischen Gebäudehülle umschliesst.

- Ebene 2.1 - **Konzept-Lösungsmodell**: Alle Bauteile, welche das Zonenmodell des Dämmperimeters an dessen Oberfläche berühren, haben somit eine Anforderung U-Wert zu erfüllen. Damit hätten wir ein konzeptionelles Modell als **1-Schicht-Modell**.

- Ebene 2.2 - **Projekt-Lösungsmodell**: Dabei geht es um die drei Komponenten tragen/ dämmen/ schützen. Diese Parameter definieren wir dann im etwas detaillierteren **3-Schicht-Modell**.

- Ebene 3 - **Produktionsmodell**: Hier geht es um die genaue Definition der Materialien, welche Stärke, Eigenschaften und die Befestigungsthematik. Diese Informationen fliessen dann wiederum ins **n-Schicht-Modell**.

BIM, ein Digital Twin oder eben ein digitales Gebäudemodell kann als 3D visualisierte Datenbank verstanden werden, diese Datenbank lässt sich aber auch als Kuchendiagramm visualisieren😎. Doch warum brauchen wir nun diese drei Ebenen und warum wollen wir die Informationen in verschiedene Schichten aufbrechen?

💡 Wir wollen über alle Projektphasen durchgängige Informationsstrukturen, diese drei Ebenen und die entsprechende Aufsplittung in Schichten bilden die Struktur der Datenbank und gewährleisten die Durchgängigkeit der Information.

❗ Die drei Ebenen, die verschiedenen Modelle und die damit zusammenhängenden Informations-Gefässe stehen in Abhängigkeit zueinander und existieren über alle Projektphasen zugleich. 💡 Wenn eine Anforderung auf Ebene 1 ändert, dann verändern sich auf Grund der Abhängigkeiten auch die Informationen auf den Ebenen 2 und 3.

❗❗ Wir sprechen also von einer Methodik, welche zu einem durchgängigen System führt. Diese Datenstrukturen sind die Grundlage für eine mögliche Automatisierung und da wollen wir doch hin...
---
**Veröffentlicht am:** {{ page.meta.date }} | **Code** {{ page.file.name[:9] }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }}
