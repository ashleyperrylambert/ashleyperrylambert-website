# Ashley Perry Lambert Website (Final Draft)

> Option A (black bodysuit), updated with Ashley's September 21 notes.

Built to the master build specification and the approved Direction One mockup.
Static site: plain HTML, one stylesheet, no build step required to run it.

## Pages

    index.html              Home (13 sections, in spec order)
    about.html              About Ashley
    method.html             The Reinvention Method
    coaching.html           Coaching
    speaking.html           Speaking
    podcast.html            Fat Loss Reinvention
    resources.html          Resources / Start Here
    faq.html                FAQ (12 questions)
    quiz.html               Free quiz landing page
    work-with-ashley.html   Three pathways
    speaking-inquiry.html   Speaking inquiry form
    coaching-inquiry.html   Coaching inquiry form

    css/style.css           All styling. Tokens at the top.
    images/                 Ashley's photos, optimized
    _build/build.py         Content source + page generator (optional)

## Preview

Double-click `index.html`. Every link works locally.

## Brand tokens

Top of `css/style.css`:

    --navy:#14243F;    --pink:#E8246E;    --apricot:#FF9E4A;
    --petal:#FDE8F1;   --cream:#FBF9F6;   --ink:#1E2636;   --gray:#6A7180;

Fonts are Playfair Display (all headings, brand name, pull quotes) and
Poppins (body, nav, buttons, labels, forms), loaded from Google Fonts.

## Editing copy

Two options.

**Directly.** Open the `.html` file and edit the text. Nothing is compiled.

**Centrally.** All copy lives in `_build/build.py`. Edit there and run:

    cd _build && python3 build.py

That regenerates all eleven pages. `METHOD_NAME` is a single constant at the top,
so renaming The Reinvention Method updates every page at once.

## Publish free on GitHub Pages

1. github.com, sign in, **New repository**. Name it `ashleyperrylambert`, Public, Create.
2. Click **uploading an existing file**. Drag in everything here, including the
   `css` and `images` folders. Commit.
3. **Settings > Pages**. Source: Deploy from a branch, branch `main`, folder `/ (root)`. Save.
4. About a minute later it is live at `https://<username>.github.io/ashleyperrylambert/`.

### Custom domain

**Settings > Pages > Custom domain**, enter `ashleyperrylambert.com`, then at the
registrar add:

    A     @    185.199.108.153
    A     @    185.199.109.153
    A     @    185.199.110.153
    A     @    185.199.111.153
    CNAME www  <username>.github.io

Tick **Enforce HTTPS** once it appears.

### Transferring to Ashley

**Settings > General > Transfer ownership**, enter her GitHub username.

## Making the forms send

GitHub Pages is static, so forms cannot email on their own. Easiest fix is Formspree:
create a free form, then change

    <form class="form" onsubmit="return false;">

to

    <form class="form" action="https://formspree.io/f/YOURFORMID" method="POST">

Every input already has a `name` attribute, so nothing else is needed. Do this on
`speaking-inquiry.html` and `coaching-inquiry.html`, and point the email signup on
`resources.html` at her email platform.

## Built from Ashley's brand foundation document

The following came straight out of Rebranding With Jennifer Jones and is live on the site:

- Positioning as Transformation Coach, not only a fitness coach
- Mission and framework: Renew Your Mind. Transform Your Body. Redefine Your Life.
- Brand statement: Fitness is one doorway. The body is one piece. But the woman is the work.
- Core message: Your body should support your life. Your life should not revolve around your body.
- Real story: dance from age three, Nala in The Lion King on Broadway, physique competition,
  two decades of strength training, 60 pounds lost after her first son
- Faith stance written as she described it: foundational, not positioned as a Christian business
- All five real coaching offers with real pricing
- The "not sure which option" decision helper
- The free quiz and the 5-Day Reinvention Reset
- The BUILD Framework and The Flat Stomach Reset on Resources
- Two new FAQs covering pricing and where to start

Note: Ashley's document says **Redefine** Your Life throughout. The build spec said
Redesign. The site uses Redefine, her word.

## Still to fill in

- Podcast: episode titles, descriptions, artwork, and real Apple/Spotify links
- Resources: download links for the BUILD Framework and The Flat Stomach Reset
- Instagram and YouTube URLs in the footer
- Privacy Policy, Terms, and Disclaimer pages
- Podcast cover art (currently a styled navy placeholder)

## The quiz link

`QUIZ_URL` in `_build/build.py` points at https://www.ashleyperrylambert.com/quiz1
It is linked from the nav, the homepage, Resources, Work With Ashley, the FAQ CTA,
and its own landing page at `quiz.html`.

## Notes on assets

`images/hero-cutout.png` is `IMG_4869.jpeg` with the background removed so Ashley
sits directly on the Ink Navy hero, matching the approved mockup. Her bodysuit has
been recolored from tan to black; fabric seams and folds are preserved. A `.webp` version
is included and is roughly eight times smaller if you want to swap it in.

Testimonials are rebuilt as HTML cards from the Golden Era graphic, per spec. No
client headshots are used; add them only where written permission exists.
