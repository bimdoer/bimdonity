---
title: "Markdown Templates"
date: "2024-01-17"
author: "Manuel Emmenegger | bimdo.ch"
original: "Deutsch"
tags:
  - "Markdown"
  - "Template"
  - "Documentation"
  - "Guide"
---

This template demonstrates common Markdown formatting elements and how to use them effectively in documentation.

## Header
Always use a header, title is used for navigation and title. Date appears in the footer and tags in the search.

```
---
title: "Markdown Templates"
date: "2024-01-17"
author: "Manuel Emmenegger | bimdo.ch"
original: "Deutsch"
tags:
  - "Markdown"
  - "Template"
  - "Documentation"
  - "Guide"
---
```

## Comments
Comments are not visible.

```
<!-- comments -->
```

## Chapters
_# h1 not used, title will appear automatic_
## h2 chapters
```
## h2 chapters
```
### h3 subchapters
```
### h3 subchapters
```


## YouTube
Take the right embed link from youtube (only link), is connected with custom.css
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
Can't select in the interface.
![Parameter](assets/example-image.svg)

```
![Parameter](assets/example-image.svg)
```

Can select in the interface.
[![Parameter](assets/example-image.svg)](assets/example-image.svg)

```
[![Parameter](assets/example-image.svg)](assets/example-image.svg)
```
---

## Lists

### Numbered List
<!-- Enter is needed for right representation -->
1. First item
2. Second item
3. Third item
```
### Numbered List
<!-- Enter is needed for right representation -->
1. First item
2. Second item
3. Third item

```
### Bulleted List
<!-- Enter is needed for right representation -->
- First point
- Second point
- Third point
```
### Bulleted List
<!-- Enter is needed for right representation -->
- First point
- Second point
- Third point

```
### Combined List
<!-- Enter is needed for right representation -->
1. First item
      - First point <!-- indent for right representation -->
      - Second point
2. Second item
3. Third item
```
### Combined List
<!-- Enter is needed for right representation -->
1. First item
      - First point <!-- indent for right representation -->
      - Second point
2. Second item
3. Third item

```
---

## Responsive Design with Two Images

<div class="responsive-container"> <!-- defined in custom.css -->
  <div>
    <img src="../assets/example-image.svg" alt="Image 1" style="width:100%">
  </div>
  <div>
    <img src="../assets/example-image.svg" alt="Image 2" style="width:100%">
  </div>
</div>

```
<div class="responsive-container"> <!-- defined in custom.css -->
  <div>
    <img src="assets/example-image.svg" alt="Image 1" style="width:100%">
  </div>
  <div>
    <img src="assets/example-image.svg" alt="Image 2" style="width:100%">
  </div>
</div>
```


---

## Code Block

```python
def hello_world():
    print("Hello, world!")
```

```
```python
def hello_world():
    print("Hello, world!")```
```

---

## Table

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | More Data|
| Row 2    | Data     | More Data|
| Row 3    | Data     | More Data|

```
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | More Data|
| Row 2    | Data     | More Data|
| Row 3    | Data     | More Data|

```
---

## Blockquote

> This is a blockquote. It is used to highlight a quote or a piece of text.

```
> This is a blockquote. It is used to highlight a quote or a piece of text.
```
---

## Horizontal Line

---

```
---
```

## Link

[Visit OpenAI](https://www.openai.com)

```
[Visit OpenAI](https://www.openai.com)
```
---

## Inline Code

Use the `print()` function to display output in Python.

```
Use the `print()` function to display output in Python.
```


---
**Veröffentlicht am:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Autor:** {{ page.meta.author }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}

```
**Veröffentlicht am:** {{ page.meta.date }} | **Code:** {{ page.file.name[:10] }}  | **Autor:** {{ page.meta.author }}

**Schlagwörter:** {{ page.meta.tags | join(', ') }} | **Original:** {{ page.meta.original }}
```
