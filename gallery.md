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
<img src="./assets/paintings/Chacho.JPG" />
<div class=gallery-item>
<img src="./assets/paintings/Chacho.JPG" />
</div>
{% endraw %}

![IMGIMG](https://github.com/nancytravers/nancytravers.github.io/blob/main/assets/nancy/nancy.JPG)

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/paintings'" %}

{% for painting in paintings %}
	![img]({{ site.baseurl }}{{ painting.path }})
{% endfor %}


{% for painting in sit.static_files %}
 {% if painting.path contains '/assets/paintings/' %}
  ![image]({{ painting.path }} 'image')
	<p> {{ painting.path }} </p>
 {% endif %}
{% endfor %}

