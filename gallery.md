---
layout: default
title: Gallery
---

# Gallery Page

{% raw %}
<style>
.column {
  width: 50%;
  box-sizing: border-box;
  padding: 5px;
}

@media (max-width: 768px) {
  .column {
    width: 100%;
    float: none;
  }
}

.gallery {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.gallery-item {
  margin-bottom: 10px;
  display: inline-block;
  vertical-align: top;
  box-sizing: border-box;
  padding: 10px;
}

.gallery-item img {
  width: 100%;
  height: auto;
  transition: transform 0.3s;
}
    
.gallery-item:hover img {
  transform: scale(1.1);
}

@media (max-width: 768px) {
  .gallery-item {
    width: 100%;
  }
}
</style>
{% endraw %}

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% assign col2 = site.static_files | where_exp: "file", "file.path contains '/assets/col2'" %}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js"></script>

<div class="gallery">
  <div class="column">
    {% for painting in paintings %}
<div class="gallery-item">
  <a href="{{ painting.path | relative_url }}" data-lightbox="gallery" data-title="{{ painting.name }}">
    <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}" loading="lazy">
  </a>
</div>

    {% endfor %}
  </div>
  
  <div class="column">
    {% for painting in col2 %}

<div class="gallery-item">
  <a href="{{ painting.path | relative_url }}" data-lightbox="gallery" data-title="{{ painting.name }}">
    <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}" loading="lazy">
  </a>
</div>
    {% endfor %}
  </div>
</div>
<script>
  lightbox.option({
    'resizeDuration': 200,
    'wrapAround': true,
    'showImageNumberLabel': false, 
    'disableScrolling': true, 
    'alwaysShowNavOnTouchDevices': true, // Optional: Show navigation buttons on touch devices
    'albumLabel': 'Image %1 of %2', // Optional: Customize the album label
    'fadeDuration': 300, // Optional: Customize the fade-in/out duration
    'closeButtonCaption': '&times;', // Custom close button caption ('&times;' is the HTML code for 'x')
  });
</script>


