---
title: "Teaching to the Commute: 104 AI-Generated Certification Podcasts"
excerpt: "An audio study library for students with hour-long drives and evening shifts — 104 episodes, ~78 hours, across a dozen certification tracks. The engineering is in the prompt.<br/><img src='/images/itech-csit-podcasts.png'>"
collection: portfolio
---

*Immokalee Technical College · [iTECH CSIT Study Podcasts on Spotify](https://open.spotify.com/show/500DGcPqdkUAzYVfOjsCd2) · Built with Google NotebookLM*

| | |
|---|---|
| **Episodes** | 104 |
| **Average length** | ~45 minutes |
| **Total audio** | ~78 hours |
| **Structure** | A library of separate shows, one per certification track |
| **Tracks covered** | AWS Cloud Practitioner, AWS Machine Learning Specialty, CompTIA Tech+ (Security and Databases domains), Cisco CCST Networking, Cisco IT Support, CCNA Cybersecurity, IC3 Spark, Python ITS, AI Studycasts |
| **Localization** | IC3 Spark published in a Haitian Creole edition |
| **Distribution** | Canvas and in live lecture |
| **AI disclosure** | Stated in the show description |

## The problem

My students are not sitting at a desk with a textbook. They have hour-long commutes. They work evening shifts. Many are English language learners who are new to the United States. Some are sixteen; some are seventy; a good number are veterans. What they share is that reading a 300-page certification guide is not the constraint — *finding the hours to sit still and do it* is.

Audio solves a scheduling problem before it solves a pedagogical one. A forty-five minute drive is forty-five minutes a student already has.

The library is organised as separate shows rather than one feed — AWS Cloud Practitioner, CompTIA Tech+ broken out by domain, Cisco CCST Networking, CCNA Cybersecurity, IC3 Spark, Python, AWS Machine Learning Specialty — so a student preparing for one exam subscribes to that exam, not to everything.

**IC3 Spark is also published in a Haitian Creole edition.** Writing a prompt that avoids idiom for English language learners helps. Producing the material in a student's first language is the stronger version of the same decision, and it is the part of this project I would want to extend to the other tracks.

## The prompt is the work

Generating audio with NotebookLM is a button press. Generating audio that a sixteen-year-old ELL student will voluntarily listen to for forty-five minutes, and come out of it able to answer exam questions, is a design problem. Here is an actual prompt, for the Security domain of the Cisco CCST Networking exam:

```text
Subject: 100-150 CCST Networking domain 6 and related objectives in the
IT Specialist - Networking Exam

6. Security
6.1 Describe how firewalls operate to filter traffic. • Firewalls (blocked
ports and protocols); rules deny or permit access
6.2 Describe foundational security concepts. • Confidentiality, integrity,
and availability (CIA); authentication, authorization, and accounting (AAA);
Multifactor Authentication (MFA); encryption, certificates, and password
complexity; identity stores/databases (Active Directory); threats and
vulnerabilities; spam, phishing, malware, and denial of service
6.3 Configure basic wireless security on a home router (WPAx). • WPA, WPA2,
WPA3; choosing between Personal and Enterprise; wireless security concepts

Create a funny standup-like podcast with fictional stories about each concept
using easy to understand language using examples and analogies. Give real
world examples of how each concept is used. Draw parallels to how they may see
the topic in other exams they may wish to pursue. (In educator speak,
scaffolding) (Part 1 for each concept) Include example questions that one may
find on the subject exam. Explain answers and why they are wrong or right.
provide keywords for the exam, tips and tricks (Part 2 for each concept)

Format:
- tell a memorable funny story (similar to stand-up) illustrating a success or
  failure for the concept. (Part 1 for each concept)
- Explain part 2 for each concept
- Switch host for each standup routine
Feel free to play with the format as you see best.

Audience: students at a rural technical college looking to start a career in IT
(Assume no greater than a sixth grade reading level as some students are
English language learners and new to the united states.) Avoid idioms and
references to a shared US culture. Most students are 16 to 27 although students
can be as old as 70 and we get a fair share of veterans.

They are studying for any or all of the following exams in addition to the
subject: [CompTIA Tech+, A+, Network+, Security+; Cisco System Support
Technician; Oracle Database Foundations; AWS Cloud Practitioner; Azure AZ-900,
MS-900, AI-900, DP-900, PL-900, MB-910, MB-920, SC-900; PMI Project Ready;
Intuit Design for Delight; Certiport Professional Communication and Generative
AI Foundations; Pearson IT Specialist across nine domains] (These are listed
for reference and do not need to be listed in the podcast unless a direct
parallel is being appropriately made.)

Constraint: No outer time limit on how long this podcast should be. It will be
listened to during commutes, and work shifts. It should be long enough to cover
each concept thoroughly. Spend no longer than 2 minutes on the intro including
the science behind the funny stories. But do give a brief mention how this exam
prepares students for the larger CompTIA Exams which is usually students end goal.
```

## What each decision is doing

**Pasting the objectives verbatim.** The prompt opens with the exact published exam objectives, numbered. This grounds generation in the authoritative source rather than the model's impression of what a networking exam covers. It is the difference between content *about* the domain and content *aligned to* it.

**A two-part structure per concept.** Part 1 is the story. Part 2 is exam mechanics — sample questions, why each distractor is wrong, keywords, tips. Entertainment earns the attention; the second half converts it. Separating them means neither one dilutes the other.

**"Avoid idioms and references to a shared US culture."** This is the line I'd point at first. Humour is the most culture-bound thing there is, and a joke built on American sports or a sitcom reference lands as noise for a student who arrived last year. Specifying a sixth-grade reading level is common; ruling out idiom and shared cultural reference is not, and it is the constraint that makes a *comedy* format viable for an ELL audience at all.

**Switching host between routines.** Two voices alternating resets attention across a forty-five minute run.

**Naming the other exams, and saying not to list them.** This is the scaffolding instruction. It gives the model a map of where each concept recurs — CIA triad shows up in Security+, SC-900 and the Pearson Cybersecurity exam — so it can draw genuine cross-exam parallels without turning the episode into a catalogue. Students hear that what they are learning now is not disposable.

**Removing the length limit on purpose.** Nearly all guidance on instructional media says shorter. I said the opposite, because the constraint isn't attention span — it's that the listening block is already fixed at the length of a drive. Content shorter than the commute wastes the commute.

**Capping the intro at two minutes, and including "the science behind the funny stories" inside it.** Students are told why the format is built this way before they get the content. That's a metacognitive move: a student who understands that narrative aids recall listens differently from one who thinks it's just a joke.

The narrative-and-memory premise comes from reading on storytelling and retention — the general claim that narrative structure improves encoding and recall by tying abstract material to concrete, emotionally salient events.

## Quality control

I listen to every episode before it is published, during my own commute — an hour each way. Across 104 episodes that is roughly seventy-eight hours of review, and it is the part of the workflow I would not remove. Generated audio built partly from open-web sources is unverified by default, and this is going to students preparing for exams they pay to sit. Episodes get checked against the published objectives before they go out.

The show description states that the content was AI-generated. Students are told the same thing in lecture.

## Results, honestly

Pass rates rose markedly after the podcasts went into circulation, and student feedback has been positive. I tried several formats early on and converged on the humorous-story structure because it was clearly the one that worked.

That said, what I have is not evidence in the strict sense. There was no control group. Students who choose to listen on their own time are likely more motivated to begin with. I changed other things about the program over the same period. The honest claim is that pass rates improved while this was running and students say it helps — not that 78 hours of audio caused the gain.

## What I'd do next

Tag episodes to objectives so a student can jump to a single weak area rather than a whole domain. Track listens against exam attempts to get past impressions. And find out whether the format holds for the students who *don't* currently choose it — the ones who aren't listening are the ones the format hasn't reached.
