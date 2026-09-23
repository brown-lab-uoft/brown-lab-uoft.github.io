---
title: "About"
layout: gridlay
permalink: /about/
description: "Joseph S. Brown is an Assistant Professor at the Leslie Dan Faculty of Pharmacy, University of Toronto, and Faculty Advisor to the Medicinal Chemistry Self-Driving Lab (MedChem SDL). Education, grants, awards, and mentoring."
---

## About

<div class="section-card">
<div class="pi-card">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ site.photo }}" class="pi-photo" alt="{{ site.pi_name }}" loading="lazy">
<div>
<h3 class="pi-name">{{ site.pi_name }}</h3>
<p style="font-style: italic; color: var(--text-secondary);">{{ site.title }}, {{ site.institution }}</p>
<div class="pi-links">
{% if site.email %}<a href="mailto:{{ site.email }}" class="icon-link" title="Email"><i class="fa-solid fa-envelope"></i></a>{% endif %}
{% if site.links.cv and site.links.cv != "" %}<a href="{{ site.url }}{{ site.baseurl }}/{{ site.links.cv }}" class="icon-link" title="CV"><i class="ai ai-cv"></i></a>{% endif %}
{% if site.links.google_scholar and site.links.google_scholar != "" %}<a href="{{ site.links.google_scholar }}" class="icon-link" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>{% endif %}
{% if site.links.github and site.links.github != "" %}<a href="{{ site.links.github }}" class="icon-link" title="GitHub"><i class="fa-brands fa-github"></i></a>{% endif %}
{% if site.links.researchgate and site.links.researchgate != "" %}<a href="{{ site.links.researchgate }}" class="icon-link" title="ResearchGate"><i class="ai ai-researchgate"></i></a>{% endif %}
</div>
{% if site.data.pi[0].education %}
<ul style="margin-top: var(--space-4);">
{% for education in site.data.pi[0].education %}
<li>{{ education | replace: "-","&#8211;" }}</li>
{% endfor %}
</ul>
{% endif %}
</div>
</div>
</div>

<div class="section-card">
Joseph S. Brown is an Assistant Professor at the Leslie Dan Faculty of Pharmacy and Faculty Advisor to the Medicinal Chemistry Self-Driving Lab (MedChem SDL) at the University of Toronto.
Before his faculty appointment, he was a PhRMA Foundation Drug Discovery Postdoctoral Fellow at MIT with Bradley Pentelute, specializing in combining machine learning with AS-MS to identify high-affinity ligands from diverse peptide and abiotic libraries.
He earned his PhD in Chemical and Biomolecular Engineering from Cornell University with Christopher Alabi as a National Science Foundation Graduate Research Fellow.
</div>

{% if site.data.grants %}
<div class="section-card">
<h3>Grants</h3>
<ul>
{% for grant in site.data.grants %}
<li>{{ grant.name }}</li>
{% endfor %}
</ul>
</div>
{% endif %}

{% if site.data.awards %}
<div class="section-card">
<h3>Awards</h3>
<ul>
{% for award in site.data.awards %}
<li>{{ award.name | replace: "-","&#8211;" }}</li>
{% endfor %}
</ul>
</div>
{% endif %}

{% if site.data.people %}
<div class="section-card">
<h3>Students and Mentoring</h3>
{% for group in site.data.people %}
<h5 style="margin: var(--space-4) 0 var(--space-2); color: var(--text-secondary);">{{ group.group }}</h5>
<ul>
{% for member in group.members %}
<li>
  {{ member.name }}{% if member.pub %}<sup>†</sup>{% endif %}{% if member.time %} ({{ member.time }}){% endif %}{% if member.role %} — {{ member.role }}{% endif %}{% if member.current %}; now {{ member.current }}{% endif %}
</li>
{% endfor %}
</ul>
{% endfor %}
<p style="font-size: 0.85em; color: var(--text-secondary); margin-top: var(--space-4);">† Co-authored publication with this mentee.</p>
</div>
{% endif %}

{% if site.data.funders %}
<div class="section-card">
<h4>Sponsors and Collaborators</h4>
<div class="sponsor-logos" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: var(--space-6);">
{% for funder in site.data.funders %}
<a href="{{ funder.url }}" target="_blank"><img src="{{ site.url }}{{ site.baseurl }}/images/{{ funder.image }}" alt="Funder logo" style="max-height: 80px; max-width: 200px; border-radius: 0;" loading="lazy"></a>
{% endfor %}
</div>
</div>
{% endif %}
