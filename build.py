#!/usr/bin/env python3
"""Static site generator for Mount Cable India.

Generates index.html and one landing page per electrical brand.
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

# slug, name, color, tier, tagline, categories[], blurb
BRANDS = [
    ("finolex", "Finolex", "#0054A6", "Authorized Distributor",
     "Wires, cables & electrical essentials from one of India's most trusted names.",
     ["House Wires (FR / FR-LSH)", "Power & Control Cables", "Switches & Accessories", "Conduits & Fittings", "Water Heaters", "Fans"],
     "Finolex is a household name in Indian wiring, known for safety-first FR and flame-retardant cables that meet stringent IS standards. As an authorized Finolex distributor in Bengaluru, Mount Cable India supplies the complete range at genuine distributor pricing."),
    ("polycab", "Polycab", "#E4002B", "Authorized Distributor",
     "India's largest wires & cables manufacturer and a full-line FMEG brand.",
     ["Wires & Cables", "Fans", "LED Lighting", "Switches & Switchgear", "Pumps & Motors", "Conduits"],
     "Polycab leads the Indian wires & cables market and offers a complete FMEG portfolio. Mount Cable India is an authorized Polycab distributor in Bengaluru, stocking everything from house wiring to fans, lighting and switchgear."),
    ("wipro", "Wipro", "#5C2D91", "Authorized Distributor",
     "Premium lighting, fans and modular wiring devices.",
     ["LED Lighting", "Smart Lighting", "Ceiling & Decorative Fans", "Modular Switches", "Battens & Panels"],
     "Wipro Lighting and Consumer Care brings energy-efficient LED lighting and stylish fans to homes and offices. As an authorized Wipro distributor, Mount Cable India offers the full catalogue with reliable stock and distributor pricing."),
    ("havells", "Havells", "#E2231A", "Authorized Dealer",
     "A complete electrical brand — wires, switchgear, fans, lighting & appliances.",
     ["Wires & Cables", "Switchgear & MCBs", "Fans", "LED Lighting", "Modular Switches", "Home Appliances"],
     "Havells is one of India's most recognised electrical brands. Mount Cable India is an authorized Havells dealer in Bengaluru offering its wide range of wires, switchgear, fans, lighting and appliances."),
    ("legrand", "Legrand", "#E2001A", "Authorized Dealer",
     "Global leader in wiring devices, modular switches and home automation.",
     ["Modular Switches (Myrius, Arteor)", "Wiring Devices", "MCBs & DBs", "Home Automation", "Cable Management"],
     "Legrand sets the global benchmark for premium modular switches and electrical infrastructure. Mount Cable India stocks Legrand's Myrius and Arteor ranges along with protection devices for residential and commercial projects."),
    ("schneider", "Schneider Electric", "#3DCD58", "Authorized Dealer",
     "World-class switches, distribution boards and circuit protection.",
     ["Modular Switches (Livia, Zencelo)", "MCBs & RCCBs", "Distribution Boards", "Industrial Switchgear", "Home Automation"],
     "Schneider Electric delivers safe, smart and reliable electrical solutions worldwide. Mount Cable India supplies its modular switch ranges and protection devices for homes, offices and industry."),
    ("gm-modular", "GM Modular", "#D81E27", "Authorized Dealer",
     "Modular switches, wires, fans and lighting under one roof.",
     ["Modular Switches & Plates", "Wires & Cables", "LED Lighting", "Fans", "Wiring Accessories"],
     "GM Modular offers a versatile range of modular switches, wiring accessories and home electricals. Mount Cable India keeps the popular GM ranges in stock for quick supply across Bengaluru."),
    ("goldmedal", "Goldmedal", "#C8102E", "Authorized Dealer",
     "Modular switches, wires and the Espelio smart-home ecosystem.",
     ["Modular Switches", "Wires & Cables", "Smart Home (Espelio)", "Fans & Lighting", "Wiring Accessories"],
     "Goldmedal is a fast-growing electrical brand known for stylish modular switches and smart-home devices. Mount Cable India is an authorized Goldmedal dealer serving Bengaluru."),
    ("cona", "Cona", "#C8102E", "Authorized Dealer",
     "Trusted switches and wiring accessories for everyday installations.",
     ["Piano & Modular Switches", "Plates & Frames", "Wiring Accessories", "Plug-tops & Sockets"],
     "Cona has been a dependable name in Indian switches and wiring accessories for decades. Mount Cable India supplies the full Cona range at distributor pricing."),
    ("lisha", "Lisha", "#16A34A", "Authorized Dealer",
     "Value-driven modular switches and electrical accessories.",
     ["Modular Switches", "Plates & Frames", "Wiring Accessories", "Industrial Plugs & Sockets"],
     "Lisha offers reliable, value-for-money modular switches and accessories. Mount Cable India keeps Lisha's range readily available for electricians and contractors."),
    ("hifi", "Hifi", "#0067B1", "Authorized Dealer",
     "Affordable switches and wiring accessories you can rely on.",
     ["Switches & Sockets", "Modular Plates", "Wiring Accessories", "Holders & Plug-tops"],
     "Hifi provides economical and durable switches and wiring accessories. Mount Cable India stocks the Hifi range for fast, cost-effective supply."),
    ("norisys", "Norisys", "#111827", "Authorized Dealer",
     "Designer modular switches that elevate any interior.",
     ["Premium Modular Switches", "Designer Plates", "Glass & Metal Finishes", "Wiring Accessories"],
     "Norisys is known for premium, design-led modular switches with distinctive finishes. Mount Cable India supplies the Norisys range for architects, interior designers and discerning homeowners."),
    ("indo-asian", "Indo Asian", "#C8102E", "Authorized Dealer",
     "Dependable circuit protection — MCBs, RCCBs and distribution boards.",
     ["MCBs & Isolators", "RCCBs", "Distribution Boards", "Changeover Switches"],
     "Indo Asian is a respected name in circuit protection and switchgear. Mount Cable India supplies its MCBs, RCCBs and distribution boards for safe, code-compliant installations."),
]

CATEGORIES = [
    ("⚡", "Wires & Cables", "House wiring, power, control & flexible cables from Finolex, Polycab & Havells."),
    ("🔌", "Switches & Modular", "Designer & modular switch ranges from Legrand, Schneider, GM, Goldmedal & more."),
    ("💡", "Lighting & Fans", "LED lighting, panels, battens and ceiling fans for home and commercial use."),
    ("🛡️", "Switchgear & MCBs", "MCBs, RCCBs, distribution boards & isolators for safe circuit protection."),
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
      <a href="{prefix}index.html#distributors">Distributors</a>
      <a href="{prefix}index.html#brands">All Brands</a>
      <a href="{prefix}index.html#categories">Categories</a>
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
    dist = "".join(f'<a href="{prefix}brands/{b[0]}.html">{html.escape(b[1])}</a>' for b in BRANDS if "Distributor" in b[3])
    deal = "".join(f'<a href="{prefix}brands/{b[0]}.html">{html.escape(b[1])}</a>' for b in BRANDS if "Distributor" not in b[3])
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
        <p>Authorized distributors of Finolex, Polycab &amp; Wipro and dealers for India's leading electrical brands — serving Bengaluru with genuine products at distributor pricing.</p>
        <p>📞 <a href="tel:{PHONE_HREF}">{PHONE}</a><br>✉️ <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h4>Authorized Distributors</h4>
        {dist}
      </div>
      <div>
        <h4>We Also Deal In</h4>
        {deal}
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
    short = "Distributor" if "Distributor" in b[3] else "Dealer"
    return f"""<a class="brand-tile" href="{prefix}brands/{b[0]}.html">
      <div class="swatch" style="background:{b[2]}"></div>
      <div class="name" style="color:{b[2]}">{html.escape(b[1])}</div>
      <div class="tag">Authorized {short}</div>
    </a>"""

def build_index():
    dist_cards = ""
    for b in [x for x in BRANDS if "Distributor" in x[3]]:
        dist_cards += f"""
      <a class="dist-card" href="brands/{b[0]}.html">
        <div class="top-accent" style="background:linear-gradient(90deg,{b[2]},{b[2]}99)"></div>
        <div class="ribbon">★ Authorized Distributor</div>
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

    desc = "Mount Cable India — authorized distributor of Finolex, Polycab & Wipro in Bengaluru. Dealers for Havells, Legrand, Schneider, GM, Goldmedal, Cona, Lisha, Norisys, Indo Asian & more. 100% original material at distributor prices. Showrooms in Jayanagar & Chickpete."
    body = head("Mount Cable India | Authorized Electrical Distributors in Bengaluru", desc)
    body += header()
    body += f"""
<section class="hero">
  <div class="container hero-inner">
    <span class="hero-badge"><span class="dot"></span> Jayanagar &amp; Chickpete · Bengaluru</span>
    <h1>Bengaluru's trusted distributor of <span class="accent">India's top electrical brands</span></h1>
    <p class="lead">Authorized distributors of <strong>Finolex</strong>, <strong>Polycab</strong> &amp; <strong>Wipro</strong> — and dealers for every leading switch, wire &amp; lighting brand. 100% original material at genuine distributor prices.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="#distributors">Explore Brands</a>
      <a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}">💬 Get a Quote</a>
    </div>
  </div>
</section>
<div class="trust">
  <div class="container">
    <div class="item"><div class="n">13+</div><div class="l">Leading Brands</div></div>
    <div class="item"><div class="n">100%</div><div class="l">Original Material</div></div>
    <div class="item"><div class="n">100%</div><div class="l">Distributor Price</div></div>
    <div class="item"><div class="n">2</div><div class="l">Bengaluru Showrooms</div></div>
  </div>
</div>

<section id="distributors">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Authorized Distributors</p>
      <h2>Direct distribution partners</h2>
      <p>We are official authorized distributors — full ranges, genuine stock and the best pricing, direct from the brand.</p>
    </div>
    <div class="dist-grid">{dist_cards}</div>
  </div>
</section>

<section class="bg-soft" id="brands">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Brand Directory</p>
      <h2>Every electrical brand, one trusted partner</h2>
      <p>From premium modular switches to circuit protection — explore the brands we supply across Bengaluru.</p>
    </div>
    <div class="brand-grid">{all_tiles}</div>
  </div>
</section>

<section id="categories">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">What We Supply</p>
      <h2>Product categories</h2>
    </div>
    <div class="cat-grid">{cats}</div>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Why Mount Cable India</p>
      <h2>The distributor contractors trust</h2>
    </div>
    <div class="feat-grid">
      <div class="feat"><div class="ic">✓</div><h3>100% Original Material</h3><p>Every product is genuine, brand-sealed and warranty-backed — sourced directly through authorized channels.</p></div>
      <div class="feat"><div class="ic">₹</div><h3>100% Distributor Price</h3><p>As authorized distributors we pass on the best possible pricing to electricians, contractors and builders.</p></div>
      <div class="feat"><div class="ic">📦</div><h3>Ready Stock &amp; Fast Supply</h3><p>Deep inventory across 13+ brands at two Bengaluru showrooms means quick fulfilment for projects big and small.</p></div>
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
    slug, name, color, tier, tagline, cats, blurb = b
    short = "Distributor" if "Distributor" in tier else "Dealer"
    chips = "".join(f'<span class="chip">{html.escape(c)}</span>' for c in cats)
    related = "".join(brand_tile(x, prefix="../") for x in BRANDS if x[0] != slug)[:0] or \
              "".join(brand_tile(x, prefix="../") for x in BRANDS if x[0] != slug)
    # limit related to 4
    rel_list = [x for x in BRANDS if x[0] != slug][:4]
    related = "".join(brand_tile(x, prefix="../") for x in rel_list)

    title = f"{name} {short} in Bengaluru | Mount Cable India"
    desc = f"Mount Cable India is an authorized {name} {short.lower()} in Bengaluru. {tagline} 100% original material at distributor prices. Showrooms in Jayanagar & Chickpete."
    body = head(title, desc, css_prefix="../")
    body += header(prefix="../")
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../index.html#brands">Brands</a> &nbsp;/&nbsp; {html.escape(name)}</div>
    <span class="badge">★ Authorized {html.escape(tier.split()[-1])}</span>
    <div class="bp-logo" style="color:{color}">{html.escape(name)}</div>
    <h1>Authorized {html.escape(name)} {short} in Bengaluru</h1>
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
