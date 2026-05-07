---
title: "News"
layout: gridlay
sitemap: false
permalink: /news/
---

## News

<div class="section-card" markdown="0">
{% for article in site.data.news %}
<div style="display: flex; gap: 1.25rem; padding: 1.25rem 0; border-bottom: 1px solid var(--border-color); align-items: flex-start;">
  {% if article.image %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ article.image }}" alt="{{ article.headline }}" loading="lazy"
    style="width: 120px; height: 90px; object-fit: cover; border-radius: 6px; flex-shrink: 0;">
  {% endif %}
  <div style="flex: 1; min-width: 0;">
    <div class="news-date" style="margin-bottom: 0.25rem;">{{ article.date }}</div>
    <div class="news-headline" style="margin-bottom: 0.4rem;">
      {% if article.link %}<a href="{{ article.link }}" target="_blank">{{ article.headline }}</a>{% else %}{{ article.headline }}{% endif %}
    </div>
    {% if article.description %}
    <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem; line-height: 1.55;">{{ article.description }}</p>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>
