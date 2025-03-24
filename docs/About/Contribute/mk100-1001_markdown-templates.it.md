---
title: "Template Markdown"
date: "2024-01-17"
author: "Manuel Emmenegger | bimdo.ch"
original: "Tedesco"
tags:
  - "Markdown"
  - "Template"
  - "Documentazione"
  - "Guida"
---

Questo template dimostra gli elementi di formattazione Markdown comuni e come utilizzarli efficacemente nella documentazione.

## Intestazione
Utilizzare sempre un'intestazione, il titolo viene utilizzato per la navigazione e il titolo. La data appare nel piè di pagina e i tag nella ricerca.

```
---
title: "Template Markdown"
date: "2024-01-17"
author: "Manuel Emmenegger | bimdo.ch"
original: "Tedesco"
tags:
  - "Markdown"
  - "Template"
  - "Documentazione"
  - "Guida"
---
```

## Commenti
I commenti non sono visibili.

```
<!-- commenti -->
```

## Capitoli
_# h1 non utilizzato, il titolo apparirà automaticamente_
## Capitoli h2
```
## Capitoli h2
```
### Sottocapitoli h3
```
### Sottocapitoli h3
```


## YouTube
Prendere il collegamento di incorporamento corretto da YouTube (solo il link), è collegato con custom.css
<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/cgiI8TBw9H0?si=NWXfqKQGowqPxPVR" frameborder="0" allowfullscreen></iframe>
</div>
```html
<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/cgiI8TBw9H0?si=NWXfqKQGowqPxPVR" frameborder="0" allowfullscreen></iframe>
</div>
```

---

## Immagine
Non può essere selezionata nell'interfaccia.
![Parametro](assets/example-image.svg)

```
![Parametro](assets/example-image.svg)
```

Può essere selezionata nell'interfaccia.
[![Parametro](assets/example-image.svg)](assets/example-image.svg)

```
[![Parametro](assets/example-image.svg)](assets/example-image.svg)
```
---

## Liste

### Lista numerata
<!-- È necessario premere Invio per una corretta rappresentazione -->
1. Primo elemento
2. Secondo elemento
3. Terzo elemento
```
### Lista numerata
<!-- È necessario premere Invio per una corretta rappresentazione -->
1. Primo elemento
2. Secondo elemento
3. Terzo elemento

```
### Lista puntata
<!-- È necessario premere Invio per una corretta rappresentazione -->
- Primo punto
- Secondo punto
- Terzo punto
```
### Lista puntata
<!-- È necessario premere Invio per una corretta rappresentazione -->
- Primo punto
- Secondo punto
- Terzo punto

```
### Lista combinata
<!-- È necessario premere Invio per una corretta rappresentazione -->
1. Primo elemento
      - Primo punto <!-- rientro per una corretta rappresentazione -->
      - Secondo punto
2. Secondo elemento
3. Terzo elemento
```
### Lista combinata
<!-- È necessario premere Invio per una corretta rappresentazione -->
1. Primo elemento
      - Primo punto <!-- rientro per una corretta rappresentazione -->
      - Secondo punto
2. Secondo elemento
3. Terzo elemento

```
---

## Design responsive con due immagini

<div class="responsive-container"> <!-- definito in custom.css -->
  <div>
    <img src="../assets/example-image.svg" alt="Immagine 1" style="width:100%">
  </div>
  <div>
    <img src="../assets/example-image.svg" alt="Immagine 2" style="width:100%">
  </div>
</div>

```
<div class="responsive-container"> <!-- definito in custom.css -->
  <div>
    <img src="assets/example-image.svg" alt="Immagine 1" style="width:100%">
  </div>
  <div>
    <img src="assets/example-image.svg" alt="Immagine 2" style="width:100%">
  </div>
</div>
```


---

## Blocco di codice

```python
def ciao_mondo():
    print("Ciao, mondo!")
```

```
```python
def ciao_mondo():
    print("Ciao, mondo!")```
```

---

## Tabella

| Intestazione 1 | Intestazione 2 | Intestazione 3 |
|----------------|----------------|----------------|
| Riga 1         | Dati           | Più dati       |
| Riga 2         | Dati           | Più dati       |
| Riga 3         | Dati           | Più dati       |

```
| Intestazione 1 | Intestazione 2 | Intestazione 3 |
|----------------|----------------|----------------|
| Riga 1         | Dati           | Più dati       |
| Riga 2         | Dati           | Più dati       |
| Riga 3         | Dati           | Più dati       |

```
---

## Citazione

> Questa è una citazione. Viene utilizzata per evidenziare una citazione o un pezzo di testo.

```
> Questa è una citazione. Viene utilizzata per evidenziare una citazione o un pezzo di testo.
```
---

## Linea orizzontale

---

```
---
```

## Collegamento

[Visita OpenAI](https://www.openai.com)

```
[Visita OpenAI](https://www.openai.com)
```
---

## Codice in linea

Utilizzare la funzione `print()` per visualizzare l'output in Python.

```
Utilizzare la funzione `print()` per visualizzare l'output in Python.
```


---
**Pubblicato il:** {{ page.meta.date }} | **Codice:** {{ page.file.name[:10] }}  | **Autore:** {{ page.meta.author }}

**Tag:** {{ page.meta.tags | join(', ') }} | **Originale:** {{ page.meta.original }}

```
**Pubblicato il:** {{ page.meta.date }} | **Codice:** {{ page.file.name[:10] }}  | **Autore:** {{ page.meta.author }}

**Tag:** {{ page.meta.tags | join(', ') }} | **Originale:** {{ page.meta.original }}
```