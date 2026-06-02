#!/usr/bin/env python3
"""Static site generator for Mount Cable India.

One of India's largest Finolex distributors + multi-brand electrical dealer,
Bengaluru. Focus: individual home builders. 35 years in business.

Generates: home, per-brand pages, product-category pages, Bengaluru area
(local-SEO) pages, a photo-upload quote page, robots.txt and sitemap.xml.

Run:  python3 build.py
"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://mountcable.com"

PHONE = "+91 88676 76700"
PHONE_HREF = "+918867676700"
EMAIL = "mountcable@gmail.com"
WHATSAPP = "918867676700"
YEARS = "35"

OFFICES = [
    {"tag": "Showroom 1", "area": "Jayanagar", "addr": "Jayanagar, Bengaluru, Karnataka 560011"},
    {"tag": "Showroom 2", "area": "Chickpete", "addr": "Chickpete, Bengaluru, Karnataka 560053"},
]

# Which brands have a downloaded logo file (others fall back to a wordmark)
LOGO = {
    "finolex": "finolex.svg", "polycab": "polycab.png", "kei": "kei.png",
    "rr-kabel": "rr-kabel.svg", "v-guard": "v-guard.jpg", "greatwhite": "greatwhite.png",
    "legrand": "legrand.png", "hpl": "hpl.png", "anchor-panasonic": "anchor-panasonic.png",
}

CATEGORIES = [
    ("switches-and-sockets", "🔌", "Switches & Sockets",
     "Modular switches, plates, sockets and wiring accessories from Anchor by Panasonic, Schneider, Legrand, Greatwhite, HPL & more.",
     ["anchor-panasonic", "schneider", "legrand", "greatwhite", "hpl"],
     ["Modular Switches", "Plates & Frames", "Sockets & Plug-tops", "USB & Smart Switches", "Bell & Fan Regulators"], ""),
    ("wires-and-cables", "⚡", "Wires & Cables",
     "House wiring, power, control and flexible cables from Finolex, Polycab, KEI, RR Kabel, V-Guard and Univyin — every gauge for your home.",
     ["finolex", "polycab", "kei", "rr-kabel", "v-guard", "univyin-cables"],
     ["FR / FR-LSH House Wires", "Multi-core Flexible Cables", "Power & Control Cables", "Co-Axial Cables", "Telephone & LAN Cables"], "banner-finolex-fr.jpg"),
    ("pipes-and-conduits", "🧰", "Pipes & Conduits",
     "PVC electrical conduits, casing-capping, pipes, bends and fittings from Precision Pipes, Finolex and Polycab for clean, safe cable runs.",
     ["precision-pipes", "finolex", "polycab"],
     ["PVC Electrical Conduits", "Casing & Capping", "Bends, Couplers & Fittings", "Junction Boxes", "Flexible Conduits"], ""),
    ("lighting", "💡", "Lighting",
     "LED bulbs, panels, battens, downlights and decorative lighting from Finolex, Polycab, V-Guard, HPL and Greatwhite.",
     ["finolex", "polycab", "v-guard", "hpl", "greatwhite"],
     ["LED Bulbs & Battens", "Panel & Down Lights", "Flood & Street Lights", "Decorative Lighting", "Smart Lighting"], "banner-finolex-led.jpg"),
    ("switchgear-and-mcb", "🛡️", "Switchgear & MCBs",
     "MCBs, RCCBs, isolators, distribution boards plus 3M tapes, connectors and cable accessories for safe circuit protection.",
     ["schneider", "legrand", "hpl", "3m"],
     ["MCBs & Isolators", "RCCBs & RCBOs", "Distribution Boards", "Changeover Switches", "3M Tapes & Connectors"], ""),
]

# slug, name, color, featured(bool), tagline, products[], blurb
BRANDS = [
    ("finolex", "Finolex", "#0054A6", True,
     "Our flagship — 100% original Finolex wires & cables, every range always in stock.",
     ["Finolex 90M Silver", "Finolex 90M Gold", "Finolex 90M FRLS", "Finolex 180M", "Finolex 300M", "Finolex 300M FRLS", "Finolex Ultra", "Co-Axial Cables", "Telephone Cables", "Internet / LAN Cables"],
     "Finolex is India's most trusted name in house wiring. Mount Cable India is one of the largest distributors of Finolex cables in India — and our surety is that we sell only 100% original Finolex wires. Every range — 90M Silver, 90M Gold, 90M FRLS, 180M, 300M, 300M FRLS, Finolex Ultra, plus co-axial, telephone and internet cables — is in stock and always available. Confirm your order and we deliver to your site within 3 hours, and collect payment right at your site."),
    ("polycab", "Polycab", "#E4002B", True,
     "India's largest wires & cables maker and a complete FMEG brand.",
     ["Wires & Cables", "Power & Control Cables", "Fans", "LED Lighting", "Switchgear", "Conduits"],
     "Polycab is India's No.1 wires & cables manufacturer and offers a full FMEG portfolio. Mount Cable India supplies the complete Polycab range — from house wiring to fans, lighting and switchgear — at genuine distributor pricing."),
    ("kei", "KEI", "#ED1C24", True,
     "High-quality wires, power cables and stainless steel wires.",
     ["House Wires (FR / FR-LSH)", "LT & HT Power Cables", "Control & Instrumentation Cables", "Flexible Cables", "Stainless Steel Wires"],
     "KEI Industries is a trusted name for housing wires, power cables and specialty conductors built to strict IS standards. Mount Cable India stocks the KEI range for residential, commercial and industrial projects."),
    ("anchor-panasonic", "Anchor by Panasonic", "#0B5DAA", True,
     "Switches, wiring devices, lighting and fans backed by Panasonic.",
     ["Modular Switches & Sockets", "Piano Switches", "Wires & Cables", "LED Lighting", "Fans", "Conduits"],
     "Anchor by Panasonic combines India's most familiar switch brand with Panasonic's global engineering. Mount Cable India is an authorized Anchor dealer offering its full range of switches, wiring devices, lighting and fans."),
    ("greatwhite", "Greatwhite", "#ED1C24", False,
     "Modern modular switches, wires, fans and lighting.",
     ["Modular Switches (Fiana, Myrah)", "Wires & Cables", "Fans", "LED Lighting", "Home Automation"],
     "Greatwhite Global brings contemporary design to modular switches, wiring and home electricals. Mount Cable India supplies the Greatwhite range across Bengaluru."),
    ("v-guard", "V-Guard", "#ED1C24", False,
     "Wires, cables, stabilizers, pumps, fans and home appliances.",
     ["Wires & Cables", "Voltage Stabilizers", "Pumps & Motors", "Fans", "Water Heaters", "Switchgear"],
     "V-Guard is a leading consumer electrical brand known for stabilizers, wires and home appliances. Mount Cable India offers the V-Guard range with genuine warranty and distributor pricing."),
    ("rr-kabel", "RR Kabel", "#E2231A", True,
     "Premium wires & cables plus a growing FMEG range.",
     ["House Wires (FireX / HF)", "Power & Flexible Cables", "Fans", "LED Lighting", "Switches", "Conduits"],
     "RR Kabel is a globally recognised wires & cables brand with a strong FMEG portfolio. Mount Cable India supplies RR Kabel housing wires, cables, fans and lighting at the best distributor rates."),
    ("precision-pipes", "Precision Pipes", "#0E7C4A", False,
     "PVC conduits, pipes and fittings for clean electrical runs.",
     ["PVC Electrical Conduits", "Casing & Capping", "Bends, Couplers & Fittings", "Junction Boxes"],
     "Precision Pipes manufactures durable PVC conduits and electrical piping systems. Mount Cable India stocks the full range for safe, tidy cable management on every project."),
    ("schneider", "Schneider Electric", "#3DCD58", True,
     "World-class switches, switchgear and circuit protection.",
     ["Modular Switches (Livia, Zencelo)", "MCBs & RCCBs", "Distribution Boards", "Industrial Switchgear", "Home Automation"],
     "Schneider Electric delivers safe, smart and reliable electrical solutions worldwide. Mount Cable India supplies its modular switch ranges and protection devices for homes, offices and industry."),
    ("3m", "3M", "#E2231A", False,
     "Electrical tapes, connectors and cable accessories you can trust.",
     ["Electrical Insulation Tapes", "Cable Connectors & Lugs", "Cable Jointing Kits", "Heat-shrink & Accessories"],
     "3M sets the global standard for electrical tapes, connectors and cable jointing solutions. Mount Cable India stocks genuine 3M electrical accessories for professional installations."),
    ("legrand", "Legrand", "#E2001A", False,
     "Global leader in wiring devices and modular switches.",
     ["Modular Switches (Myrius, Arteor)", "Wiring Devices", "MCBs & DBs", "Home Automation", "Cable Management"],
     "Legrand sets the global benchmark for premium modular switches and electrical infrastructure. Mount Cable India stocks Legrand's Myrius and Arteor ranges along with protection devices."),
    ("hpl", "HPL", "#C8102E", False,
     "Switchgear, MCBs, wires, lighting and energy meters.",
     ["MCBs, RCCBs & Isolators", "Distribution Boards", "Wires & Cables", "LED Lighting", "Energy Meters"],
     "HPL is a well-established Indian brand for switchgear, wires, lighting and metering. Mount Cable India supplies the HPL range for residential and industrial requirements."),
    ("univyin-cables", "Univyin Cables", "#1E6BD6", False,
     "Reliable wires and flexible cables at value pricing.",
     ["House Wires", "Multi-core Flexible Cables", "Submersible Cables", "Power Cables"],
     "Univyin Cables offers dependable wires and flexible cables for everyday wiring needs. Mount Cable India keeps the range in ready stock for fast, economical supply."),
]

# Bengaluru areas for local SEO. slug, display name, nearby areas
AREAS = [
    ("jayanagar", "Jayanagar", "Basavanagudi, JP Nagar, Banashankari and South Bengaluru"),
    ("chickpete", "Chickpete", "Balepete, Avenue Road, KR Market and City Market"),
    ("basavanagudi", "Basavanagudi", "Jayanagar, Gandhi Bazaar, NR Colony and South Bengaluru"),
    ("jp-nagar", "JP Nagar", "Jayanagar, BTM Layout, Bannerghatta Road and Sarakki"),
    ("banashankari", "Banashankari", "JP Nagar, Kathriguppe, Padmanabhanagar and Girinagar"),
    ("btm-layout", "BTM Layout", "JP Nagar, Madiwala, HSR Layout and Bommanahalli"),
    ("koramangala", "Koramangala", "HSR Layout, Madiwala, Ejipura and Indiranagar"),
    ("hsr-layout", "HSR Layout", "Koramangala, BTM Layout, Agara and Sarjapur Road"),
    ("indiranagar", "Indiranagar", "Domlur, CV Raman Nagar, Halasuru and Old Airport Road"),
    ("rajajinagar", "Rajajinagar", "Malleshwaram, Basaveshwaranagar, Vijayanagar and Mahalakshmi Layout"),
    ("malleshwaram", "Malleshwaram", "Rajajinagar, Sadashivanagar, Yeshwanthpur and Seshadripuram"),
    ("whitefield", "Whitefield", "Marathahalli, ITPL, Brookefield and Varthur"),
    ("electronic-city", "Electronic City", "Bommanahalli, Hosur Road, Anekal and Bommasandra"),
    ("yelahanka", "Yelahanka", "Hebbal, Jakkur, Doddaballapur Road and Vidyaranyapura"),
]

# Featured Finolex products (image, name, desc)
FINOLEX_PRODUCTS = [
    ("prod-90m-silver.png", "Finolex 90M Silver", "FR-grade PVC house wire, 90-metre coil — the everyday choice for home wiring."),
    ("prod-fr-red.png", "Finolex FR House Wire", "New Improved FR PVC insulated wire — high insulation, anti-termite, RoHS compliant."),
    ("prod-frls-flamegard.png", "Finolex Flamegard FR-LSH", "Flame-retardant, low-smoke & halogen wire for safer homes."),
    ("prod-finolex-ultra.png", "Finolex Ultra", "E-Beam irradiated, low-smoke zero-halogen premium wire."),
]

# ---------- helpers ----------
def url_for(path):
    """Clean canonical URL for a generated file path."""
    p = path
    if p.endswith("index.html"):
        p = p[:-len("index.html")]
    elif p.endswith(".html"):
        p = p[:-len(".html")]
    return SITE_URL + "/" + p

def local_business_jsonld():
    addrs = ", ".join(
        f'{{"@type":"PostalAddress","streetAddress":"{o["area"]}","addressLocality":"Bengaluru","addressRegion":"Karnataka","postalCode":"{o["addr"].split()[-1]}","addressCountry":"IN"}}'
        for o in OFFICES)
    return ("""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ElectronicsStore","name":"Mount Cable India",
"image":\"""" + SITE_URL + """/assets/img/banner-finolex-wires.jpg","url":\"""" + SITE_URL + """",
"telephone":\"""" + PHONE_HREF + """","email":\"""" + EMAIL + """","priceRange":"₹₹",
"foundingDate":"1990","areaServed":"Bengaluru, Karnataka, India",
"description":"One of India's largest distributors of Finolex cables and a multi-brand electrical products dealer in Bengaluru, serving individual home builders for over """ + YEARS + """ years.",
"openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00","closes":"20:00"},
"address":[""" + addrs + """]}
</script>""")

def head(title, desc, path, css_prefix="", extra_jsonld=""):
    canonical = url_for(path)
    img = SITE_URL + "/assets/img/banner-finolex-wires.jpg"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mount Cable India">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{img}">
<meta name="theme-color" content="#0A1A33">
<link rel="icon" href="{css_prefix}assets/logos/finolex.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_prefix}assets/styles.css">
{local_business_jsonld()}
{extra_jsonld}
</head>
<body>"""

def header(prefix=""):
    return f"""
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{prefix}index.html">
      <span class="mark">M</span>
      <span>Mount Cable<small>India · Est. 1990</small></span>
    </a>
    <nav class="nav-links" id="navlinks">
      <a href="{prefix}index.html#finolex">Finolex</a>
      <a href="{prefix}index.html#categories">Categories</a>
      <a href="{prefix}index.html#brands">Brands</a>
      <a href="{prefix}index.html#areas">Areas We Serve</a>
      <a href="{prefix}index.html#offices">Showrooms</a>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-outline" href="tel:{PHONE_HREF}">📞 {PHONE}</a>
      <a class="btn btn-gold" href="{prefix}quote.html">Get a Quote</a>
      <button class="nav-toggle" aria-label="Menu" onclick="document.getElementById('navlinks').classList.toggle('open')">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>"""

def logo_wrap(b, prefix=""):
    slug, name, color = b[0], b[1], b[2]
    fb = f'<span class="logo-fallback" style="color:{color}{";display:inline-block" if slug not in LOGO else ""}">{html.escape(name)}</span>'
    if slug in LOGO:
        img = (f'<img class="logo-img" src="{prefix}assets/logos/{LOGO[slug]}" alt="{html.escape(name)} logo" '
               f'loading="lazy" onerror="this.style.display=\'none\';this.parentNode.querySelector(\'.logo-fallback\').style.display=\'inline-block\'">')
        return f'<span class="logo-wrap">{img}{fb}</span>'
    return f'<span class="logo-wrap">{fb}</span>'

def footer(prefix=""):
    half = (len(BRANDS) + 1) // 2
    col1 = "".join(f'<a href="{prefix}brands/{b[0]}.html">{html.escape(b[1])}</a>' for b in BRANDS[:half])
    col2 = "".join(f'<a href="{prefix}brands/{b[0]}.html">{html.escape(b[1])}</a>' for b in BRANDS[half:])
    cats = "".join(f'<a href="{prefix}{c[0]}.html">{html.escape(c[2])}</a>' for c in CATEGORIES)
    return f"""
<section class="cta-band">
  <div class="container">
    <h2>Building your home? Buy from the best brand distributor.</h2>
    <p>100% original material, 3-hour site delivery, free across Bangalore — and {YEARS} years of trust behind every order.</p>
    <div class="cta-actions">
      <a class="btn btn-gold" href="{prefix}quote.html">📷 Upload Your List — Get a Quote</a>
      <a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}">💬 WhatsApp {PHONE}</a>
    </div>
  </div>
</section>
<footer class="site-footer" id="contact">
  <div class="container">
    <div class="foot-grid">
      <div>
        <div class="foot-brand"><span class="mark" style="width:36px;height:36px;border-radius:9px;background:linear-gradient(135deg,var(--navy-3),var(--navy));display:grid;place-items:center;color:var(--gold)">M</span> Mount Cable India</div>
        <p>One of India's largest distributors of Finolex cables, and a multi-brand electrical dealer in Bengaluru for over {YEARS} years. 100% original material, free delivery across Bangalore and distributor pricing for everyone building their home.</p>
        <p>📞 <a href="tel:{PHONE_HREF}">{PHONE}</a><br>✉️ <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h4>Brands</h4>
        {col1}
      </div>
      <div>
        <h4>&nbsp;</h4>
        {col2}
      </div>
      <div>
        <h4>Shop By Category</h4>
        {cats}
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Mount Cable India · Serving Bengaluru since 1990. All rights reserved.</span>
      <span>Jayanagar · Chickpete · Free delivery across Bangalore</span>
    </div>
  </div>
</footer>
<script src="{prefix}assets/main.js"></script>
</body>
</html>"""

def brand_tile(b, prefix=""):
    return f"""<a class="brand-tile" href="{prefix}brands/{b[0]}.html">
      <div class="swatch" style="background:{b[2]}"></div>
      <div class="brand-tile-media">{logo_wrap(b, prefix)}</div>
      <div class="tag">Dealer &amp; Distributor</div>
    </a>"""

def breadcrumb_jsonld(items):
    el = ",".join(
        f'{{"@type":"ListItem","position":{i+1},"name":"{html.escape(n)}","item":"{u}"}}'
        for i, (n, u) in enumerate(items))
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{el}]}}</script>'

# ---------- pages ----------
def build_index():
    feat_cards = ""
    for b in [x for x in BRANDS if x[3]]:
        feat_cards += f"""
      <a class="dist-card" href="brands/{b[0]}.html">
        <div class="top-accent" style="background:linear-gradient(90deg,{b[2]},{b[2]}99)"></div>
        <div class="dist-media">{logo_wrap(b)}</div>
        <p>{html.escape(b[4])}</p>
        <span class="go">View {html.escape(b[1])} range →</span>
      </a>"""

    all_tiles = "".join(brand_tile(b) for b in BRANDS)
    cats = "".join(f"""<a class="cat" href="{c[0]}.html"><div class="ic">{c[1]}</div><h4>{html.escape(c[2])}</h4><p>{html.escape(c[3])}</p><span class="cat-go">Explore →</span></a>""" for c in CATEGORIES)
    prods = "".join(f"""<div class="prod"><div class="prod-img"><img src="assets/img/{p[0]}" alt="{html.escape(p[1])}" loading="lazy"></div><h4>{html.escape(p[1])}</h4><p>{html.escape(p[2])}</p></div>""" for p in FINOLEX_PRODUCTS)
    areas = "".join(f'<a class="area-chip" href="areas/{a[0]}.html">{html.escape(a[1])}</a>' for a in AREAS)
    offices = "".join(f"""
      <div class="office">
        <span class="tag">{o['tag']}</span>
        <h3>{o['area']}</h3>
        <p><span class="pi">📍</span> {html.escape(o['addr'])}</p>
        <p><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
        <p><span class="pi">🕘</span> Mon–Sat, 10:00 AM – 8:00 PM</p>
      </div>""" for o in OFFICES)

    desc = f"Building your home in Bengaluru? Mount Cable India is one of India's largest Finolex distributors & a multi-brand electrical dealer for {YEARS}+ years. 100% original Finolex wires, all ranges in stock, 3-hour free site delivery across Bangalore. Showrooms in Jayanagar & Chickpete."
    body = head("Mount Cable India | Finolex Distributor & Electrical Dealer, Bengaluru", desc, "index.html")
    body += header()
    body += f"""
<section class="hero">
  <div class="container hero-inner">
    <span class="hero-badge"><span class="dot"></span> Serving Bengaluru home builders for {YEARS}+ years</span>
    <h1>Building your house? Get <span class="accent">100% original Finolex wires</span> at distributor prices.</h1>
    <p class="lead">Mount Cable India is one of the largest distributors of Finolex cables in India. Every range is always in stock — and once your order is confirmed, we <strong>deliver to your site within 3 hours</strong> and collect payment right there. Free delivery across Bangalore.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="quote.html">📷 Upload Your List — Get a Quote</a>
      <a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}?text=Hi,%20I'm%20building%20my%20home%20and%20need%20a%20quote%20for%20electrical%20material">💬 WhatsApp 88676 76700</a>
    </div>
  </div>
</section>
<div class="trust">
  <div class="container">
    <div class="item"><div class="n">{YEARS}+</div><div class="l">Years in Business</div></div>
    <div class="item"><div class="n">100%</div><div class="l">Original Finolex Wires</div></div>
    <div class="item"><div class="n">3 Hrs</div><div class="l">Free Site Delivery</div></div>
    <div class="item"><div class="n">Always</div><div class="l">In Stock</div></div>
  </div>
</div>

<section class="finolex-spot" id="finolex">
  <div class="container">
    <div class="fs-grid">
      <div>
        <p class="eyebrow">Our Flagship · {YEARS} Years of Trust</p>
        <h2>One of India's largest Finolex distributors</h2>
        <p class="muted">Wiring a home is a once-in-a-lifetime decision — so it has to be right. Our surety to you: <strong>we sell only 100% original Finolex wires</strong>, sealed and warranty-backed, at genuine distributor prices. No fakes, no seconds, no compromises.</p>
        <p class="fs-ranges-label">Every Finolex range — always in stock:</p>
        <div class="chip-row fs-chips">
          <span class="chip">90M Silver</span><span class="chip">90M Gold</span><span class="chip">90M FRLS</span>
          <span class="chip">180M</span><span class="chip">300M</span><span class="chip">300M FRLS</span>
          <span class="chip">Finolex Ultra</span><span class="chip">Co-Axial</span><span class="chip">Telephone</span><span class="chip">Internet / LAN</span>
        </div>
        <ul class="tick-list">
          <li><strong>Always in stock</strong> — every Finolex range is available and ready to dispatch, no waiting.</li>
          <li><strong>3-hour site delivery</strong> — confirm your order and we deliver to your site within 3 hours.</li>
          <li><strong>Pay at your site</strong> — we collect payment right at your site, in any mode you prefer.</li>
        </ul>
        <a class="btn btn-dark" href="brands/finolex.html">Explore Finolex range →</a>
      </div>
      <div class="fs-visual">
        <img src="assets/img/banner-finolex-wires.jpg" alt="Finolex wires and cables" loading="lazy">
        <div class="fs-floatcard">
          <div class="fs-badge">★ 100% Original · All Ranges In Stock</div>
          <p>Send us your wiring list — we'll prepare a complete Finolex quote and deliver to your site in <strong>3 hours</strong>.</p>
          <a class="btn btn-gold" style="width:100%;justify-content:center" href="quote.html">📷 Get a Finolex Quote</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="products">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">In Stock Now</p>
      <h2>Popular Finolex products for your home</h2>
      <p>Genuine, sealed and ready to deliver across Bangalore the same day.</p>
    </div>
    <div class="prod-grid">{prods}</div>
  </div>
</section>

<section class="bg-soft" id="categories">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">What We Supply</p>
      <h2>Everything for your new home, under one roof</h2>
      <p>From the first switch to the final cable run — Mount Cable India stocks every category your house needs.</p>
    </div>
    <div class="cat-grid">{cats}</div>
  </div>
</section>

<section id="featured">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Featured Brands</p>
      <h2>Trusted names we proudly carry</h2>
      <p>Full ranges, genuine stock and the best pricing on the brands professionals ask for most.</p>
    </div>
    <div class="dist-grid">{feat_cards}</div>
  </div>
</section>

<section class="bg-soft" id="brands">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Brand Directory</p>
      <h2>Every brand we deal in</h2>
      <p>Tap any brand to see its product range and request pricing.</p>
    </div>
    <div class="brand-grid">{all_tiles}</div>
  </div>
</section>

<section id="why">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Built for Home Builders</p>
      <h2>Why families building their home choose us</h2>
      <p>If you're building your house, buy from the best brand distributor. For {YEARS} years, that's been us.</p>
    </div>
    <div class="feat-grid">
      <div class="feat"><div class="ic">🏅</div><h3>{YEARS} Years of Trust</h3><p>Three generations of Bengaluru home builders have wired their homes through us — experience you can rely on.</p></div>
      <div class="feat"><div class="ic">✓</div><h3>100% Original Material</h3><p>Genuine, brand-sealed and warranty-backed — especially our 100% original Finolex wires. What you pay for is what you get.</p></div>
      <div class="feat"><div class="ic">⏱️</div><h3>3-Hour Site Delivery</h3><p>Confirm your order and your material reaches your site within 3 hours — free across Bangalore.</p></div>
      <div class="feat"><div class="ic">💳</div><h3>Pay At Your Site</h3><p>We collect payment right at your site, in any mode — cash, UPI, card or bank transfer. No advance hassles.</p></div>
      <div class="feat"><div class="ic">↩️</div><h3>Free Pickup of Excess Stock</h3><p>Ordered a little extra? If you have surplus material left over, we'll pick it up free of charge.</p></div>
      <div class="feat"><div class="ic">🧭</div><h3>Expert Guidance</h3><p>First time wiring a home? We'll help you choose the right wires, gauges and brands for every room of your house.</p></div>
    </div>
  </div>
</section>

<section class="bg-soft" id="areas">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Local Delivery</p>
      <h2>Areas we serve across Bangalore</h2>
      <p>Free 3-hour delivery to your home site. Find your area for local pricing and stock.</p>
    </div>
    <div class="area-grid">{areas}</div>
  </div>
</section>

<section id="offices">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Visit Us</p>
      <h2>Two showrooms in Bengaluru</h2>
      <p>Walk in to either location — our team will help you pick the right products at the right price.</p>
    </div>
    <div class="office-grid">{offices}</div>
  </div>
</section>
"""
    body += footer()
    write("index.html", body)

def build_brand(b):
    slug, name, color, featured, tagline, prods, blurb = b
    chips = "".join(f'<span class="chip">{html.escape(p)}</span>' for p in prods)
    rel_list = [x for x in BRANDS if x[0] != slug][:4]
    related = "".join(brand_tile(x, prefix="../") for x in rel_list)
    path = f"brands/{slug}.html"
    title = f"{name} Dealer & Distributor in Bengaluru | Mount Cable India"
    desc = f"Authorized {name} dealer & distributor in Bengaluru. {tagline} 100% original material, free 3-hour delivery across Bangalore, distributor prices. {YEARS} years of trust. Showrooms in Jayanagar & Chickpete."
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), ("Brands", SITE_URL + "/index.html#brands"), (name, url_for(path))])
    body = head(title, desc, path, css_prefix="../", extra_jsonld=crumbs)
    body += header(prefix="../")
    has_logo = slug in LOGO
    logo_block = (f'<img class="bp-logo-img" src="../assets/logos/{LOGO[slug]}" alt="{html.escape(name)} logo" '
                  f'onerror="this.style.display=\'none\';document.getElementById(\'bpfb\').style.display=\'block\'">' if has_logo else "")
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../index.html#brands">Brands</a> &nbsp;/&nbsp; {html.escape(name)}</div>
    <span class="badge">★ Authorized Dealer &amp; Distributor</span>
    <div class="bp-logo-box">{logo_block}<div class="bp-logo" id="bpfb" style="color:{color};{'display:none' if has_logo else ''}">{html.escape(name)}</div></div>
    <h1>{html.escape(name)} dealer &amp; distributor in Bengaluru</h1>
    <p>{html.escape(tagline)}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="../quote.html">📷 Get {html.escape(name)} Quote</a>
      <a class="btn btn-ghost" href="tel:{PHONE_HREF}">📞 Call {PHONE}</a>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="prose">
      <h2>About our {html.escape(name)} range</h2>
      <p>{html.escape(blurb)}</p>
      <h2 style="margin-top:34px">Available products</h2>
      <div class="chip-row">{chips}</div>
      <h2 style="margin-top:34px">Why buy {html.escape(name)} from Mount Cable</h2>
      <ul class="tick-list">
        <li><strong>{YEARS} years of trust</strong> — one of Bengaluru's longest-serving electrical distributors.</li>
        <li><strong>100% genuine &amp; warranty-backed</strong> — sourced through authorized channels only.</li>
        <li><strong>Free 3-hour site delivery</strong> across Bangalore, and free pickup of any excess stock.</li>
        <li><strong>All payment modes accepted</strong> plus expert guidance for everyone building their home.</li>
      </ul>
    </div>
    <aside>
      <div class="side-card">
        <h3>Enquire about {html.escape(name)}</h3>
        <p class="muted" style="font-size:14.5px;margin:6px 0 0">Get pricing &amp; stock availability in minutes.</p>
        <div class="row"><span class="pi">📷</span> <a href="../quote.html">Upload your list for a quote</a></div>
        <div class="row"><span class="pi">💬</span> <a href="https://wa.me/{WHATSAPP}">WhatsApp {PHONE}</a></div>
        <div class="row"><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></div>
        <div class="row"><span class="pi">📍</span> Jayanagar &amp; Chickpete, Bengaluru</div>
        <a class="btn btn-gold" style="width:100%;justify-content:center;margin-top:10px" href="../quote.html">Request a Quote</a>
      </div>
    </aside>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head"><p class="eyebrow">More Brands</p><h2>We also supply</h2></div>
    <div class="related">{related}</div>
  </div>
</section>
"""
    body += footer(prefix="../")
    write(path, body)

def build_category(c):
    slug, icon, name, intro, brand_slugs, prods, banner = c
    bmap = {x[0]: x for x in BRANDS}
    tiles = "".join(brand_tile(bmap[s]) for s in brand_slugs if s in bmap)
    chips = "".join(f'<span class="chip">{html.escape(p)}</span>' for p in prods)
    path = f"{slug}.html"
    title = f"{name} in Bangalore | Buy at Distributor Price — Mount Cable India"
    desc = f"Buy {name.lower()} in Bangalore at distributor prices. {intro} 100% original, free 3-hour site delivery, {YEARS} years of trust. Showrooms in Jayanagar & Chickpete."
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), ("Categories", SITE_URL + "/index.html#categories"), (name, url_for(path))])
    banner_html = f'<div class="cat-banner"><img src="assets/img/{banner}" alt="{html.escape(name)} in Bangalore" loading="lazy"></div>' if banner else ""
    body = head(title, desc, path, css_prefix="", extra_jsonld=crumbs)
    body += header()
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; <a href="index.html#categories">Categories</a> &nbsp;/&nbsp; {html.escape(name)}</div>
    <span class="badge">{icon} Distributor Price · Bangalore</span>
    <h1>{html.escape(name)} in Bangalore</h1>
    <p>{html.escape(intro)}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="quote.html">📷 Upload Your List — Get a Quote</a>
      <a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}">💬 WhatsApp {PHONE}</a>
    </div>
  </div>
</section>
{banner_html}
<section>
  <div class="container">
    <div class="section-head"><p class="eyebrow">In This Category</p><h2>What you can buy</h2></div>
    <div class="chip-row" style="justify-content:center;max-width:760px;margin:0 auto">{chips}</div>
  </div>
</section>
<section class="bg-soft">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Top Brands</p><h2>Brands we stock for {html.escape(name).lower()}</h2></div>
    <div class="brand-grid">{tiles}</div>
  </div>
</section>
<section>
  <div class="container">
    <div class="section-head"><p class="eyebrow">Why Mount Cable</p><h2>Best place to buy {html.escape(name).lower()} in Bangalore</h2></div>
    <div class="feat-grid">
      <div class="feat"><div class="ic">🏅</div><h3>{YEARS} Years of Trust</h3><p>One of Bengaluru's longest-serving electrical distributors — relied on by thousands of home builders.</p></div>
      <div class="feat"><div class="ic">✓</div><h3>100% Original</h3><p>Every product is genuine, sealed and warranty-backed, sourced through authorized channels.</p></div>
      <div class="feat"><div class="ic">⏱️</div><h3>Free 3-Hour Delivery</h3><p>Confirm your order and we deliver to your site within 3 hours, free across Bangalore — pay at your site.</p></div>
    </div>
  </div>
</section>
"""
    body += footer()
    write(path, body)

def build_area(a):
    slug, name, nearby = a
    path = f"areas/{slug}.html"
    cats = "".join(f'<a class="area-chip" href="../{c[0]}.html">{html.escape(c[2])}</a>' for c in CATEGORIES)
    fbrands = "".join(brand_tile(b, prefix="../") for b in BRANDS if b[3])
    title = f"Electrical Shop & Finolex Wire Dealer in {name}, Bangalore | Mount Cable India"
    desc = f"Looking for electrical products or a Finolex wire dealer in {name}, Bangalore? Mount Cable India delivers 100% original Finolex wires, switches, cables, pipes & lighting to {name} in 3 hours, free. {YEARS} years of trust. Call {PHONE}."
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), ("Areas We Serve", SITE_URL + "/index.html#areas"), (name, url_for(path))])
    body = head(title, desc, path, css_prefix="../", extra_jsonld=crumbs)
    body += header(prefix="../")
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../index.html#areas">Areas We Serve</a> &nbsp;/&nbsp; {html.escape(name)}</div>
    <span class="badge">📍 Free 3-Hour Delivery in {html.escape(name)}</span>
    <h1>Electrical products &amp; Finolex wire dealer in {html.escape(name)}, Bangalore</h1>
    <p>Building or wiring a home in {html.escape(name)}? Mount Cable India delivers 100% original Finolex wires and every electrical essential to {html.escape(name)} and nearby {html.escape(nearby)} — within 3 hours of confirmation, free of cost.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="../quote.html">📷 Upload Your List — Get a Quote</a>
      <a class="btn btn-ghost" href="tel:{PHONE_HREF}">📞 Call {PHONE}</a>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="prose">
      <h2>Your local electrical distributor for {html.escape(name)}</h2>
      <p>For over {YEARS} years, home builders across South Bengaluru have trusted Mount Cable India for genuine electrical material at distributor prices. We deliver free to {html.escape(name)} and surrounding {html.escape(nearby)}, so you never have to leave your site or chase a local shop.</p>
      <p>As one of India's largest Finolex distributors, our surety to {html.escape(name)} customers is simple: <strong>100% original Finolex wires</strong>, every range in stock, delivered in 3 hours — and you pay at your site, in any mode.</p>
      <h2 style="margin-top:30px">Shop by category</h2>
      <div class="area-grid">{cats}</div>
      <h2 style="margin-top:30px">Why {html.escape(name)} home builders choose us</h2>
      <ul class="tick-list">
        <li><strong>Free 3-hour delivery</strong> to {html.escape(name)} and nearby {html.escape(nearby)}.</li>
        <li><strong>100% original Finolex</strong> and 12+ other trusted brands, always in stock.</li>
        <li><strong>Distributor prices</strong> with {YEARS} years of trust — better than any local outlet.</li>
        <li><strong>Pay at your site</strong>, all payment modes, plus free pickup of excess stock.</li>
      </ul>
    </div>
    <aside>
      <div class="side-card">
        <h3>Order for {html.escape(name)}</h3>
        <p class="muted" style="font-size:14.5px;margin:6px 0 0">Snap your wiring list — get an instant quote.</p>
        <div class="row"><span class="pi">📷</span> <a href="../quote.html">Upload your list for a quote</a></div>
        <div class="row"><span class="pi">💬</span> <a href="https://wa.me/{WHATSAPP}">WhatsApp {PHONE}</a></div>
        <div class="row"><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></div>
        <div class="row"><span class="pi">🚚</span> Free 3-hour delivery in {html.escape(name)}</div>
        <a class="btn btn-gold" style="width:100%;justify-content:center;margin-top:10px" href="../quote.html">Get a Quote</a>
      </div>
    </aside>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Top Brands</p><h2>Brands we deliver to {html.escape(name)}</h2></div>
    <div class="brand-grid">{fbrands}</div>
  </div>
</section>
"""
    body += footer(prefix="../")
    write(path, body)

def build_quote():
    path = "quote.html"
    title = "Get an Instant Quote — Upload Your Requirement | Mount Cable India"
    desc = f"Building your home? Upload a photo of your wiring list or requirement and get an instant quote on 100% original Finolex wires & electrical material. Free 3-hour delivery across Bangalore. {YEARS} years of trust."
    body = head(title, desc, path)
    body += header()
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; Get a Quote</div>
    <span class="badge">📷 Instant Quote · Free Delivery</span>
    <h1>Upload your requirement — get an instant quote</h1>
    <p>Just snap a photo of your wiring list, estimate or site requirement. We'll prepare a quote on 100% original Finolex wires and any other material — and deliver to your site in 3 hours.</p>
  </div>
</section>

<section>
  <div class="container quote-wrap">
    <form class="quote-form" action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="_subject" value="New Quote Request — Mount Cable India">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="{SITE_URL}/thank-you.html">
      <h2>Tell us what you need</h2>
      <div class="fld"><label>Your name *</label><input type="text" name="Name" required placeholder="e.g. Ramesh Kumar"></div>
      <div class="fld"><label>Phone / WhatsApp number *</label><input type="tel" name="Phone" required placeholder="10-digit mobile number" pattern="[0-9+ ]&#123;10,14&#125;"></div>
      <div class="fld"><label>Your area in Bangalore</label><input type="text" name="Area" placeholder="e.g. Jayanagar, JP Nagar, Whitefield"></div>
      <div class="fld"><label>What do you need?</label><textarea name="Requirement" rows="4" placeholder="e.g. Wiring for a 2BHK — Finolex 90M 1.0/1.5/2.5 sqmm, switches, MCB box…"></textarea></div>
      <div class="fld">
        <label>📷 Upload a photo of your list / requirement</label>
        <input type="file" name="attachment" accept="image/*" capture="environment" id="photo">
        <div class="photo-preview" id="preview"></div>
        <p class="hint">Snap your wiring list, estimate or site — JPG/PNG. We'll quote from it instantly.</p>
      </div>
      <button type="submit" class="btn btn-gold" style="width:100%;justify-content:center;font-size:16px;padding:15px">Get My Instant Quote →</button>
      <p class="hint center" style="margin-top:14px">Prefer chat? <a href="https://wa.me/{WHATSAPP}?text=Hi,%20here's%20my%20requirement%20for%20a%20quote">Send your photo on WhatsApp ({PHONE})</a></p>
    </form>
    <aside class="quote-side">
      <div class="qs-card">
        <h3>Why builders quote with us</h3>
        <ul class="tick-list">
          <li><strong>{YEARS} years</strong> of trust with Bengaluru home builders.</li>
          <li><strong>100% original Finolex</strong> — every range always in stock.</li>
          <li><strong>3-hour free delivery</strong> to your site across Bangalore.</li>
          <li><strong>Pay at your site</strong> — cash, UPI, card or transfer.</li>
          <li><strong>Free pickup</strong> of any excess stock you over-order.</li>
        </ul>
        <div class="qs-call">
          <span>Need it urgently?</span>
          <a class="btn btn-dark" href="tel:{PHONE_HREF}">📞 Call {PHONE}</a>
        </div>
      </div>
    </aside>
  </div>
</section>
<script>
  var p=document.getElementById('photo');
  if(p)p.addEventListener('change',function(){{
    var f=this.files&&this.files[0];var v=document.getElementById('preview');
    if(f){{var r=new FileReader();r.onload=function(e){{v.innerHTML='<img src="'+e.target.result+'" alt="preview">';}};r.readAsDataURL(f);}}
    else v.innerHTML='';
  }});
</script>
"""
    body += footer()
    write(path, body)

def build_thankyou():
    path = "thank-you.html"
    body = head("Thank You — We'll Quote You Shortly | Mount Cable India",
                "Thanks for your enquiry. Mount Cable India will send your quote shortly.", path)
    body += header()
    body += f"""
<section class="hero" style="min-height:60vh;display:flex;align-items:center">
  <div class="container hero-inner center" style="margin:0 auto">
    <span class="hero-badge" style="margin:0 auto 22px"><span class="dot"></span> Request received</span>
    <h1 style="margin:0 auto">Thank you! 🎉</h1>
    <p class="lead" style="margin:18px auto 30px">We've received your requirement and will send your quote shortly. For anything urgent, reach us right away.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-gold" href="https://wa.me/{WHATSAPP}">💬 WhatsApp {PHONE}</a>
      <a class="btn btn-ghost" href="index.html">← Back to Home</a>
    </div>
  </div>
</section>
"""
    body += footer()
    write(path, body)

def build_sitemap():
    paths = ["index.html", "quote.html", "thank-you.html"]
    paths += [f"{c[0]}.html" for c in CATEGORIES]
    paths += [f"brands/{b[0]}.html" for b in BRANDS]
    paths += [f"areas/{a[0]}.html" for a in AREAS]
    urls = ""
    for p in paths:
        pr = "1.0" if p == "index.html" else ("0.9" if p == "quote.html" else "0.8")
        urls += f"  <url><loc>{url_for(p)}</loc><changefreq>weekly</changefreq><priority>{pr}</priority></url>\n"
    sm = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True) if os.path.dirname(full) else None
    with open(full, "w") as f:
        f.write(content)

if __name__ == "__main__":
    build_index()
    for b in BRANDS: build_brand(b)
    for c in CATEGORIES: build_category(c)
    for a in AREAS: build_area(a)
    build_quote()
    build_thankyou()
    build_sitemap()
    total = 1 + len(BRANDS) + len(CATEGORIES) + len(AREAS) + 2
    print(f"Done — {total} pages + sitemap.xml + robots.txt")
    print(f"  1 home, {len(BRANDS)} brands, {len(CATEGORIES)} categories, {len(AREAS)} areas, quote, thank-you")
