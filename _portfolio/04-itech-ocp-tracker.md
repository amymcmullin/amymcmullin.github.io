---
permalink: /portfolio/itech-ocp-tracker/
redirect_from:
  - /portfolio/03-itech-ocp-tracker/
title: "iTech Differentiated OCP Tracker"
excerpt: "A PHP/MySQL application mapping student skill mastery to Florida DOE curriculum frameworks — and a security review of my own 2021 code, written five years later as a cybersecurity instructor.<br/><img src='/images/ocp-tracker-progress.png'>"
collection: portfolio
---

*LIS 5367, M.S. Information Technology, Florida State University — Summer 2021.*
*Code, screenshots and full write-up: [github.com/amymcmullin/itech-ocp-tracker](https://github.com/amymcmullin/itech-ocp-tracker)*

## The problem

Florida's career certificate programs are built around **Occupational Completion Points**. A student earns an industry credential by demonstrating mastery of a defined list of standards — not by accumulating seat time. The program I teach, Y100200 (Computer Systems & Information Technology), has four OCPs, 50 standards and 245 skills beneath them.

Tracking that on paper is miserable. A student halfway through has demonstrated some standards through coursework and others by doing live work around the building, with no clear view of what remains.

## What I built

A PHP/MySQL web application over an 11-table normalized schema that does three things:

1. Shows a student their own progress — which standards they've mastered, at what level, and what's left.
2. Lets an instructor record skills **observed during work-based activities**, not just graded assignments. A student who struggles with a written test can demonstrate the same standard by installing a workstation, and it counts.
3. Keeps assignments mapped to framework standards, so coursework and credential requirements stay connected.

![Student progress report showing mastered standards with level descriptions](/images/ocp-tracker-progress.png)

Mastery is recorded at four levels, from *can identify and recall* through *can apply in a real-world scenario*, so progress reads as a gradient rather than pass/fail.

I started it on a local Ubuntu LAMP VM, then migrated it to AWS — web server and PHP onto an EC2 instance, the database onto Amazon RDS — to decouple the application from its data. HTML, PHP, SQL and Git were all new to me at the time; I came from the infrastructure side.

## The part I find more interesting now

I teach applied cybersecurity. Reading my own code back five years later is a useful exercise, so the repository includes an honest audit rather than a cleanup.

My original write-up already listed hardening as future work — input validation, SQL sanitization, access control, OAuth2 from Canvas. I even noted in the demo instructions that a real implementation wouldn't let anonymous users look up student records. The gaps were visible to me then; I just couldn't close them yet.

What I'd flag now, specifically: **SQL injection in every query** (user input interpolated straight into query strings), **live database credentials committed to the repository**, **no authentication or authorization of any kind** on records covered by FERPA, **stored XSS** in the observation notes, and **random integers used as primary keys** with no uniqueness check.

None of that is unusual for a first web application. Publishing it unedited is the point — the distance between "it works" and "it's safe to put in front of real students" is exactly what I spend my time teaching now.

## A note on the data

The original database held real student records — names from an actual cohort paired with skill-mastery data and observation notes. That dump is not published. The repository ships a de-identified seed with invented names, regenerated IDs and rewritten notes, with foreign keys remapped so the application behaves identically against it.
