---
title: "Pizza Quality Control with Amazon Rekognition Custom Labels"
excerpt: "I rebuilt an AWS computer-vision case study end to end to find out what the marketing page leaves out. F1 of 0.971 — and the honest reasons that number doesn't mean what it looks like.<br/><img src='/images/pizza-evaluation.png'>"
collection: portfolio
---

*M.S. Information Technology (Machine Learning focus), Florida State University — data analytics coursework, Fall 2021.*
*Full write-up and console screenshots: [github.com/amymcmullin/pizza-quality-control-aws-rekognition](https://github.com/amymcmullin/pizza-quality-control-aws-rekognition)*

<video controls preload="metadata" poster="/images/pizza-walkthrough-poster.jpg" style="width:100%;max-width:760px;height:auto;border-radius:6px;">
  <source src="/files/case-study-walkthrough.mp4" type="video/mp4">
  Your browser can't play embedded video — <a href="/files/case-study-walkthrough.mp4">download the walkthrough (MP4, 48 seconds)</a>.
</video>

*A 48-second silent walkthrough of the build, cut from the original presentation slides and AWS console screenshots. The video was produced with AI assistance; the project, the screenshots and the analysis it summarizes are mine.*

## The project

The assignment was to pick a technology and teach the class how it works. Rather than read a feature list aloud, I took a published AWS customer case study and rebuilt the machine learning pipeline it described — in my own AWS account, with my own data, start to finish.

[Maestro's Pizza](https://aws.amazon.com/solutions/case-studies/maestro-pizza-case-study/), a chain in Saudi Arabia, had put cameras in every branch to monitor pizza quality. Reviewing that footage took **13 full-time employees more than 10 hours a day**, filling out checklists by hand. They had bought a data problem to solve a quality problem.

I rebuilt the classification half of their solution with Amazon Rekognition Custom Labels: images to S3, a five-label model trained on 24 images (`Good`, `Bad`, `Pepperoni`, `Supreme`, `White`), evaluation, and deployment via the Rekognition API.

![Evaluation results: F1 0.971, average precision 0.950, overall recall 1.000](/images/pizza-evaluation.png)

**Results:** F1 0.971 · average precision 0.950 · overall recall 1.000 · trained in 0.992 hours.

## Why that number doesn't mean what it looks like

The most useful part of this project was not getting a good score. It was working out why the score was not trustworthy:

- **The test set is seven images.** One misclassification moves F1 by about a tenth. This is a smoke test, not a generalization estimate.
- **The training data is out of domain.** My images came from web search — studio lighting, centered framing. Maestro's come from a fixed camera over a prep counter, with glare, hands, and occlusion. Domain mismatch is the most likely reason a project like this fails in production, and my rebuild has it in full.
- **"Bad" was never operationally defined.** I labeled by instinct. A production system needs a written rubric and a measure of agreement between raters *before* labeling starts.
- **Cost is billed by inference hour, not by call** — so the architecture decision that actually matters for the budget is batch versus always-on, and nothing in the ML workflow surfaces that for you.

## What I took from it

AWS's claim — that machine learning is now accessible without deep ML training — mostly holds. I deployed a working image classifier without writing a training loop. What AutoML does not remove is the judgment: defining labels, sourcing representative data, deciding which errors are expensive, and recognizing when a metric is flattering you.

Those are the parts I now spend the most time teaching. This project became the template for how I introduce applied machine learning at Immokalee Technical College: start from a real business problem, build the smallest working version, then interrogate your own results until you find where they break. It's part of the curriculum behind iTECH's [AI Innovation Lab](/talks/itech-ai-innovation-lab.html).
