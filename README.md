---
layout: home
title: Nancy Travers Art
nav_exclude: true
permalink: /:path/
seo:
  type: Course
  name: Just the Class
---

# Nancy Travers Art
{% raw %}
<style>
.banner {
  text-align: center;
}

.banner img {
  width: 100%;
  max-height: 300px; 
}
</style>


{% endraw %}

{% assign banners = site.static_files | where_exp: "file", "file.path contains '/assets/images/banner'" %}

{% for banner in banners %}
  <div class="banner">
    <img src="{{ banner.path | relative_url }}" alt="{{ banner.name }}">
  </div>
{% endfor %}
Nancy Travers, a renowned Oregon painter, has left an indelible mark on the artistic landscape with her captivating works. With a passion for ceramics and watercolors, Nancy dedicated an impressive 25 years of her career teaching these art forms at Clackamas Community College. Her expertise lies in both thrown work and hand building techniques, showcasing her versatility and deep understanding of her craft.

Drawing inspiration from her extensive travels across Europe and Mexico, Nancy's artwork reflects the vibrant cultures and breathtaking landscapes she has encountered. Her explorations in these regions, often supplemented by sabbatical leaves dedicated to immersive study in Mexico, have greatly influenced her artistic style and vision.

Nancy's paintings encompass a wide range of subjects, with a focus on people, landscapes, and the beauty of nature. Working primarily with watercolor and acrylic, she skillfully captures the essence and spirit of her subjects, creating captivating portraits that evoke a sense of emotion and connection.

Throughout her artistic journey, Nancy Travers continues to inspire and engage viewers with her masterful use of color, composition, and technique. Her dedication to her craft and her ability to convey the intricacies of life through her art make her a revered figure in the Oregon art community and beyond.

{% assign paintings = site.static_files | where_exp: "file", "file.path contains '/assets/nancy'" %}

{% for painting in paintings %}
  <div class="gallery-item">
    <img src="{{ painting.path | relative_url }}" alt="{{ painting.name }}">
  </div>
{% endfor %}
