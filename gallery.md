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

{% capture image_paths %}
  /path/to/image1.jpg
  /path/to/image2.jpg
  /path/to/image3.jpg
{% endcapture %}

{% assign images = image_paths | strip_newlines | split: '\n' %}

{% for image in images %}
  <div class="gallery-item">
    ![Image]({{ image }})
  </div>
{% endfor %}

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% for painting in paintings %}
  <div class="gallery-item">
    ![{{ painting.name }}]({{ painting.path | relative_url }})
  </div>
{% endfor %}


