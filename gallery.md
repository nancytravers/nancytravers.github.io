---
layout: default
title: Gallery
---

# Gallery Page
{% raw %}
<style>
.gallery-item {
  display: inline-block;
  margin: 10px;
}

.gallery-item img {
  width: 200px;
  height: 200px;
  object-fit: cover;
}
</style>
{% endraw %}

{% assign images = image_paths | strip_newlines | split: '\n' %}

{% for image in images %}
  <div class="gallery-item">
    ![Image]({{ image }})
  </div>
{% endfor %}

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% for painting in paintings %}
	![]({{ painting.path }})
  <div class="gallery-item">
   <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}"/>  
<p> {{ painting.path }} </p>
</div>

{% endfor %}


