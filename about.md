---
layout: page
title: About
description: >-
    Course policies and information.
---

# About
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## About

Nancy Travers is an artist, painter, former ceramics teacher at Clackamas Community College, and Oregon native.
{% raw %}
<head>
  <style>
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      grid-gap: 10px;
    }
    
    .gallery-item {
      position: relative;
      overflow: hidden;
    }
    
    .gallery-item img {
      width: 100%;
      height: auto;
      transition: transform 0.3s;
    }
    
    .gallery-item:hover img {
      transform: scale(1.1);
    }
  </style>
</head>
<body>
  
  <div class="gallery">
    <!-- JavaScript loop to generate gallery items -->
    <script>
      
	var imagePaths = [
	"./assets/nancy/nancy.JPG",


	];
      var galleryContainer = document.querySelector(".gallery");
      
      imagePaths.forEach(function(path) {
        var galleryItem = document.createElement("div");
        galleryItem.className = "gallery-item";
        
        var image = document.createElement("img");
        image.src = path;
        image.alt = "Artsy Photo";
        
        galleryItem.appendChild(image);
        galleryContainer.appendChild(galleryItem);
      });
    </script>
  </div>
</body>
{% endraw %}

