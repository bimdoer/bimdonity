# Tag Overview

{% set tag_dict = get_tags(pages) %}
{% for tag, pages in tag_dict.items() %}
## {{ tag | capitalize }}

{% for p in pages %}
- [{{ p.title }}]({{ p.url }})
{% endfor %}

{% endfor %}

# Test Macro

{{ test_macro() }}
