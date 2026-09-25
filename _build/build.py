# -*- coding: utf-8 -*-
"""
Ashley Perry Lambert: site generator.

All copy lives in CONTENT below. Edit here, run `python3 build.py`, and every
page is regenerated. METHOD_NAME is a single global constant per spec item 20.9.
"""
import os

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ----------------------------------------------------------------- constants
METHOD_NAME = "The Reinvention Method"
BRAND = "Ashley Perry Lambert"
TITLE_LINE = "Transformation Coach &bull; Speaker &bull; Podcast Host"
TAGLINE = "Reinvent What Strong Looks Like."
EMAIL = "hello@ashleyperrylambert.com"

# ======== FILL THESE IN, then every page updates ========
INSTAGRAM_URL = "https://www.instagram.com/ashleyperrylambert/"
TIKTOK_URL    = "https://www.tiktok.com/@ashleyperrylambert"
YOUTUBE_URL   = "https://www.youtube.com/@AshleyPerryLambert"
PODCAST_APPLE_URL   = "https://podcasts.apple.com/us/podcast/fat-loss-reinvention-lose-weight-build-muscle-strength/id1865337221"
PODCAST_SPOTIFY_URL = "#"
COLLECTIVE_SIGNUP_URL = "https://go.ashleyperrylambert.com/collective"
FORMSPREE_ID = "YOUR_FORM_ID"   # from formspree.io, looks like xyzabcde
# =========================================================
FORM_ACTION = "https://formspree.io/f/%s" % FORMSPREE_ID
COACHING_FORM_ACTION = "https://formspree.io/f/xyezjopn"
SPEAKING_FORM_ACTION = COACHING_FORM_ACTION  # same inbox; distinct _subject field
SITE_URL = "https://ashleyperrylambert.com"
OG_IMAGE = SITE_URL + "/images/og-image.jpg"
QUIZ_URL = "https://go.ashleyperrylambert.com/quiz"
QUIZ_NAME = "What&rsquo;s Keeping You From Feeling Like Yourself Again?"
FRAMEWORK = "Renew Your Mind. Transform Your Body. Redefine Your Life."
BRAND_STATEMENT = "Fitness is one doorway. The body is one piece. But the woman is the work."

NAV = [
    ("about.html", "About"),
    ("method.html", "Method"),
    ("coaching.html", "Coaching"),
    ("speaking.html", "Speaking"),
    ("podcast.html", "Podcast"),
    ("resources.html", "Resources"),
    ("quiz.html", "Free Quiz"),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?'
         'family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&'
         'family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">')

TESTIMONIALS = [
    ("Ashley really opens your eyes in a way that helps you see inside first. I felt for the "
     "first time the freedom to find the new version of me and stop trying to find the old "
     "version. I also learned how to be confident and own my choices in a way that didn&rsquo;t "
     "make me feel shame.", "Ashley Valerius", "Coaching client"),
    ("This program opened my eyes to the importance of protein in my diet, drinking lots of "
     "water, and having balanced physical, mental, spiritual and emotional awareness and "
     "actions as keys to overall health success.", "Shawnda Tablert", "Coaching client"),
    ("This program gave me my confidence back. After having a baby and nursing I struggled with "
     "losing weight. Nothing I tried seemed to work. Ashley&rsquo;s program helped me learn "
     "sustainable ways to eat and workout. I began prioritizing myself and learned how to work "
     "on my goals while at the same time still being a mom and wife.", "Stacia Brown", "Coaching client"),
    ("I lost 20 of the 30 pounds I gained and that extra 10 pounds is pure muscle. I am much stronger and "
     "physically capable than I&rsquo;ve ever been! Ashley also spent time with me to figure a nutrition plan "
     "that helped boost my results! Ashley is fantastic! She is the best part and wonderful to work with. "
     "She listens to your needs and gives great techniques that you can take with you.", "Shani W.", "Coaching client"),
]

FAQS = [
    ("Is Ashley only a fitness coach?",
     "No. Ashley is a Transformation Coach. Fitness is one important part of her work, and she approaches transformation from the inside out, helping women with mindset, identity, health, habits, strength, and the way they show up in their lives."),
    ("Who does Ashley work with?",
     "Ashley primarily works with women 30 to 45, many of them mothers, who are already trying to care for themselves but feel stuck, disconnected, or unsure of who they are in this season."),
    ("I&rsquo;m not sure which kind of support I need. Where should I start?",
     "Take the free quiz, What&rsquo;s Keeping You From Feeling Like Yourself Again? It points you toward where your transformation needs to begin, so you can choose your next step with clarity."),
    ("What is 16-Week Transformation Coaching?",
     "Ashley&rsquo;s signature, high-touch experience. It includes personalized fitness programming and a personalized nutrition strategy alongside whole-woman transformation work on mindset, identity, habits, confidence, and purpose. Fitness and nutrition are always part of it. What changes from woman to woman is the plan, intensity, strategy, and goals. The investment is $3,000, paid in full or in four monthly payments of $750."),
    ("What is Reinvented Collective?",
     "Ashley&rsquo;s ongoing fitness and nutrition membership, launching October 1, 2026. It includes structured workouts through the APL Wellness app, personalized macros and nutrition guidance, monthly group coaching calls, accountability, and ongoing support. Founding members pay $49 a month through December 31, 2026 and keep that price as long as they do not cancel. Beginning January 2027, membership is $59 a month, or $490 for twelve months with a complimentary private 60-Minute Fitness Roadmap Call valued at $200."),
    ("Will I receive a workout and nutrition plan?",
     "Yes. Both 16-Week Transformation Coaching and Reinvented Collective include fitness and nutrition support. Transformation Coaching includes a fully personalized plan."),
    ("Do I have to be a Christian to work with Ashley?",
     "No. Ashley&rsquo;s faith shapes who she is and how she lives, and women from every background are welcome in her coaching and resources."),
    ("Is coaching therapy?",
     "No. Ashley provides coaching, education, strategy, accountability, and wellness support. Coaching does not replace therapy, medical care, mental-health treatment, or other licensed professional services."),
    ("Is %s a weight-loss program?" % METHOD_NAME,
     "No. Physical transformation may be part of the process, but the method is designed around whole-woman transformation rather than a number on the scale."),
    ("Can Ashley speak at corporate events?",
     "Yes. Ashley is available for select corporate wellness programs, workshops, conferences, panels, and events."),
    ("Does Ashley speak at churches or women&rsquo;s ministry events?",
     "Yes. Faith-centered events allow Ashley to speak more explicitly about faith, identity, purpose, and spiritual transformation."),
    ("Can I book Ashley for a podcast or media appearance?",
     "Yes. Use the speaking inquiry form and select Podcast/Media."),
]

FAQ_PREVIEW = [0, 2, 3, 4, 6]


# ----------------------------------------------------------------- components
def header(active):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' class="active"' if h == active else "", t)
        for h, t in NAV)
    return """<header class="site-header" id="siteHeader">
  <div class="header-inner">
    <a class="brand" href="index.html">%s</a>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav">%s<a class="btn btn-pink" href="work-with-ashley.html">Work With Ashley</a></nav>
  </div>
</header>""" % (BRAND, links)


def footer():
    nav = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in NAV)
    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <span class="brand">%s</span>
        <div class="title">%s</div>
        <div class="tag">%s</div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>%s<li><a href="work-with-ashley.html">Work With Ashley</a></li><li><a href="faq.html">FAQ</a></li></ul>
      </div>
      <div>
        <h4>Connect</h4>
        <ul>
          <li><a href="%s" target="_blank" rel="noopener">Instagram</a></li>
          <li><a href="{{APPLE_FOOT}}" target="_blank" rel="noopener">Reinvented Podcast</a></li>
          <li><a href="%s" target="_blank" rel="noopener">TikTok</a></li>
          <li><a href="%s" target="_blank" rel="noopener">YouTube</a></li>
          <li><a href="mailto:%s">%s</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 %s. All rights reserved.</span>
      <span>Transformation Coach &bull; Speaker &bull; Podcast Host</span>
    </div>
  </div>
</footer>""" % (BRAND, TITLE_LINE, TAGLINE, nav, INSTAGRAM_URL, TIKTOK_URL, YOUTUBE_URL, EMAIL, EMAIL, BRAND)


SCRIPT = """<script>
(function(){
  var t=document.getElementById('navToggle'),n=document.getElementById('nav'),h=document.getElementById('siteHeader');
  if(t){t.addEventListener('click',function(){
    var open=n.classList.toggle('open');
    t.setAttribute('aria-expanded',open?'true':'false');
    t.setAttribute('aria-label',open?'Close menu':'Open menu');
  });}
  if(h){window.addEventListener('scroll',function(){h.classList.toggle('stuck',window.scrollY>8);},{passive:true});}
  var sf=document.getElementById('speakingForm');
  if(sf){sf.addEventListener('submit',function(){
    var t=sf.querySelector('[name=type]'), sub=document.getElementById('speakingSubject');
    if(t&&sub){sub.value = /podcast|media/i.test(t.value) ? 'Podcast / Media Request (website)' : 'Speaking Request (website)';}
  });}
  // ---- scroll motion: text rises, photos slide in from their side, grids stagger ----
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce && 'IntersectionObserver' in window){
    var main=document.querySelector('main'); if(!main) return;
    var boxes='.card,.tcard,.path,.topic,.formcard,.faq details,.band4 > div,.method > div,.taggrid';
    var text='h2,h3,h4,p,ul,ol,.eyebrow,.statement,.btn-row,.q,.lede';
    var targets=[];
    main.querySelectorAll(boxes).forEach(function(el){ if(!el.closest('.hero') && !el.parentElement.closest(boxes)) targets.push([el,'up']); });
    main.querySelectorAll(text).forEach(function(el){ if(!el.closest('.hero') && !el.closest(boxes)) targets.push([el,'up']); });
    main.querySelectorAll('img').forEach(function(img){
      if(img.closest('.hero') && img.classList.contains('hero-cutout')) return;
      if(img.closest(boxes)) return;
      if(img.closest('.photobreak')){ targets.push([img,'zoom']); return; }
      var grid=img.parentElement, kids=grid?Array.prototype.filter.call(grid.children,function(c){return c.offsetParent!==null||true;}):[];
      targets.push([img, kids[0]===img ? 'left' : 'right']);
    });
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12,rootMargin:'0px 0px -60px 0px'});
    var seen=new Map();
    targets.forEach(function(t){
      var el=t[0], parent=el.parentElement, n=(seen.get(parent)||0);
      seen.set(parent,n+1);
      el.classList.add('reveal','reveal-'+t[1]);
      el.style.transitionDelay=Math.min(n*90,450)+'ms';
      io.observe(el);
    });
  }
})();
</script>"""


def testimonial_cards(scroll=True):
    cards = "".join(
        '<div class="tcard"><span class="mark">&ldquo;</span><p>%s</p>'
        '<div class="who">%s</div><div class="role">%s</div></div>' % t
        for t in TESTIMONIALS)
    base = "grid2" if len(TESTIMONIALS) % 2 == 0 else "grid3"
    cls = base + (" tscroll" if scroll else "")
    return '<div class="%s">%s</div>' % (cls, cards)


def faq_block(indexes=None):
    items = FAQS if indexes is None else [FAQS[i] for i in indexes]
    return '<div class="faq">%s</div>' % "".join(
        '<details%s><summary>%s</summary><div class="a">%s</div></details>' %
        (' open' if i == 0 else '', q, a) for i, (q, a) in enumerate(items))


def cta_band(h2, body, buttons, bg="bg-petal"):
    btns = "".join('<a class="btn %s" href="%s">%s</a>' % (c, h, t) for t, h, c in buttons)
    return """<section class="ctaband %s">
  <div class="wrap">
    <h2>%s</h2>
    <p class="lede center">%s</p>
    <div class="btn-row">%s</div>
  </div>
</section>""" % (bg, h2, body, btns)


def page(filename, title, description, body, active=None, schema=None, full_title=None):
    body = (body.replace("{{COACHING_FORM_ACTION}}", COACHING_FORM_ACTION)
                .replace("{{SPEAKING_FORM_ACTION}}", SPEAKING_FORM_ACTION)
                .replace("{{FORM_ACTION}}", FORM_ACTION)
                .replace("{{IG}}", INSTAGRAM_URL).replace("{{TT}}", TIKTOK_URL)
                .replace("{{APPLE}}", PODCAST_APPLE_URL).replace("{{SPOTIFY}}", PODCAST_SPOTIFY_URL)
                .replace("{{COLLECTIVE}}", COLLECTIVE_SIGNUP_URL))
    page_title = full_title or ("%s | %s" % (title, BRAND))
    canonical = SITE_URL + "/" + ("" if filename == "index.html" else filename)
    ld = ""
    if schema:
        import json
        ld = '<script type="application/ld+json">%s</script>' % json.dumps(schema, ensure_ascii=False)
    head_meta = """<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta name="robots" content="index, follow">
<meta name="author" content="Ashley Perry Lambert">
<meta name="theme-color" content="#14243F">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ashley Perry Lambert">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ashley Perry Lambert, Transformation Coach, smiling in a coral top">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%s">
<meta name="twitter:description" content="%s">
<meta name="twitter:image" content="%s">
<link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
%s""" % (page_title, description, canonical, page_title, description, canonical, OG_IMAGE,
         page_title, description, OG_IMAGE, ld)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
%s
%s
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
%s
<main id="main" tabindex="-1">
%s
</main>
%s
%s
</body>
</html>""" % (head_meta, FONTS, header(active or filename), body, footer(), SCRIPT)
    html = html.replace("{{APPLE_FOOT}}", PODCAST_APPLE_URL)
    if PODCAST_SPOTIFY_URL == "#":
        html = html.replace('<a class="btn btn-outline" href="#" target="_blank" rel="noopener">Listen on Spotify</a>', '')
    # every link that opens a new tab tells screen reader users so
    import re as _re
    html = _re.sub(r'(<a [^>]*target="_blank"[^>]*>)(.*?)</a>',
                   lambda m: m.group(1) + m.group(2) + '<span class="sr-only"> (opens in a new tab)</span></a>', html)
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)
    print("wrote", filename, len(html) // 1024, "kb")


# ----------------------------------------------------------------- HOME
home = """<section class="hero hero--home">
  <div class="hero-inner">
    <div>
      <div class="eyebrow">Transformation Coach &bull; Speaker &bull; Podcast Host</div>
      <h1>Reinvent What<br><span style="white-space:nowrap"><span class="pink">Strong</span> Looks Like.</span></h1>
      <p>You&rsquo;ve spent years trying to improve yourself, stay disciplined, keep up, and become the version of yourself you think you should be.</p>
      <p>Maybe the focus has been your body. Maybe it has been your confidence, your habits, your identity, or simply trying to feel like yourself again.</p>
      <p>But lasting transformation is not just about changing what people can see.</p>
      <p>Ashley helps women renew their minds, transform their bodies, and redefine their lives so they can become stronger from the inside out.</p>
      <div class="btn-row">
        <a class="btn btn-pink" href="coaching.html">Explore Coaching</a>
        <a class="btn btn-light" href="method.html">Explore the Method</a>
      </div>
    </div>
    <div class="hero-figure">
      <div class="hero-script" aria-hidden="true">Stronger<br>Women<br>Brighter<br>Futures<span class="swash"></span></div>
      <img class="hero-cutout" src="images/hero-cutout.png" alt="Ashley Perry Lambert in a black bodysuit, smiling and flexing both arms">
      <div class="hero-mark" aria-hidden="true">Real<br>Women<br>Stronger<span class="dash"></span><br>Lives</div>
    </div>
  </div>
</section>

<section class="section short bg-white">
  <div class="wrap">
    <div class="band4">
      <div><h3>Feel like yourself again</h3><p>Stop trying to recover an old version of you and understand who you are becoming.</p></div>
      <div><h3>Trust yourself again</h3><p>Build the confidence to make decisions without constantly second-guessing yourself.</p></div>
      <div><h3>Build a body that supports your life</h3><p>Pursue strength, health, and physical goals without making your body your identity.</p></div>
      <div><h3>Make room for what is next</h3><p>Create a life that reflects your priorities, your values, and the woman you are becoming.</p></div>
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="split wide-left">
      <div>
        <div class="eyebrow">When doing more isn&rsquo;t working</div>
        <h2>You&rsquo;re doing all the things. So why don&rsquo;t you feel like yourself?</h2>
        <p style="margin-top:26px">You are capable. Responsible. Used to handling a lot.</p>
        <p>You take care of the people you love. You show up. You work. You exercise. You try to eat well.</p>
        <p>You keep telling yourself you should be more disciplined, more grateful, more consistent, more together.</p>
        <p>And yet something still feels off.</p>
        <p>Your body has changed. Your life has changed. Motherhood has changed you. The things that used to work do not always fit the woman you are now.</p>
        <p>And somewhere along the way, your confidence, identity, appearance, expectations, and sense of self became tangled together.</p>
        <p>You do not need another plan for fixing yourself.</p>
        <p>You need the space and tools to understand what is actually keeping you stuck.</p>
        <p class="pull">Stop searching outward for what has to change inward.</p>
      </div>
      <img src="images/portrait-coral-close.jpg" alt="Ashley smiling with her chin resting on her hand, wearing a coral top, seated in front of red brick steps">
    </div>
  </div>
</section>

<section class="section bg-petal">
  <div class="wrap">
    <div class="eyebrow">A different approach</div>
    <h2>%(METHOD)s</h2>
    <p class="lede" style="margin-top:22px">%(METHOD)s is Ashley&rsquo;s whole-person approach to transformation. It recognizes that lasting change doesn&rsquo;t happen by focusing on your body while ignoring your mind, your identity, your habits, and the life you&rsquo;re actually living.</p>
    <p class="lede" style="margin-top:14px">The work moves from the inside out.</p>
    <div class="method" style="margin-top:62px">
      <div>
        <div class="num">01</div>
        <h3>Renew Your Mind</h3>
        <p>Before we change what you do, we look at what you believe. Because a different body cannot free you from a belief that was never created by your body in the first place.</p>
        <div class="tags">Identity &bull; Mindset &bull; Beliefs &bull; Body Image &bull; Patterns</div>
      </div>
      <div>
        <div class="num">02</div>
        <h3>Transform Your Body</h3>
        <p>Build strength, energy, health, and sustainable habits without asking your body to carry the weight of your identity.</p>
        <div class="tags">Strength &bull; Nutrition &bull; Fitness &bull; Energy &bull; Health</div>
      </div>
      <div>
        <div class="num">03</div>
        <h3>Redefine Your Life</h3>
        <p>Decide how you want to live now that appearance, achievement, expectations, and old versions of you no longer get to make every decision.</p>
        <div class="tags">Motherhood &bull; Career &bull; Leadership &bull; Faith &bull; Purpose</div>
      </div>
    </div>
    <div class="center" style="margin-top:62px">
      <div class="statement">A woman who is strong from the inside out.</div>
      <div class="btn-row" style="justify-content:center"><a class="btn btn-pink" href="method.html">Explore the Method</a></div>
    </div>
  </div>
</section>

<section class="quote-band bg-navy">
  <div class="wrap">
    <div class="q">Your body should support your life.<em>Your life should not revolve around your body.</em></div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap center">
    <div class="eyebrow">Free quiz</div>
    <h2 style="max-width:20ch;margin:0 auto">{{QUIZNAME}}</h2>
    <p class="lede center" style="margin-top:22px">A short quiz for the woman who is doing all the things and still does not feel like herself.</p>
    <p class="lede center" style="margin-top:12px">You do not need another list of things to fix. You need clarity about where to begin.</p>
    <p class="lede center" style="margin-top:12px">Take the quiz to discover which area of your transformation needs your attention first.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn btn-pink" href="{{QUIZURL}}">Take the Quiz</a></div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="split wide-right">
      <img src="images/family-walk.jpg" alt="Ashley walking hand in hand with her husband and two young sons in a bright white studio">
      <div>
        <div class="eyebrow">Meet Ashley</div>
        <h2>I didn&rsquo;t learn reinvention from a textbook. I lived it.</h2>
        <p style="margin-top:26px">I know what it feels like to have your identity connected to performance, appearance, achievement, and the version of yourself everyone else sees.</p>
        <p>I&rsquo;ve been the dancer. The performer. The fitness professional. The entrepreneur. The wife. The mother. The woman whose body changed and whose life changed with it.</p>
        <p>And I learned something along the way: strength is bigger than muscle.</p>
        <p>Real transformation happens when you stop trying to recover an old version of yourself and begin discovering who you are becoming in this season.</p>
        <p>Today, I help women do that work mentally, physically, emotionally, and spiritually.</p>
        <p class="pull">Fitness is one doorway. The body is one piece. But the woman is the work.</p>
        <div class="btn-row"><a class="btn btn-outline" href="about.html">Read Ashley&rsquo;s Story</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="split wide-left">
      <div>
        <div class="eyebrow">Coaching</div>
        <h2>Transformation that goes deeper than the scale.</h2>
        <p style="margin-top:26px">Ashley&rsquo;s coaching combines body transformation with the deeper work required to create sustainable change.</p>
        <ul class="ticks cols2" style="margin-top:28px">
          <li>Strength + fitness strategy</li>
          <li>Nutrition guidance</li>
          <li>Mindset coaching</li>
          <li>Body image + identity work</li>
          <li>Habits</li>
          <li>Accountability</li>
          <li>Whole-person wellness</li>
          <li>Purpose + life integration</li>
        </ul>
        <div class="statement" style="margin-top:38px">You are not just building a different body.<strong>You are building a stronger woman.</strong></div>
        <div class="btn-row"><a class="btn btn-pink" href="coaching.html">Explore Coaching</a></div>
      </div>
      <img src="images/lifestyle-1.jpg" alt="Ashley seated on a cream sofa in front of a white brick wall, wearing black and smiling at the camera">
    </div>
  </div>
</section>

<section class="section bg-navy">
  <div class="wrap">
    <div class="split wide-left">
      <img src="images/portrait-coral-full.jpg" alt="Ashley in a coral bell-sleeve blouse, hand on her hip, smiling outdoors in front of greenery" class="short">
      <div>
        <div class="eyebrow">Bring Ashley to your audience</div>
        <h2>Conversations that challenge women to rethink strength.</h2>
        <p style="margin-top:26px">Ashley Perry Lambert is a transformation coach, speaker, and podcast host who helps women rethink the relationship between their bodies, identity, health, confidence, and purpose.</p>
        <p>Her teaching is practical, honest, encouraging, and rooted in the belief that women were created for more than constantly fixing themselves.</p>
        <div class="btn-row">
          <a class="btn btn-pink" href="speaking.html">Explore Speaking</a>
          <a class="btn btn-light" href="speaking-inquiry.html">Submit an Inquiry</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-petal">
  <div class="wrap">
    <div class="eyebrow">Real women. Real transformation.</div>
    <h2>The change goes deeper than what you see.</h2>
    <p class="lede" style="margin-top:22px;margin-bottom:54px">Ashley&rsquo;s clients often come looking for physical results. What they discover is confidence, awareness, strength, healthier patterns, and a different relationship with themselves.</p>
    %(TESTIMONIALS)s
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="eyebrow">The podcast</div>
    <h2 style="margin-bottom:54px">Reinvented with Ashley Perry Lambert</h2>
    <div class="pod">
      <img class="pod-cover" src="images/podcast-cover.jpg" alt="Podcast cover art: Ashley seated on a cream sofa in a black jumpsuit and coral wedge sandals, beside the title Reinvention With Ashley Perry Lambert and the line For Moms Wanting to Rebuild Strength, Identity, and Confidence After Kids">
      <div>
        <p>Honest conversations about renewing your mind, transforming your body, and redefining your life. For moms 30 to 45 who are tired of believing the next change to their body, schedule, circumstances, or accomplishments will finally make them feel like themselves again.</p>
        <p>As Ashley&rsquo;s brand expands, the podcast will continue becoming a place for conversations about not only transforming the body, but transforming the woman.</p>
        <div class="btn-row"><a class="btn btn-pink" href="{{APPLE}}" target="_blank" rel="noopener">Listen to the Podcast</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <h2>Start Here</h2>
    <p class="lede" style="margin-top:22px;margin-bottom:54px">You do not have to change everything overnight. Start with one resource that helps you understand where you are and what your next step could be.</p>
    <div class="grid4">
      <div class="card"><div class="placeholder">Resource</div><div class="kicker">Fitness</div><h3>Fitness Resource 1</h3><p>Short description of this resource and who it helps.</p><a class="textlink" href="resources.html">Get it</a></div>
      <div class="card"><div class="placeholder">Resource</div><div class="kicker">Fitness</div><h3>Fitness Resource 2</h3><p>Short description of this resource and who it helps.</p><a class="textlink" href="resources.html">Get it</a></div>
      <div class="card"><div class="placeholder">Coming soon</div><div class="kicker">Identity</div><h3>Identity / Reinvention Resource</h3><p>A guide for the woman rebuilding how she sees herself.</p><a class="textlink" href="resources.html">Notify me</a></div>
      <div class="card"><div class="placeholder">Coming soon</div><div class="kicker">Mindset</div><h3>Mindset / Freedom Resource</h3><p>Tools for breaking the cycle of starting over.</p><a class="textlink" href="resources.html">Notify me</a></div>
    </div>
    <div class="btn-row" style="justify-content:center"><a class="btn btn-outline" href="resources.html">View All Resources</a></div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="eyebrow">Questions</div>
    <h2 style="margin-bottom:44px">Before you reach out.</h2>
    %(FAQPREVIEW)s
    <div class="btn-row"><a class="btn btn-outline" href="faq.html">View All FAQs</a></div>
  </div>
</section>

<section class="ctaband bg-pink">
  <div class="wrap">
    <h2>Ready to stop trying to become who you used to be?</h2>
    <p class="lede center" style="color:rgba(255,255,255,.9)">Build strength for the woman you are becoming.</p>
    <div class="btn-row">
      <a class="btn btn-white" href="work-with-ashley.html">Work With Ashley</a>
      <a class="btn btn-light" href="quiz.html">Take the Free Quiz</a>
    </div>
  </div>
</section>""" % {"METHOD": METHOD_NAME, "TESTIMONIALS": testimonial_cards(), "FAQPREVIEW": faq_block(FAQ_PREVIEW)}
home = home.replace("{{QUIZNAME}}", QUIZ_NAME).replace("{{QUIZURL}}", QUIZ_URL)


# ----------------------------------------------------------------- ABOUT
about = """<section class="page-hero bg-cream">
  <div class="inner">
    <div>
      <div class="eyebrow">About Ashley</div>
      <h1>Becoming stronger changed more than my body.</h1>
      <p class="lede">I help women renew their minds, transform their bodies, and redefine their lives. Fitness is part of the transformation, but it is not the entire transformation.</p>
    </div>
    <img src="images/portrait-coral-alt.jpg" alt="Ashley in a coral blouse and gray trousers, smiling over her shoulder on a tree-lined path">
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="split wide-left">
      <div>
    <h2>I was my first client.</h2>
    <p style="margin-top:26px">I started dancing when I was three years old. My body became connected to performance very early. What it could do, how it looked, and how it was perceived were significant parts of my world. I eventually performed professionally and played Nala in The Lion King on Broadway.</p>
    <p>Achievement, performance, appearance, attention, and external validation were familiar territory for me.</p>
    <p>I&rsquo;ve spent almost two decades strength training. I competed in a physique competition and learned what it looks like to take discipline and body control to an extreme. I knew how to change my body. What I didn&rsquo;t understand yet was that changing my body couldn&rsquo;t answer every question I had about myself.</p>
    <p>Then came motherhood, which became one of my greatest reinventions. After my first son I lost around 60 pounds. From the outside, that should have been the victory. I had lost the weight. I had gotten my body back.</p>
    <p>Except I still felt empty.</p>
    <p>Motherhood had changed more than my body. My life changed. My priorities changed. My responsibilities changed. My identity changed. I couldn&rsquo;t simply lose weight and return to the woman I had been before children.</p>
    <p class="pull">I didn&rsquo;t need to get the old Ashley back. I needed to discover who I was becoming.</p>
    <p style="margin-top:26px">Those questions became much bigger than fitness. Who am I when I&rsquo;m not performing? Who am I when nobody is applauding? Who am I if my body changes? Who am I when a season of life requires something different from me?</p>
      </div>
      <img src="images/family-sons.jpg" alt="Ashley kneeling on a red carpet with her arms around her two young sons, all three smiling, in front of a Glendora Music and Arts School backdrop">
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="split wide-right">
      <img src="images/family-park.jpg" alt="Ashley in a black velvet dress walking through a tree-lined park with her husband, holding hands with their toddler son between them">
      <div>
    <div class="eyebrow">What I had to learn</div>
    <h2>You can completely transform your body and still not be free.</h2>
    <p style="margin-top:26px">You can look confident and still need validation. You can be disciplined and still be controlled. You can be physically strong and internally exhausted. You can achieve the thing you thought would finally make you feel whole and discover you&rsquo;re still searching.</p>
    <p>I had to become free from people pleasing, seeking attention, external validation, control, feelings of unworthiness, and an identity that was too deeply connected to my physical body.</p>
    <p>Freedom hasn&rsquo;t meant I stopped caring about fitness, beauty, achievement, or goals. It has meant putting those things in their proper place.</p>
    <p>Every version of me contributed something. Dancer. Broadway performer. Fitness professional. Wife. Mother. Entrepreneur. Coach. Speaker. Reinvention doesn&rsquo;t require rejecting who I used to be. Nothing was wasted. It&rsquo;s all being used differently in this next season.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap" style="max-width:900px">
    <div class="eyebrow">My mission</div>
    <h2 style="font-size:40px">To help women renew their minds, transform their bodies, and redefine their lives so they can become free from the mental, physical, emotional, and spiritual distractions keeping them from boldly stepping into who they were created to be.</h2>
  </div>
</section>

<section class="photobreak">
  <img src="images/squat.jpg" alt="Ashley in a red sports top holding a deep squat outdoors on gravel, mountains in the distance">
  <div class="overlay"><span>Strength is bigger than muscle.</span></div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="eyebrow">What I believe</div>
    <h2 style="margin-bottom:54px">Three things that shape the work.</h2>
    <div class="method">
      <div><div class="num">01</div><h3>Your body deserves care.</h3><p>But it was never meant to become your identity.</p></div>
      <div><div class="num">02</div><h3>Health should create capacity.</h3><p>It should support your life, not consume it.</p></div>
      <div><div class="num">03</div><h3>Transformation starts inside.</h3><p>Lasting change happens when mind, body, identity, and life begin moving in the same direction.</p></div>
    </div>
  </div>
</section>

<section class="section bg-petal">
  <div class="wrap">
    <div class="split wide-right">
      <img src="images/prayer-circle.jpg" alt="Ashley standing with her eyes closed as she prays over a small group of women gathered in a living room, some holding hands">
      <div>
        <h2>Faith is part of my foundation.</h2>
        <p style="margin-top:26px">My relationship with God is foundational to who I am and how I understand identity, purpose, stewardship, freedom, and transformation.</p>
        <p>My work is open to women from all backgrounds. You do not have to share my faith to be welcomed, supported, or served here.</p>
        <p>In faith-centered spaces and events, I speak more directly about God, calling, spiritual wholeness, identity, and freedom.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="split wide-left">
      <div>
    <div class="eyebrow">Official bio</div>
    <h2 style="margin-bottom:26px">Ashley Perry Lambert</h2>
    <p>Ashley Perry Lambert is a Transformation Coach, Speaker, and host of Reinvented with Ashley Perry Lambert. She helps women renew their minds, transform their bodies, and redefine their lives so they can become free from the mental, physical, emotional, and spiritual distractions keeping them from boldly stepping into who they were created to be.</p>
    <p>A lifelong performer, Ashley began dancing at three years old and later performed professionally, including playing Nala in The Lion King on Broadway. After nearly two decades of strength training, a physique competition, entrepreneurship, marriage, motherhood, and her own seasons of reinvention, Ashley learned that changing your body cannot answer every question you have about who you are.</p>
    <p>Today, her work brings together identity, mindset, strength, health, confidence, purpose, and practical transformation. Ashley believes your body should support your life. Your life should not revolve around your body.</p>
    <p>Through coaching, speaking, teaching, and her podcast, Ashley helps women become stronger from the inside out and step more fully into the life they were created to live.</p>
      </div>
      <img src="images/couple.jpg" alt="Ashley and her husband standing close together against a white brick wall, both in workout clothes">
    </div>
  </div>
</section>

%s""" % cta_band("Ready to see yourself differently?",
                 "Start where it makes sense for you.",
                 [("Explore Coaching", "coaching.html", "btn-pink"),
                  ("Explore the Method", "method.html", "btn-outline")], "bg-cream")


# ----------------------------------------------------------------- METHOD
method = """<section class="hero" style="min-height:0">
  <div class="hero-inner" style="grid-template-columns:48% 52%;align-items:center">
    <div>
      <div class="eyebrow">{{METHOD}}</div>
      <h1>Reinvent What<br><span class="pink">Strong</span> Looks Like.</h1>
      <p style="margin-top:24px">Lasting transformation does not come from changing what people can see while ignoring what is happening underneath.</p>
      <p>{{METHOD}} helps women renew the beliefs shaping their lives, build bodies that support the lives they want to live, and redefine what strength looks like in the season they are in.</p>
      <div class="btn-row"><a class="btn btn-pink" href="work-with-ashley.html">Work With Ashley</a></div>
    </div>
    <div class="hero-figure" style="min-height:0">
      <img src="images/jump.jpg" alt="Ashley leaping high in the air mid-stride against a blue sky, braids flying" style="width:100%;height:540px;object-fit:cover;border-radius:12px">
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap" style="max-width:900px">
    <h2>You don&rsquo;t need another version of yourself to chase.</h2>
    <p style="margin-top:26px">You need to understand what has been driving the cycle you keep returning to.</p>
    <p class="pull">{{METHOD}} works from the inside out because lasting change happens when the way you think, care for your body, see yourself, and live your life begin moving in the same direction.</p>
  </div>
</section>

<section class="pillar bg-white">
  <div class="inner">
    <div class="copy">
      <div class="num">01</div>
      <h2>Renew Your Mind</h2>
      <p style="margin-top:22px">Before changing what you do, we look at what you believe.</p>
      <p class="pull" style="font-size:22px;margin-top:10px">A different body cannot free you from a belief that was never created by your body in the first place.</p>
      <p style="margin-top:22px">We identify the thought patterns, expectations, identities, and stories shaping how you see yourself, your body, your worth, and what you believe is possible for your life. Then we begin building something different.</p>
      <ul class="ticks cols2" style="margin-top:26px">
        <li>Identity</li><li>Mindset</li><li>Beliefs</li><li>Body image</li><li>Patterns</li><li>Expectations</li>
      </ul>
    </div>
    <img src="images/lifestyle-2.jpg" alt="Close-up of Ashley laughing, seated on a sofa in a black sleeveless top">
  </div>
</section>

<section class="pillar bg-petal flip">
  <div class="inner">
    <div class="copy">
      <div class="num">02</div>
      <h2>Transform Your Body</h2>
      <p style="margin-top:22px">Your body still matters.</p>
      <p>We build strength, improve your fitness, support your health, and create a nutrition strategy that aligns with your goals and the season of life you are in.</p>
      <p>You can want muscle. You can want fat loss. You can want definition, confidence, energy, strength, or simply to feel better in your body.</p>
      <p>The difference is that your body no longer has to determine how valuable, successful, or worthy you feel.</p>
      <p class="pull" style="font-size:22px">You do not have to stop caring about your body to stop making your body your identity.</p>
      <ul class="ticks cols2" style="margin-top:26px">
        <li>Strength</li><li>Fitness</li><li>Nutrition</li><li>Energy</li><li>Health</li><li>Consistency</li>
      </ul>
    </div>
    <img src="images/studio-laugh.jpg" alt="Ashley laughing in a black bodysuit and pink glitter sneakers, stepping across a yoga mat in a white brick studio">
  </div>
</section>

<section class="pillar bg-white">
  <div class="inner">
    <div class="copy">
      <div class="num">03</div>
      <h2>Redefine Your Life</h2>
      <p style="margin-top:22px">When you stop organizing your life around the thing that once controlled you, new choices become possible.</p>
      <p>We look at how you want to show up in motherhood, relationships, work, leadership, faith, confidence, purpose, and everyday life.</p>
      <p class="pull" style="font-size:22px">The question shifts from, &ldquo;How do I get back to who I was?&rdquo; to, &ldquo;Who am I becoming now?&rdquo;</p>
      <ul class="ticks cols2" style="margin-top:26px">
        <li>Motherhood</li><li>Relationships</li><li>Career</li><li>Leadership</li><li>Faith</li><li>Confidence</li><li>Calling</li><li>Purpose</li>
      </ul>
    </div>
    <img src="images/family-couch.jpg" alt="Ashley sitting on a sofa hugging her young son while her husband holds their other son beside them">
  </div>
</section>

<section class="quote-band bg-pink">
  <div class="wrap">
    <h2 style="font-size:44px;margin-bottom:20px">The goal is not a smaller life in a smaller body.</h2>
    <p class="lede center" style="font-size:24px;color:#fff;max-width:26ch">The goal is freedom. A stronger woman who has the capacity to live fully.</p>
  </div>
</section>

{{CTA}}"""
method = (method
          .replace("{{METHOD}}", METHOD_NAME)
          .replace("{{CTA}}", cta_band(
              "Ready to begin?", "Apply for coaching or read how the coaching works.",
              [("Apply for Coaching", "coaching-inquiry.html", "btn-pink"),
               ("Explore Coaching", "coaching.html", "btn-outline")], "bg-cream")))


# ----------------------------------------------------------------- COACHING
coaching = """<section class="page-hero bg-cream">
  <div class="inner">
    <div>
      <div class="eyebrow">Coaching</div>
      <h1>Choose the support that matches the work you are ready to do.</h1>
      <p class="lede">Two ways to work with Ashley. One for whole-woman transformation. One for ongoing fitness and nutrition support.</p>
      <div class="btn-row">
        <a class="btn btn-pink" href="#transformation">16-Week Transformation Coaching</a>
        <a class="btn btn-outline" href="#collective">Reinvented Collective</a>
      </div>
    </div>
    <img src="images/outdoor-fence.jpg" alt="Ashley in a pink sports top and black leggings, leaning on a white fence along a sunny tree-lined trail">
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="split wide-left">
      <div>
        <div class="eyebrow">Who this is for</div>
        <h2>This may be for you if&hellip;</h2>
        <ul class="ticks" style="margin-top:30px">
          <li>You are doing all the things but still do not feel like yourself.</li>
          <li>You are tired of starting over every time life changes.</li>
          <li>You want physical goals without allowing your body to control your identity.</li>
          <li>You are in a changing season and need clarity about who you are becoming.</li>
          <li>You want greater strength, confidence, consistency, and self-trust.</li>
          <li>You are ready to stop collecting more information and start creating lasting change.</li>
        </ul>
      </div>
      <img src="images/seated-couch.jpg" alt="Ashley seated on the arm of a cream sofa in black wide-leg pants, smiling warmly">
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="eyebrow">What we may work on</div>
    <h2 style="margin-bottom:44px">The full scope of the work.</h2>
    <div class="taggrid">
      <span>Strength</span><span>Fitness Strategy</span><span>Nutrition</span><span>Habits</span><span>Body Image</span>
      <span>Identity</span><span>Mindset</span><span>Confidence</span><span>Consistency</span><span>Life Integration</span>
    </div>
  </div>
</section>

<section class="section bg-white" id="transformation">
  <div class="wrap">
    <div class="card feature">
      <div class="kicker">Signature experience</div>
      <h3 style="font-size:42px">16-Week Transformation Coaching</h3>
      <p style="font-family:var(--serif);font-size:24px;color:var(--navy);margin:12px 0 20px">$3,000 <span style="font-family:var(--sans);font-size:15px;color:var(--gray)">paid in full, or four monthly payments of $750</span></p>
      <p style="font-size:19px;color:var(--ink);font-weight:500">Private coaching for the woman who knows this is about more than changing her body.</p>
      <p>You know how to work hard. You have probably changed yourself before. You have followed plans, set goals, started over, pushed harder, and tried to become the version of yourself you thought would finally feel like enough.</p>
      <p>But something deeper is asking for your attention.</p>
      <p>Over 16 weeks, we work with the whole woman. Your beliefs. Your identity. Your body. Your habits. Your confidence. Your priorities. Your current season. And the life you are building next.</p>
      <div class="statement" style="font-size:30px;margin:28px 0">Renew Your Mind. Transform Your Body.<strong>Redefine Your Life.</strong></div>
      <p>For Transform Your Body, we create an individualized fitness and nutrition strategy based on your goals and desires. That could include fat loss, building muscle, body composition, strength, energy, health, confidence, or other goals.</p>
      <h4 style="margin:26px 0 14px">The offer includes</h4>
      <ul class="ticks cols2">
        <li>Weekly private Transformation Coaching calls</li>
        <li>Personalized fitness programming based on your goals</li>
        <li>Personalized nutrition strategy and guidance</li>
        <li>Support around mindset, identity, habits, confidence, and life transformation</li>
        <li>Practical action steps between sessions</li>
        <li>Accountability and ongoing support throughout the 16 weeks</li>
        <li>A personalized roadmap based on your goals, desires, and current season</li>
      </ul>
      <p class="pull" style="font-size:24px;margin-top:30px">&ldquo;I&rsquo;m ready to stop trying to get the old me back and start becoming who I am now.&rdquo;</p>
      <div class="btn-row"><a class="btn btn-pink" href="coaching-inquiry.html">Apply for Transformation Coaching</a></div>
    </div>
  </div>
</section>

<section class="section bg-petal" id="collective">
  <div class="wrap">
    <div class="card">
      <div class="kicker">Launching October 1, 2026</div>
      <h3 style="font-size:40px">Reinvented Collective</h3>
      <p style="font-size:19px;color:var(--ink);font-weight:500;margin-top:12px">Ongoing fitness and nutrition coaching for women who want to get stronger, make progress, and have a plan without making fitness their entire life.</p>
      <p>You want results. You want to feel strong. You want to look like you work out. And you want to know that the work you are putting in is actually moving you toward your goals.</p>
      <p>Reinvented Collective gives you the structure, guidance, and support to do exactly that without spending your life trying to figure out what workout to do next or whether you are eating the right amount.</p>
      <h4 style="margin:26px 0 14px">The membership includes</h4>
      <ul class="ticks cols2">
        <li>Structured workouts through the APL Wellness app</li>
        <li>Personalized macros and nutrition guidance</li>
        <li>Monthly group coaching calls</li>
        <li>Ongoing support</li>
      </ul>
      <div class="grid3" style="margin:34px 0 8px">
        <div style="border-top:3px solid var(--pink);padding-top:16px">
          <div class="kicker">Founding member</div>
          <div style="font-family:var(--serif);font-weight:700;font-size:34px;color:var(--navy)">$49<span style="font-family:var(--sans);font-size:15px;font-weight:500;color:var(--gray)"> / month</span></div>
          <p style="margin-top:8px">Through December 31, 2026. Join before January and keep $49 a month for as long as you stay.</p>
        </div>
        <div style="border-top:3px solid var(--line);padding-top:16px">
          <div class="kicker" style="color:var(--gray)">Beginning January 2027</div>
          <div style="font-family:var(--serif);font-weight:700;font-size:34px;color:var(--navy)">$59<span style="font-family:var(--sans);font-size:15px;font-weight:500;color:var(--gray)"> / month</span></div>
          <p style="margin-top:8px">Standard membership price.</p>
        </div>
        <div style="border-top:3px solid var(--apricot);padding-top:16px">
          <div class="kicker" style="color:#9A5210">Full year</div>
          <div style="font-family:var(--serif);font-weight:700;font-size:34px;color:var(--navy)">$490<span style="font-family:var(--sans);font-size:15px;font-weight:500;color:var(--gray)"> / 12 months</span></div>
          <p style="margin-top:8px">Includes a complimentary private 60-Minute Fitness Roadmap Call with Ashley, valued at $200.</p>
        </div>
      </div>
      <p style="margin-top:18px">During the Roadmap Call, you and Ashley map out your fitness goals, priorities, training, nutrition, and overall strategy for the next 12 months so you have a clear plan for where you are going.</p>
      <div class="btn-row"><a class="btn btn-pink" href="{{COLLECTIVE}}" target="_blank" rel="noopener">Become a Founding Member</a></div>
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap center">
    <div class="eyebrow">Not sure where to begin?</div>
    <h2>Start with the free quiz.</h2>
    <p class="lede center" style="margin-top:20px">It will point you toward where your transformation needs to begin, so you can choose your next step with clarity instead of guessing.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn btn-pink" href="quiz.html">Take the Free Quiz</a></div>
  </div>
</section>

<section class="section bg-petal">
  <div class="wrap">
    <div class="eyebrow">Real women. Real transformation.</div>
    <h2 style="margin-bottom:54px">What changes when the work goes deeper.</h2>
    %(TESTIMONIALS)s
  </div>
</section>

%(CTA)s""" % {"TESTIMONIALS": testimonial_cards(),
              "CTA": cta_band("Ready to stop starting over?",
                              "Applications are reviewed personally.",
                              [("Apply for Coaching", "coaching-inquiry.html", "btn-pink")], "bg-cream")}


# ----------------------------------------------------------------- SPEAKING
speaking = """<section class="hero" style="min-height:0">
  <div class="hero-inner" style="align-items:center">
    <div>
      <div class="eyebrow">Speaker &bull; Workshops &bull; Events</div>
      <h1>Teaching that challenges women to rethink strength, identity, and what it means to live free.</h1>
      <p style="margin-top:24px">Ashley Perry Lambert is a Transformation Coach, Speaker, and Podcast Host who helps women examine the beliefs shaping how they see themselves, their bodies, their worth, and the lives they believe they are allowed to live.</p>
      <p>Through personal storytelling, practical teaching, and honest conversations, Ashley gives women language for what they have been feeling and tools to begin creating something different.</p>
      <div class="btn-row"><a class="btn btn-pink" href="speaking-inquiry.html">Invite Ashley to Speak</a></div>
    </div>
    <div class="hero-figure" style="min-height:0">
      <img src="images/speaking.jpg" alt="Ashley seated in front of an audience, speaking into a microphone beside a lit fireplace" style="width:100%%;height:520px;object-fit:cover;border-radius:12px">
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="split wide-left">
      
      <div>
        <div class="eyebrow">Why Ashley</div>
        <h2>A message she has lived.</h2>
        <p style="margin-top:26px">Ashley brings the perspective of a lifelong performer, Broadway actress, fitness professional, entrepreneur, wife, mother, coach, and woman who has had to redefine strength through multiple seasons of her own life.</p>
        <p>Her work sits at the intersection of identity, strength, body image, confidence, freedom, motherhood, health, and purpose.</p>
      </div>
      <img src="images/speaking-podium.jpg" alt="Ashley smiling as she speaks into a microphone from a wooden podium on stage, with balloon arches behind her and women seated in the audience">
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="eyebrow">Speaking topics</div>
    <h2 style="margin-bottom:48px">What Ashley speaks on.</h2>
    <div class="topics">
      <div class="topic"><div class="n">01</div><h3>Reinvent What Strong Looks Like</h3><p>Why women need a new definition of strength in changing seasons of life.</p></div>
      <div class="topic"><div class="n">02</div><h3>Strong From the Inside Out</h3><p>What happens when physical transformation and identity transformation work together.</p></div>
      <div class="topic"><div class="n">03</div><h3>Stop Searching Outward</h3><p>Breaking the cycle of chasing external solutions for internal dissatisfaction. What am I actually searching for?</p></div>
      <div class="topic"><div class="n">04</div><h3>Health That Supports Your Life</h3><p>Creating sustainable wellness for women carrying careers, families, leadership, and responsibility.</p></div>
      <div class="topic"><div class="n">05</div><h3>Identity Beyond the Mirror</h3><p>Helping women disconnect their worth from appearance, achievement, and other people&rsquo;s validation.</p></div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="eyebrow">Ideal events</div>
    <h2 style="margin-bottom:44px">Where Ashley fits.</h2>
    <div class="taggrid">
      <span>Corporate Wellness</span><span>Conferences</span><span>Women&rsquo;s Events</span><span>Churches &amp; Ministries</span>
      <span>Retreats</span><span>Workshops</span><span>Panels</span><span>Podcasts &amp; Media</span>
      <span>Leadership Programs</span><span>Employee Resource Groups</span>
    </div>
  </div>
</section>

<section class="quote-band bg-navy">
  <div class="wrap">
    <div class="q">Fitness is one doorway. The body is one piece.<em>But the woman is the work.</em></div>
  </div>
</section>

%s""" % cta_band("Bring Ashley to your audience.",
                 "Tell us about your event and Ashley&rsquo;s team will follow up with next steps.",
                 [("Submit a Speaking Inquiry", "speaking-inquiry.html", "btn-pink")], "bg-petal")


# ----------------------------------------------------------------- PODCAST
podcast = """<section class="page-hero bg-cream">
  <div class="inner">
    <div>
      <div class="eyebrow">The podcast</div>
      <h1>Reinvented with Ashley Perry Lambert</h1>
      <p class="lede">Honest conversations about renewing your mind, transforming your body, and redefining your life.</p>
      <div class="btn-row">
        <a class="btn btn-pink" href="{{APPLE}}" target="_blank" rel="noopener">Listen on Apple Podcasts</a>
        <a class="btn btn-outline" href="{{SPOTIFY}}" target="_blank" rel="noopener">Listen on Spotify</a>
      </div>
    </div>
    <img class="pod-cover" src="images/podcast-cover.jpg" style="max-width:420px;margin-left:auto" alt="Podcast cover art: Ashley seated on a cream sofa in a black jumpsuit and coral wedge sandals, beside the title Reinvention With Ashley Perry Lambert and the line For Moms Wanting to Rebuild Strength, Identity, and Confidence After Kids">
  </div>
</section>

<section class="section bg-white">
  <div class="wrap" style="max-width:900px">
    <p style="font-size:19px">Reinvented with Ashley Perry Lambert is for moms 30 to 45 who are tired of believing the next change to their body, schedule, circumstances, or accomplishments will finally make them feel like themselves again.</p>
    <p>Each week, Ashley brings honest, practical, encouraging conversations about identity, motherhood, confidence, strength, health, body image, mindset, purpose, and the woman you are becoming.</p>
    <p class="pull">Because fitness is one doorway. Your body is one piece. But the woman is the work.</p>
    <p style="margin-top:26px;font-weight:600;color:var(--pink-text);letter-spacing:.08em;text-transform:uppercase;font-size:13px">New episodes every week</p>
  </div>
</section>

<section class="section bg-cream">
  <div class="wrap">
    <div class="card feature" style="align-items:center;text-align:center;padding:56px 40px">
      <div class="eyebrow" style="margin-bottom:14px">Latest episodes</div>
      <h2 style="margin-bottom:14px">New episodes every week.</h2>
      <p class="lede center" style="margin:0 auto 30px">Listen to the latest conversations on Apple Podcasts, and follow the show so every new episode comes straight to you.</p>
      <a class="btn btn-pink" href="{{APPLE}}" target="_blank" rel="noopener">Listen on Apple Podcasts</a>
    </div>
  </div>
</section>

<section class="quote-band bg-petal">
  <div class="wrap">
    <h2 style="font-size:44px;margin-bottom:18px">From the podcast to your life.</h2>
    <p class="lede center" style="max-width:34ch">One conversation can change how you see your body. Another can change how you see yourself.</p>
  </div>
</section>

%s""" % cta_band("Never miss an episode.",
                 "Subscribe wherever you listen, or explore the full archive.",
                 [("Subscribe", PODCAST_APPLE_URL, "btn-pink"), ("Explore All Episodes", PODCAST_APPLE_URL, "btn-outline")], "bg-cream")


quiz = """<section class="page-hero solo bg-cream">
  <div class="inner">
    <div class="eyebrow">Free quiz</div>
    <h1>{{QUIZNAME}}</h1>
    <p class="lede">You&rsquo;re doing all the things. You&rsquo;re working out, eating well, listening to podcasts, setting goals, and trying to be a good mother, wife, friend, and woman. And you still don&rsquo;t feel like yourself.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn btn-pink" href="{{QUIZURL}}">Take the Quiz</a></div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap" style="max-width:900px">
    <h2>You do not need another list of things to fix.</h2>
    <p style="margin-top:26px">You need clarity about where to begin. Take the quiz to discover which area of your transformation needs your attention first.</p>
    <p>In a few minutes it will point you toward one of four starting places.</p>
  </div>
</section>

<section class="section bg-petal">
  <div class="wrap">
    <div class="eyebrow">Where your transformation may need to begin</div>
    <h2 style="margin-bottom:48px">Four possible starting places.</h2>
    <div class="grid2">
      <div class="card"><div class="kicker">01</div><h3>You are disconnected from yourself</h3><p>Your life may look good from the outside. You&rsquo;re capable, responsible, and trying. But somewhere along the way you lost touch with who you are underneath all of the doing.</p></div>
      <div class="card"><div class="kicker">02</div><h3>Your self-trust needs rebuilding</h3><p>You&rsquo;ve started over enough times that you&rsquo;ve stopped believing yourself when you say this time will be different. That is a repairable thing, and it starts smaller than you think.</p></div>
      <div class="card"><div class="kicker">03</div><h3>Your body is asking for more support</h3><p>Sometimes the answer really is physical. Strength, nutrition, recovery, and energy all affect how much of your life you are able to participate in.</p></div>
      <div class="card"><div class="kicker">04</div><h3>Your life needs to make room for you</h3><p>You&rsquo;ve built a life around everyone else&rsquo;s needs and expectations. Redefining it means deciding, on purpose, what this next season is actually going to look like.</p></div>
    </div>
  </div>
</section>

<section class="quote-band bg-navy">
  <div class="wrap">
    <div class="q">Your body should support your life.<em>Your life should not revolve around your body.</em></div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="split wide-left">
      <div>
        <div class="eyebrow">What happens after</div>
        <h2>The 5-Day Reinvention Reset.</h2>
        <p style="margin-top:26px">Once you know where to begin, the quiz leads into a free five-day experience. It is not a fitness challenge. It introduces the whole-woman approach and helps you create movement in five areas:</p>
        <ul class="ticks" style="margin-top:22px">
          <li>Seeing yourself clearly</li>
          <li>Renewing the stories and beliefs keeping you stuck</li>
          <li>Rebuilding self-trust</li>
          <li>Strengthening and supporting your body</li>
          <li>Redesigning something in your everyday life</li>
        </ul>
        <div class="btn-row"><a class="btn btn-pink" href="{{QUIZURL}}">Start With the Quiz</a></div>
      </div>
      <img src="images/family-street.jpg" alt="Ashley and her husband walking down a city sidewalk, each holding one of their sons">
    </div>
  </div>
</section>
"""
quiz = quiz.replace("{{QUIZNAME}}", QUIZ_NAME).replace("{{QUIZURL}}", QUIZ_URL)


# ----------------------------------------------------------------- RESOURCES
resources = """<section class="page-hero solo bg-cream">
  <div class="inner">
    <div class="eyebrow">Resources</div>
    <h1>Start Here</h1>
    <p class="lede">You do not have to change everything overnight. Start with one resource that helps you understand where you are and what your next step could be.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn btn-pink" href="quiz.html">Take the Free Quiz</a></div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="grid2">
      <div class="card feature">
        <div class="kicker">Free quiz</div>
        <h3>{{QUIZNAME}}</h3>
        <p>A short diagnostic for the woman who is doing all the things and still does not feel like herself. It points you toward one of four starting places instead of asking you to change everything at once.</p>
        <a class="btn btn-pink" href="quiz.html" style="align-self:flex-start">Start Here</a>
      </div>
      <div class="card">
        <div class="kicker">Free challenge</div>
        <h3>The 5-Day Reinvention Reset</h3>
        <p>A five-day experience that introduces the whole-woman approach: seeing yourself clearly, renewing the beliefs keeping you stuck, rebuilding self-trust, supporting your body, and redesigning something in your everyday life.</p>
        <a class="btn btn-outline" href="quiz.html" style="align-self:flex-start">Begin With the Quiz</a>
      </div>
      <div class="card">
        <div class="kicker">Fitness framework</div>
        <h3>The BUILD Framework</h3>
        <p><strong>B</strong> &nbsp;Build the muscle signal<br>
           <strong>U</strong> &nbsp;Use nutrition for your season<br>
           <strong>I</strong> &nbsp;Invest in recovery<br>
           <strong>L</strong> &nbsp;Load progressively<br>
           <strong>D</strong> &nbsp;Define what you have built</p>
        <p>Ashley&rsquo;s philosophy that women should build strong, capable bodies rather than spend their lives trying to become smaller. Covered in a six-part podcast series.</p>
        <a class="textlink" href="podcast.html">Listen to the series</a>
      </div>
      <div class="card">
        <div class="kicker">Coming soon</div>
        <h3>The Flat Stomach Reset</h3>
        <p>A practical fitness resource for a very real concern, especially for mothers. A doorway into the larger work through a physical problem you already want help solving.</p>
        <a class="textlink" href="quiz.html">Notify me</a>
      </div>
    </div>
  </div>
</section>

<section class="section bg-petal">
  <div class="wrap center">
    <h2>Get practical tools for becoming stronger from the inside out.</h2>
    <form class="signup" action="{{FORM_ACTION}}" method="POST"><input type="hidden" name="_subject" value="New Email Signup (website)">
      <input type="email" name="email" required autocomplete="email" placeholder="Your email address" aria-label="Your email address">
      <button type="submit">Send it to me</button>
    </form>
  </div>
</section>"""


resources = resources.replace("{{QUIZNAME}}", QUIZ_NAME).replace("{{QUIZURL}}", QUIZ_URL)


# ----------------------------------------------------------------- FAQ
faq = """<section class="page-hero solo bg-cream">
  <div class="inner">
    <div class="eyebrow">FAQ</div>
    <h1>Frequently Asked Questions</h1>
    <p class="lede">If you don&rsquo;t find what you&rsquo;re looking for, reach out and Ashley&rsquo;s team will help.</p>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap" style="max-width:900px">
    %(FAQ)s
  </div>
</section>

%(CTA)s""" % {"FAQ": faq_block(),
              "CTA": cta_band("Not sure where to start?", "The free quiz will point you toward where your transformation needs to begin.",
                              [("Take the Free Quiz", "quiz.html", "btn-pink"),
                               ("Work With Ashley", "work-with-ashley.html", "btn-outline")], "bg-petal")}


# ----------------------------------------------------------------- WORK WITH ASHLEY
work = """<section class="page-hero solo bg-cream">
  <div class="inner">
    <div class="eyebrow">Work With Ashley</div>
    <h1>Let&rsquo;s find the right next step.</h1>
    <p class="lede">Whether you&rsquo;re looking for coaching, a speaker, or simply a place to begin, choose the path that fits what you need right now.</p>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="paths">
      <div class="path">
        <div class="kicker" style="font-family:var(--sans);font-weight:600;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--pink-text);margin-bottom:14px">Coaching</div>
        <h3>Work one to one</h3>
        <p>Build strength and create sustainable change from the inside out.</p>
        <a class="btn btn-pink" href="coaching.html">Explore Coaching</a>
      </div>
      <div class="path">
        <div class="kicker" style="font-family:var(--sans);font-weight:600;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--pink-text);margin-bottom:14px">Speaking</div>
        <h3>Book Ashley</h3>
        <p>Bring Ashley to your conference, company, retreat, church, or women&rsquo;s event.</p>
        <a class="btn btn-outline" href="speaking-inquiry.html">Speaking Inquiry</a>
      </div>
      <div class="path">
        <div class="kicker" style="font-family:var(--sans);font-weight:600;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--pink-text);margin-bottom:14px">Start free</div>
        <h3>Start with a resource</h3>
        <p>Not ready for coaching? Take the free quiz and find out where your transformation needs to begin.</p>
        <a class="btn btn-outline" href="quiz.html">Take the Quiz</a>
      </div>
    </div>
  </div>
</section>"""


# ----------------------------------------------------------------- FORMS
def field(label, fid, kind="text", ph="", options=None, required=False):
    req = ' required' if required else ''
    if options:
        opts = "".join("<option>%s</option>" % o for o in options)
        ctrl = '<select id="%s" name="%s"%s>%s</select>' % (fid, fid, req, opts)
    elif kind == "textarea":
        ctrl = '<textarea id="%s" name="%s" placeholder="%s"%s></textarea>' % (fid, fid, ph, req)
    else:
        ac = {"name": "name", "email": "email", "phone": "tel", "org": "organization", "website": "url"}.get(fid)
        acattr = ' autocomplete="%s"' % ac if ac else ''
        ctrl = '<input id="%s" name="%s" type="%s" placeholder="%s"%s%s>' % (fid, fid, kind, ph, req, acattr)
    return '<div class="field"><label for="%s">%s</label>%s</div>' % (fid, label, ctrl)


speaking_form = """<section class="page-hero solo bg-cream">
  <div class="inner">
    <div class="eyebrow">Speaking inquiry</div>
    <h1>Bring Ashley to Your Audience</h1>
    <p class="lede">Tell us a little about your event and what you&rsquo;re hoping to create. Ashley&rsquo;s team will review your inquiry and follow up with next steps.</p>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap" style="max-width:920px">
    <div class="formcard">
      <form class="form" id="speakingForm" action="{{SPEAKING_FORM_ACTION}}" method="POST"><input type="hidden" name="subject" id="speakingSubject" value="Speaking Request (website)">
        <div class="f2">%s%s</div>
        <div class="f2">%s%s</div>
        <div class="f2">%s%s</div>
        <div class="f2">%s%s</div>
        <div class="f2">%s%s</div>
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        <div><button class="btn btn-pink" type="submit">Submit Speaking Inquiry</button></div>
        <p class="formnote">Thank you for considering Ashley for your event. We&rsquo;ll review the details and follow up soon.</p>
      </form>
    </div>
  </div>
</section>""" % (
    field("Name", "name", required=True), field("Organization", "org"),
    field("Email", "email", "email", required=True), field("Phone", "phone", "tel"),
    field("Website", "website", "url"), field("Event name", "eventname"),
    field("Event date", "eventdate", "date"), field("Event location", "eventloc"),
    field("Virtual or in person", "format", options=["In person", "Virtual", "Either"]),
    field("Estimated audience size", "size"),
    field("Audience description", "audience", ph="Who will be in the room?"),
    field("Type of event", "type", options=["Keynote", "Workshop", "Panel", "Retreat",
                                            "Corporate Wellness", "Church or Ministry",
                                            "Podcast/Media", "Other"]),
    field("Topic you&rsquo;re interested in", "topic",
          options=["Reinvent What Strong Looks Like", "Strong From the Inside Out",
                   "Stop Searching Outward", "Health That Supports Your Life",
                   "Identity Beyond the Mirror", "Not sure yet"]),
    field("Tell us about your event", "details", "textarea"),
    field("What would you like your audience to walk away with?", "outcome", "textarea"),
    field("Speaking budget range", "budget"),
    field("Additional notes", "notes", "textarea"),
)

coaching_form = """<section class="page-hero solo bg-cream">
  <div class="inner">
    <div class="eyebrow">Coaching inquiry</div>
    <h1>Ready to Work With Ashley?</h1>
    <p class="lede">Tell her where you are right now. Applications are reviewed personally.</p>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap" style="max-width:920px">
    <div class="formcard">
      <form class="form" action="{{COACHING_FORM_ACTION}}" method="POST"><input type="hidden" name="subject" value="Coaching Request (website)">
        <div class="f2">%s%s</div>
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        <div><button class="btn btn-pink" type="submit">Submit Coaching Inquiry</button></div>
        <p class="formnote">Ashley reads every application personally and follows up within a few business days.</p>
      </form>
    </div>
  </div>
</section>""" % (
    field("Name", "name", required=True), field("Email", "email", "email", required=True),
    field("Phone", "phone", "tel"),
    field("What are you currently struggling with?", "struggle", "textarea"),
    field("What have you already tried?", "tried", "textarea"),
    field("What would you most like to change in the next 3&ndash;6 months?", "change", "textarea"),
    field("What are you most interested in?", "focus",
          options=["16-Week Transformation Coaching", "Reinvented Collective", "Not sure yet"]),
    field("Why now?", "why", "textarea"),
    field("Preferred contact method", "contact", options=["Email", "Phone", "Text"]),
)


# ----------------------------------------------------------------- write
PERSON = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Ashley Perry Lambert",
    "jobTitle": "Transformation Coach, Speaker, and Podcast Host",
    "description": "Ashley Perry Lambert helps women renew their minds, transform their bodies, and redefine their lives through coaching, speaking, and her podcast.",
    "url": SITE_URL,
    "image": OG_IMAGE,
    "email": "mailto:" + EMAIL,
    "sameAs": [u for u in [INSTAGRAM_URL, TIKTOK_URL, YOUTUBE_URL, PODCAST_APPLE_URL] if u.startswith("http")],
    "knowsAbout": ["Transformation coaching", "Strength training for women", "Nutrition coaching",
                   "Body image", "Identity", "Motherhood", "Women's wellness"],
}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "name": "Ashley Perry Lambert", "url": SITE_URL}
PODCAST_LD = {
    "@context": "https://schema.org", "@type": "PodcastSeries",
    "name": "Reinvented with Ashley Perry Lambert",
    "description": "Honest conversations for moms 30 to 45 about renewing your mind, transforming your body, and redefining your life.",
    "url": SITE_URL + "/podcast.html", "webFeed": PODCAST_APPLE_URL,
    "author": {"@type": "Person", "name": "Ashley Perry Lambert"},
}
COACHING_LD = {
    "@context": "https://schema.org", "@type": "ItemList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "item": {
            "@type": "Service", "name": "16-Week Transformation Coaching",
            "provider": {"@type": "Person", "name": "Ashley Perry Lambert"},
            "description": "Private whole-woman coaching with personalized fitness programming and nutrition strategy.",
            "offers": {"@type": "Offer", "price": "3000", "priceCurrency": "USD"}}},
        {"@type": "ListItem", "position": 2, "item": {
            "@type": "Service", "name": "Reinvented Collective",
            "provider": {"@type": "Person", "name": "Ashley Perry Lambert"},
            "description": "Ongoing fitness and nutrition coaching membership with structured workouts, personalized macros, and monthly group coaching.",
            "offers": {"@type": "Offer", "price": "49", "priceCurrency": "USD"}}},
    ],
}

page("index.html", "", "Ashley Perry Lambert is a Transformation Coach for women. Coaching, strength and nutrition support, speaking, and the Reinvented podcast for moms 30 to 45.",
     home, schema=[PERSON, WEBSITE],
     full_title="Ashley Perry Lambert | Transformation Coach for Women, Speaker and Podcast Host")
page("about.html", "About Ashley", "Former Broadway performer, strength coach, wife, and mother. Ashley Perry Lambert's story of reinvention and the whole-woman work she does today.", about, schema=[PERSON])
page("method.html", METHOD_NAME, "The Reinvention Method: renew your mind, transform your body, and redefine your life. A whole-woman approach to lasting transformation.", method)
page("coaching.html", "Coaching for Women", "16-Week Transformation Coaching and the Reinvented Collective fitness and nutrition membership. Personalized coaching for women and moms 30 to 45.", coaching, schema=[COACHING_LD])
page("speaking.html", "Speaking", "Book Ashley Perry Lambert to speak on strength, identity, body image, and purpose at conferences, corporate wellness events, churches, and retreats.", speaking)
page("podcast.html", "Reinvented Podcast", "Reinvented with Ashley Perry Lambert: honest weekly conversations for moms about mindset, identity, strength, body image, and purpose.", podcast, schema=[PODCAST_LD])
page("resources.html", "Free Resources", "Free resources from Ashley Perry Lambert, including the quiz and the 5-Day Reinvention Reset, to help you take your next step.", resources)
page("quiz.html", "Free Quiz", "What's keeping you from feeling like yourself again? Take Ashley Perry Lambert's free quiz to find where your transformation should begin.", quiz)
page("faq.html", "FAQ", "Answers about Ashley Perry Lambert's coaching, Reinvented Collective, pricing, faith, speaking, and where to start.", faq)
page("work-with-ashley.html", "Work With Ashley", "Coaching, speaking, or a free starting point. Find the right way to work with Ashley Perry Lambert.", work, active="work-with-ashley.html")
page("speaking-inquiry.html", "Speaking Inquiry", "Invite Ashley Perry Lambert to speak at your conference, retreat, church, corporate wellness program, or podcast.", speaking_form, active="speaking.html")
page("coaching-inquiry.html", "Coaching Inquiry", "Apply for 16-Week Transformation Coaching or Reinvented Collective with Ashley Perry Lambert.", coaching_form, active="coaching.html")
print("done")
