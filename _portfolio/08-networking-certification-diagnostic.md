---
permalink: /portfolio/networking-certification-diagnostic/
title: "Networking Certification Diagnostic"
excerpt: "One practice test that tells a networking student whether they're closest to passing Cisco's CCST Networking, IT Specialist: Networking, or IT Specialist: Network Security, with the class's own practice-test results shaping where the questions lean.<br/><img src='/images/networking-diagnostic-report.png'>"
collection: portfolio
---

*[Take the diagnostic »](https://amymcmullin.github.io/AI-Certification-Diagnostic/networking/) · [Source on GitHub](https://github.com/amymcmullin/AI-Certification-Diagnostic) · [Scoring method and weights](https://github.com/amymcmullin/AI-Certification-Diagnostic/blob/main/docs/SCORING.md)*

## The problem

My networking students can sit three entry-level certifications: **Cisco Certified Support Technician (CCST) Networking**, **IT Specialist: Networking**, and **IT Specialist: Network Security**. The first two overlap heavily, with the same models, addressing and troubleshooting, but the Cisco exam expects show commands and device work, and the ITS exam goes deeper on protocols, DNS and WAN technology. The third is a different exam altogether: firewalls, permissions, encryption and malware.

A student who is strong on subnetting but has never read `show ip interface brief` output is in a different place than one who knows Windows security cold but can't name the OSI layers. One practice test for one exam doesn't show that.

## What I built

A 50-question diagnostic on the same engine as my [AI Certification Diagnostic](/portfolio/ai-certification-diagnostic/). I mapped the three exams' published objectives onto twelve shared topics, and gave each topic a weight for each exam. One sitting produces a readiness score for every exam, a recommended exam, and a study plan ordered by how many points each weak topic is worth on that exam.

![Score report recommending CCST Networking, with readiness for all three exams and a study plan](/images/networking-diagnostic-report.png)

None of the three vendors publishes domain percentages, so the weights are estimates. They come from the breadth of each exam's objectives and from how the GMetrix practice-test banks spread their questions across those objectives.

## Letting my class's results decide where the questions lean

My students had already taken GMetrix practice tests for two of these exams: 138 questions on IT Specialist: Networking (up to 16 students) and 145 on CCST Networking (up to 25). Their pass rates by objective showed a clear pattern:

- **IT Specialist: Networking:** the OSI model (39%), the TCP/IP model (44%), switching processes (44%), WAN technologies (45%) and IPv4 (47%) were among the weakest objectives.
- **CCST Networking:** Diagnosing Problems was the weakest domain (52%), and reading Cisco show-command output was the weakest objective in it (47%).

So the diagnostic leans toward those areas: five questions each on the network models, addressing, and switching and routing, and a separate topic for Cisco device management and show commands. Those are the places a student's readiness is most likely to be decided.

## For the teacher

Students turn in a short results code. Pasting a class's codes, or a Canvas quiz export, into the Teacher view shows each student's recommended exam and the two topics they should study first.

![Teacher view with a class of example students](/images/networking-diagnostic-teacher.png)
*The Teacher view, filled with built-in example data.*

As with the AI diagnostic, the engine and documentation are open source. The question bank lives in a private repository, and the published test keeps its answer keys encoded, so students can't read them from the page source. Graded attempts go through the Canvas version.

## What's next

Cloud is the next overlapping set. After that comes a version for single exams with many domains, like CompTIA A+ and Tech+, where the question becomes which domains are holding a student back.

*Built with AI assistance against my specification. The choice of exams, using my class's GMetrix results to decide where the questions lean, and the decisions about format and keeping the bank private are mine. The questions, explanations, weights draft, software and this write-up were produced with AI assistance from the vendors' published objectives.*

<small>Not affiliated with or endorsed by Cisco, Pearson, or Certiport. Exam names are trademarks of their owners.</small>
