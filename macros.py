# macros.py

def define_env(env):
    @env.macro
    def get_tags(pages):
        """
        Scans all pages and collects tags from the Front Matter.
        Returns a dictionary with tag (lowercase) as keys and list of pages as values.
        """
        tags = {}
        for page in pages:
            # page.meta ist ein Dictionary mit den Front Matter-Daten.
            page_tags = page.meta.get("tags", [])
            for tag in page_tags:
                tag_key = tag.lower()
                if tag_key not in tags:
                    tags[tag_key] = []
                tags[tag_key].append(page)
        return tags

    # Testmacro, um sicherzugehen, dass macros.py geladen wird:
    @env.macro
    def test_macro():
        return "Macro funktioniert!"
