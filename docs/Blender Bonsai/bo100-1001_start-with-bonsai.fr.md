---
title: "Débuter avec Bonsai"
date: "2024-03-20"
author: "Manuel Emmenegger"
original: "Allemand"
tags:
  - "Blender"
  - "Bonsai"
---

## Introduction
Dans le cadre d'une série d'interviews Bonsai par [Petru Conduraru](https://www.linkedin.com/in/petruc/), les contenus suivants ont été créés pour vous aider à démarrer avec Bonsai. Vous souhaitez également partager vos connaissances ? Contactez directement Petru et faites partie de la série d'interviews.
Vous pouvez trouver l'interview associée [ici](https://www.youtube.com/watch?v=bp3uZyTVqpk).

<div class="video-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/bp3uZyTVqpk?si=ZIHVXgTVxoe754So" frameborder="0" allowfullscreen></iframe>
</div>


---
## Liens utiles
### Logiciel
- [Télécharger Blender](https://www.blender.org/download/)
- [Télécharger l'add-on Bonsai](https://blenderbim.org/download.html)

### Communauté & Support
- [Dépôt GitHub de Bonsai](https://github.com/IfcOpenShell/IfcOpenShell)
- [IFC Architect - Documentation Bonsai](https://ifcarchitect.com/)
- [Chaîne YouTube IFC Architect](https://www.youtube.com/@ifcarchitect)
- [Chaîne YouTube BIMvoice](https://www.youtube.com/@BIMvoice)
- [Forum de la communauté Bonsai](https://community.osarch.org/)

---
## Aperçu des fonctionnalités
Bonsai est un puissant outil BIM open-source pour Blender qui offre diverses fonctions:

### Fonctionnalités principales que j'utilise activement

- **Visualisation BIM & Coordination**
    - Navigation rapide et visualisation des modèles IFC
    - Options de filtrage flexibles pour une analyse ciblée des composants du bâtiment

- **Gestion de l'information**
    - Accès facile à toutes les propriétés et attributs IFC
    - Affichage structuré de la hiérarchie du bâtiment

- **Visualisation**
    - Schémas de couleurs personnalisables pour différentes propriétés

- **Modification de modèle**
    - Ajustement des propriétés et attributs

### Fonctionnalités supplémentaires disponibles

- **Modélisation**: Création d'éléments BIM natifs
- **Gestion des coûts**: Liaison avec les données de coûts
- **Planification des ressources**: Gestion des ressources temporelles et matérielles
- **Contrôle qualité**: Vérifications automatisées du modèle
- **Calcul**: Détermination des quantités et des masses
- **Gestion des installations**: Support pour l'exploitation des bâtiments

[![Aperçu de Bonsai](assets/bo100-1001_01_bonsai-overview.jpg)](assets/bo100-1001_01_bonsai-overview.jpg)

---
## Paramètres de navigation
- **Depth**: Cette case à cocher optimise le défilement et empêche que la navigation soit bloquée par des objets au premier plan.
- **Zoom to Mouse Position**: Ce paramètre fait que le zoom s'effectue directement à la position de la souris, au lieu de zoomer depuis le centre de l'écran.

[![Paramètres Blender](assets/bo100-1001_02_bonsai-blender-settings.jpg)](assets/bo100-1001_02_bonsai-blender-settings.jpg)

---
## Filtre de sélection du navigateur
La fonction de filtre permet un filtrage sélectif de la structure arborescente hiérarchique - particulièrement utile pour les grands modèles IFC. Cela fait que la structure arborescente n'affiche que les éléments actuellement sélectionnés dans le modèle.

[![Navigateur Bonsai](assets/bo100-1001_03_bonsai-navigator.jpg)](assets/bo100-1001_03_bonsai-navigator.jpg)

---
## Structure IFC et Shift
- **shift**: Une fonction utile consiste à maintenir la touche Shift enfoncée lors de l'ouverture et de la fermeture de la structure arborescente, ce qui permet d'ouvrir et de fermer la structure, y compris tous les sous-dossiers.
- **Structure IFC**: Comparé à d'autres visualiseurs IFC, on remarque que la structure semble quelque peu différente, par exemple, les niveaux sont représentés géométriquement. Cette approche "différente" est probablement la structure IFC native et correctement affichée.

[![Shift Bonsai](assets/bo100-1001_04_bonsai-shift.jpg)](assets/bo100-1001_04_bonsai-shift.jpg)

---
## Affichage de l'environnement
La capture d'écran suivante montre comment les paramètres visuels tels que les couleurs des axes et la grille de travail peuvent être ajustés. De plus, les croix de référence pour les niveaux et autres éléments peuvent être affichées ou masquées.

[![Niveaux Bonsai](assets/bo100-1001_05_bonsai-levels.jpg)](assets/bo100-1001_05_bonsai-levels.jpg)

---
## Sauvegarde de l'environnement de travail
Comme vous le savez peut-être d'autres outils, vous pouvez également enregistrer vos paramètres pour votre environnement de travail dans Blender, comme par exemple l'agencement de différents espaces de travail.

[![Préférences utilisateur Bonsai](assets/bo100-1001_06_bonsai-userpref.jpg)](assets/bo100-1001_06_bonsai-userpref.jpg)

---
## Raccourcis
- **shift**: Shift est très puissant, permettant d'ouvrir et de fermer des structures arborescentes avec des sous-structures, ou d'afficher et de masquer tous les sous-éléments dans la structure arborescente.
- **Point**: Utiliser le raccourci "." ou selon les paramètres de langue "," optimise le zoom sur la sélection. Vous sélectionnez l'élément par exemple dans le navigateur et zoomez directement sur l'élément en 3D.
- **Transparence**: Certes, ce n'est pas un raccourci, mais c'est tout de même très utile pour la coordination.
- **H**: Masquer un élément sélectionné
- **alt+H**: Tout afficher
- **shift+H**: Masquer tous les éléments non sélectionnés

[![Raccourcis Bonsai](assets/bo100-1001_07_bonsai-shortcuts.jpg)](assets/bo100-1001_07_bonsai-shortcuts.jpg)

---
## Coloration par propriété
Une fonction très pratique pour colorer les éléments du modèle. Important à savoir: si votre propriété ou ensemble de propriétés n'apparaît pas, sélectionnez un élément et réessayez.
[![Coloration Bonsai](assets/bo100-1001_08_bonsai-colorizing.jpg)](assets/bo100-1001_08_bonsai-colorizing.jpg)

### Bonsai vs. Solibri
Dans Bonsai, il n'existe actuellement pas de liste qui contient également des couleurs. Ces fonctions sont séparées, soit liste, soit couleur.
> C'est une fonction très pratique pour effectuer des vérifications visuelles et obtenir un aperçu des données.

[![Bonsai Solibri](assets/bo100-1001_09_bonsai-solibri.jpg)](assets/bo100-1001_09_bonsai-solibri.jpg)

---
## Filtre
La fonction de filtre est très puissante; notez les différences entre propriété et attribut.
[![Filtres Bonsai](assets/bo100-1001_10_bonsai-filters.jpg)](assets/bo100-1001_10_bonsai-filters.jpg)

---
## Sections dans le modèle
L'utilisation des coupes de section n'est pas la méthode la plus facile et est encore un peu instable. Cependant, elle fonctionne dans la version montrée dans la capture d'écran.
> Une application plus optimale consiste à sélectionner l'outil "Fetch" sur le côté gauche dans la barre d'outils Bonsai (icône de boîte verte avec curseur blanc). Avec Shift+C, un plan de coupe peut ensuite être placé comme souhaité.

[![Sections Bonsai](assets/bo100-1001_11_bonsai-sections.jpg)](assets/bo100-1001_11_bonsai-sections.jpg)


---
**Publié le:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Auteur:** {{ page.meta.author }}

**Tags:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}