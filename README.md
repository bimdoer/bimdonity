# BIMDONITY Documentation

This repository contains the BIMDONITY documentation, built using MkDocs, a fast and simple static site generator that's geared towards building project documentation.

## 🚀 Tech Stack

- **Documentation Framework**: MkDocs
- **Theme**: Material for MkDocs with custom BIMDONITY styling
- **Markdown**: Standard Markdown with MkDocs extensions
- **Internationalization**: mkdocs-static-i18n for German, French, Italian and English support

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.7 or higher)
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/bimdoer/bimdonity
cd bimdonity
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install MkDocs and required packages:
```bash
pip install mkdocs
pip install mkdocs-material
pip install mkdocs-static-i18n
pip install mkdocs-macros-plugin
# Install any additional plugins you're using
```

4. Run the development server:
```bash
mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000`

## 📁 Project Structure

```
bimdonity/
├── docs/ # Main documentation source directory
│ ├── index.de.md # German landing page (default)
│ ├── index.en.md # English landing page
│ ├── index.fr.md # French landing page
│ ├── index.it.md # Italian landing page
│ ├── MKDocs/ # Contains MkDocs specific documentation
│ │ ├── markdown-empty.de.md # German markdown template
│ │ ├── markdown-empty.en.md # English markdown template
│ │ ├── markdown-empty.fr.md # French markdown template
│ │ ├── markdown-empty.it.md # Italian markdown template
│ │ └── assets/ # Resources used within markdown files
│ ├── BIM/ # BIM related documentation
│ │ ├── example.de.md # German BIM documentation
│ │ ├── example.en.md # English BIM documentation
│ │ └── assets/ # Resources used within markdown files
│ ├── Grasshopper/ # Grasshopper related documentation
│ │ ├── tutorial.de.md # German Grasshopper tutorial
│ │ ├── tutorial.en.md # English Grasshopper tutorial
│ │ └── assets/ # Resources used within markdown files
│ ├── Archicad/ # Archicad related documentation
│ │ ├── 1 Preperation/ # Preparation section
│ │ │ ├── topic.de.md # German preparation topic
│ │ │ └── topic.en.md # English preparation topic
│ │ ├── 2 Foundation/ # Foundation section
│ │ │ ├── 2.1 Library/ # Library subsection
│ │ │ │ ├── gdl-intro.de.md # German GDL introduction
│ │ │ │ └── gdl-intro.en.md # English GDL introduction
│ │ └── assets/ # Resources used within markdown files
│ ├── images/ # Images for site construction (logos, UI elements)
│ └── styles/ # Custom CSS overrides
│ └── custom.css # Custom styling
├── mkdocs.yml # MkDocs configuration file
└── requirements.txt # Python dependencies
```

### Directory Purposes

- `docs/`: Contains all source content. This is the only directory used to generate the final site
  - `index.md`: Main landing page and entry point of the blog
  - `MKDocs/`, `BIM/`, `Grasshopper/`, `Archicad/`: Subdirectories for organizing content by topic
  - `images/`: Contains structural images for the site itself
    - Logo, favicon, UI elements
    - Not for blog content images
  - `styles/`: Contains style overrides
    - Customizes the material theme
    - Implements BIMDO's blue color scheme
  - `assets/`: Contains all resources that are referenced in markdown files
    - Organized structure for easy content management
    - Keep your blog post images and files here

### Usage as a Blog

This documentation site is structured as a blog, which means:
- Each markdown file in `docs/` represents a blog post or page
- Posts can be organized in subdirectories for better structure
- Use front matter in markdown files to add metadata:
  ```yaml
  ---
  title: Your Blog Post Title
  date: 2024-01-01
  author: Author Name
  tags:
    - category
    - topic
  ---
  ```
- Images for blog posts should be placed in `docs/../assets/`
- Reference images in posts using relative paths:
  ```markdown
  ![Image Description](../assets/your-image.png)
  ```

## 📝 Writing Documentation

- All documentation is written in Markdown format
- Place your Markdown files in the `docs/` directory
- Images and other assets should go in `docs/../assets/` or similar
- The navigation structure is configured in `mkdocs.yml`

### Writing Relative Paths

- **Markdown**: Use relative paths to reference images and other assets. For example:
  ```markdown
  ![Image Description](assets/your-image.png)
  ```
- **HTML**: When using HTML within Markdown files, ensure paths are relative to the Markdown file's location:
  ```html
  <img src="../assets/images/your-image.png" alt="Image Description">
  ```

## ⚙️ Configuration

The main configuration file is `mkdocs.yml`. Here you can configure:
- Site name and metadata
- Theme settings
- Navigation structure
- Plugins
- Markdown extensions
- Additional customization

## 🎨 Customization

### Theme

This documentation uses Material for MkDocs theme. You can customize:
- Colors and fonts
- Navigation
- Search functionality
- And more in `mkdocs.yml`

## 🚀 Building and Deployment

The documentation site is automatically built and deployed through GitHub Actions workflows. The process is:

1. Make changes to documentation files in the `docs/` directory
2. Create a pull request targeting the `main` branch
3. Once the PR is merged, GitHub Actions will:
   - Build the documentation
   - Deploy it to GitHub Pages
   - Make it available at https://bimdoer.github.io/bimdonity/

⚠️ Important Notes:
- Direct pushes to `main` are blocked - all changes must go through pull requests
- The site is automatically generated from the `main` branch
- Manual builds and deployments are not needed

## 📚 Available Commands

- `mkdocs serve` - Start the live-reloading development server
- `mkdocs build` - Build the documentation site
- `mkdocs gh-deploy` - Deploy to GitHub Pages
- `mkdocs -h` - Print help message and exit

## 📄 License

See the LICENSE file for details.

## 📚 Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
