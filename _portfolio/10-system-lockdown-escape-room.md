---
permalink: /portfolio/system-lockdown-escape-room/
redirect_from:
  - /portfolio/06-system-lockdown-escape-room/
title: "SYSTEM LOCKDOWN: A Print-and-Play Escape Room"
excerpt: "A ransomware incident-response escape room that runs on paper in 45 minutes with no lab, no computers and no prerequisite instruction. Four parallel stations feed one meta-code — and the codes are configurable, because the answer key is public.<br/><img src='/images/system-lockdown-pack.png'>"
collection: portfolio
---

*Immokalee Technical College · Computer Systems & Information Technology (Y100200)*
*Print pack, generator and facilitator guide: [github.com/amymcmullin/educational-escape-rooms](https://github.com/amymcmullin/educational-escape-rooms)*

## The constraint

I needed a week-one activity for a cohort I had not met, in a week with no lab
access, for students who had been taught nothing yet. Most active-learning
material assumes at least one of those three things.

So the design brief was narrow: it has to run entirely on paper, it has to work
cold with zero prerequisite knowledge, and it has to tell me something useful
about the people in the room.

## What it is

A ransomware worm called BLACKOUT has locked a client's server. Students are the
incident response team. The client's only IT tech quit two weeks ago and left
four sealed envelopes and a locked recovery box.

| | |
|---|---|
| **Play time** | 45 minutes, plus ~10 briefing and ~20 debrief |
| **Group size** | Teams of 3–5; runs from 8 to 30 students |
| **Prep** | ~25 minutes of printing and cutting for six teams |
| **Cost** | Free with sealed envelopes; about $40 with combination locks |

Each envelope holds one puzzle producing a four-digit station code:

| Station | Content | Employability skill on display |
|---|---|---|
| A — Parts Requisition | Match function descriptions to component cards; six of ten are decoys | Reading technical documentation for meaning |
| B — Memory Dump | Binary → decimal → ASCII; decodes to a recovery command | Precision, checking your own work |
| C — Network Map | Find the device off the /24, identify the protocol in the traffic log | Comparing data systematically |
| D — Ransom Note | Caesar cipher solved with a cut-out cipher wheel | Following a procedure exactly |
| Final | Third digit of each code, in order | Documentation and handoff |

![Pages from the print pack: network map, cipher wheel discs, and the Recovery Console worksheet](/images/system-lockdown-pack.png)

## The design decisions worth defending

**The stations are parallel, not sequential.** This is the structural choice the
whole activity rests on. Sequential puzzles mean one stuck team is stuck for the
rest of the hour, and in practice one confident student solves everything while
the others watch. Four independent envelopes means everyone is working at once,
a quiet student can own a station, and the only bottleneck is the final code.

**It runs cold, so it doubles as a diagnostic.** Every reference card a student
needs is inside the envelope — binary place values, an ASCII table, a subnet
explainer, a ports table. Nothing is pre-taught. That means I can run it on day
two and spend 45 minutes watching who reads the reference card versus who
guesses, who writes things down unprompted, who checks a teammate's arithmetic,
who takes over and who disappears. That is better information about a new cohort
than any icebreaker produces.

**Documentation is a role, not an afterthought.** One of the five role cards owns
the Recovery Console worksheet, and nothing counts until it is written there. The
debrief asks why. Real incident response is incomplete documentation, time
pressure, and a team you barely know — the activity is shaped like the job.

**Three delivery modes, because budgets differ.** Physical combination locks give
the best experience. Sealed envelopes with the code written on the outside cost
nothing and keep the whole feel. A Google Form using regex response validation
blocks a student from advancing until the code is right, so it behaves like a
lock, works on phones with no lab, and timestamps every team's progress.

**There is an Easter egg.** The master code is also the incident ticket number
printed on the first page students read. Teams almost never notice. Revealing it
at the end of the debrief makes a real point about how much information walks
past an analyst unnoticed.

## The problem with publishing it

Open-sourcing an answer key is self-defeating when your students can find your
GitHub. I hit the same question with the [AI Certification
Diagnostic](/portfolio/ai-certification-diagnostic/) and solved it there by
keeping the keys out of the repository.

That does not work here, because the generator source *is* the answer key —
anyone reading the script sees the component ID digits and the binary values.

So the fix was to make the codes configurable instead. Every station answer is
derived from a config block at the top of the generator: the component ID
mapping, the word hidden in the memory dump, the rogue host octet and port, the
cipher shift word and the ransom note plaintext. Change those, rebuild, and the
puzzles, reference cards and prose all follow — the memory dump table even
resizes if the recovery word is a different length. The build prints the
resulting answer key to the terminal.

The published defaults are the ones in the facilitator guide. Any teacher using
this, including me, regenerates before running it. That is a better outcome than
hiding the key would have been: it makes the pack reusable across cohorts and
genuinely adaptable by other programs.

## Reuse

The shell outlasts the content. Station B can become subnetting practice once
subnetting has been taught, Station C a Wireshark capture excerpt, Station D hash
identification or a password policy audit. What should not change is the
four-parallel-stations-plus-meta structure — that is the part that makes it work.

Everything is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for any
CTE program that wants it.

*Scenario design, content alignment and facilitation decisions are mine. The
print pack generator and the facilitator guide were produced with AI assistance
against that specification.*
