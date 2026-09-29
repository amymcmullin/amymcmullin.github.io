---
layout: archive
title: "Certifications & Achievements"
permalink: /certifications/
author_profile: true
redirect_from:
  - /badges/
  - /credentials/
---

{% include base_path %}
{% assign credly = site.data.credly %}
{% assign active = credly.badges | where: "status", "active" %}
{% assign expired = credly.badges | where: "status", "expired" %}
{% assign issuers = credly.badges | group_by: "issuer" %}

<style>
  .cred-stats { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0 2rem; }
  .cred-stat { flex: 1 1 8rem; border: 1px solid #e3e6ea; border-radius: 8px; padding: .8rem 1rem; }
  .cred-stat b { display: block; font-size: 1.6rem; line-height: 1.2; }
  .cred-stat span { font-size: .8rem; color: #6b7280; }
  .badge-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr)); gap: 1rem; margin: .5rem 0 2rem; padding: 0; list-style: none; }
  .badge-grid li { margin: 0; }
  .badge-card { display: flex; flex-direction: column; align-items: center; text-align: center; height: 100%; padding: .8rem .6rem; border: 1px solid #e3e6ea; border-radius: 8px; text-decoration: none !important; color: inherit !important; transition: box-shadow .15s, transform .15s; }
  .badge-card:hover { box-shadow: 0 4px 14px rgba(0,0,0,.08); transform: translateY(-2px); }
  .badge-card img { width: 96px; height: 96px; object-fit: contain; margin-bottom: .5rem; }
  .badge-card .n { font-size: .78rem; font-weight: 600; line-height: 1.3; }
  .badge-card .d { font-size: .7rem; color: #6b7280; margin-top: .3rem; }
  .badge-card.is-expired img { filter: grayscale(1); opacity: .7; }
  .cred-issuer { font-size: 1rem; margin: 1.5rem 0 .3rem; }
  .cred-issuer small { color: #6b7280; font-weight: normal; }
  details.cred-more summary { cursor: pointer; font-weight: 600; margin: 1rem 0; }
</style>

A running record of the industry certifications, digital badges and recognition I've earned over 25 years in IT and 13+ years in the classroom. Every badge below is issued and verified through Credly. Select a badge to see its verification page.

<div class="cred-stats">
  <div class="cred-stat"><b>{{ credly.badges | size }}</b><span>Credly badges</span></div>
  <div class="cred-stat"><b>{{ issuers | size }}</b><span>Issuing organizations</span></div>
  <div class="cred-stat"><b>2025–26</b><span>Outstanding Post-Secondary Teacher of the Year</span></div>
</div>

Achievements & recognition
======
* **2026 Outstanding Post-Secondary Teacher of the Year**, Collier County Public Schools (SY 2025–2026)
* **2025 NCWIT Southwest Florida Affiliate Educator Award**, Honorable Mention (SY 2024–2025)
* **2024 iTECH Golden Apple Teacher of Distinction**, Champions for Learning (SY 2023–2024)
* **Credly Top Legacy Badge Earner**, Credly/Pearson (2024)
* **Rated Highly Effective**, Florida teacher evaluation, every year from 2014 through 2025
* **Florida Best and Brightest Teacher Scholarship**, Florida DOE (four consecutive years, 2014–2018)
* Selected for the first two cohorts of Collier County Public Schools' **Innovative Teacher Leaders** program
* **ISTE+ASCD Certified Instructional Leader**

Highlighted certifications
======
* **Cybersecurity:** CompTIA SecurityX (CASP+), CompTIA CySA+, Cisco CCST Cybersecurity, and CompTIA Security Analytics Expert (CSAE)
* **Networking & infrastructure:** CompTIA Network+, Cisco CCST Networking, CompTIA Server+, and CompTIA Network Infrastructure Professional (CNIP)
* **Cloud:** CompTIA Cloud+, AWS Certified Cloud Practitioner, and Microsoft Azure, Azure Data and Microsoft 365 Fundamentals
* **Artificial intelligence:** AWS Certified AI Practitioner, Microsoft Azure AI Fundamentals, Pearson IT Specialist – Artificial Intelligence, and Certiport Generative AI Foundations
* **Teaching:** Microsoft Certified Trainer (MCT), Microsoft Certified Educator (MCE), AWS Academy Certified Educator, and Cisco NetAcad Instructor (5 years of service)

Verified badges
======
{% for group in issuers %}
  {% assign group_active = group.items | where: "status", "active" %}
  {% if group_active.size > 0 %}
<h3 class="cred-issuer">{{ group.name }} <small>· {{ group_active.size }}</small></h3>
<ul class="badge-grid">
  {% for b in group_active %}
  <li><a class="badge-card" href="{{ b.url }}" target="_blank" rel="noopener" title="{{ b.name | escape }}">
    <img src="{{ b.image }}" alt="{{ b.name | escape }} badge" loading="lazy">
    <span class="n">{{ b.name }}</span>
    <span class="d">{{ b.issued | date: "%b %Y" }}</span>
  </a></li>
  {% endfor %}
</ul>
  {% endif %}
{% endfor %}

{% if expired.size > 0 %}
<details class="cred-more">
  <summary>Earlier credentials ({{ expired.size }})</summary>
  <p>Credentials that have reached their renewal date. They are still verifiable on Credly.</p>
  <ul class="badge-grid">
  {% for b in expired %}
    <li><a class="badge-card is-expired" href="{{ b.url }}" target="_blank" rel="noopener" title="{{ b.name | escape }}">
      <img src="{{ b.image }}" alt="{{ b.name | escape }} badge" loading="lazy">
      <span class="n">{{ b.name }}</span>
      <span class="d">{{ b.issued | date: "%Y" }}–{{ b.expires | date: "%Y" }}</span>
    </a></li>
  {% endfor %}
  </ul>
</details>
{% endif %}

Retired certifications
======
Credentials from programs the vendor has since retired, which aren't on Credly.

* **Microsoft Technology Associate (MTA): Introduction to Programming Using HTML and CSS.** Covers basic HTML and CSS design and programming. [View the certificate (PDF)](/files/MTAHTMLCSS.pdf)

<p style="font-size:.8rem;color:#6b7280;margin-top:2rem">Badge list last synced from <a href="{{ credly.profile }}">Credly</a> on {{ credly.updated | date: "%B %-d, %Y" }}. It refreshes automatically every week.</p>
