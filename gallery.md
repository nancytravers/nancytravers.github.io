---
layout: default
title: Gallery
---

# Gallery Page


{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% for painting in paintings %}
  <div class="gallery-item">
    <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}">
  </div>
{% endfor %}



