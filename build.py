#!/usr/bin/env python3
"""Static site generator for Mount Cable India.

One of India's largest Finolex distributors + multi-brand electrical dealer,
Bengaluru. Focus: individual home builders. 35 years in business.

Generates: home, per-brand pages, product-category pages, Bengaluru area
(local-SEO) pages, a photo-upload quote page, robots.txt and sitemap.xml.

Run:  python3 build.py
"""
import os, html, json, urllib.parse, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))

def _ver(rel):
    """Content hash of a static asset, for cache-busting its URL."""
    try:
        with open(os.path.join(ROOT, rel), "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return "1"

CSS_VER = _ver("assets/styles.css")
JS_VER = _ver("assets/main.js")

def _json(s):
    """JSON-encode a string for safe embedding in a JSON-LD script."""
    return json.dumps(s, ensure_ascii=False)
SITE_URL = "https://mountcable.com"

PHONE = "+91 88676 76700"
PHONE_HREF = "+918867676700"
EMAIL = "mountcable@gmail.com"
WHATSAPP = "918867676700"
YEARS = "35"
# Google review link (opens the verified Google listing). For a true one-tap
# write-review funnel, replace with the GBP "Get more reviews" link (g.page/r/.../review)
# and regenerate assets/review-qr.svg.
REVIEW_URL = "https://share.google/G4NjwO8AuH9Ae5wJ1"

OFFICES = [
    {"tag": "Main Showroom", "area": "BVK Iyengar Road", "street": "10/3, Sri Complex, BVK Iyengar Road",
     "addr": "10/3, Sri Complex, BVK Iyengar Road, Near Rama Temple, Bengaluru, Karnataka 560053",
     "pin": "560053", "map": "Mount Cable India, 10/3 Sri Complex, BVK Iyengar Road, Bengaluru 560053"},
    {"tag": "Showroom 2", "area": "Jayanagar", "street": "Jayanagar",
     "addr": "Jayanagar, Bengaluru, Karnataka 560011",
     "pin": "560011", "map": "Jayanagar, Bengaluru"},
]

# Which brands have a downloaded logo file (others fall back to a wordmark)
LOGO = {
    "finolex": "finolex.svg", "polycab": "polycab.png", "kei": "kei.png",
    "rr-kabel": "rr-kabel.svg", "v-guard": "v-guard.webp", "greatwhite": "greatwhite.png",
    "hpl": "hpl.png", "anchor-panasonic": "anchor-panasonic.svg",
}

CATEGORIES = [
    ("switches-and-sockets", "🔌", "Switches & Sockets",
     "Modular switches, plates, sockets and wiring accessories from Anchor by Panasonic, Schneider, Legrand, Greatwhite, HPL & more.",
     ["anchor-panasonic", "schneider", "legrand", "greatwhite", "hpl"],
     ["Modular Switches", "Plates & Frames", "Sockets & Plug-tops", "USB & Smart Switches", "Bell & Fan Regulators"], ""),
    ("wires-and-cables", "⚡", "Wires & Cables",
     "House wiring, power, control and flexible cables from Finolex, Polycab, KEI, RR Kabel, V-Guard and Univyin — every gauge for your home.",
     ["finolex", "polycab", "kei", "rr-kabel", "v-guard", "univyin-cables"],
     ["FR / FR-LSH House Wires", "Multi-core Flexible Cables", "Power & Control Cables", "Co-Axial Cables", "Telephone & LAN Cables"], "banner-finolex-fr.webp"),
    ("pipes-and-conduits", "🧰", "Pipes & Conduits",
     "PVC electrical conduits, casing-capping, pipes, bends and fittings from Precision Pipes, Finolex and Polycab for clean, safe cable runs.",
     ["precision-pipes", "finolex", "polycab"],
     ["PVC Electrical Conduits", "Casing & Capping", "Bends, Couplers & Fittings", "Junction Boxes", "Flexible Conduits"], ""),
    ("lighting", "💡", "Lighting",
     "LED bulbs, panels, battens, downlights and decorative lighting from Finolex, Polycab, V-Guard, HPL and Greatwhite.",
     ["finolex", "polycab", "v-guard", "hpl", "greatwhite"],
     ["LED Bulbs & Battens", "Panel & Down Lights", "Flood & Street Lights", "Decorative Lighting", "Smart Lighting"], "banner-finolex-led.webp"),
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

# High-intent Finolex SEO landing pages (root-level).
# slug, title, h1, desc, badge, intro, sections[(h2, html)], faqs[(q,a)]
SEO_PAGES = [
 {"slug": "finolex-wire-price-list-bangalore",
  "title": "Finolex Wire Price List in Bangalore (2026) | Distributor Rate — Mount Cable India",
  "h1": "Finolex wire price list in Bangalore — get today's distributor rate",
  "desc": "Looking for the Finolex wire price list in Bangalore? Get today's genuine distributor rate for every Finolex range (90M, 180M, 300M, FRLS, Ultra) and gauge (1.0, 1.5, 2.5, 4.0 sq mm). 100% original, free 3-hour delivery. WhatsApp +91 88676 76700 for the latest price list.",
  "badge": "💰 Live Distributor Pricing · Updated Daily",
  "intro": "Want the latest Finolex wire price list in Bangalore? Because wire prices move with the copper market, we don't publish fixed figures that go stale — instead we send you today's genuine distributor rate within minutes. Message us your sizes and we'll share the current Finolex price list right away.",
  "sections": [
    ("Why Finolex wire prices change",
     "<p>Finolex house wire is made largely of copper, so its price tracks the global copper market and can change frequently. Anyone showing a fixed 'price list' that never updates is quoting stale rates. We quote the <strong>live distributor rate</strong> on the day you order — the same rate your local shop pays, passed straight to you.</p>"),
    ("Finolex wire sizes &amp; where each is used",
     "<p>Use this guide to work out which gauges you need, then message us for today's rate on each:</p>"
     "<div class=\"ptable-wrap\"><table class=\"ptable\"><thead><tr><th>Size</th><th>Typical use in a home</th><th>Coil options</th></tr></thead><tbody>"
     "<tr><td>0.75 sq mm</td><td>Lighting points, bulbs, tube lights</td><td>90M</td></tr>"
     "<tr><td>1.0 sq mm</td><td>Lights &amp; fan points, general 5A circuits</td><td>90M / 180M</td></tr>"
     "<tr><td>1.5 sq mm</td><td>Fan &amp; light circuits, utility points</td><td>90M / 180M / 300M</td></tr>"
     "<tr><td>2.5 sq mm</td><td>6A/16A sockets, fridge, TV, kitchen points</td><td>90M / 180M / 300M</td></tr>"
     "<tr><td>4.0 sq mm</td><td>Air-conditioners, geysers, heavy 16A loads</td><td>90M / 180M</td></tr>"
     "<tr><td>6.0 sq mm</td><td>Sub-mains, heavy kitchen / longer runs</td><td>90M / 180M</td></tr>"
     "</tbody></table></div>"
     "<p class=\"ptable-note\">Available in FR, FR-LSH (Flamegard) and Finolex Ultra grades. <a href=\"blog/fr-vs-frls-vs-finolex-ultra.html\">Which grade should you choose?</a></p>"),
    ("Get today's Finolex price list — in minutes",
     "<p>Send us your list of sizes and quantities (or a photo of your estimate) and we'll reply with the current Finolex price list at distributor rates. <a href=\"quote.html\">Upload your list here</a> or WhatsApp <a href=\"https://wa.me/918867676700\">+91 88676 76700</a>. Free 3-hour delivery across Bangalore, pay at your site.</p>"),
    ("Distributor price vs local shop (MRP)",
     "<p>Local shops usually sell close to MRP. As one of India's largest Finolex distributors, we give you the distributor rate — which, across a full house of wiring, saves a meaningful amount. Same 100% original Finolex, lower price. See the <a href=\"brands/finolex.html\">full Finolex range</a>.</p>"),
  ],
  "faqs": [
    ("What is the price of Finolex wire in Bangalore today?", "Finolex wire prices change daily with the copper market, so we quote a live distributor rate rather than a fixed list. Message us your sizes on WhatsApp at +91 88676 76700 and we'll send today's exact Finolex price list within minutes."),
    ("Do you have a Finolex wire price list 2026 PDF?", "Yes — we share the latest Finolex price list directly on WhatsApp or email, updated to the current copper rate (a static PDF goes out of date quickly). Send us your requirement and we'll forward the current list."),
    ("What is the price of Finolex 2.5 sq mm wire?", "The rate for 2.5 sq mm depends on the grade (FR, FR-LSH or Ultra), coil length (90M/180M/300M) and the day's copper price. Ask us for the current rate — as a distributor we offer it below typical MRP."),
    ("Is Finolex wire cheaper from a distributor than a local shop?", "Yes. Local shops sell near MRP, while we pass on the distributor rate. For a full house of wiring the saving is significant — for the same 100% original Finolex product."),
  ]},
 {"slug": "finolex-dealer-near-me",
  "title": "Finolex Dealer Near Me | Authorized Finolex Distributor in Bangalore",
  "h1": "Finolex dealer near me — we bring Finolex to your doorstep",
  "desc": "Searching for a Finolex dealer near me in Bangalore? Mount Cable India is an authorized Finolex distributor with free 3-hour delivery to your site across Bangalore. 100% original Finolex wires, all ranges in stock, distributor prices. Call +91 88676 76700.",
  "badge": "📍 Authorized Finolex Dealer · Free 3-Hour Delivery",
  "intro": "Looking for a 'Finolex dealer near me' in Bangalore? The nearest Finolex dealer is the one that comes to you. Mount Cable India is one of India's largest Finolex distributors, and we deliver 100% original Finolex wires free to your site — anywhere in Bangalore — within 3 hours of confirmation.",
  "sections": [
    ("The nearest Finolex dealer is the one that delivers to you",
     "<p>Instead of driving around looking for a Finolex shop, let the dealer come to you. We hold every Finolex range in stock and deliver free to your home or site across Bangalore within 3 hours of confirming your order — and you pay right at your site, in any mode. For over 35 years, that's how Bengaluru's home builders have wired their homes with us.</p>"),
    ("Finolex ranges we keep in stock — always",
     "<p>Whatever your wiring needs, the range is ready to dispatch: <strong>Finolex 90M Silver, 90M Gold, 90M FRLS, 180M, 300M, 300M FRLS and Finolex Ultra</strong>, plus co-axial, telephone and internet/LAN cables. See the full <a href=\"brands/finolex.html\">Finolex range and product photos</a>, or read our <a href=\"blog/house-wiring-wire-size-guide.html\">wire-size guide</a> to choose the right gauge.</p>"),
    ("Areas we deliver to across Bangalore",
     "<p>We deliver to all major localities — find yours below for local stock and pricing.</p>{areas}"),
    ("How to order from your nearest Finolex dealer",
     "<p>It takes a minute: <a href=\"quote.html\">upload a photo of your wiring list</a> for an instant quote, WhatsApp us, or call <a href=\"tel:+918867676700\">+91 88676 76700</a>. Confirm, and your genuine Finolex wires arrive at your site within 3 hours.</p>"),
  ],
  "faqs": [
    ("Is there a Finolex dealer near me in Bangalore?", "Yes — Mount Cable India is an authorized Finolex dealer serving all of Bangalore. Rather than asking you to travel, we deliver 100% original Finolex wires free to your site within 3 hours, so the nearest Finolex dealer effectively comes to you."),
    ("How fast can you deliver Finolex wires to my location?", "Once your order is confirmed, we deliver to your site within 3 hours, free across Bangalore. Every Finolex range is in stock, so there's no waiting."),
    ("Do I have to visit your showroom to buy Finolex wires?", "No. You can order entirely online — upload your list or WhatsApp us — and we deliver to your door. You're also welcome to visit our Jayanagar or Chickpete showrooms if you prefer."),
    ("Are you an authorized Finolex dealer?", "Yes. Mount Cable India is one of the largest distributors of Finolex cables in India, sourcing only through authorized channels — so every wire is 100% genuine and warranty-backed."),
  ]},
 {"slug": "original-finolex-wires",
  "title": "Original Finolex Wires | 100% Genuine at Distributor Price, Bangalore",
  "h1": "100% original Finolex wires — guaranteed genuine",
  "desc": "Buy 100% original Finolex wires in Bangalore from Mount Cable India, an authorized Finolex distributor. Sealed, warranty-backed, all ranges in stock, distributor prices, free 3-hour delivery. Learn how to verify genuine Finolex wire.",
  "badge": "✓ 100% Original · Authorized Distributor",
  "intro": "Want 100% original Finolex wires for your home? Our surety is simple: Mount Cable India sells only genuine, sealed, warranty-backed Finolex wires, sourced through authorized channels — at honest distributor prices. No fakes, no seconds, no compromises.",
  "sections": [
    ("Why buying original Finolex wire matters",
     "<p>Wire sits hidden inside your walls for decades. Counterfeit or sub-standard wire uses less or impure copper and weaker insulation, which can overheat and become a fire risk. For a once-in-a-lifetime decision like wiring your home, genuine wire is non-negotiable.</p>"),
    ("How we guarantee your Finolex wires are original",
     "<p>As one of India's largest Finolex distributors, we source directly through Finolex's authorized channel. Every coil reaches you brand-sealed and warranty-backed. Want to verify it yourself? Read our guide on <a href=\"blog/how-to-identify-original-finolex-wire.html\">how to identify 100% original Finolex wire</a>.</p>"),
    ("Every original Finolex range, in stock",
     "<p>We stock the complete genuine range — <strong>90M Silver, 90M Gold, 90M FRLS, 180M, 300M, 300M FRLS, Finolex Ultra</strong>, plus co-axial, telephone and internet/LAN cables. Not sure which grade? Compare <a href=\"blog/fr-vs-frls-vs-finolex-ultra.html\">FR vs FR-LSH vs Finolex Ultra</a>, or see the <a href=\"brands/finolex.html\">full Finolex range</a>.</p>"),
    ("Original wire, distributor price, delivered free",
     "<p>Genuine doesn't have to mean expensive. You get the distributor rate — the same your local shop pays — with free 3-hour site delivery across Bangalore and payment collected at your site. <a href=\"quote.html\">Upload your list for an instant quote.</a></p>"),
  ],
  "faqs": [
    ("Where can I buy 100% original Finolex wires in Bangalore?", "From Mount Cable India — an authorized Finolex distributor. We supply only genuine, sealed, warranty-backed Finolex wires at distributor prices, with free 3-hour delivery across Bangalore."),
    ("How do I know if a Finolex wire is genuine?", "Buy from an authorized distributor, check the sealed packaging and clean printing, look for clear repeated markings and standards marks along the wire, and verify the sequential metre marking. Our detailed guide explains each check."),
    ("Are your Finolex wires sealed and warranty-backed?", "Yes. Every coil is brand-sealed and warranty-backed, sourced through Finolex's authorized channel — that is our surety to you."),
    ("Is original Finolex wire more expensive?", "Genuine wire has a real copper cost, but as a distributor we pass on the distributor rate, so you pay far less than near-MRP local shop prices for the same 100% original product."),
  ]},
]

BLOG_DATE = "2026-06-02"
BLOG_DATE_DISP = "June 2, 2026"

# Home-page FAQs (also emitted as FAQPage structured data)
FAQS = [
    ("Is Mount Cable India an authorized Finolex distributor?",
     "Yes. Mount Cable India is one of the largest distributors of Finolex cables in India. Our surety to every customer is that we sell only 100% original Finolex wires, sealed and warranty-backed, at genuine distributor prices."),
    ("Do you deliver electrical material across Bangalore?",
     "Yes — we offer free delivery across Bangalore. Once your order is confirmed, we deliver to your site within 3 hours, and you can pay right at your site in any mode."),
    ("How do I get a quote for my home wiring?",
     "The fastest way is to upload a photo of your wiring list, estimate or requirement on our Get a Quote page. You can also WhatsApp or call us at " + PHONE + " and we'll prepare a complete quote."),
    ("Which Finolex ranges do you keep in stock?",
     "All of them — Finolex 90M Silver, 90M Gold, 90M FRLS, 180M, 300M, 300M FRLS, Finolex Ultra, plus co-axial, telephone and internet/LAN cables. Every range is in stock and always available."),
    ("What payment modes do you accept?",
     "We accept all payment modes — cash, UPI, cards and bank transfer — and we collect payment right at your site, so there are no advance hassles."),
    ("How long have you been in business?",
     "We have served Bengaluru's home builders for over " + YEARS + " years. That experience is why families trust us to wire their homes with the right products at the right price."),
]

# Blog posts (original content). slug, title, excerpt, tag, body(html, prefix="../")
BLOG = [
    ("house-wiring-wire-size-guide", "House Wiring Wire-Size Guide: Which Finolex Gauge for Each Room",
     "0.75, 1.0, 1.5, 2.5, 4.0 or 6.0 sq mm? A simple room-by-room guide to choosing the right wire size for your new home.", "Guide",
     """<p>One of the first questions every home builder faces is: <em>which wire size do I need?</em> Indian house wires are sold by cross-sectional area in square millimetres (sq mm), and using the right gauge keeps your home safe and your bills low. Here's a simple, practical guide.</p>
<h2>What the sq mm number means</h2>
<p>The bigger the sq mm, the more current the wire can safely carry. Under-sizing a wire causes heating and is a fire risk; over-sizing wastes money. Match the gauge to the load.</p>
<h2>Room-by-room wire size guide</h2>
<ul>
<li><strong>0.75 – 1.0 sq mm</strong> — lighting circuits, bulbs, tube lights and ceiling points.</li>
<li><strong>1.0 – 1.5 sq mm</strong> — fan points and general 5A lighting/utility circuits.</li>
<li><strong>2.5 sq mm</strong> — 6A/16A power sockets, fridge, TV, washing machine, kitchen points.</li>
<li><strong>4.0 sq mm</strong> — air-conditioners, geysers and other high-load 16A appliances.</li>
<li><strong>6.0 sq mm</strong> — sub-mains, heavy kitchen loads and longer runs.</li>
<li><strong>10 sq mm and above</strong> — main incoming line and meter-to-DB connections (consult your electrician).</li>
</ul>
<h2>How many coils will a home need?</h2>
<p>Finolex wires come in 90-metre, 180-metre and 300-metre coils. As a rough starting point, a 2BHK often needs several 90M coils across the common gauges, while a 3BHK or duplex needs more. The exact count depends on your floor plan and number of points — the easiest way is to share your wiring list with us for a precise material estimate.</p>
<h2>Don't forget FR vs FR-LSH</h2>
<p>For most homes, Finolex FR (flame-retardant) is the standard choice. If you want lower smoke and halogen emission in case of fire — recommended for bedrooms, kids' rooms and enclosed spaces — choose <a href="../brands/finolex.html">Finolex FR-LSH or Finolex Ultra</a>. Read our <a href="../blog/fr-vs-frls-vs-finolex-ultra.html">FR vs FR-LSH vs Ultra comparison</a> to decide.</p>
<p><strong>Not sure what to order?</strong> <a href="../quote.html">Upload your wiring list</a> and we'll prepare a complete, correctly-sized Finolex quote — delivered to your site in 3 hours.</p>"""),

    ("finolex-wire-price-bangalore", "Finolex Wire Price in Bangalore: How to Buy at Distributor Rate",
     "Why wire prices move, how MRP differs from distributor price, and the simplest way to get today's genuine rate for your home.", "Pricing",
     """<p>If you're wiring a house, wire is one of your biggest electrical costs — so it pays to understand how Finolex pricing works and how to buy at the genuine distributor rate.</p>
<h2>What affects the price of house wire</h2>
<ul>
<li><strong>Copper rate</strong> — wire prices move with the global copper market, so they change frequently. Always ask for today's rate.</li>
<li><strong>Cross-section (sq mm)</strong> — thicker wires use more copper and cost more per coil.</li>
<li><strong>Coil length</strong> — Finolex sells 90M, 180M and 300M coils; per-metre cost usually improves on longer coils.</li>
<li><strong>Grade</strong> — FR, FR-LSH and Finolex Ultra are priced differently for their safety features.</li>
</ul>
<h2>MRP vs distributor price</h2>
<p>Local shops typically sell near MRP. As one of India's largest Finolex distributors, we pass the distributor rate on to you — the same rate your local shop pays. For a full house, that difference adds up significantly.</p>
<h2>How to get today's rate</h2>
<p>Because prices change with copper, we don't publish fixed figures — instead, we give you a live quote. The fastest way: <a href="../quote.html">upload a photo of your wiring list or estimate</a>, or WhatsApp us at """ + PHONE + """. You'll get a complete, itemised quote at distributor pricing, plus free 3-hour delivery and payment collected at your site.</p>
<p>See the full <a href="../wires-and-cables.html">wires &amp; cables range</a> we stock, or read our <a href="../blog/house-wiring-wire-size-guide.html">wire-size guide</a> first.</p>"""),

    ("fr-vs-frls-vs-finolex-ultra", "FR vs FR-LSH vs Finolex Ultra: Which House Wire Should You Choose?",
     "A plain-English comparison of Finolex's three main house-wire grades so you can pick the right safety level for your home.", "Comparison",
     """<p>Finolex house wires come in a few grades, and the names can be confusing. Here's what FR, FR-LSH and Finolex Ultra actually mean — and where each one fits in a home.</p>
<h2>FR — Flame Retardant</h2>
<p>The standard, most widely used house wire. FR insulation resists catching fire and slows flame spread. It's a solid, value-for-money choice for general home wiring.</p>
<h2>FR-LSH — Flame Retardant Low Smoke &amp; Halogen</h2>
<p>Everything FR does, plus it releases <strong>less smoke and fewer toxic halogen gases</strong> if exposed to fire. In a house fire, smoke and gas are often more dangerous than flames — so FR-LSH (Finolex's Flamegard range) is a smart upgrade for bedrooms, children's rooms, and enclosed or poorly-ventilated areas.</p>
<h2>Finolex Ultra — E-Beam, Low Smoke Zero Halogen</h2>
<p>Finolex's premium wire, using electron-beam (E-Beam) irradiated insulation for superior heat resistance and the lowest smoke and halogen emission. It's the safest choice for premium homes and anyone who wants maximum fire safety.</p>
<h2>Which should you choose?</h2>
<ul>
<li><strong>Budget-conscious, general wiring</strong> → Finolex FR.</li>
<li><strong>Better fire safety for living spaces</strong> → Finolex FR-LSH.</li>
<li><strong>Premium home, maximum safety</strong> → Finolex Ultra.</li>
</ul>
<p>Many builders mix grades — Ultra/FR-LSH for bedrooms and FR for utility areas. We stock <a href="../brands/finolex.html">every Finolex grade and coil length</a>, always in stock. <a href="../quote.html">Share your list</a> and we'll recommend the right mix.</p>"""),

    ("electrical-checklist-building-house-bangalore", "Electrical Materials Checklist for Building a House in Bangalore",
     "A complete, room-ready checklist of everything electrical you'll need — so nothing holds up your construction.", "Checklist",
     """<p>Building a home means buying a lot of electrical material. Use this checklist so you order everything in one go and avoid last-minute site delays.</p>
<h2>Wires &amp; cables</h2>
<ul>
<li>House wires across gauges — 1.0, 1.5, 2.5, 4.0 sq mm (<a href="../brands/finolex.html">Finolex</a>, Polycab, KEI, RR Kabel)</li>
<li>Co-axial cable (TV), telephone cable, and internet/LAN cable</li>
<li>Bell wire and flexible multi-core cable for appliances</li>
</ul>
<h2>Switches, sockets &amp; accessories</h2>
<ul>
<li>Modular <a href="../switches-and-sockets.html">switches and sockets</a>, plates and frames</li>
<li>Fan regulators, bell push, USB sockets, TV/data outlets</li>
</ul>
<h2>Protection &amp; distribution</h2>
<ul>
<li>Main and sub <a href="../switchgear-and-mcb.html">distribution boards (DBs)</a></li>
<li>MCBs, RCCBs/RCBOs and isolators sized to your load</li>
</ul>
<h2>Pipes, conduits &amp; boxes</h2>
<ul>
<li><a href="../pipes-and-conduits.html">PVC conduits</a>, bends, couplers and junction boxes</li>
<li>Modular mounting boxes and fan hooks/boxes</li>
</ul>
<h2>Lighting</h2>
<ul>
<li><a href="../lighting.html">LED bulbs, battens, panel and downlights</a>, outdoor/flood lights</li>
</ul>
<h2>Earthing &amp; finishing</h2>
<ul>
<li>Earthing wire/strip and accessories</li>
<li>3M insulation tape, connectors, lugs and cable ties</li>
</ul>
<p>Don't want to itemise it all yourself? <a href="../quote.html">Upload your house plan or estimate</a> and we'll build the complete material list for you — at distributor prices, delivered free in 3 hours.</p>"""),

    ("how-to-identify-original-finolex-wire", "How to Identify 100% Original Finolex Wire (and Avoid Fakes)",
     "Counterfeit wire is a real safety risk. Here's how to make sure the Finolex wire you buy is genuine.", "Safety",
     """<p>Wire is hidden inside your walls for decades — so buying genuine, quality wire is one of the most important safety decisions in your home. Counterfeit and sub-standard wire uses less or impure copper and weaker insulation, which can overheat. Here's how to protect yourself.</p>
<h2>1. Buy from an authorized distributor</h2>
<p>The single best safeguard. Authorized distributors source directly through Finolex's official channel, so the product is guaranteed genuine and warranty-backed. Mount Cable India is one of India's largest Finolex distributors — our surety is 100% original Finolex, every time.</p>
<h2>2. Check the packaging and printing</h2>
<p>Genuine Finolex boxes are cleanly printed with consistent branding, batch details and grade markings (FR, FR-LSH, etc.). Be wary of blurry print, spelling errors or tampered seals.</p>
<h2>3. Look for standards markings on the wire</h2>
<p>Original wire carries clear, repeated printing along its length — brand, size (sq mm), grade and standards mark. The print should be sharp and evenly spaced.</p>
<h2>4. Sequential metre marking</h2>
<p>Quality wire is printed with running metre markings so you can verify coil length. Missing or irregular markings are a red flag.</p>
<h2>5. Don't chase the lowest price</h2>
<p>If a price looks far below the market, ask why. Genuine wire has a real copper cost. A distributor rate from an authorized seller is the right kind of saving — not a suspiciously cheap "deal".</p>
<p>Want certainty? Buy your <a href="../brands/finolex.html">Finolex wires</a> from us — sealed, genuine and delivered to your site. <a href="../quote.html">Get a quote here.</a></p>"""),

    ("best-electrical-brands-home-wiring-india", "Best Electrical Brands for Home Wiring in India (2026 Guide)",
     "From wires to switches to protection — the trusted brands to consider for your home, and what each is known for.", "Guide",
     """<p>Choosing brands for a new home can be overwhelming. Here's a practical rundown of trusted electrical brands by category, all of which we stock at distributor prices.</p>
<h2>Wires &amp; cables</h2>
<ul>
<li><a href="../brands/finolex.html">Finolex</a> — India's most trusted house wire; FR, FR-LSH and Ultra grades.</li>
<li><a href="../brands/polycab.html">Polycab</a> — India's largest cables maker, full FMEG range.</li>
<li><a href="../brands/kei.html">KEI</a> and <a href="../brands/rr-kabel.html">RR Kabel</a> — strong housing-wire and power-cable options.</li>
<li><a href="../brands/v-guard.html">V-Guard</a> — wires plus stabilizers and appliances.</li>
</ul>
<h2>Switches &amp; sockets</h2>
<ul>
<li><a href="../brands/anchor-panasonic.html">Anchor by Panasonic</a> — India's most familiar switches, Panasonic-backed.</li>
<li><a href="../brands/schneider.html">Schneider</a>, <a href="../brands/legrand.html">Legrand</a> and <a href="../brands/greatwhite.html">Greatwhite</a> — premium and modern modular ranges.</li>
</ul>
<h2>Circuit protection (MCBs, DBs)</h2>
<ul>
<li><a href="../brands/schneider.html">Schneider</a>, <a href="../brands/legrand.html">Legrand</a> and <a href="../brands/hpl.html">HPL</a> — reliable MCBs, RCCBs and distribution boards.</li>
</ul>
<h2>Pipes, conduits &amp; accessories</h2>
<ul>
<li><a href="../brands/precision-pipes.html">Precision Pipes</a> — PVC conduits and fittings.</li>
<li><a href="../brands/3m.html">3M</a> — tapes, connectors and cable jointing accessories.</li>
</ul>
<h2>The bottom line</h2>
<p>There's no single "best" brand — the right choice depends on your budget and where the product is used. A good distributor helps you mix the right brands for each part of your home. <a href="../quote.html">Share your requirement</a> and we'll recommend a complete, value-for-money package — delivered free across Bangalore.</p>"""),
]

# Featured Finolex products (image, name, desc)
FINOLEX_PRODUCTS = [
    ("prod-90m-silver.webp", "Finolex 90M Silver", "FR-grade PVC house wire, 90-metre coil — the everyday choice for home wiring."),
    ("prod-fr-red.webp", "Finolex FR House Wire", "New Improved FR PVC insulated wire — high insulation, anti-termite, RoHS compliant."),
    ("prod-frls-flamegard.webp", "Finolex Flamegard FR-LSH", "Flame-retardant, low-smoke & halogen wire for safer homes."),
    ("prod-finolex-ultra.webp", "Finolex Ultra", "E-Beam irradiated, low-smoke zero-halogen premium wire."),
]

HOUSE_SIZES = ["0.75 sq mm", "1.0 sq mm", "1.5 sq mm", "2.5 sq mm", "4.0 sq mm", "6.0 sq mm"]

# Finolex ranges → individual product pages. slug, name, image, tagline, grade, coil, sizes[], desc
FINOLEX_RANGE = [
    ("90m-silver", "Finolex 90M Silver", "prod-90m-silver.webp",
     "FR-grade PVC house wire in a 90-metre coil — the dependable everyday choice.",
     "FR (Flame Retardant)", "90 metres", HOUSE_SIZES,
     "Finolex 90M Silver is the go-to FR-grade house wire for everyday home wiring. With high insulation resistance, anti-termite and anti-rodent properties and 99.97% pure bare copper conductor, it delivers safe, reliable performance for lighting, fan and socket circuits. Supplied in convenient 90-metre coils across all common gauges."),
    ("90m-gold", "Finolex 90M Gold", "prod-fr-red.webp",
     "Premium FR house wire, 90-metre coil — superior finish and performance.",
     "FR (Flame Retardant)", "90 metres", HOUSE_SIZES,
     "Finolex 90M Gold is the premium FR house wire for homeowners who want the best. Built on the same New Improved FR technology with high-grade copper and robust insulation, it offers excellent current-carrying capacity and long service life. Ideal for quality-conscious home builders, in 90-metre coils."),
    ("90m-frls", "Finolex 90M FRLS", "prod-frls-flamegard.webp",
     "Flame-retardant, low-smoke & halogen house wire — safer for living spaces.",
     "FR-LSH (Flamegard)", "90 metres", HOUSE_SIZES,
     "Finolex 90M FRLS (Flamegard) goes beyond flame retardance to emit low smoke and reduced halogen gases in case of fire — protecting your family where it matters most. Recommended for bedrooms, children's rooms and enclosed spaces. Available in 90-metre coils across all gauges."),
    ("180m", "Finolex 180M", "prod-fr-red.webp",
     "FR house wire in a 180-metre coil — fewer joins, better value for bigger jobs.",
     "FR (Flame Retardant)", "180 metres", HOUSE_SIZES,
     "Finolex 180M offers the same trusted FR-grade quality in a larger 180-metre coil — ideal for medium-to-large homes where longer continuous runs mean fewer joints and better value. High insulation, anti-termite and RoHS compliant."),
    ("300m", "Finolex 300M", "prod-fr-red.webp",
     "FR house wire in a 300-metre coil — best value for full-house wiring.",
     "FR (Flame Retardant)", "300 metres", HOUSE_SIZES,
     "Finolex 300M comes in a large 300-metre coil — the most economical choice for wiring an entire house or larger project. Genuine FR-grade insulation, 99.97% pure copper and long continuous lengths that reduce wastage and joints."),
    ("300m-frls", "Finolex 300M FRLS", "prod-frls-flamegard.webp",
     "Flame-retardant low-smoke & halogen wire in a 300-metre coil.",
     "FR-LSH (Flamegard)", "300 metres", HOUSE_SIZES,
     "Finolex 300M FRLS combines the safety of low-smoke, low-halogen Flamegard insulation with the value of a 300-metre coil. The smart choice when you want maximum fire safety across a whole home without compromising on coil economy."),
    ("ultra", "Finolex Ultra", "prod-finolex-ultra.webp",
     "E-Beam, low-smoke zero-halogen premium wire — the safest Finolex house wire.",
     "LSZH (E-Beam irradiated)", "90 / 180 metres", HOUSE_SIZES,
     "Finolex Ultra is the flagship house wire, using electron-beam (E-Beam) irradiated insulation for superior heat resistance and the lowest smoke and halogen emission. The premium choice for high-end homes and anyone who wants the highest level of electrical fire safety."),
    ("co-axial-cables", "Finolex Co-Axial Cables", "banner-finolex-wires.webp",
     "RG-series co-axial cables for crisp TV, dish and CCTV signals.",
     "Co-Axial", "Multiple lengths", ["RG-6", "RG-11", "RG-59", "CATV / Dish", "CCTV"],
     "Finolex co-axial cables deliver clear, low-loss signal transmission for cable TV, DTH/dish and CCTV installations. Precision-engineered shielding and conductors ensure minimal interference — wire your home's entertainment and security points right the first time."),
    ("telephone-cables", "Finolex Telephone Cables", "banner-finolex-wires.webp",
     "Reliable multi-pair telephone cables for clear home & office lines.",
     "Telephone", "Multiple lengths", ["1 Pair", "2 Pair", "3 Pair", "5 Pair", "10 Pair"],
     "Finolex telephone cables provide dependable, noise-free voice connectivity for homes and offices. Available in multiple pair configurations with quality copper conductors for clear, consistent lines."),
    ("internet-lan-cables", "Finolex Internet / LAN Cables", "banner-finolex-wires.webp",
     "Cat5e & Cat6 LAN cables for fast, stable home and office networks.",
     "LAN / Networking", "Box / Reel", ["Cat5e", "Cat6", "UTP", "Outdoor / Armoured"],
     "Finolex internet and LAN cables (Cat5e, Cat6) deliver fast, stable wired networking for your home or office. Build a reliable backbone for your routers, smart devices and work-from-home setup with genuine Finolex data cable."),
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
        f'{{"@type":"PostalAddress","streetAddress":"{o["street"]}","addressLocality":"Bengaluru","addressRegion":"Karnataka","postalCode":"{o["pin"]}","addressCountry":"IN"}}'
        for o in OFFICES)
    return ("""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ElectronicsStore","name":"Mount Cable India",
"image":\"""" + SITE_URL + """/assets/img/banner-finolex-wires.jpg","url":\"""" + SITE_URL + """",
"telephone":\"""" + PHONE_HREF + """","email":\"""" + EMAIL + """","priceRange":"₹₹",
"foundingDate":"1991","areaServed":"Bengaluru, Karnataka, India",
"description":"One of India's largest distributors of Finolex cables and a multi-brand electrical products dealer in Bengaluru, serving individual home builders for over """ + YEARS + """ years.",
"openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00","closes":"20:00"},
"sameAs":["https://www.justdial.com/Bangalore/Mount-Cable-INDIA-Near-Rama-Temple-Bvk-Iyengar-Road/080PXX80-XX80-120530111557-V4V6_BZDET","https://www.indiamart.com/mountcableindia/","https://share.google/G4NjwO8AuH9Ae5wJ1"],
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
<link rel="stylesheet" href="{css_prefix}assets/styles.css?v={CSS_VER}">
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
      <span>Mount Cable<small>India · Est. 1991</small></span>
    </a>
    <nav class="nav-links" id="navlinks">
      <a href="{prefix}index.html#finolex">Finolex</a>
      <a href="{prefix}index.html#categories">Categories</a>
      <a href="{prefix}index.html#brands">Brands</a>
      <a href="{prefix}index.html#areas">Areas We Serve</a>
      <a href="{prefix}blog.html">Blog</a>
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
        <h4 style="margin-top:18px">Finolex</h4>
        <a href="{prefix}finolex-wire-price-list-bangalore.html">Finolex Price List Bangalore</a>
        <a href="{prefix}original-finolex-wires.html">Original Finolex Wires</a>
        <a href="{prefix}finolex-dealer-near-me.html">Finolex Dealer Near Me</a>
        <a href="{prefix}review.html">★ Review us on Google</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Mount Cable India · Serving Bengaluru since 1991. All rights reserved.</span>
      <span>Jayanagar · Chickpete · Free delivery across Bangalore</span>
    </div>
  </div>
</footer>
<script src="{prefix}assets/main.js?v={JS_VER}"></script>
<script defer src="/_vercel/insights/script.js"></script>
<script defer src="/_vercel/speed-insights/script.js"></script>
</body>
</html>"""

def review_block(prefix=""):
    return f"""
<section class="review-sec" id="review">
  <div class="container">
    <div class="review-card">
      <div class="review-text">
        <p class="eyebrow">Loved our service?</p>
        <h2>Leave us a Google review</h2>
        <p class="muted">Your review helps other home builders in Bangalore find genuine Finolex wires at the right price. It takes 30 seconds — scan the code or tap the button.</p>
        <div class="review-actions">
          <a class="btn btn-gold" href="{REVIEW_URL}" target="_blank" rel="noopener">★ Write a Google Review</a>
          <a class="btn btn-outline" href="{prefix}review.html">View QR &amp; steps</a>
        </div>
      </div>
      <div class="review-qr">
        <img src="{prefix}assets/review-qr.svg" alt="Scan to review Mount Cable India on Google" width="170" height="170">
        <span>📷 Scan to review</span>
      </div>
    </div>
  </div>
</section>"""

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

def blog_card(p, prefix=""):
    slug, title, excerpt, tag = p[0], p[1], p[2], p[3]
    return f"""<a class="blog-card" href="{prefix}blog/{slug}.html">
      <span class="blog-tag">{html.escape(tag)}</span>
      <h3>{html.escape(title)}</h3>
      <p>{html.escape(excerpt)}</p>
      <span class="go">Read guide →</span>
    </a>"""

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
    areas = "".join(f'<a class="area-chip" href="areas/{a[0]}.html">{html.escape(a[1])}</a>' for a in AREAS)
    offices = "".join(f"""
      <div class="office">
        <span class="tag">{o['tag']}</span>
        <h3>{o['area']}</h3>
        <p><span class="pi">📍</span> {html.escape(o['addr'])}</p>
        <p><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
        <p><span class="pi">🕘</span> Mon–Sat, 10:00 AM – 8:00 PM</p>
        <a class="office-dir" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(o['map'])}">🧭 Get directions →</a>
        <iframe class="map-embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={urllib.parse.quote(o['map'])}&output=embed" title="{html.escape(o['area'])} map"></iframe>
      </div>""" for o in OFFICES)

    faq_q = ",".join(
        f'{{"@type":"Question","name":{_json(q)},"acceptedAnswer":{{"@type":"Answer","text":{_json(a)}}}}}'
        for q, a in FAQS)
    faq_jsonld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_q}]}}</script>'
    faq_html = "".join(
        f'<details class="faq"><summary>{html.escape(q)}</summary><div class="faq-a">{html.escape(a)}</div></details>'
        for q, a in FAQS)
    blog_teaser = "".join(blog_card(p, prefix="") for p in BLOG[:3])
    desc = f"Building your home in Bengaluru? Mount Cable India is one of India's largest Finolex distributors & a multi-brand electrical dealer for {YEARS}+ years. 100% original Finolex wires, all ranges in stock, 3-hour free site delivery across Bangalore. Showrooms in Jayanagar & Chickpete."
    body = head("Mount Cable India | Finolex Distributor & Electrical Dealer, Bengaluru", desc, "index.html", extra_jsonld=faq_jsonld)
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
        <img src="assets/img/banner-finolex-wires.webp" alt="Finolex wires and cables" loading="lazy">
        <div class="fs-floatcard">
          <div class="fs-badge">★ 100% Original · All Ranges In Stock</div>
          <p>Send us your wiring list — we'll prepare a complete Finolex quote and deliver to your site in <strong>3 hours</strong>.</p>
          <a class="btn btn-gold" style="width:100%;justify-content:center" href="quote.html">📷 Get a Finolex Quote</a>
        </div>
      </div>
    </div>
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
      <p class="eyebrow">Free Delivery · All Bengaluru</p>
      <h2>We serve all of Bangalore</h2>
      <p>Wherever your home or site is in Bengaluru, we deliver 100% original material free, within 3 hours of confirmation. Here are some of the localities we cover — tap yours for local stock &amp; pricing:</p>
    </div>
    <div class="area-grid">{areas}</div>
    <p class="area-note">…and every other locality across Bengaluru — North, South, East &amp; West. <a href="quote.html">Tell us your area</a> and we'll deliver to you.</p>
  </div>
</section>

<section id="faq">
  <div class="container narrow">
    <div class="section-head">
      <p class="eyebrow">Questions, Answered</p>
      <h2>Frequently asked questions</h2>
    </div>
    <div class="faq-list">{faq_html}</div>
  </div>
</section>

<section class="bg-soft" id="blog-teaser">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">From Our Blog</p>
      <h2>Guides for home builders</h2>
      <p>Practical advice on wires, brands and buying right for your new home.</p>
    </div>
    <div class="blog-grid">{blog_teaser}</div>
    <div class="center" style="margin-top:30px"><a class="btn btn-outline" href="blog.html">View all guides →</a></div>
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
{review_block()}
"""
    body += footer()
    write("index.html", body)

def build_brand(b):
    slug, name, color, featured, tagline, prods, blurb = b
    chips = "".join(f'<span class="chip">{html.escape(p)}</span>' for p in prods)
    rel_list = [x for x in BRANDS if x[0] != slug][:4]
    related = "".join(brand_tile(x, prefix="../") for x in rel_list)
    products_section = ""
    if slug == "finolex":
        prods = "".join(range_card(r, prefix="../") for r in FINOLEX_RANGE)
        products_section = f"""
<section>
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">In Stock Now</p>
      <h2>Explore every Finolex range</h2>
      <p>Genuine, sealed and ready to deliver across Bangalore the same day. Tap any range for details &amp; a quote.</p>
    </div>
    <div class="prod-grid">{prods}</div>
  </div>
</section>"""
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

{products_section}
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
    is_chick = (slug == "chickpete")
    main = OFFICES[0]  # BVK Iyengar Road showroom
    if is_chick:
        title = f"Finolex Wire Dealer in Chickpet (BVK Iyengar Road), Bangalore | Mount Cable India"
        desc = f"Mount Cable India is a Finolex wire dealer & wholesale distributor in Chickpet, Bangalore — at {main['street']}, 560053. 100% original Finolex wires, all ranges in stock, distributor prices, free 3-hour delivery. {YEARS} years. Call {PHONE}."
        badge = "📍 Our Showroom · BVK Iyengar Road, Chickpet"
        h1 = "Finolex wire dealer in Chickpet — BVK Iyengar Road, Bangalore"
        intro = (f"Our main showroom is right here in Chickpet, at {main['street']}, near Rama Temple (560053). "
                 f"Mount Cable India is one of India's largest Finolex distributors and a wholesale wire dealer in Chickpet — "
                 f"walk in, or get 100% original Finolex wires delivered free across Bangalore within 3 hours.")
    else:
        title = f"Electrical Shop & Finolex Wire Dealer in {name}, Bangalore | Mount Cable India"
        desc = f"Looking for electrical products or a Finolex wire dealer in {name}, Bangalore? Mount Cable India delivers 100% original Finolex wires, switches, cables, pipes & lighting to {name} in 3 hours, free. {YEARS} years of trust. Call {PHONE}."
        badge = f"📍 Free 3-Hour Delivery in {name}"
        h1 = f"Electrical products &amp; Finolex wire dealer in {html.escape(name)}, Bangalore"
        intro = (f"Building or wiring a home in {html.escape(name)}? Mount Cable India delivers 100% original Finolex wires "
                 f"and every electrical essential to {html.escape(name)} and nearby {html.escape(nearby)} — within 3 hours of confirmation, free of cost.")
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), ("Areas We Serve", SITE_URL + "/index.html#areas"), (name, url_for(path))])
    chick_map = (f"""
<section>
  <div class="container">
    <div class="office" style="max-width:760px;margin:0 auto">
      <span class="tag">Visit Our Showroom</span>
      <h3>Mount Cable India — Chickpet</h3>
      <p><span class="pi">📍</span> {html.escape(main['addr'])}</p>
      <p><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
      <p><span class="pi">🕘</span> Mon–Sat, 10:00 AM – 8:00 PM</p>
      <a class="office-dir" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(main['map'])}">🧭 Get directions →</a>
      <iframe class="map-embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={urllib.parse.quote(main['map'])}&output=embed" title="Mount Cable India Chickpet map"></iframe>
    </div>
  </div>
</section>""") if is_chick else ""
    body = head(title, desc, path, css_prefix="../", extra_jsonld=crumbs)
    body += header(prefix="../")
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../index.html#areas">Areas We Serve</a> &nbsp;/&nbsp; {html.escape(name)}</div>
    <span class="badge">{badge}</span>
    <h1>{h1}</h1>
    <p>{intro}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="../quote.html">📷 Upload Your List — Get a Quote</a>
      <a class="btn btn-ghost" href="tel:{PHONE_HREF}">📞 Call {PHONE}</a>
    </div>
  </div>
</section>
{chick_map}

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
    area_opts = "".join(f'<option value="{html.escape(a[1])}">{html.escape(a[1])}</option>' for a in AREAS)
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

<section class="quote-sec">
  <div class="container quote-wrap">
    <form class="qform" action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="_subject" value="New Quote Request — Mount Cable India">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="{SITE_URL}/thank-you.html">

      <div class="qform-head">
        <h2>Request your instant quote</h2>
        <p>Fill in a few details and attach a photo — we'll do the rest.</p>
      </div>

      <label class="dropzone" id="dropzone" for="photo">
        <input type="file" name="attachment" accept="image/*" capture="environment" id="photo" hidden>
        <div class="dz-default">
          <div class="dz-icon">📷</div>
          <div class="dz-title">Tap to add a photo of your list</div>
          <div class="dz-sub">or drag &amp; drop here · JPG / PNG · wiring list, estimate or site photo</div>
        </div>
        <div class="dz-preview" id="preview"></div>
      </label>
      <div class="dz-filerow" id="filerow" hidden>
        <span class="dz-fname" id="fname"></span>
        <button type="button" class="dz-remove" id="removephoto">Remove</button>
      </div>

      <div class="qrow">
        <div class="qfield">
          <label for="qname">Your name <span class="req">*</span></label>
          <div class="qinput"><span class="qic">👤</span><input id="qname" type="text" name="Name" required placeholder="e.g. Ramesh Kumar"></div>
        </div>
        <div class="qfield">
          <label for="qphone">Phone / WhatsApp <span class="req">*</span></label>
          <div class="qinput"><span class="qic">📞</span><input id="qphone" type="tel" name="Phone" required placeholder="10-digit mobile" pattern="[0-9+ ]&#123;10,14&#125;"></div>
        </div>
      </div>

      <div class="qfield">
        <label for="qarea">Your area in Bangalore</label>
        <div class="qinput"><span class="qic">📍</span>
          <select id="qarea" name="Area">
            <option value="" selected disabled>Select your area</option>
            {area_opts}
            <option value="Other / elsewhere in Bangalore">Other / elsewhere in Bangalore</option>
          </select>
        </div>
      </div>

      <div class="qfield">
        <label for="qreq">What do you need?</label>
        <div class="qinput"><textarea id="qreq" name="Requirement" rows="4" placeholder="e.g. Wiring for a 2BHK — Finolex 90M 1.0 / 1.5 / 2.5 sq mm, modular switches, MCB distribution box, LED lights…"></textarea></div>
      </div>

      <button type="submit" class="btn btn-gold qsubmit">Get My Instant Quote →</button>
      <div class="qtrust"><span>🔒 Your details stay private</span><span>·</span><span>⚡ Reply within minutes</span></div>
      <p class="qalt">Prefer to chat? <a href="https://wa.me/{WHATSAPP}?text=Hi,%20here's%20my%20requirement%20for%20a%20quote">Send your photo on WhatsApp</a> or call <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
    </form>

    <aside class="quote-side">
      <div class="qs-card">
        <div class="qs-steps">
          <div class="qs-step"><span class="qs-num">1</span><div><strong>Share your list</strong><br>Snap a photo or type what you need.</div></div>
          <div class="qs-step"><span class="qs-num">2</span><div><strong>Get your quote</strong><br>Genuine material at distributor price.</div></div>
          <div class="qs-step"><span class="qs-num">3</span><div><strong>Delivered in 3 hrs</strong><br>Free to your site. Pay on delivery.</div></div>
        </div>
        <h3>Why builders quote with us</h3>
        <ul class="tick-list">
          <li><strong>{YEARS} years</strong> of trust with Bengaluru home builders.</li>
          <li><strong>100% original Finolex</strong> — every range always in stock.</li>
          <li><strong>Free 3-hour delivery</strong> across all of Bangalore.</li>
          <li><strong>Pay at your site</strong> — cash, UPI, card or transfer.</li>
        </ul>
        <div class="qs-call">
          <span>Need it urgently?</span>
          <a class="btn" style="background:#fff;color:var(--navy);width:100%;justify-content:center" href="tel:{PHONE_HREF}">📞 Call {PHONE}</a>
        </div>
      </div>
    </aside>
  </div>
</section>
<script>
(function(){{
  var input=document.getElementById('photo'),zone=document.getElementById('dropzone'),
      prev=document.getElementById('preview'),frow=document.getElementById('filerow'),
      fname=document.getElementById('fname'),rm=document.getElementById('removephoto');
  function show(f){{
    if(!f){{clear();return;}}
    var r=new FileReader();
    r.onload=function(e){{prev.innerHTML='<img src="'+e.target.result+'" alt="Your uploaded requirement">';
      zone.classList.add('has-file');fname.textContent=f.name;frow.hidden=false;}};
    r.readAsDataURL(f);
  }}
  function clear(){{prev.innerHTML='';zone.classList.remove('has-file');frow.hidden=true;input.value='';}}
  input.addEventListener('change',function(){{show(this.files&&this.files[0]);}});
  rm.addEventListener('click',function(e){{e.preventDefault();clear();}});
  ['dragover','dragenter'].forEach(function(ev){{zone.addEventListener(ev,function(e){{e.preventDefault();zone.classList.add('drag');}});}});
  ['dragleave','dragend','drop'].forEach(function(ev){{zone.addEventListener(ev,function(e){{e.preventDefault();zone.classList.remove('drag');}});}});
  zone.addEventListener('drop',function(e){{var fs=e.dataTransfer&&e.dataTransfer.files;if(fs&&fs.length){{input.files=fs;show(fs[0]);}}}});
}})();
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

def build_blog_index():
    path = "blog.html"
    cards = "".join(blog_card(p, prefix="") for p in BLOG)
    title = "Electrical Guides for Home Builders in Bangalore | Mount Cable India Blog"
    desc = f"Practical guides for building your home: house-wiring wire sizes, Finolex wire prices in Bangalore, FR vs FR-LSH, materials checklists and how to buy 100% original wire. By Mount Cable India, {YEARS} years trusted."
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), ("Blog", url_for(path))])
    body = head(title, desc, path, extra_jsonld=crumbs)
    body += header()
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; Blog</div>
    <span class="badge">📖 Guides for Home Builders</span>
    <h1>Electrical guides for building your home</h1>
    <p>Honest, practical advice on wires, brands, pricing and safety — from one of India's largest Finolex distributors.</p>
  </div>
</section>
<section>
  <div class="container">
    <div class="blog-grid">{cards}</div>
  </div>
</section>
"""
    body += footer()
    write(path, body)

def build_blog_post(p):
    slug, title, excerpt, tag, bodyhtml = p
    path = f"blog/{slug}.html"
    desc = excerpt
    article_ld = ('<script type="application/ld+json">'
        + '{"@context":"https://schema.org","@type":"BlogPosting",'
        + f'"headline":{_json(title)},"description":{_json(excerpt)},'
        + f'"datePublished":"{BLOG_DATE}","dateModified":"{BLOG_DATE}",'
        + f'"image":"{SITE_URL}/assets/img/banner-finolex-wires.jpg",'
        + '"author":{"@type":"Organization","name":"Mount Cable India"},'
        + '"publisher":{"@type":"Organization","name":"Mount Cable India",'
        + f'"logo":{{"@type":"ImageObject","url":"{SITE_URL}/assets/logos/finolex.svg"}}}},'
        + f'"mainEntityOfPage":"{url_for(path)}"}}</script>')
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), ("Blog", SITE_URL + "/blog.html"), (title, url_for(path))])
    rel = [x for x in BLOG if x[0] != slug][:3]
    related = "".join(blog_card(x, prefix="../") for x in rel)
    body = head(f"{title} | Mount Cable India", desc, path, css_prefix="../", extra_jsonld=article_ld + crumbs)
    body += header(prefix="../")
    body += f"""
<article class="post">
  <div class="container narrow">
    <div class="crumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../blog.html">Blog</a> &nbsp;/&nbsp; {html.escape(tag)}</div>
    <span class="blog-tag">{html.escape(tag)}</span>
    <h1>{html.escape(title)}</h1>
    <p class="post-meta">By Mount Cable India · {BLOG_DATE_DISP} · {YEARS} years serving Bengaluru</p>
    <div class="post-body">
      {bodyhtml}
    </div>
    <div class="post-cta">
      <h3>Ready to order for your home?</h3>
      <p>Upload your wiring list for an instant quote — 100% original material, free 3-hour delivery across Bangalore.</p>
      <div class="cta-actions">
        <a class="btn btn-gold" href="../quote.html">📷 Get a Quote</a>
        <a class="btn btn-outline" href="https://wa.me/{WHATSAPP}">💬 WhatsApp {PHONE}</a>
      </div>
    </div>
  </div>
</article>
<section class="bg-soft">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Keep Reading</p><h2>More guides</h2></div>
    <div class="blog-grid">{related}</div>
  </div>
</section>
"""
    body += footer(prefix="../")
    write(path, body)

def build_seo_page(p):
    path = f"{p['slug']}.html"
    areas_html = '<div class="area-grid" style="justify-content:flex-start;margin-top:14px">' + \
        "".join(f'<a class="area-chip" href="areas/{a[0]}.html">{html.escape(a[1])}</a>' for a in AREAS) + "</div>"
    secs = ""
    for h2, htmlc in p["sections"]:
        secs += f"<h2>{html.escape(h2)}</h2>{htmlc.replace('{areas}', areas_html)}"
    faq_html = "".join(
        f'<details class="faq"><summary>{html.escape(q)}</summary><div class="faq-a">{html.escape(a)}</div></details>'
        for q, a in p["faqs"])
    faq_q = ",".join(
        f'{{"@type":"Question","name":{_json(q)},"acceptedAnswer":{{"@type":"Answer","text":{_json(a)}}}}}'
        for q, a in p["faqs"])
    faq_ld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_q}]}}</script>'
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), (p["h1"], url_for(path))])
    body = head(p["title"], p["desc"], path, extra_jsonld=faq_ld + crumbs)
    body += header()
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; {html.escape(p['h1'])}</div>
    <span class="badge">{p['badge']}</span>
    <h1>{html.escape(p['h1'])}</h1>
    <p>{html.escape(p['intro'])}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="quote.html">📷 Upload Your List — Get a Quote</a>
      <a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}">💬 WhatsApp {PHONE}</a>
    </div>
  </div>
</section>
<section>
  <div class="container narrow">
    <div class="post-body">{secs}</div>
  </div>
</section>
<section class="bg-soft">
  <div class="container narrow">
    <div class="section-head"><p class="eyebrow">Questions, Answered</p><h2>Frequently asked questions</h2></div>
    <div class="faq-list">{faq_html}</div>
  </div>
</section>
"""
    body += footer()
    write(path, body)

def range_card(r, prefix=""):
    slug, name, img = r[0], r[1], r[2]
    tagline = r[3]
    return f"""<a class="prod" href="{prefix}finolex/{slug}.html">
      <div class="prod-img"><img src="{prefix}assets/img/{img}" alt="{html.escape(name)}" loading="lazy"></div>
      <h4>{html.escape(name)}</h4>
      <p>{html.escape(tagline)}</p>
      <span class="go">View details →</span>
    </a>"""

def build_finolex_product(r):
    slug, name, img, tagline, grade, coil, sizes, desc = r
    path = f"finolex/{slug}.html"
    img_url = f"{SITE_URL}/assets/img/{img}"
    chips = "".join(f'<span class="chip">{html.escape(s)}</span>' for s in sizes)
    rel = [x for x in FINOLEX_RANGE if x[0] != slug][:4]
    related = "".join(range_card(x, prefix="../") for x in rel)
    title = f"{name} — Buy in Bangalore at Distributor Price | Mount Cable India"
    desc_meta = f"Buy {name} in Bangalore from Mount Cable India, an authorized Finolex distributor. {tagline} 100% original, in stock, free 3-hour delivery. Grade: {grade}, coil: {coil}."
    prod_ld = ('<script type="application/ld+json">'
        + '{"@context":"https://schema.org","@type":"Product",'
        + f'"name":{_json(name)},"image":"{img_url}","description":{_json(desc)},'
        + '"brand":{"@type":"Brand","name":"Finolex"},"category":"Electrical Wire & Cable",'
        + '"offers":{"@type":"Offer","priceCurrency":"INR","availability":"https://schema.org/InStock",'
        + f'"seller":{{"@type":"Organization","name":"Mount Cable India"}},"url":"{url_for(path)}"}}}}</script>')
    crumbs = breadcrumb_jsonld([("Home", SITE_URL + "/"), ("Finolex", SITE_URL + "/brands/finolex.html"), (name, url_for(path))])
    body = head(title, desc_meta, path, css_prefix="../", extra_jsonld=prod_ld + crumbs)
    body += header(prefix="../")
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../brands/finolex.html">Finolex</a> &nbsp;/&nbsp; {html.escape(name)}</div>
    <span class="badge">★ 100% Original · In Stock</span>
    <h1>{html.escape(name)}</h1>
    <p>{html.escape(tagline)}</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="../quote.html">📷 Get a Quote</a>
      <a class="btn btn-ghost" href="https://wa.me/{WHATSAPP}?text=Hi,%20I%20need%20a%20quote%20for%20{urllib.parse.quote(name)}">💬 WhatsApp {PHONE}</a>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="prose">
      <div class="pd-imgwrap"><img src="../assets/img/{img}" alt="{html.escape(name)}" loading="lazy"></div>
      <h2>About {html.escape(name)}</h2>
      <p>{html.escape(desc)}</p>
      <h2 style="margin-top:30px">Available sizes &amp; variants</h2>
      <div class="chip-row">{chips}</div>
      <ul class="tick-list" style="margin-top:24px">
        <li><strong>Grade:</strong> {html.escape(grade)}</li>
        <li><strong>Coil / pack:</strong> {html.escape(coil)}</li>
        <li><strong>100% original Finolex</strong> — sealed &amp; warranty-backed, in stock now.</li>
        <li><strong>Free 3-hour delivery</strong> across Bangalore · pay at your site.</li>
      </ul>
    </div>
    <aside>
      <div class="side-card">
        <h3>Get a price for {html.escape(name)}</h3>
        <p class="muted" style="font-size:14.5px;margin:6px 0 0">Distributor pricing · all gauges in stock.</p>
        <div class="row"><span class="pi">📷</span> <a href="../quote.html">Upload your list for a quote</a></div>
        <div class="row"><span class="pi">💬</span> <a href="https://wa.me/{WHATSAPP}">WhatsApp {PHONE}</a></div>
        <div class="row"><span class="pi">📞</span> <a href="tel:{PHONE_HREF}">{PHONE}</a></div>
        <a class="btn btn-gold" style="width:100%;justify-content:center;margin-top:10px" href="../quote.html">Request a Quote</a>
      </div>
    </aside>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head"><p class="eyebrow">More Finolex Ranges</p><h2>Explore the full range</h2></div>
    <div class="prod-grid">{related}</div>
  </div>
</section>
"""
    body += footer(prefix="../")
    write(path, body)

def build_review():
    path = "review.html"
    title = "Review Mount Cable India on Google | Finolex Distributor, Bengaluru"
    desc = "Leave a Google review for Mount Cable India — scan the QR code or tap to rate your experience. It helps other Bangalore home builders find genuine Finolex wires."
    body = head(title, desc, path)
    body += header()
    body += f"""
<section class="bp-hero">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; Review Us</div>
    <span class="badge">★ Your Feedback Matters</span>
    <h1>Review us on Google</h1>
    <p>Thank you for choosing Mount Cable India! A quick review helps other home builders in Bangalore buy genuine Finolex wires with confidence.</p>
  </div>
</section>
<section>
  <div class="container narrow center">
    <div class="qr-big"><img src="assets/review-qr.svg" alt="Scan to review Mount Cable India on Google" width="240" height="240"></div>
    <a class="btn btn-gold" style="font-size:16.5px;padding:15px 30px" href="{REVIEW_URL}" target="_blank" rel="noopener">★ Write a Google Review</a>
    <div class="rev-steps">
      <div class="rev-step"><span class="qs-num">1</span> Scan the QR with your phone camera, or tap the button.</div>
      <div class="rev-step"><span class="qs-num">2</span> Tap the stars and write a quick line about your experience.</div>
      <div class="rev-step"><span class="qs-num">3</span> Post — and thank you! It means a lot to us. 🙏</div>
    </div>
  </div>
</section>
"""
    body += footer()
    write(path, body)

def build_sitemap():
    paths = ["index.html", "quote.html", "blog.html", "review.html", "thank-you.html"]
    paths += [f"{p['slug']}.html" for p in SEO_PAGES]
    paths += [f"{c[0]}.html" for c in CATEGORIES]
    paths += [f"brands/{b[0]}.html" for b in BRANDS]
    paths += [f"finolex/{r[0]}.html" for r in FINOLEX_RANGE]
    paths += [f"areas/{a[0]}.html" for a in AREAS]
    paths += [f"blog/{p[0]}.html" for p in BLOG]
    urls = ""
    for p in paths:
        pr = "1.0" if p == "index.html" else ("0.9" if p in ("quote.html", "blog.html") else "0.8")
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
    build_blog_index()
    for p in BLOG: build_blog_post(p)
    for p in SEO_PAGES: build_seo_page(p)
    for r in FINOLEX_RANGE: build_finolex_product(r)
    build_review()
    build_sitemap()
    total = 1 + len(BRANDS) + len(CATEGORIES) + len(AREAS) + 3 + len(BLOG) + len(SEO_PAGES) + len(FINOLEX_RANGE)
    print(f"Done — {total} pages + sitemap.xml + robots.txt")
    print(f"  1 home, {len(BRANDS)} brands, {len(CATEGORIES)} categories, {len(AREAS)} areas, "
          f"{len(SEO_PAGES)} Finolex SEO pages, blog index + {len(BLOG)} posts, quote, thank-you")
