---
title: "Media"
layout: gridlay
sitemap: false
permalink: /media/
---

## Media

<p style="color: var(--text-secondary); margin-bottom: var(--space-6);">Press coverage, outreach, recorded talks, and lab news.</p>

{% if site.posts.size > 0 %}
<div class="section-card" markdown="0">
{% for post in site.posts %}
<div class="news-item" style="padding: 1rem 0; border-bottom: 1px solid var(--border-color);">
<span class="news-date">{{ post.date | date: "%b %-d, %Y" }}</span><br>
<a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" style="font-weight: 600;">{{ post.title }}</a>
{% if post.excerpt %}
<p style="margin: 0.4rem 0 0; color: var(--text-secondary); font-size: 0.9rem;">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
{% endif %}
</div>
{% endfor %}
</div>
{% else %}
<div class="section-card">
<p class="text-muted">No media posts yet. Add posts to the <code>_posts/</code> directory to populate this page.</p>
</div>
{% endif %}
