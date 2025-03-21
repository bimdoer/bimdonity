---
title: "Building Physics Typology"
date: "2022-09-14"
author: "Manuel Emmenegger | bimdo.ch"
tags: 
  - "Building Physics"
  - "BIM"
  - "IFC"
  - "Typology"
  - "Workflow"
---
## Typology
The typology of building elements is a central aspect of BIM methodology. Elements with similar or identical requirements are grouped into logical categories. This systematic categorization allows understanding and managing the building as a structured database.

The following model was developed based on existing typology concepts (e.g., from Pirmin Jung AG) and project experiences to illustrate the grouping. The two visualizations below show different aspects of typology:

<div class="responsive-container">
  <div>
    <img src="assets/bi100-1003_01_perimeter-model.png" alt="Perimeter Model" style="width:100%">
  </div>
  <div>
    <img src="assets/bi100-1003_02_type-model.png" alt="Type Model" style="width:100%">
  </div>
</div>

## BIMx Viewer
Both models can be examined in detail in the BIMx web viewer. The perimeter model uses a clear color coding:

- Red: Perimeter-forming elements
- Blue: Elements in the cold area
- Transparent: Elements in the warm interior area

The type model classifies the individual building components according to the building physics report. The typology covers the most important standard cases, while more complex structures such as subfloors or flat roofs must be treated separately. A main goal is to convey the basic concept of typology.

There is potential for improvement in the ground area: Currently, only the basic types WE ("Wall to exterior") and DE ("Bottom slab to exterior") exist. For a complete typology, further subtypes would be useful, especially with regard to insulation perimeter calculation.

<iframe width="960" height="320" src="https://bimx-webviewer.graphisoft.com/?modelId=94c1dd96-9b8a-4770-a72c-321009c36b8b&amp;modelType=HyperModel&amp;auth=eyJhbGciOiJIUzI1NiIsImtpZCI6Ikc0MmdJR1ZzUWpLdGtpdk1YT0h5VmciLCJ0eXAiOiJKV1QifQ.eyJ0c19tb2RlbF9pZCI6Ijk0YzFkZDk2LTliOGEtNDc3MC1hNzJjLTMyMTAwOWMzNmI4YiIsInhfaWV2IjoiMCIsIm5iZiI6MTYyODUwMTU5NywiZXhwIjoyMTM2NTMzNTk3LCJpYXQiOjE2NjMxNDc5OTcsImlzcyI6Imh0dHBzOi8vYmlteC5ncmFwaGlzb2Z0LmNvbSIsImF1ZCI6Imh0dHBzOi8vYmlteC13ZWJ2aWV3ZXIuZ3JhcGhpc29mdC5jb20ifQ.lZXrN3Pobvo4OiCrp2rZTKzcpc9A-eXh43uaCEjeG1g&amp;linkVersion=2.0" frameborder="0" allowfullscreen></iframe>

Language choice is an important aspect of typology. Different project phases and stakeholders use different languages. Consistent use of English would be one solution but brings its own challenges. The developed system automatically contains German and English designations, as choosing a single national language often leads to the "Röstigraben problem" with disadvantaged language groups. A uniform typology language is recommended for a project.

| German | English |
|---------|----------|
| WE - Wand gegen Erdreich | WE - Wall to exterior |
| BE - Boden gegen Erdreich | BE - Bottom slab to exterior |

## BIMx Instructions
### Opening the Model
To open a model, click Play in BIMx. Select one of the two models on the left and click on the corresponding preview image at the bottom.

[![Instructions](assets/bi100-1003_03_instructions.png)](assets/bi100-1003_03_instructions.png)

### Component Information
In the type model, the meanings of the colors can be displayed by right-clicking on an element and selecting "Info". There, the typologies are stored in German and English.

[![Component Information](assets/bi100-1003_04_instructions.png)](assets/bi100-1003_04_instructions.png)

### Heating Status
The red and blue spheres show the heating status (heated/unheated) of the rooms. Details are displayed by right-clicking on "Info". The rooms themselves can also be displayed and filtered by warm/cold, as shown in the screenshot.

[![Heating Status](assets/bi100-1003_05_instructions.png)](assets/bi100-1003_05_instructions.png)

## Conclusion
Typology existed before BIM - even a marked plan groups elements. The advantage of the digital model lies in consistent data management and efficient visualization, allowing all project participants to develop a better understanding of the construction project.


---
**Published on:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Author:** {{ page.meta.author }}

**Tags:** {{ page.meta.tags | join(', ') }} 