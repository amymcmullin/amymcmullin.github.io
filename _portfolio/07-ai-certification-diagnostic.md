---
permalink: /portfolio/ai-certification-diagnostic/
redirect_from:
  - /portfolio/04-ai-certification-diagnostic/
title: "AI Certification Diagnostic"
excerpt: "One practice test that tells a student which of three overlapping AI certifications they're closest to passing, and what to study first. The answer keys stay private, but the tool is open source.<br/><img src='/images/ai-diagnostic-report.png'>"
collection: portfolio
---

*Open source. [Try the demo »](https://amymcmullin.github.io/AI-Certification-Diagnostic/demo/) · [Source on GitHub](https://github.com/amymcmullin/AI-Certification-Diagnostic) · [Scoring method](https://github.com/amymcmullin/AI-Certification-Diagnostic/blob/main/docs/SCORING.md)*

## The problem

Students in my program can earn three entry-level AI certifications: Certiport's **Generative AI Foundations**, Microsoft's **Azure AI Fundamentals (AI-901)**, and Certiport's **IT Specialist: Artificial Intelligence**. They overlap, but not much. One is mostly about prompting and the responsible use of generative AI. One is mostly Azure services. One is about data preparation, model training, and keeping models running in production.

Students usually pick whichever exam a friend took. A practice test for one exam can't tell them they'd do better on a different one. And on test day, a voucher spent on the wrong exam is wasted.

## What I built

One 45-question diagnostic covering all three exams. I mapped each exam's published objectives onto ten shared topics. Each exam gives each topic a weight, so a single sitting produces a readiness score for every exam.

![Score report showing the recommended exam, readiness for each exam, and a study plan](/images/ai-diagnostic-report.png)

When a student finishes, they see:

- **the exam they're most likely to pass**, and how close the runner-up is;
- **readiness for each exam** against a 75% "likely ready" line;
- **a study plan** for the recommended exam, ordered by how many points each topic is worth on that exam. A weak topic the exam barely tests drops down the list.

"Choose two" questions are scored all-or-nothing, the way the real exams score them. Every question is original, written to the vendors' public objectives. No practice-test items are reused.

## For the teacher

Students turn in a short results code. I paste a whole class's codes, or a Canvas quiz export, into the Teacher view and see every student's recommended exam, what each one should study first, class averages by topic, and the most-missed questions.

![Teacher view with a class of example students](/images/ai-diagnostic-teacher.png)
*The Teacher view, filled with built-in example data.*

The same question bank also builds as a Canvas quiz, so I can give it in the gradebook when I need a graded attempt. Everything runs in the browser. There's no server and no student accounts, and no student data is stored anywhere.

## An open-source test without open answer keys

I wanted other teachers to be able to use the engine, but a public repository full of answer keys would be useless for an actual class. So:

- The **engine and documentation** are public, under the MIT license.
- A **12-question demo set** is public, with its answers visible, under CC BY-NC-SA 4.0.
- The **real question banks** live in a private repository.
- When a real test is published, each **answer key is hashed** and each **explanation is encoded**. Students can't find the answers by viewing the page source.

That doesn't stop a determined student with developer tools, and the documentation says so: any test that scores itself in the browser has that limit. Graded attempts go through Canvas, which scores on its own server.

Teachers also choose how much students see afterward: the full key, right/wrong with explanations, or right/wrong only. That way, answers don't travel from morning to afternoon sections.

## What's next

The engine is built around question packs, so a new subject is new data, not new code. Next up:

- **Networking and cloud**, which have the same overlapping-certification problem.
- **Single exams with many domains, like CompTIA A+ and Tech+**, where the question becomes which domains are holding a student back.

The plan is to compare each student's diagnostic readiness with their real exam result. After a term or two, that will show whether the readiness score predicts passing, and give me real data for tuning the 75% line and the topic weights.

<small>Not affiliated with or endorsed by Pearson, Certiport, or Microsoft. Exam names are trademarks of their owners.</small>
