#!/usr/bin/env python3
"""Static site generator for Mount Cable India.

Multi-brand electrical products dealers & distributors, Bengaluru.
Generates index.html and one landing page per brand.
Run:  python3 build.py
"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))

PHONE = "+91 98800 00000"          # TODO: replace with real number
PHONE_HREF = "+919880000000"
EMAIL = "sales@mountcable.com"     # TODO: replace with real email
WHATSAPP = "919880000000"

OFFICES = [
    {"tag": "Showroom 1", "area": "Jayanagar", "addr": "Jayanagar, Bengaluru, Karnataka 560011"},
    {"tag": "Showroom 2", "area": "Chickpete", "addr": "Chickpete, Bengaluru, Karnataka 560053"},
]

# 5 product categories from the business profile
CATEGORIES = [
    ("🔌", "Switches & Sockets", "Modular switches, plates, sockets and wiring accessories from Anchor, Schneider, Legrand, Greatwhite & more."),
    ("⚡", "Wires & Cables", "House wiring, power, control & flexible cables from Polycab, KEI, RR Kabel, V-Guard & Univyin."),
    ("🧰", "Pipes & Conduits", "PVC conduits, casing-capping, pipes, bends and fittings from Precision Pipes and leading brands."),
    ("💡", "Lighting", "LED bulbs, panels, battens, downlights and decorative lighting for home and commercial use."),
    ("🛡️", "Switchgears & Accessories", "MCBs, RCCBs, distribution boards, 3M tapes, connectors and electrical accessories."),
]

# slug, name, color, featured(bool), tagline, products[], blurb
BRANDS = [
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

def head(title, desc, css_prefix=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_prefix}assets/styles.css">
</head>
<body>"""

def header(prefix=""):
    return f"""
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{prefix}index.html">
      <span class="mark">M</span>
      <span>Mount Cable<small>India · Bengaluru</small></span>
    </a>
    <nav class="nav-links" id="navlinks">
      <a href="{prefix}index.html#categories">Categories</a>
      <a href="{prefix}index.html#brands">Brands</a>
      <a href="{prefix}index.html#why">Why Us</a>
      <a href="{prefix}index.html#offices">Offices</a>
      <a href="{prefix}index.html#contact">Contact</a>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-outline" href="tel:{PHONE_HREF}">📞 {PHONE}</a>
      <a class="btn btn-gold" href="https://wa.me/{WHATSAPP}">Get a Quote</a>
      <button class="nav-toggle" aria-label="Menu" onclick="document.getElementById('navlinks').classList.toggle('open')">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>"""

def footer(prefix=""):
    half = (len(BRANDS) + 1) // 2
    col1 = "".join(f'<a href="{prefix}brands/{b[0]}.html">{html.escape(b[1])}</a>' for b in BRANDS[:half])
    col2 = "".join(f'<a href="{prefix}brands/{b[0]}.html">{html.escape(b[1])}</a>' for b in BRANDS[half:])
    return f"""
<section class="cta-band">
  <div class="container">
    <h2>100% Original Material. 100% Distributor Price.</h2>
    <p>Visit our Jayanagar or Chickpete showroom, or message us for a quote on any brand.</p>
    <div class="cta-actions">
      <a class="btn btn-gold" href="https://wa.me/{WHATSAPP}">💬 WhatsApp Us</a>
      <a class="btn btn-ghost" href="tel:{PHONE_HREF}">📞 Call {PHONE}</a>
    </div>
  </div>
</section>
<footer class="site-footer" id="contact">
  <div class="container">
    <div class="foot-grid">
      <div>
        <div class="foot-brand"><span class="mark" style="width:36px;height:36px;border-radius:9px;background:linear-gradient(135deg,var(--navy-3),var(--navy));display:grid;place-items:center;color:var(--gold)">M</span> Mount Cable India</div>
        <p>Multi-brand electrical products dealers &amp; distributors in Bengaluru — switches, wires &amp; cables, pipes, lighting and switchgear from India's leading brands, at genuine distributor pricing.</p>
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
        <h4>Our Showrooms</h4>
        <p>Jayanagar<br>Bengaluru 560011</p>
        <p>Chickpete<br>Bengaluru 560053</p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Mount Cable India. All rights reserved.</span>
      <span>Genuine products · Distributor pricing · Bengaluru</span>
    </div>
  </div>
</footer>
<script src="{prefix}assets/main.js"></script>
</body>
</html>"""

def brand_tile(b, prefix=""):
    return f"""<a class="brand-tile" href="{prefix}brands/{b[0]}.html">
      <div class="swatch" style="background:{b[2]}"></div>
      <div class="name" style="color:{b[2]}">{html.escape(b[1])}</div>
      <div class="tag">Dealer &amp; Distributor</div>
    </a>"""

def build_index():
    feat_cards = ""
    for b in [x for x in BRANDS if x[3]]:
        feat_cards += f"""
      <a class="dist-card" href="brands/{b[0]}.html">
        <div class="top-accent" style="background:linear-gradient(90deg,{b[2]},{b[2]}99)"></div>
        <div class="ribbon">★ Featured Brand</div>
        <div class="brand-logo" style="color:{b[2]}">{html.escape(b[1])}</div>
        <p>{html.escape(b[4])}</p>
        <span class="go">View {html.escape(b[1])} range →</span>
      </a>"""

    all_tiles = "".join(brand_tile(b) for b in BRANDS)
    cats = "".join(f"""<div class="cat"><div class="ic">{c[0]}</div><h4>{html.escape(c[1])}</h4><p>{html.escape(c[2])}</p></div>""" for c in CATEGORIES)
    offices = "".join(f"""
      <div class="office">
        <span class="tag">{o['tag']}</span>
        <h3>{o['area']}</h3>
        <p><span class="pi">📍</span> {html.escape(o['addr'])}</p>
        <p><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
        <p><span class="pi">🕘</span> Mon–Sat, 10:00 AM – 8:00 PM</p>
      </div>""" for o in OFFICES)

    desc = "Mount Cable India — multi-brand electrical products dealers & distributors in Bengaluru. Switches & sockets, wires & cables, pipes & conduits, lighting and switchgear from Polycab, KEI, Anchor by Panasonic, Greatwhite, V-Guard, RR Kabel, Schneider, Legrand, HPL, 3M & more. 100% original material at distributor prices. Showrooms in Jayanagar & Chickpete."
    body = head("Mount Cable India | Electrical Dealers & Distributors, Bengaluru", desc)
    body += header()
    body += f"""
<section class="hero">
  <div class="container hero-inner">
    <span class="hero-badge"><span class="dot"></span> Jayanagar &amp; Chickpete · Bengaluru</span>
    <h1>Your one-stop shop for <span class="accent">multi-brand electrical products</span></h1>
    <p class="lead">Dealers &amp; distributors of switches, wires &amp; cables, pipes, lighting and switchgear — from <strong>Polycab, KEI, Anchor by Panasonic, RR Kabel, Schneider</strong> and more. 100% original material at genuine distributor prices.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="#brands">Explore Brands</a>
      <a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}">💬 Get a Quote</a>
    </div>
  </div>
</section>
<div class="trust">
  <div class="container">
    <div class="item"><div class="n">12+</div><div class="l">Leading Brands</div></div>
    <div class="item"><div class="n">100%</div><div class="l">Original Material</div></div>
    <div class="item"><div class="n">100%</div><div class="l">Distributor Price</div></div>
    <div class="item"><div class="n">2</div><div class="l">Bengaluru Showrooms</div></div>
  </div>
</div>

<section id="categories">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">What We Supply</p>
      <h2>Everything electrical, under one roof</h2>
      <p>From the first switch to the final cable run — Mount Cable India stocks every category your project needs.</p>
    </div>
    <div class="cat-grid">{cats}</div>
  </div>
</section>

<section class="bg-soft" id="featured">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Featured Brands</p>
      <h2>Trusted names we proudly carry</h2>
      <p>Full ranges, genuine stock and the best pricing on the brands professionals ask for most.</p>
    </div>
    <div class="dist-grid">{feat_cards}</div>
  </div>
</section>

<section id="brands">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Brand Directory</p>
      <h2>Every brand we deal in</h2>
      <p>Tap any brand to see its product range and request pricing.</p>
    </div>
    <div class="brand-grid">{all_tiles}</div>
  </div>
</section>

<section class="bg-soft" id="why">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Why Mount Cable India</p>
      <h2>The distributor contractors trust</h2>
    </div>
    <div class="feat-grid">
      <div class="feat"><div class="ic">✓</div><h3>100% Original Material</h3><p>Every product is genuine, brand-sealed and warranty-backed — sourced directly through authorized channels.</p></div>
      <div class="feat"><div class="ic">₹</div><h3>100% Distributor Price</h3><p>We pass on the best possible pricing to electricians, contractors and builders — no middlemen.</p></div>
      <div class="feat"><div class="ic">📦</div><h3>Ready Stock &amp; Fast Supply</h3><p>Deep inventory across 12+ brands at two Bengaluru showrooms means quick fulfilment for projects big and small.</p></div>
    </div>
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

    title = f"{name} Dealer & Distributor in Bengaluru | Mount Cable India"
    desc = f"Mount Cable India is an authorized {name} dealer & distributor in Bengaluru. {tagline} 100% original material at distributor prices. Showrooms in Jayanagar & Chickpete."
    body = head(title, desc, css_prefix="../")
    body += header(prefix="../")
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../index.html#brands">Brands</a> &nbsp;/&nbsp; {html.escape(name)}</div>
    <span class="badge">★ Authorized Dealer &amp; Distributor</span>
    <div class="bp-logo" style="color:{color}">{html.escape(name)}</div>
    <h1>{html.escape(name)} dealer &amp; distributor in Bengaluru</h1>
    <p>{html.escape(tagline)}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="https://wa.me/{WHATSAPP}?text=Hi,%20I%20need%20a%20quote%20for%20{name.replace(' ','%20')}%20products">💬 Get {html.escape(name)} Quote</a>
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
        <li><strong>100% genuine &amp; warranty-backed</strong> — sourced through authorized channels only.</li>
        <li><strong>Distributor pricing</strong> — the best rates for electricians, contractors &amp; builders.</li>
        <li><strong>Ready stock</strong> at our Jayanagar and Chickpete showrooms for fast supply.</li>
        <li><strong>Expert guidance</strong> on selecting the right {html.escape(name)} products for your project.</li>
      </ul>
    </div>
    <aside>
      <div class="side-card">
        <h3>Enquire about {html.escape(name)}</h3>
        <p class="muted" style="font-size:14.5px;margin:6px 0 0">Get pricing &amp; stock availability in minutes.</p>
        <div class="row"><span class="pi">💬</span> <a href="https://wa.me/{WHATSAPP}">WhatsApp {PHONE}</a></div>
        <div class="row"><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></div>
        <div class="row"><span class="pi">✉️</span> <a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="row"><span class="pi">📍</span> Jayanagar &amp; Chickpete, Bengaluru</div>
        <a class="btn btn-gold" style="width:100%;justify-content:center;margin-top:10px" href="https://wa.me/{WHATSAPP}">Request a Quote</a>
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
    write(f"brands/{slug}.html", body)

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", path)

if __name__ == "__main__":
    build_index()
    for b in BRANDS:
        build_brand(b)
    print(f"Done — index + {len(BRANDS)} brand pages.")
