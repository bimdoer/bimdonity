---
title: "Typologie de la Physique du Bâtiment"
date: "2022-09-14"
author: "Manuel Emmenegger | bimdo.ch"
original: "Allemand"
tags: 
  - "Physique du Bâtiment"
  - "BIM"
  - "IFC"
  - "Typologie" 
  - "Workflow"
---
## Typologie
La typologie des éléments de construction est un aspect central de la méthodologie BIM. Les éléments ayant des exigences similaires ou identiques sont regroupés en catégories logiques. Cette catégorisation systématique permet de comprendre et de gérer le bâtiment comme une base de données structurée.

Le modèle suivant a été développé sur la base de concepts de typologie existants (par exemple, de Pirmin Jung AG) et d'expériences de projets pour illustrer le regroupement. Les deux visualisations ci-dessous montrent différents aspects de la typologie:

<div class="responsive-container">
  <div>
    <img src="assets/bi100-1003_01_perimeter-model.png" alt="Modèle de périmètre" style="width:100%">
  </div>
  <div>
    <img src="assets/bi100-1003_02_type-model.png" alt="Modèle de type" style="width:100%">
  </div>
</div>

## Visualiseur BIMx
Les deux modèles peuvent être examinés en détail dans le visualiseur web BIMx. Le modèle de périmètre utilise un code couleur clair:

- Rouge: Éléments formant le périmètre
- Bleu: Éléments dans la zone froide
- Transparent: Éléments dans la zone intérieure chaude

Le modèle de type classe les composants individuels du bâtiment selon le rapport de physique du bâtiment. La typologie couvre les cas standard les plus importants, tandis que des structures plus complexes comme les chapes ou les toits plats doivent être traitées séparément. Un objectif principal est de transmettre le concept de base de la typologie.

Il y a un potentiel d'amélioration dans la zone du sol: Actuellement, seuls les types de base WE ("Mur contre terre") et DE ("Dalle contre terre") existent. Pour une typologie complète, d'autres sous-types seraient utiles, notamment en ce qui concerne le calcul du périmètre d'isolation.

<iframe width="960" height="320" src="https://bimx-webviewer.graphisoft.com/?modelId=94c1dd96-9b8a-4770-a72c-321009c36b8b&amp;modelType=HyperModel&amp;auth=eyJhbGciOiJIUzI1NiIsImtpZCI6Ikc0MmdJR1ZzUWpLdGtpdk1YT0h5VmciLCJ0eXAiOiJKV1QifQ.eyJ0c19tb2RlbF9pZCI6Ijk0YzFkZDk2LTliOGEtNDc3MC1hNzJjLTMyMTAwOWMzNmI4YiIsInhfaWV2IjoiMCIsIm5iZiI6MTYyODUwMTU5NywiZXhwIjoyMTM2NTMzNTk3LCJpYXQiOjE2NjMxNDc5OTcsImlzcyI6Imh0dHBzOi8vYmlteC5ncmFwaGlzb2Z0LmNvbSIsImF1ZCI6Imh0dHBzOi8vYmlteC13ZWJ2aWV3ZXIuZ3JhcGhpc29mdC5jb20ifQ.lZXrN3Pobvo4OiCrp2rZTKzcpc9A-eXh43uaCEjeG1g&amp;linkVersion=2.0" frameborder="0" allowfullscreen></iframe>

Le choix de la langue est un aspect important de la typologie. Différentes phases de projet et parties prenantes utilisent différentes langues. L'utilisation cohérente de l'anglais serait une solution mais apporte ses propres défis. Le système développé contient automatiquement des désignations en allemand et en anglais, car le choix d'une seule langue nationale conduit souvent au "problème du Röstigraben" avec des groupes linguistiques désavantagés. Une langue de typologie uniforme est recommandée pour un projet.

| Allemand | Anglais |
|---------|----------|
| WE - Wand gegen Erdreich | WE - Wall to exterior |
| BE - Boden gegen Erdreich | BE - Bottom slab to exterior |

## Instructions BIMx
### Ouverture du modèle
Pour ouvrir un modèle, cliquez sur Play dans BIMx. Sélectionnez l'un des deux modèles à gauche et cliquez sur l'image d'aperçu correspondante en bas.

[![Instructions](assets/bi100-1003_03_instructions.png)](assets/bi100-1003_03_instructions.png)

### Informations sur les composants
Dans le modèle de type, les significations des couleurs peuvent être affichées en faisant un clic droit sur un élément et en sélectionnant "Info". Les typologies y sont stockées en allemand et en anglais.

[![Informations sur les composants](assets/bi100-1003_04_instructions.png)](assets/bi100-1003_04_instructions.png)

### Statut de chauffage
Les sphères rouges et bleues montrent le statut de chauffage (chauffé/non chauffé) des pièces. Les détails s'affichent en faisant un clic droit sur "Info". Les pièces elles-mêmes peuvent également être affichées et filtrées par chaud/froid, comme illustré dans la capture d'écran.

[![Statut de chauffage](assets/bi100-1003_05_instructions.png)](assets/bi100-1003_05_instructions.png)

## Conclusion
La typologie existait avant le BIM - même un plan marqué regroupe des éléments. L'avantage du modèle numérique réside dans la gestion cohérente des données et la visualisation efficace, permettant à tous les participants au projet de développer une meilleure compréhension du projet de construction.


---
**Publié le:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Auteur:** {{ page.meta.author }}

**Tags:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}