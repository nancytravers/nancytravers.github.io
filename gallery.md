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
{% raw %}
<img src="./assets/paintings/Chacho.JPG" >
{% endraw %}

![IMGIMG](https://github.com/nancytravers/nancytravers.github.io/blob/main/assets/paintings/DSCN2377.jpg)

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% for painting in paintings %}
  <div class="gallery-item">
    ![{{ painting.name }}]({{ painting.path | relative_url }})
  </div>
{% endfor %}

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% for painting in paintings %}
  <div class="gallery-item">
    <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}">
  </div>
{% endfor %}


