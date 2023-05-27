---
layout: default
title: Gallery
---

# Gallery Page

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
