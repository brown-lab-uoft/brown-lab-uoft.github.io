---
title: "Home"
layout: homelay
permalink: /
description: "The Brown Lab at the University of Toronto builds a self-driving laboratory for peptide drug discovery, combining affinity-selection mass spectrometry (AS-MS), automated peptide synthesis, and active learning to design antimicrobial peptides against drug-resistant infections."
---

<div class="hero-banner" markdown="0">
<img src="{{ site.url }}{{ site.baseurl }}/images/banner/colorful-test-tubes.jpg" alt="Peptide library, ready for screening" class="hero-banner-img">
<div class="hero-scrim"></div>
<div class="hero-text">
<h1 class="hero-title">Brown Lab</h1>
<p class="hero-subtitle">at Leslie Dan Faculty of Pharmacy<br>University of Toronto</p>
</div>
</div>

<div class="chip-container" markdown="0">
<a href="{{ site.url }}{{ site.baseurl }}/research" class="chip">Peptide Drug Discovery</a>
<a href="{{ site.url }}{{ site.baseurl }}/research" class="chip">Self-Driving Laboratories</a>
<a href="{{ site.url }}{{ site.baseurl }}/research" class="chip">Active Learning</a>
<a href="{{ site.url }}{{ site.baseurl }}/research" class="chip">Affinity-Selection MS</a>
<a href="{{ site.url }}{{ site.baseurl }}/research" class="chip">Automated Chemistry</a>
<a href="{{ site.url }}{{ site.baseurl }}/research" class="chip">Antimicrobial Resistance</a>
</div>

## About Us

Peptides sit between small molecules and proteins in size and complexity.
With the right chemistry — cyclization, non-natural amino acids, methylation — they can match the potency and selectivity of antibodies while keeping the drug-like properties of small molecules.
Peptides are no longer a niche modality: Blockbusters like Ozempic anchor a $72-billion-and-growing market, peptides now account for more than 8% of FDA approvals, and roughly 13% of Americans have tried one.
Yet navigating the effectively infinite chemical space of non-natural peptides remains a fundamental challenge.

We are building a **self-driving laboratory (SDL) for peptide drug discovery** — an AI-directed loop where each round of wet-lab experiments generates data that improves the next round of model-driven design.
We rely on direct-to-biology methods, particularly **affinity-selection mass spectrometry (AS-MS)**, to evaluate molecules without purification and feed results immediately back to the models that design the next experiment.

Read more about the [research areas]({{ site.url }}{{ site.baseurl }}/research/) that make this possible, meet the [team]({{ site.url }}{{ site.baseurl }}/team/) behind it, or learn about the [PI]({{ site.url }}{{ site.baseurl }}/about/).

## The Lab

<div class="group-photo-section" markdown="0">
<div class="banner-frame">
<img src="{{ site.url }}{{ site.baseurl }}/images/group/group-photo-main.jpg" alt="The Brown Lab group photo, Summer 2026">
<div class="banner-caption">The Brown Lab, Summer 2026</div>
</div>
</div>

## Contact Us

<div class="contact-letterhead" markdown="0">
<img src="{{ site.url }}{{ site.baseurl }}/images/logo_large.png" alt="Brown Lab logo" class="contact-logo">
</div>

<div class="contact-grid" markdown="0">
<div class="contact-details">
<img src="{{ site.url }}{{ site.baseurl }}/images/contact/jb-contact.jpg" alt="" class="contact-photo" loading="lazy">
<address>
{{ site.address.building }}<br>
{{ site.address.street }}<br>
{{ site.address.city }}, {{ site.address.region }} {{ site.address.postal_code }}<br>
{{ site.address.country }}
</address>
<p><a href="mailto:{{ site.email }}"><i class="fa-solid fa-envelope"></i> {{ site.email }}</a></p>
</div>
{% assign map_address = site.address.building | append: ", " | append: site.address.street | append: ", " | append: site.address.city | append: ", " | append: site.address.region | append: " " | append: site.address.postal_code %}
<div class="contact-map">
<iframe src="https://www.google.com/maps?q={{ map_address | uri_escape }}&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map to {{ site.address.building }}"></iframe>
</div>
</div>

{% if site.data.funders %}
## Sponsors and Collaborators

<div class="sponsor-logos" markdown="0">
{% for funder in site.data.funders %}
<a href="{{ funder.url }}" target="_blank"><img src="{{ site.url }}{{ site.baseurl }}/images/{{ funder.image }}" alt="Funder logo" class="sponsor-logo" loading="lazy"></a>
{% endfor %}
</div>
{% endif %}
