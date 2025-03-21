---
title: "Il Tuo Primo GDL"
date: "2025-03-15"
author: "Manuel Emmenegger | bimdo.ch"
original: "Tedesco"
tags:
  - "Archicad"
  - "GDL"
  - "Libreria"
---

## Consigli generali

Prima di iniziare con il tuo primo script, ecco alcuni consigli utili:

1. **Abbozza le tue idee**: Annota brevemente le tue idee per identificare i parametri importanti.
2. **Definisci i requisiti**: Dividi i requisiti in funzioni di base e funzioni "nice to have".
3. **Prototipazione**: Sperimenta diversi approcci per trovare soluzioni. La prototipazione può aiutarti a testare e affinare le tue idee.

4. **Struttura dello script**: Commenta il tuo script e usa le intestazioni per migliorare la leggibilità. Un codice chiaramente strutturato facilita la collaborazione in team.

```
!Inizia il tuo script con alcune informazioni
    !Titolo dell'oggetto
    !Data
    !Il tuo nome
    !Nome dello script, ad esempio Script 3D

Struttura
    il tuo
        lavoro
    con
tabulazioni.

"M A I U S C O L O & minuscolo" serve solo per una migliore panoramica
    >>Graphisoft scrive quasi tutto in minuscolo
    >>Il ricettario GDL raccomanda comandi   "MAIUSCOLO"
                                 attributi "minuscolo"

END !--------------- Termina il tuo script con END.
```
---
## Struttura dello script

- Commenta lo script con `!` e aggiungi intestazioni.
- Usa le tabulazioni per una struttura chiara.
- Usa lettere maiuscole per i comandi e minuscole per gli attributi.
- Utilizza subroutine per organizzare script complessi.
- Termina ogni script con il comando `END`.
- Crea un nuovo GDL e verifica il risultato nella vista 3D.
- Ulteriori informazioni possono essere trovate nella [Guida di stile GDL di Graphisoft](http://gdl.graphisoft.com/gdl-style-guide).

---
## Creazione di GDL
### Script 3D
**1. Crea un nuovo GDL:**

- Apri ArchiCAD e vai al menu "File".
- Seleziona "Nuovo" e poi "Oggetto GDL" per creare un nuovo script GDL.

**2. Inserisci lo script del blocco:**

- Apri l'editor di script 3D nel tuo nuovo oggetto GDL.
- Copia e incolla il seguente script di blocco nell'editor.

**3. Verifica il risultato:**

- Apri la vista 3D sul lato sinistro.


<div class="responsive-container">
  <div>
    <pre><code>
!Blocco su blocco
!20210903
!Manuel Emmenegger
!Script 3D

block 1,2,3

end !Fine dello script
    </code></pre>
  </div>
  <div>
      <img src="../assets/ac210-1010_01_3D-View-300x278.png" alt="Vista 3D">
  </div>
</div>

**4. Verifica il risultato:**

- Dopo il comando, gli input _1,2,3_ rappresentano _x,y,z_. Gioca con questi valori e controlla il risultato nella vista 3D. Ulteriori informazioni su questo comando possono essere trovate su [selfgdl.de](https://www.selfgdl.de/3d-elemente/grundkoerper/block/).

---

### Script 2D
Nel prossimo passo, revisioniamo la rappresentazione 2D. Apri lo script 2D e aggiungi le righe appropriate per generare una proiezione automatica dallo script 3D. Usa questo comando solo per la verifica, poiché può rallentare la costruzione della pianta con geometria complessa. Ulteriori informazioni possono essere trovate su [selfgdl.de](https://www.selfgdl.de/2d-elemente-2/projektionen/project2/).


<div class="responsive-container">
  <div>
    <pre><code>
!Blocco su blocco
!20210903
!Manuel Emmenegger
!Script 2D

project2 3,270,1

end !Fine dello script
    </code></pre>
  </div>
  <div>
        <img src="../assets/ac210-1010_02_2D-View-300x273.png" alt="Vista 2D">
  </div>
</div>

---

### Salvataggio
Salva il tuo primo GDL nella libreria incorporata tramite "File/salva" e salva il file ArchiCAD come .pln per integrare il GDL.

---

## Parametri 3D
### Geometria
Ora è il momento di parametrizzare questo elemento. Inizieremo con alcuni parametri standard. Apri la scheda "Parametri" sul lato sinistro nel nostro elemento già creato. Dovrebbero esserci tre parametri standard qui: Parametro A per l'asse X, Parametro B per l'asse Y e Parametro ZZYZX per l'asse Z.

Sostituisci i numeri nello script con i parametri standard A, B e ZZYZX e verifica i cambiamenti nella vista 3D. Questi parametri influenzano anche la vista 2D grazie al comando "project2".

Salva l'elemento, chiudi l'editor GDL e posiziona l'elemento con lo strumento oggetto.

```
!Blocco su blocco
!20210903
!Manuel Emmenegger
!Script 3D

block A,B,ZZYZX

end !Fine dello script
```

Premi "T" per aprire le impostazioni dell'oggetto, dove troverai i parametri A, B e ZZYZX. Il tuo oggetto GDL parametrizzato è ora creato.
[![Parametri](assets/ac210-1010_03_Settings-Dialog.png)](assets/ac210-1010_03_Settings-Dialog.png)

---

### Rappresentazione
Per esplorare più parametri, seleziona l'oggetto GDL e premi Ctrl+Shift+O.

Crea due nuovi parametri nella scheda "Parametri". Per la denominazione, si consiglia un concetto coerente, eventualmente basato sullo [Standard Graphisoft](https://gdl.graphisoft.com/gdl-style-guide/naming-conventions). Nomi più lunghi sono utili per riconoscere direttamente i parametri senza bisogno di una legenda.

[![Parametro](assets/ac210-1010_04_Parameter.png)](assets/ac210-1010_04_Parameter.png)

La tabella dei parametri contiene le seguenti colonne importanti:

- Display: Controlla la visualizzazione nell'interfaccia (ad esempio, grassetto, nascosto)
- Variabile: Nome della variabile per lo script
- Tipo: Tipo di variabile (ad esempio, penna, superficie)
- Nome: Nome visualizzato per l'utente
- Valore: Valore predefinito del parametro

Maggiori dettagli sui tipi di parametri possono essere trovati nella [documentazione](https://help.graphisoft.com/AC/25/ger/_AC25_Help/140_UserInterfaceDialogBoxes/140_UserInterfaceDialogBoxes-66.htm#XREF_66121_GDL_Master_Window).

Ora aggiungiamo i comandi "pen" per la penna del contorno e "set material" per la superficie nello script. Quindi salva l'elemento e verifica il risultato.

```
!Blocco su blocco
!20210903
!Manuel Emmenegger
!Script 3D

pen            penContour3D
set material   matCover

block A,B,ZZYZX

end !Fine dello script
```
---
## Script 2D personalizzato
### Parametri 2D
Ora vogliamo esaminare più da vicino la rappresentazione bidimensionale del nostro blocco. Per questo, lavoreremo con i comandi [line2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/line2/) e [rect2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/rect2/) così come con gli attributi [pen](https://www.selfgdl.de/attribute/allgemein/pen/) e [set line\_type](https://www.selfgdl.de/attribute/linien/set-line_type/).

Uno script 2D separato offre due vantaggi importanti:

1. Per elementi 3D complessi, la rappresentazione della pianta è più veloce perché non tutto deve essere proiettato.

2. Le piante spesso utilizzano simboli invece di pure proiezioni, ad esempio per prese e interruttori.

Per distinguere le linee project2 dalle nostre, creiamo prima nuovi parametri come mostrato nello screenshot.
[![Parametro](assets/ac210-1010_05_Parameter.png)](assets/ac210-1010_05_Parameter.png)


I comandi "pen" e "line_type" vengono inseriti dopo project2, in modo che le linee project2 siano disegnate con penna 1 e tipo di linea 1, e tutte le altre linee ricevano i nuovi attributi.

---

### line2
Con il comando line2, disegniamo le quattro linee del nostro blocco viste dall'alto. Il comando utilizza due coppie di coordinate (x1,y1,x2,y2) e traccia una linea tra questi punti. Le quattro linee formano un rettangolo che dovrebbe essere congruente alla rappresentazione project2 nella vista 2D.

```
!Blocco su blocco
!20210903
!Manuel Emmenegger
!Script 2D

project2 3,270,1

pen            penContour2D
set line_type  ltContour2D
   !line2 x1,y1,x2,y2
    line2 0,0,A,0
    line2 A,0,A,B
    line2 A,B,B,0
    line2 0,B,0,0

end !Fine dello script
```
---

### rect2
Il comando [rect2](https://www.selfgdl.de/2d-elemente-2/zeichnungselemente/rect2/) permette di sostituire le quattro linee con una singola definizione di rettangolo. Un rettangolo viene disegnato tra due punti (x1,y1) e (x2,y2).

```
!rect2 x1,y1,x2,y2
 rect2 0,0,A,B
```

Come avrai probabilmente notato, i due comandi "line2" e "rect2" non funzionano allo stesso modo del comando "block". Con il comando "block", non potevamo determinare il punto di partenza del blocco, cioè l'origine dell'oggetto (punto di partenza nello spazio), poiché iniziavamo sempre automaticamente al punto 0,0,0. Con il comando "[add](https://www.selfgdl.de/1_ko_trafos/3d_komplex/add/)", questa limitazione può essere aggirata in seguito. I comandi 2D offrono quindi più flessibilità nel posizionamento degli elementi.

---

### poly2
Dopo aver imparato gli strumenti di linea, ora vogliamo creare tratteggi con il comando "[poly2](https://www.selfgdl.de/2d-elemente-2/polygone/poly2/)". Per questo, abbiamo anche bisogno del comando "[set fill](https://www.selfgdl.de/attribute/schraffuren/set-fill/)" per controllare il tipo di tratteggio.

Crea i parametri come mostrato nello screenshot e aggiungi il tipo di tratteggio nello script dopo le definizioni di penna e tipo di linea.

[![Parametro](assets/ac210-1010_06_Parameter.png)](assets/ac210-1010_06_Parameter.png)


Sostituisci il comando rect2 con poly2 e aggiungi il numero di angoli (4) e il tipo di visualizzazione (1+2+4+0) prima dei valori xy. I punti corrispondono agli stessi punti finali di line2.

Il comando "poly2" differisce da "rect2" per:

- Numero variabile di angoli
- Visualizzazione del tratteggio o del contorno
- Possibilità di poligoni aperti

```
!Blocco su blocco
!20210903
!Manuel Emmenegger
!Script 2D

project2 3,270,1

pen            penContour2D
set line_type  ltContour2D
set fill       fillType2D
   !poly2 n,ContorniERiempimento,
   !      x1,y1,
   !      ..
   !      Xn,yn
    poly2 4,1+2+4+0,
          0,0,
          A,0,
          A,B,
          0,B

end !Fine dello script
```
---

### poly2_
Il comando poly2_ offre opzioni di controllo estese per bordi e penne. Iniziamo con [poly2_](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_/), dove ogni valore xy riceve uno stato: 1 per linee visibili, -1 per il punto finale del poligono. Dettagli sullo stato possono essere trovati su [selfgdl.de](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_/).

```
!poly2_ n,ContorniERiempimento,
!       x1,y1,Stato,
!       ..
!       x2,y2,Stato
 poly2_ 4,1+2+4+0,
        0,0,1,
        A,0,1,
        A,B,1,
        0,B,1
```
---

### poly2_A
Con [poly2_A](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_a/), controlliamo la penna in primo piano del tratteggio - ideale per tratteggi solidi.

```
!poly2_A n,ContorniERiempimento,PennaRiempimento,
!        x1,y1,Stato,
!        ..
!        x2,y2,Stato
 poly2_A 4,1+2+4+0,penFront2D,
         0,0,1,
         A,0,1,
         A,B,1,
         0,B,1
```
---

### poly2_B
Il comando [poly2_B](https://www.selfgdl.de/2d-elemente-2/polygone/poly2_b/) offre le opzioni di controllo più estese, poiché possono essere definite sia la penna in primo piano che quella di sfondo. Dopo aver salvato e posizionato l'elemento nella pianta, tutti i parametri creati possono essere testati.

```
!poly2_B n,ContorniERiempimento,PennaRiempimento,
!        PennaSfondo,
!        x1,y1,Stato,
!        ..
!        x2,y2,Stato
 poly2_B 4,1+2+4+0,penFront2D,
         penBack2D,
         0,0,1,
         A,0,1,
         A,B,1,
         0,B,1
```

---

**Pubblicato il:** {{ page.meta.date }} | **Codice:** {{ page.file.name[:10] }}  | **Autore:** {{ page.meta.author }}

**Tag:** {{ page.meta.tags | join(', ') }} | **Originale:** {{ page.meta.original }}