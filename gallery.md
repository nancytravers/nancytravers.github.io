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

.lb-close {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 30px;
  height: 30px;
  text-align: center;
  color: #fff;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  font-size: 24px;
  line-height: 30px;
  cursor: pointer;
  z-index: 9999;
}

.lb-close:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

}
</style>
{% endraw %}

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% assign col2 = site.static_files | where_exp: "file", "file.path contains '/assets/col2'" %}
<link rel="stylesheet" href="path/to/photoswipe.css">
<link rel="stylesheet" href="path/to/default-skin/default-skin.css">
<script src="path/to/photoswipe.min.js"></script>
<script src="path/to/photoswipe-ui-default.min.js"></script>


<div class="gallery">
  <div class="column">
    {% for painting in paintings %}
  <div class="gallery-item">
    <figure>
      <a href="{{ painting.path | relative_url }}" data-size="800x600">
        <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}" loading="lazy">
      </a>
      <figcaption>{{ painting.name }}</figcaption>
    </figure>
  </div>
    {% endfor %}
  </div>
  
  <div class="column">
    {% for painting in col2 %}
  <div class="gallery-item">
    <figure>
      <a href="{{ painting.path | relative_url }}" data-size="800x600">
        <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}" loading="lazy">
      </a>
      <figcaption>{{ painting.name }}</figcaption>
    </figure>
  </div>


    {% endfor %}
  </div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  var gallery = new PhotoSwipe('.gallery', PhotoSwipeUI_Default);
  gallery.init();
});
</script>



