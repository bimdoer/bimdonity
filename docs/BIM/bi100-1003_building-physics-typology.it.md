---
title: "Tipologia della Fisica degli Edifici"
date: "2022-09-14"
author: "Manuel Emmenegger | bimdo.ch"
tags: 
  - "Fisica degli Edifici"
  - "BIM"
  - "IFC"
  - "Tipologia" 
  - "Workflow"
---
## Tipologia
La tipologia degli elementi costruttivi è un aspetto centrale della metodologia BIM. Gli elementi con requisiti simili o identici vengono raggruppati in categorie logiche. Questa categorizzazione sistematica permette di comprendere e gestire l'edificio come un database strutturato.

Il seguente modello è stato sviluppato sulla base di concetti di tipologia esistenti (ad esempio, da Pirmin Jung AG) ed esperienze di progetto per illustrare il raggruppamento. Le due visualizzazioni seguenti mostrano diversi aspetti della tipologia:

<div class="responsive-container">
  <div>
    <img src="assets/bi100-1003_01_perimeter-model.png" alt="Modello Perimetrale" style="width:100%">
  </div>
  <div>
    <img src="assets/bi100-1003_02_type-model.png" alt="Modello di Tipologia" style="width:100%">
  </div>
</div>

## Visualizzatore BIMx
Entrambi i modelli possono essere esaminati in dettaglio nel visualizzatore web BIMx. Il modello perimetrale utilizza una chiara codifica a colori:

- Rosso: Elementi che formano il perimetro
- Blu: Elementi nella zona fredda
- Trasparente: Elementi nella zona interna calda

Il modello di tipo classifica i singoli componenti dell'edificio secondo il rapporto di fisica dell'edificio. La tipologia copre i casi standard più importanti, mentre strutture più complesse come sottofondi o tetti piani devono essere trattate separatamente. Un obiettivo principale è trasmettere il concetto base di tipologia.

C'è un potenziale di miglioramento nella zona del terreno: Attualmente, esistono solo i tipi base WE ("Parete contro terra") e DE ("Solaio contro terra"). Per una tipologia completa, sarebbero utili ulteriori sottotipi, specialmente per quanto riguarda il calcolo del perimetro di isolamento.

<iframe width="960" height="320" src="https://bimx-webviewer.graphisoft.com/?modelId=94c1dd96-9b8a-4770-a72c-321009c36b8b&amp;modelType=HyperModel&amp;auth=eyJhbGciOiJIUzI1NiIsImtpZCI6Ikc0MmdJR1ZzUWpLdGtpdk1YT0h5VmciLCJ0eXAiOiJKV1QifQ.eyJ0c19tb2RlbF9pZCI6Ijk0YzFkZDk2LTliOGEtNDc3MC1hNzJjLTMyMTAwOWMzNmI4YiIsInhfaWV2IjoiMCIsIm5iZiI6MTYyODUwMTU5NywiZXhwIjoyMTM2NTMzNTk3LCJpYXQiOjE2NjMxNDc5OTcsImlzcyI6Imh0dHBzOi8vYmlteC5ncmFwaGlzb2Z0LmNvbSIsImF1ZCI6Imh0dHBzOi8vYmlteC13ZWJ2aWV3ZXIuZ3JhcGhpc29mdC5jb20ifQ.lZXrN3Pobvo4OiCrp2rZTKzcpc9A-eXh43uaCEjeG1g&amp;linkVersion=2.0" frameborder="0" allowfullscreen></iframe>

La scelta della lingua è un aspetto importante della tipologia. Diverse fasi di progetto e stakeholder utilizzano lingue diverse. L'uso coerente dell'inglese sarebbe una soluzione, ma comporta le proprie sfide. Il sistema sviluppato contiene automaticamente designazioni in tedesco e inglese, poiché la scelta di una singola lingua nazionale spesso porta al "problema del Röstigraben" con gruppi linguistici svantaggiati. Si raccomanda una lingua di tipologia uniforme per un progetto.

| Tedesco | Inglese |
|---------|----------|
| WE - Wand gegen Erdreich | WE - Wall to exterior |
| BE - Boden gegen Erdreich | BE - Bottom slab to exterior |

## Istruzioni BIMx
### Apertura del modello
Per aprire un modello, clicca su Play in BIMx. Seleziona uno dei due modelli a sinistra e clicca sull'immagine di anteprima corrispondente in basso.

[![Istruzioni](assets/bi100-1003_03_instructions.png)](assets/bi100-1003_03_instructions.png)

### Informazioni sui componenti
Nel modello di tipo, i significati dei colori possono essere visualizzati facendo clic con il tasto destro su un elemento e selezionando "Info". Lì, le tipologie sono memorizzate in tedesco e in inglese.

[![Informazioni sui componenti](assets/bi100-1003_04_instructions.png)](assets/bi100-1003_04_instructions.png)

### Stato di riscaldamento
Le sfere rosse e blu mostrano lo stato di riscaldamento (riscaldato/non riscaldato) delle stanze. I dettagli vengono visualizzati facendo clic con il tasto destro su "Info". Le stanze stesse possono anche essere visualizzate e filtrate per caldo/freddo, come mostrato nello screenshot.

[![Stato di riscaldamento](assets/bi100-1003_05_instructions.png)](assets/bi100-1003_05_instructions.png)

## Conclusione
La tipologia esisteva prima del BIM - anche un piano contrassegnato raggruppa elementi. Il vantaggio del modello digitale risiede nella gestione coerente dei dati e nella visualizzazione efficiente, consentendo a tutti i partecipanti al progetto di sviluppare una migliore comprensione del progetto di costruzione.


---
**Pubblicato il:** {{ page.meta.date }} | **Codice:** {{ page.file.name[:10] }}  | **Autore:** {{ page.meta.author }}

**Tag:** {{ page.meta.tags | join(', ') }} 