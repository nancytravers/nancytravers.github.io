---
layout: default
title: Gallery
---

# Gallery Page

{% raw %}
<style>
.column {
  width: 50%;
  float: left;
  box-sizing: border-box;
  padding: 10px;
}

@media (max-width: 768px) {
  .column {
    width: 100%;
    float: none;
  }
}

.gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.gallery-item {
  width: 45%;
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  .gallery-item {
    width: 100%;
  }
}
</style>
{% endraw %}

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

<div class="gallery">
  <div class="column">
    {% for painting in paintings %}
      {% if forloop.index0 | modulo: 2 == 0 %}
        <div class="gallery-item">
          <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}">
        </div>
      {% endif %}
    {% endfor %}
  </div>
  
  <div class="column">
    {% for painting in paintings %}
      {% if forloop.index0 | modulo: 2 != 0 %}
        <div class="gallery-item">
          <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}">
        </div>
      {% endif %}
    {% endfor %}
  </div>
</div>

```
/*
#{% for painting in paintings %}
#  <div class="gallery-item">
#    <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}">
#  </div>
#{% endfor %}
*/
```

