---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  # ──────────────────────────────────────────────────────
  # 1. ABOUT THE LAB — top of the page, the "what and why"
  # ────────────────────────────────────────
  - block: markdown
    id: about
    content:
      title: 'About the Brown Lab'
      subtitle: 'Peptide drug discovery at the intersection of automation, mass spectrometry, and machine learning.'
      text: |-
        ### Why peptides?

        Peptides sit between small molecules and proteins in size and complexity. With the right chemistry — cyclization, non-natural amino acids, methylation — they can match the potency and selectivity of antibodies while keeping the drug-like properties of small molecules, including oral bioavailability. Peptides are no longer a niche modality: blockbusters like Ozempic anchor a $72-billion-and-growing market, peptides now account for more than 8% of FDA approvals, and roughly 13% of Americans have tried one.

        ### The challenge

        Peptides are natural substrates for proteases, and their size limits diffusion into cells. Improving potency, permeability, stability, and selectivity means searching a chemical space that is, for practical purposes, infinite. The question driving our lab is how to navigate that space efficiently — how algorithms, automation, and data can together compress the path from initial hit to therapeutic candidate.

        AI-driven ligand discovery is now tractable for proteins (AlphaFold, ESM, BindCraft, RFdiffusion — recognized by the 2024 Nobel Prize) and is showing promise for small molecules (BoltzGen, MolPILE). But existing foundation models are not effective for peptide therapeutics, particularly for the non-natural chemistries that make peptides drug-like. That gap blocks AI-enabled discovery for a clinically validated, commercially successful drug class.

        ### What we build: a peptide self-driving lab

        We are building a self-driving laboratory (SDL) for peptide drug discovery — an AI-directed loop where each round of wet-lab experiments generates data that improves the next round of model-driven design. SDLs have repeatedly surpassed best-in-class designs in materials science, but remain rare in drug discovery. We believe they are uniquely well-suited to the peptide modality.

        In practice, this means automating chemical synthesis, biological testing, and the data flow between them. We rely on direct-to-biology methods — particularly affinity-selection mass spectrometry (AS-MS) — to evaluate molecules without purification and feed results immediately back to the models that design the next experiment.

        ### Impact

        The lab is new, but its foundations are not. Prior contributions from the PI include automation-friendly biological assays, synthetic chemistry for large cyclic-peptide libraries, and bioinformatics tools that increase data throughput. We are now applying active-learning strategies to molecular discovery, demonstrating faster and smarter optimization cycles that shorten the path from hit to drug-like molecule.
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true
  # ──────────────────────────────────────────────
  # 2. PI BIOGRAPHY — moved below the lab description
  # ──────────────────────────────────────────────
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      # button:
      #   text: Download CV
      #   url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: false

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  # ──────────────────────────────────────────────
  # 3. RESEARCH — hidden
  # ──────────────────────────────────────────────
  # - block: markdown
  #   content:
  #     title: 'My Research'
  #     subtitle: ''
  #     text: |-
  #       Use this area to speak to your mission.
  #       I apply a range of qualitative and quantitative methods to comprehensively investigate the role of x in Y.
  #   design:
  #     columns: '1'
  # ──────────────────────────────────────────────
  # 4. FEATURED PUBS
  # ──────────────────────────────────────────────
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
  # ──────────────────────────────────────────────
  # 5. RECENT PUBS
  # ──────────────────────────────────────────────
  # - block: collection
  #   content:
  #     title: Recent Publications
  #     text: ''
  #     filters:
  #       folders:
  #         - publications
  #       exclude_featured: false
  #   design:
  #     view: citation
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - events
  #   design:
  #     view: card
  # ──────────────────────────────────────────────
  # 6. RECENT NEWS
  # ──────────────────────────────────────────────
  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 10
      # Filter on criteria
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: card
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---
