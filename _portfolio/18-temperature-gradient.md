---
permalink: /portfolio/temperature-gradient/
redirect_from:
  - /portfolio/14-temperature-gradient/
  - /portfolio/15-temperature-gradient/
title: "PHP Temperature Gradient"
excerpt: "A first-semester PHP exercise with a deceptively interesting bonus: map 101 temperature rows onto a smooth blue-to-red color gradient. Still running on FSU's servers.<br/><img src='/images/temperature-gradient.png'>"
collection: portfolio
---

*LIS 5367 Advanced Web Applications, M.S. Information Technology, Florida State University — Summer 2021*

**[See it running →](https://torch.cci.fsu.edu/~ajm20dp/LIS5367/McSuperBonus.php)**

## The exercise

Build a Fahrenheit-to-Celsius conversion table in PHP. At least 100 rows, Celsius accurate to a tenth, and at least three named temperature bands — the instructor left the band names and thresholds to us. Three sub-problems: arithmetic in PHP, a finite incrementing loop, and selecting a description based on a numeric range.

Then two optional extensions, offered for nothing but bragging rights:

- **Bonus** — color each description by its band. Hot red, cold blue.
- **Super bonus** — give *every line* its own color, slightly different from the ones above and below, producing a smooth gradient from deep blue at the cold end to bright red at the hot end.

## Why the super bonus is the interesting one

The base exercise is a loop and a conditional. The super bonus is a different kind of problem: it needs a continuous mapping from one range onto another.

The bands are discrete — a row is COLD or NICE or HOT, nothing in between. But the gradient has to be continuous across all 101 rows, which means per-row color can't come from the band at all. You have to interpolate: normalize each temperature to a position between 0 and 1 across the full range, then interpolate the red and blue channels across that position and emit the result as a hex value, every row, inside the same loop that's already doing the conversion and the band lookup.

So one pass through the loop produces three things computed three different ways — an arithmetic conversion, a discrete lookup, and a continuous interpolation. For a first semester of PHP that's a genuinely good exercise, and I remember it being the first time the language stopped feeling like filling in a template.

I set my bands at COLD below 65°F, NICE from 65 through 85, and HOT at 86 and above.

![The super bonus submission: a 101-row conversion table shading from blue through to red](/images/temperature-gradient.png)

## Submissions

All three are still live on FSU's Torch server, five years on:

- [Super bonus](https://torch.cci.fsu.edu/~ajm20dp/LIS5367/McSuperBonus.php) — the full per-row gradient, and the one worth looking at
- [Bonus](https://torch.cci.fsu.edu/~ajm20dp/LIS5367/McBonus.php)
- [Simple](https://torch.cci.fsu.edu/~ajm20dp/LIS5367/McTemp.php)

A caveat on the last two: they currently render the table structure and the band labels but not the numeric values. I no longer have access to the account, so I can't read the source to say whether those two were always incomplete or whether something broke under a later PHP version. The super bonus submission still renders correctly, which is the one I'd have spent the most time on.

The larger project from this course was the [iTech Differentiated OCP Tracker](/portfolio/itech-ocp-tracker/).
