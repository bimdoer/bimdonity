# BIMDO Wiki Documentation

This repository contains the BIMDO Wiki documentation, built using MkDocs, a fast and simple static site generator that's geared towards building project documentation.

## 🚀 Tech Stack

- **Documentation Framework**: MkDocs
- **Theme**: Material for MkDocs
- **Markdown**: Standard Markdown with MkDocs extensions

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.7 or higher)
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd bimdo-wiki
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
# Install any additional plugins you're using
```

4. Run the development server:
```bash
mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000`

## 📁 Project Structure

```
bimdo-wiki/
├── docs/                  # Main documentation source directory
│   ├── index.md          # Main landing page of the blog
│   ├── assets/           # Resources used within markdown files
│   │   ├── images/       # Images referenced in markdown content
│   │   └── files/        # Other assets (PDFs, etc.)
│   ├── images/           # Images for site construction (logos, UI elements)
│   └── styles/      # Custom CSS overrides
│       └── extra.css     # Custom styling (blue color scheme)
├── mkdocs.yml            # MkDocs configuration file
└── requirements.txt      # Python dependencies
```

### Directory Purposes

- `docs/`: Contains all source content. This is the only directory used to generate the final site
  - `index.md`: Main landing page and entry point of the blog
  - `assets/`: Contains all resources that are referenced in markdown files
    - Organized structure for easy content management
    - Keep your blog post images and files here
  - `images/`: Contains structural images for the site itself
    - Logo, favicon, UI elements
    - Not for blog content images
  - `styles/`: Contains style overrides
    - Customizes the material theme
    - Implements BIMDO's blue color scheme

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
- Images for blog posts should be placed in `docs/assets/images/`
- Reference images in posts using relative paths:
  ```markdown
  ![Image Description](../assets/images/your-image.png)
  ```

## 📝 Writing Documentation

- All documentation is written in Markdown format
- Place your Markdown files in the `docs/` directory
- Images and other assets should go in `docs/assets/` or similar
- The navigation structure is configured in `mkdocs.yml`

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

To build the documentation site:
```bash
mkdocs build
```

This will create a `site` directory with your built documentation.

For deployment:
1. The documentation is automatically published to the `bimdo-wiki` branch:
```bash
mkdocs gh-deploy --remote-branch bimdo-wiki
```

This command will:
- Build your documentation
- Create or update the `bimdo-wiki` branch
- Push the built documentation to this branch
- Make it available through GitHub Pages

Note: Always ensure you're working on the main branch for development and let the deploy command handle the `bimdo-wiki` branch for publishing.

## 📚 Available Commands

- `mkdocs serve` - Start the live-reloading development server
- `mkdocs build` - Build the documentation site
- `mkdocs gh-deploy` - Deploy to GitHub Pages
- `mkdocs -h` - Print help message and exit

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📚 Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)

## 📺 Embedding YouTube Videos

To embed a YouTube video, use the following HTML structure:

```html
<div class="video-container">
  <iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID" allowfullscreen></iframe>
</div>
```

Ensure your `styles/custom.css` includes the necessary CSS for responsiveness.
