---
title: "Modèles Markdown"
date: "2024-01-17"
author: "Manuel Emmenegger | bimdo.ch"
tags:
  - "Markdown"
  - "Modèle"
  - "Documentation"
  - "Guide"
---

Ce modèle démontre les éléments de formatage Markdown courants et comment les utiliser efficacement dans la documentation.

## En-tête
Utilisez toujours un en-tête, le titre est utilisé pour la navigation et le titre. La date apparaît dans le pied de page et les tags dans la recherche.

```
---
title: "Modèles Markdown"
date: "2024-01-17"
author: "Manuel Emmenegger | bimdo.ch"
tags:
  - "Markdown"
  - "Modèle"
  - "Documentation"
  - "Guide"
---
```

## Commentaires
Les commentaires ne sont pas visibles.

```
<!-- commentaires -->
```

## Chapitres
_# h1 n'est pas utilisé, le titre apparaîtra automatiquement_
## Chapitres h2
```
## Chapitres h2
```
### Sous-chapitres h3
```
### Sous-chapitres h3
```


## YouTube
Prenez le bon lien d'intégration de YouTube (uniquement le lien), est connecté avec custom.css
<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/cgiI8TBw9H0?si=NWXfqKQGowqPxPVR" frameborder="0" allowfullscreen></iframe>
</div>
```html
<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/cgiI8TBw9H0?si=NWXfqKQGowqPxPVR" frameborder="0" allowfullscreen></iframe>
</div>
```

---

## Image
Ne peut pas être sélectionnée dans l'interface.
![Paramètre](assets/example-image.svg)

```
![Paramètre](assets/example-image.svg)
```

Peut être sélectionnée dans l'interface.
[![Paramètre](assets/example-image.svg)](assets/example-image.svg)

```
[![Paramètre](assets/example-image.svg)](assets/example-image.svg)
```
---

## Listes

### Liste numérotée
<!-- Entrée nécessaire pour une bonne représentation -->
1. Premier élément
2. Deuxième élément
3. Troisième élément
```
### Liste numérotée
<!-- Entrée nécessaire pour une bonne représentation -->
1. Premier élément
2. Deuxième élément
3. Troisième élément

```
### Liste à puces
<!-- Entrée nécessaire pour une bonne représentation -->
- Premier point
- Deuxième point
- Troisième point
```
### Liste à puces
<!-- Entrée nécessaire pour une bonne représentation -->
- Premier point
- Deuxième point
- Troisième point

```
### Liste combinée
<!-- Entrée nécessaire pour une bonne représentation -->
1. Premier élément
      - Premier point <!-- indentation pour une bonne représentation -->
      - Deuxième point
2. Deuxième élément
3. Troisième élément
```
### Liste combinée
<!-- Entrée nécessaire pour une bonne représentation -->
1. Premier élément
      - Premier point <!-- indentation pour une bonne représentation -->
      - Deuxième point
2. Deuxième élément
3. Troisième élément

```
---

## Design responsive avec deux images

<div class="responsive-container"> <!-- défini dans custom.css -->
  <div>
    <img src="../assets/example-image.svg" alt="Image 1" style="width:100%">
  </div>
  <div>
    <img src="../assets/example-image.svg" alt="Image 2" style="width:100%">
  </div>
</div>

```
<div class="responsive-container"> <!-- défini dans custom.css -->
  <div>
    <img src="assets/example-image.svg" alt="Image 1" style="width:100%">
  </div>
  <div>
    <img src="assets/example-image.svg" alt="Image 2" style="width:100%">
  </div>
</div>
```


---

## Bloc de code

```python
def bonjour_monde():
    print("Bonjour, monde!")
```

```
```python
def bonjour_monde():
    print("Bonjour, monde!")```
```

---

## Tableau

| En-tête 1 | En-tête 2 | En-tête 3 |
|-----------|-----------|-----------|
| Ligne 1   | Données   | Plus de données|
| Ligne 2   | Données   | Plus de données|
| Ligne 3   | Données   | Plus de données|

```
| En-tête 1 | En-tête 2 | En-tête 3 |
|-----------|-----------|-----------|
| Ligne 1   | Données   | Plus de données|
| Ligne 2   | Données   | Plus de données|
| Ligne 3   | Données   | Plus de données|

```
---

## Citation

> Ceci est une citation. Elle est utilisée pour mettre en évidence une citation ou un morceau de texte.

```
> Ceci est une citation. Elle est utilisée pour mettre en évidence une citation ou un morceau de texte.
```
---

## Ligne horizontale

---

```
---
```

## Lien

[Visiter OpenAI](https://www.openai.com)

```
[Visiter OpenAI](https://www.openai.com)
```
---

## Code en ligne

Utilisez la fonction `print()` pour afficher la sortie en Python.

```
Utilisez la fonction `print()` pour afficher la sortie en Python.
```


---
**Publié le:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Auteur:** {{ page.meta.author }}

**Tags:** {{ page.meta.tags | join(', ') }} 