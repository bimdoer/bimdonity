---
title: "Getting Started with GDL"
date: "2025-03-15"
author: "Manuel Emmenegger | bimdo.ch"
original: "German"
tags:
  - "Archicad"
  - "GDL"
  - "Library"
---

## GDL in Archicad

In this article, we answer frequently asked questions about the Geometric Description Language (GDL) – the scripting language that ArchiCAD uses to create parametric objects. We explain what GDL is, why it's worth learning GDL, and how to take your first steps in the GDL world.

---

### What is GDL?
GDL (Geometric Description Language) is the scripting language that ArchiCAD libraries use to define parametric objects. Unlike a simple "Hello World", GDL delivers practical results after just a few lines of code. Complex tools such as windows or doors are not created as static elements, but as dynamic, script-based objects.  
In ArchiCAD, GDL is packaged in so-called LCF containers (with the GSM file format).

### Advantages of GDL
- **Quick Start:** Even simple scripts show visual results, which is motivating.  
- **Understanding Parametrics:** With GDL, you gain a fundamental understanding of parametric modeling in CAD software.  
- **Practical Applications:** You can optimize daily workflows since many objects and tools in ArchiCAD are based on GDL.  
- **Visual Scripting:** Newer tools like [Param-O](https://graphisoft.com/downloads/param-o) enable a visual approach, making it easier to get started.

---

## First Steps in GDL

A good starting point is to focus on a simple 2D and 3D script. In the Swiss version of ArchiCAD, you'll find the GDL editor under _File → GDL Objects → Create GDL Objects_.   

  - **Tip:** At first, limit yourself to basic commands, such as creating a cuboid with the `block` command.  
  - **Visualization:** Use the 2D and 3D views to immediately check the effects of your script.
[![Overview-Editor](assets/ac210-1000_01_Overview-Editor.png)](assets/ac210-1000_01_Overview-Editor.png)
---

## Useful Resources

- The [GDL Reference Manual](https://help.graphisoft.com/AC/24/ENG/GDL.pdf) offers a comprehensive overview of commands.
[![Reference-Manual](assets/ac210-1000_02_Reference-Manual.png)](assets/ac210-1000_02_Reference-Manual.png)
- Sites like [SelfGDL.de](https://www.selfgdl.de/) and the [GDL Cookbook](https://issuu.com/dnicholsoncole/docs/gdlcookbook3_01) by David Nicholson-Cole provide practical examples.

**Additional Resources:**   
Here's a compilation of helpful platforms where you can find ready-made GDL elements and further information:   

- [idc.ch](https://www.idc.ch/archicad/ueber-archicad/zusatzprodukte/zusatzbibliotheken/)   
- [bimobject.com](https://www.bimobject.com/de-ch/product?sort=trending)    
- [bimcomponents.com](https://bimcomponents.com/)   
- [cadswift.com.au](https://cadswift.com.au/)   
- [arroway-textures.ch](https://www.arroway-textures.ch/)   
- [mtextur.com](https://www.mtextur.com/)   
- [bimbakery.co](http://bimbakery.co/)    
- [turbosquid.com](https://www.turbosquid.com/)   
- [b-prisma.de](https://www.b-prisma.de/)   
- [concepsysbim.com](http://www.concepsysbim.com/)    
- [prodlib.com](https://www.prodlib.com/?lang=en)   
- [3dwarehouse.sketchup.com](https://3dwarehouse.sketchup.com/)   
- [archive3d.net](https://archive3d.net/)   
- [velux.at](https://www.velux.at/fachkunden/tools-technik/3d-bim-objekte)    
- [eptar.hu](https://www.eptar.hu/)   
- [poliigon.com](http://www.poliigon.com/)    

Additionally, exchanging ideas in forums (such as [ArchiCAD-Talk](https://archicad-talk.graphisoft.com/)) is helpful to benefit from other users' experiences.

---

**Published on:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Author:** {{ page.meta.author }}

**Tags:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}