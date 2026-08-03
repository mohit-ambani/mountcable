# -*- coding: utf-8 -*-
"""Finolex price-keyword blog cluster, generated from the real MRP list.

Keyword volumes from the owner's Google Keyword Planner export (Aug 2026):
  finolex wire price ...................... 5,000/mo  (High competition)
  finolex wire price list ................. 5,000/mo
  finolex 2.5 mm wire price ............... 5,000/mo
  finolex 1.5 mm wire price ............... 5,000/mo
  cost of finolex wire .................... 5,000/mo
  finolex 1 mm / 1 sq mm / 0.75 / 0.5 ..... 500/mo each
  4 mm / 6 mm finolex wire price .......... 500/mo each
  finolex 1.5 mm wire price 90 / 180 meter  500/mo each

Every price on every page comes from data_finolex_mrp.py, so the blogs, the buy
page and the price-list pages can never drift apart. Discounts are always
published NET. The discount percentage is never shown — see data_finolex_mrp.py.
"""

from data_finolex_mrp import (HOUSE_WIRE, LONG_LEN, EFFECTIVE_FROM, TAX_NOTE,
                              offer, house_wire_rows, FLEXIBLE, FLEX_COLS)

D = ("2026-08-03", "August 3, 2026")
W = "https://wa.me/918867676700"
PH = "88676 76700"

# Per-size editorial: what it is used for, protection, and house quantity.
SIZE_INFO = {
    "0.75": dict(use="light points, fan points and low-load lighting circuits",
                 mcb="6A, Curve B", rooms="lighting circuits in smaller rooms",
                 qty="3–5 coils in a 2BHK", note="Below 1.0 sq mm is only for lighting; never use it for a socket circuit."),
    "1.0":  dict(use="light and fan points, and short 6A lighting runs",
                 mcb="6A, Curve B", rooms="ceiling lights, fans, wall lights",
                 qty="3–4 coils in a 2BHK, 5–7 in a 3BHK", note="The most common lighting-circuit size in Indian homes."),
    "1.5":  dict(use="light circuits and 6A socket points",
                 mcb="6A–10A, Curve B", rooms="lighting, bedroom sockets, fan regulators",
                 qty="4–6 coils in a 2BHK, 7–10 in a 3BHK", note="The highest-volume house wire size — most homes use more 1.5 than anything else."),
    "2.5":  dict(use="16A power sockets, kitchen points and geysers",
                 mcb="16A, Curve C", rooms="kitchen, fridge, washing machine, geyser",
                 qty="3–5 coils in a 2BHK, 5–8 in a 3BHK", note="Anything intended for a fridge, microwave or washing machine belongs on 2.5, not 1.5."),
    "4.0":  dict(use="air conditioners, larger geysers and heavy appliance circuits",
                 mcb="20A, Curve C", rooms="AC points, 3000W geysers, ovens",
                 qty="1–2 coils in a 2BHK, 2–4 in a 3BHK", note="Every AC and large geyser should have its own dedicated 4.0 sq mm circuit."),
    "6.0":  dict(use="the mains run from the energy meter to the distribution board",
                 mcb="40A–63A incomer", rooms="meter to DB, sub-mains to a floor DB",
                 qty="1 coil in a 2BHK, 1–2 in a 3BHK", note="Often the single longest run in the house, so check voltage drop as well as current."),
}

GRADE_NOTE = ("<p><strong>Reading the grades.</strong> Finolex <em>Silver</em> and <em>Gold</em> are both 90 m coils — "
              "Silver is the standard FR line and Gold sits above it. <em>FR-LSH</em> is flame retardant low smoke and "
              "halogen, which matters in flats, stairwells and any enclosed escape route, and costs a little more. "
              "FR and FR-LSH are also made in 180 m coils, and in a long coil that is 300 m for 1.0&ndash;2.5 sq mm and "
              "200 m for 4.0 and 6.0 sq mm. Longer coils work out cheaper per metre and waste less at joints.</p>")

DISCOUNT_NOTE = (
    "<h2>What you get at this price</h2>"
    "<p><strong>100% genuine Finolex stock, verified by you before you pay.</strong> Every carton carries a QR on the "
    "outside and a second QR inside the box. Scan both at your own site: a genuine coil passes both, while a genuine "
    "carton refilled with duplicate wire passes only the outer scan. Anything that does not verify goes back on the "
    "vehicle and you pay nothing for it.</p>"
    f"<p>{TAX_NOTE} Larger quantities are priced better than the rates shown. Use our quote as your reference price "
    "anywhere in Bangalore — there is no obligation to buy from us, and plenty of people ask purely to cross-check "
    "another shop.</p>")

CTA = (f'<p class="muted"><strong>Want today\'s confirmed rate?</strong> Send your list to '
       f'<a href="{W}">WhatsApp {PH}</a> for an itemised quote within 60 minutes — free next-day delivery across '
       f'Bangalore, pay on delivery, and every coil QR-verifiable at your site. No obligation to buy: plenty of '
       f'people use our quote purely to cross-check another shop.</p>')


def _rs(n):
    return "&#8377;" + format(int(n), ",d")


def _size_table(size):
    rows = "".join(
        f"<tr><td>{label}</td><td>{length}</td><td><strong>{_rs(price)}</strong></td></tr>"
        for label, length, mrp, price in house_wire_rows(size))
    return ('<div class="ptable-wrap"><table class="ptable">'
            '<thead><tr><th>Finolex range</th><th>Coil</th><th>Our price</th></tr></thead>'
            f"<tbody>{rows}</tbody></table></div>"
            f'<p class="ptable-note">{TAX_NOTE} Larger quantities are priced better than the rates shown.</p>')


def _all_sizes_table():
    rows = ""
    for size, d in HOUSE_WIRE.items():
        rows += (f"<tr><td>{size} sq mm</td>"
                 f"<td><strong>{_rs(offer(d['silver'],'silver'))}</strong></td>"
                 f"<td><strong>{_rs(offer(d['gold'],'gold'))}</strong></td>"
                 f"<td><strong>{_rs(offer(d['ultra'],'ultra'))}</strong></td>"
                 f"<td><strong>{_rs(offer(d['frls90'],'frls90'))}</strong></td></tr>")
    return ('<div class="ptable-wrap"><table class="ptable">'
            '<thead><tr><th>Size</th><th>Silver FR</th><th>Gold FR</th><th>Ultra</th><th>FR-LSH</th></tr></thead>'
            f"<tbody>{rows}</tbody></table></div>"
            f'<p class="ptable-note">All 90 m coils. {TAX_NOTE}</p>')


def _size_post(size, slug, title, excerpt, keywords_extra, hero):
    """One price page per conductor size, with size-specific engineering context."""
    info = SIZE_INFO[size]
    d = HOUSE_WIRE[size]
    silver, gold, frls = offer(d["silver"]), offer(d["gold"]), offer(d["frls90"])
    body = f"""<p><strong>A Finolex {size} sq mm 90 m coil costs {_rs(d['silver'])} at MRP for the Silver FR range and
{_rs(d['gold'])} for Gold FR. At Mount Cable India you pay from {_rs(silver)} and {_rs(gold)} respectively —
a minimum our standard rate, with larger quantities earning more.</strong> FR-LSH in the same size is
{_rs(d['frls90'])} at MRP and from {_rs(frls)} with us. Prices below are from the Finolex list effective {EFFECTIVE_FROM}.</p>

<h2>Finolex {size} sq mm price — every pack</h2>
{_size_table(size)}
{GRADE_NOTE}

<h2>What {size} sq mm wire is used for</h2>
<p>Finolex {size} sq mm is the size for <strong>{info['use']}</strong>. In a normal house that means {info['rooms']}.
The matching protection is a <strong>{info['mcb']}</strong> breaker at the distribution board.</p>
<p>{info['note']}</p>
<p>Typical requirement: <strong>{info['qty']}</strong>, though the real number depends on your point count and the run
length from the distribution board. Work out your own quantity with the
<a href="../tools/wire-quantity-calculator.html">wire quantity calculator</a>, and confirm the size for each circuit
with the <a href="../tools/wire-size-calculator.html">wire size calculator</a> — a long run can need the next size up
purely because of voltage drop.</p>

{DISCOUNT_NOTE}

<h2>Why the price moves</h2>
<p>A wire coil is mostly copper, and copper is an internationally traded commodity priced in dollars. Finolex revises
MRP periodically as copper and the rupee move, so the figures above are accurate to the {EFFECTIVE_FROM} list and will
change again. That is also why no honest seller publishes a single fixed rate — the full explanation is in
<a href="copper-price-and-wire-rates-explained.html">why wire prices keep changing</a>.</p>

<h2>Before you pay for any {size} sq mm coil</h2>
<ul>
<li>Buy in <strong>your own name</strong>, not through a with-material contract — see
<a href="electrician-retailer-nexus-duplicate-wires.html">how duplicate wire reaches your home</a>.</li>
<li>Insist on <strong>sealed cartons</strong>. Loose or cut wire carries no batch, no QR and no warranty route.</li>
<li>Scan the <a href="original-finolex-wire-outer-qr-code.html">outer QR on the carton</a> and the
<a href="original-finolex-wire-inner-qr-code.html">inner QR inside the box</a>. A refilled carton passes the first
and fails the second.</li>
<li>Check the printed markings along the insulation for even spacing and crisp characters.</li>
<li>Take a <strong>GST invoice in your own name</strong> listing brand, size, grade and quantity.</li>
</ul>

<p>Order any size at our standard rate on our <a href="../buy-finolex-wires.html">buy Finolex wires page</a>.</p>
{CTA}"""
    faqs = [
        (f"What is the price of Finolex {size} sq mm wire?",
         f"A 90 m coil is {_rs(d['silver']).replace('&#8377;','Rs ')} at MRP for Silver FR and {_rs(d['gold']).replace('&#8377;','Rs ')} for Gold FR, on the list effective {EFFECTIVE_FROM}. Mount Cable India sells from Rs {silver:,} and Rs {gold:,} respectively, a minimum our standard rate, with larger quantities earning more."),
        (f"What is Finolex {size} sq mm wire used for?",
         f"It is the size for {info['use']} — in a normal house, {info['rooms']}. The matching protection is a {info['mcb']} breaker. {info['note']}"),
        (f"How many coils of {size} sq mm wire does a house need?",
         f"Typically {info['qty']}. The real number depends on your point count and the run length from the distribution board, so use the wire quantity calculator rather than a rule of thumb, and remember that a long run may need the next size up because of voltage drop."),
        (f"Is our standard rate a genuine discount?",
         f"Yes, because MRP is not the market rate. Finolex MRP is set well above the price wire actually transacts at in the trade, so our standard rate lands at roughly the normal Bangalore rate for genuine stock rather than below it. A seller quoting 15% or more below the real market rate is a different matter, and that does signal copper shortfall, a short coil or counterfeit material."),
        (f"What is the difference between Finolex Silver, Gold and FR-LSH in {size} sq mm?",
         f"Silver and Gold are both 90 m coils of flame-retardant wire, with Gold the higher line — {_rs(d['gold']).replace('&#8377;','Rs ')} against {_rs(d['silver']).replace('&#8377;','Rs ')} at MRP. FR-LSH at {_rs(d['frls90']).replace('&#8377;','Rs ')} is flame retardant low smoke and halogen, which matters in flats and enclosed stairwells where smoke, not flame, is what disables people."),
        ("How do I check the coil I receive is genuine?",
         "Buy sealed cartons, scan the QR printed on the outside of the carton and then open the box and scan the second QR inside it. A genuine coil passes both; a genuine carton refilled with duplicate wire passes only the outer scan. Then check the printed markings along the insulation and take a GST invoice in your own name."),
    ]
    return (slug, title, excerpt, "Pricing", body, D, faqs, hero, None)


BLOG_FINOLEX_PRICES = [
    _size_post("2.5", "finolex-2-5-mm-wire-price",
               "Finolex 2.5 mm Wire Price in Bangalore (2026): Current Prices",
               "Finolex 2.5 sq mm wire price — prices for Silver, Gold, FR and FR-LSH in 90 m, 180 m and 300 m coils, and what 2.5 sq mm is actually used for.",
               "finolex 2.5 mm wire price, 2.5 sq mm finolex wire price, 2.5 finolex wire price, 2.5 mm wire price finolex",
               ("wire-coils-warehouse-electrical-distributor.jpg", "Finolex 2.5 sq mm house wire coils stocked at a Bangalore distributor")),
    _size_post("1.5", "finolex-1-5-mm-wire-price",
               "Finolex 1.5 mm Wire Price in Bangalore (2026): Current Prices",
               "Finolex 1.5 sq mm wire price — prices for Silver, Gold and FR-LSH across 90 m, 180 m and 300 m coils, and how many coils a house needs.",
               "finolex 1.5 mm wire price, 1.5 sq mm finolex wire price, 1.5 mm wire finolex price, finolex 1.5 mm wire price 90 meter, finolex 1.5 mm wire price 180 meter",
               ("electrician-hands-stripping-wire-closeup.jpg", "Finolex 1.5 sq mm house wire being prepared for a lighting circuit")),
    _size_post("1.0", "finolex-1-mm-wire-price",
               "Finolex 1 mm Wire Price in Bangalore (2026): Current Prices",
               "Finolex 1 sq mm wire price — prices across Silver, Gold and FR-LSH in every coil length, and where 1.0 sq mm belongs in a house.",
               "finolex 1 mm wire price, 1 mm finolex wire price, 1 sq mm finolex wire price, finolex 1.0 mm wire price, finolex 1.0 mm wire price 90 meter",
               ("electricians-installing-conduit-ceiling.jpg", "Finolex 1 sq mm wire being pulled into conduit for lighting circuits")),
    _size_post("4.0", "finolex-4-mm-wire-price",
               "Finolex 4 mm Wire Price in Bangalore (2026): AC and Geyser Circuits",
               "Finolex 4 sq mm wire price across every pack, and why air conditioners and large geysers need this size on a dedicated circuit.",
               "4 mm finolex wire price, 4 sq mm finolex wire price, 4mm finolex wire price, 4 sq mm wire finolex price",
               ("electrician-installing-mcb-distribution-board.jpg", "A 4 sq mm dedicated circuit being wired into a distribution board")),
    _size_post("6.0", "finolex-6-mm-wire-price",
               "Finolex 6 mm Wire Price in Bangalore (2026): Mains and Sub-Mains",
               "Finolex 6 sq mm wire price across all packs, and why the meter-to-DB run needs this size and a voltage-drop check.",
               "6mm finolex wire price, 6 sq mm finolex wire price, finolex 6 mm wire price bangalore",
               ("house-under-construction-conduit-wiring.jpg", "Heavy gauge Finolex mains cable run from the meter to the distribution board")),
]


# ---------------------------------------------------------------- hub pages
_hub_body = f"""<p><strong>The full Finolex wire price list below is taken from the manufacturer's MRP sheet effective
{EFFECTIVE_FROM}, with Mount Cable India's price alongside it at a minimum our standard rate.</strong> Larger
quantities earn more. Every figure can be checked against the photographed MRP sheet on our
<a href="../buy-finolex-wires.html">buy Finolex wires page</a>.</p>

<h2>Finolex house wire price list — 90 m coils</h2>
{_all_sizes_table()}
{GRADE_NOTE}

<h2>Every pack, size by size</h2>
""" + "".join(
    f"<h3>Finolex {s} sq mm</h3>{_size_table(s)}" for s in HOUSE_WIRE
) + f"""
{DISCOUNT_NOTE}

<h2>Which size goes where</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Size</th><th>Use</th><th>MCB</th></tr></thead><tbody>
""" + "".join(
    f"<tr><td>{s} sq mm</td><td>{SIZE_INFO[s]['use']}</td><td>{SIZE_INFO[s]['mcb']}</td></tr>"
    for s in HOUSE_WIRE
) + f"""</tbody></table></div>
<p>Size each circuit properly with the <a href="../tools/wire-size-calculator.html">wire size calculator</a> and work
out coil quantities with the <a href="../tools/wire-quantity-calculator.html">wire quantity calculator</a>.</p>

<h2>Buying safely at these prices</h2>
<ul>
<li>Buy in your own name rather than on a with-material contract.</li>
<li>Sealed cartons only — no loose or cut wire.</li>
<li>Scan the <a href="original-finolex-wire-outer-qr-code.html">outer QR</a> and the
<a href="original-finolex-wire-inner-qr-code.html">inner QR</a> on every coil before paying.</li>
<li>Take a GST invoice listing brand, size, grade and quantity.</li>
</ul>
{CTA}"""

_hub_faqs = [
    ("What is the Finolex wire price list for 2026?",
     f"On the manufacturer's list effective {EFFECTIVE_FROM}, a 90 m Silver FR coil runs from Rs {HOUSE_WIRE['1.0']['silver']:,} for 1.0 sq mm to Rs {HOUSE_WIRE['6.0']['silver']:,} for 6.0 sq mm, with Gold FR and FR-LSH priced above that and 180 m and 300 m coils priced proportionally. Mount Cable India sells every line at a minimum our standard rate off those MRP figures."),
    ("How much does Finolex wire cost in Bangalore?",
     f"At a minimum our standard rate, a 90 m Silver FR coil works out from about Rs {offer(HOUSE_WIRE['1.0']['silver']):,} for 1.0 sq mm, Rs {offer(HOUSE_WIRE['1.5']['silver']):,} for 1.5 sq mm and Rs {offer(HOUSE_WIRE['2.5']['silver']):,} for 2.5 sq mm. Larger quantities earn a bigger discount, so send your full list for an itemised quote."),
    ("Why is Finolex MRP higher than the selling price?",
     "Because MRP in Indian wire is a ceiling rather than a transacting price — it is set well above the rate wire actually changes hands at in the trade. Every seller quotes below MRP; the number that matters is the final rate, which is what we publish. Compare our figure against any other quotation in the city."),
    ("What is the difference between Finolex Silver and Gold?",
     f"Both are 90 m coils of flame-retardant house wire; Gold is the higher line and carries a higher MRP — for example Rs {HOUSE_WIRE['1.5']['gold']:,} against Rs {HOUSE_WIRE['1.5']['silver']:,} in 1.5 sq mm. FR-LSH is a separate low-smoke, halogen-reduced grade that matters in flats and enclosed stairwells."),
    ("Which Finolex coil length is most economical?",
     "Longer coils cost less per metre and waste less at joints. FR and FR-LSH come in 180 m as well as 90 m, and in a long coil that is 300 m for 1.0 to 2.5 sq mm and 200 m for 4.0 and 6.0 sq mm. If a single size needs four or more 90 m coils, ask for the longer pack."),
    ("Do these prices include GST?",
     "Ask when you request the quote — our WhatsApp quotation states the tax position explicitly, itemised by line, so there is nothing to discover at delivery. Always take a GST invoice in your own name naming brand, size, grade and quantity."),
]

BLOG_FINOLEX_PRICES += [
    ("finolex-wire-price-list-bangalore-2026",
     "Finolex Wire Price List 2026: Full Current Prices in Bangalore",
     f"The complete Finolex wire price list effective {EFFECTIVE_FROM} — Prices for Silver, Gold, Ultra, FR and FR-LSH in 90 m, 180 m, 200 m and 300 m coils, with Mount Cable India's price at our standard rate.",
     "Pricing", _hub_body, D, _hub_faqs,
     ("wire-coils-warehouse-electrical-distributor.jpg",
      "Finolex wire coils across all sizes stocked at Mount Cable India in Bangalore"), None),

    ("cost-of-finolex-wire-for-a-house",
     "Cost of Finolex Wire for a House in Bangalore (2026)",
     "What Finolex wire actually costs to wire a 2BHK, 3BHK or villa — coil quantities by size, current prices, and the total wire budget.",
     "Pricing",
     f"""<p><strong>Wiring a 2BHK with genuine Finolex costs roughly &#8377;28,000&ndash;&#8377;45,000 in wire alone at our
our standard rate-off-MRP rate, and a 3BHK &#8377;48,000&ndash;&#8377;78,000.</strong> The spread comes from grade
(Silver, Gold or FR-LSH), coil length and how many air conditioner circuits the house has. Below is the build-up, size
by size, so you can price your own list rather than accept a lump sum.</p>

<h2>What a house actually consumes</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Size</th><th>2BHK</th><th>3BHK</th><th>Silver 90 m at our rate</th></tr></thead><tbody>
""" + "".join(
    f"<tr><td>{s} sq mm</td><td>{SIZE_INFO[s]['qty'].split(',')[0]}</td>"
    f"<td>{SIZE_INFO[s]['qty'].split(',')[-1].strip() if ',' in SIZE_INFO[s]['qty'] else SIZE_INFO[s]['qty']}</td>"
    f"<td>{_rs(offer(HOUSE_WIRE[s]['silver']))}</td></tr>"
    for s in HOUSE_WIRE
) + f"""</tbody></table></div>
<p class="ptable-note">Earth wire is additional — budget 2&ndash;3 coils for a 2BHK and 4&ndash;5 for a 3BHK.</p>

<h2>Worked totals</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>House</th><th>Silver FR</th><th>Gold FR</th><th>FR-LSH</th></tr></thead><tbody>
<tr><td>2BHK, ~70 points</td><td>&#8377;28,000&ndash;&#8377;36,000</td><td>&#8377;31,000&ndash;&#8377;40,000</td><td>&#8377;30,000&ndash;&#8377;45,000</td></tr>
<tr><td>3BHK, ~110 points</td><td>&#8377;48,000&ndash;&#8377;62,000</td><td>&#8377;53,000&ndash;&#8377;68,000</td><td>&#8377;52,000&ndash;&#8377;78,000</td></tr>
<tr><td>Villa / duplex</td><td>&#8377;85,000&ndash;&#8377;1,40,000</td><td>&#8377;95,000&ndash;&#8377;1,55,000</td><td>&#8377;95,000&ndash;&#8377;1,70,000</td></tr>
</tbody></table></div>
<p>Wire is only part of the electrical budget — conduit, switches, switchgear, earthing, fans and lights are separate.
The whole picture is in <a href="electrical-material-list-for-new-house-bangalore.html">the complete electrical material
list</a> and the <a href="../tools/house-wiring-cost-calculator.html">house wiring cost calculator</a>.</p>

<h2>Where people overspend</h2>
<ul>
<li><strong>Buying 90 m coils when a size needs four or more.</strong> The 180 m and 300 m packs cost less per metre.</li>
<li><strong>Over-ordering.</strong> Buy about 90% of the estimate and top up — we deliver next day and pick up surplus free.</li>
<li><strong>Paying for coils the contractor keeps.</strong> Order in your own name; leftover wire is expensive and it walks.</li>
<li><strong>Paying FR-LSH prices everywhere</strong> when it matters most on enclosed runs, stairwells and common areas.</li>
</ul>

{DISCOUNT_NOTE}
{CTA}""",
     D,
     [("How much does Finolex wire cost for a 2BHK house?",
       f"Roughly Rs 28,000 to 45,000 in wire alone at a our standard rate rate, depending on whether you choose Silver, Gold or FR-LSH and how many air conditioner circuits the house has. That is wire only — conduit, switches, switchgear, earthing, fans and lights are separate."),
      ("How much Finolex wire does a 3BHK need?",
       "Typically 24 to 36 coils of 90 m across all sizes for around 110 points, including earth wire. The exact number depends on point count, floor layout and the distance from the meter to the distribution board, which alone can consume a full coil of 6.0 sq mm."),
      ("How can I reduce the wire cost without compromising safety?",
       "Buy the longer 180 m or 300 m coils where a size needs four or more packs, order about 90% of the estimate and top up, and buy in your own name so leftover coils stay yours. Never economise by dropping the size on air conditioner, geyser or mains circuits."),
      ("Is FR-LSH worth the extra cost throughout the house?",
       "It matters most on enclosed runs, stairwells, corridors and common areas, where smoke rather than flame is what disables people. Many builders specify FR-LSH on those circuits and standard FR elsewhere, which captures most of the benefit at a lower total."),
      ("Does the wire cost include labour?",
       "No. These are material figures only. Wiring labour in Bangalore is usually quoted per point or as a percentage of material value, and you should ask for it as a separate line so you can compare contractors properly."),
      ("How do I get an exact figure for my house?",
       f"Send your list or your contractor's estimate to WhatsApp {PH} and you will have an itemised quote within 60 minutes, at a minimum our standard rate with more on larger quantities. There is no obligation to buy.")],
     ("happy-homeowner-couple-new-house-wiring.jpg",
      "Homeowners planning the Finolex wire budget for their new house in Bangalore"), None),
]


def _flex_rows(size):
    vals = FLEXIBLE[size]
    return "".join(
        f"<tr><td>{FLEX_COLS[i]}</td><td><strong>{_rs(offer(v))}</strong></td></tr>"
        for i, v in enumerate(vals) if v)


BLOG_FINOLEX_PRICES += [
    ("finolex-0-75-mm-wire-price",
     "Finolex 0.75 mm Wire Price (2026): Why It Is Not a House-Wire Size",
     "Finolex 0.75 sq mm and 0.5 sq mm prices — these are flexible-cable sizes, not house wire. Current prices, plus what these sizes are and are not for.",
     "Pricing",
     f"""<p><strong>Finolex does not make 0.75 sq mm or 0.5 sq mm in the house-wire range. These are flexible
multi-core cable sizes, used for appliance leads, extension boards and light fittings — not for wiring a wall.</strong>
A 0.75 sq mm single-core flexible coil is {_rs(FLEXIBLE['0.75'][0])} at MRP and from
{_rs(offer(FLEXIBLE['0.75'][0]))} with us, a minimum our standard rate off. If you were quoted 0.75 sq mm for a lighting
circuit in a house, that is a specification error worth correcting before the wire goes into the wall.</p>

<h2>Finolex 0.75 sq mm flexible cable price</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Construction</th><th>Our price</th></tr></thead>
<tbody>{_flex_rows('0.75')}</tbody></table></div>

<h2>Finolex 0.5 sq mm flexible cable price</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Construction</th><th>Our price</th></tr></thead>
<tbody>{_flex_rows('0.5')}</tbody></table></div>

<h2>What these sizes are actually for</h2>
<ul>
<li><strong>Appliance leads and repairs</strong> — the flexible lead on a lamp, a fan or a small appliance.</li>
<li><strong>Extension boards</strong> made up on site.</li>
<li><strong>Light fittings</strong>, where the fitting's own tail connects to the point.</li>
<li><strong>Control and signal wiring</strong> in panels.</li>
</ul>
<p>What they are <strong>not</strong> for is a concealed circuit in a wall. The smallest size used for house lighting
circuits in India is 1.0 sq mm, and most homes use 1.5 sq mm for lighting and 6A socket points. See
<a href="finolex-1-mm-wire-price.html">1 sq mm prices</a> and
<a href="finolex-1-5-mm-wire-price.html">1.5 sq mm prices</a>, or size each circuit properly with the
<a href="../tools/wire-size-calculator.html">wire size calculator</a>.</p>

<h2>Flexible cable is not the same product as house wire</h2>
<p>House wire is single-core with relatively few strands, built to sit still inside conduit for decades. Flexible cable
has many fine strands and a tougher sheath so it can bend and be handled. Using flexible where house wire belongs, or
the reverse, is a common and avoidable mistake — the difference is explained in
<a href="flexible-cable-submersible-pump-cable-guide.html">the flexible and submersible cable guide</a>.</p>

{DISCOUNT_NOTE}
{CTA}""",
     D,
     [("What is the price of Finolex 0.75 mm wire?",
       f"A 0.75 sq mm single-core flexible coil is Rs {FLEXIBLE['0.75'][0]:,} at MRP and from Rs {offer(FLEXIBLE['0.75'][0]):,} at Mount Cable India, a minimum our standard rate off. Note that 0.75 sq mm is a flexible-cable size — Finolex does not make it in the house-wire range."),
      ("Is 0.75 sq mm wire suitable for house wiring?",
       "No. It is a flexible-cable size for appliance leads, extension boards and light fittings, not for concealed circuits in a wall. The smallest size used for house lighting circuits in India is 1.0 sq mm, and most homes use 1.5 sq mm for lighting and 6A socket points."),
      ("What is the price of Finolex 0.5 mm wire?",
       f"A 0.5 sq mm single-core flexible coil is Rs {FLEXIBLE['0.5'][0]:,} at MRP and from Rs {offer(FLEXIBLE['0.5'][0]):,} with us. Like 0.75 sq mm it is a flexible-cable size for leads and fittings rather than a house-wiring size."),
      ("What is the difference between flexible cable and house wire?",
       "House wire is single-core with relatively few strands and is built to sit still inside conduit for decades. Flexible cable has many fine strands and a tougher sheath so it can bend and be handled repeatedly. They are different products for different jobs and are not interchangeable."),
      ("My electrician quoted 0.75 sq mm for lighting — is that wrong?",
       "It is a specification error worth correcting before the wire goes into the wall. Indian house lighting circuits use 1.0 sq mm at minimum and more commonly 1.5 sq mm. Concealed circuits should be single-core house wire of the correct size, protected by a matching MCB."),
      ("Do you stock Finolex flexible cable in Bangalore?",
       f"Yes, in 1, 2, 3 and 4 core across 0.5 to 16 sq mm, all at a minimum our standard rate. Send your list to WhatsApp {PH} for an itemised quote within 60 minutes, with free next-day delivery across Bangalore.")],
     ("shop-owner-explaining-wire-quality.jpg", "Explaining the difference between flexible cable and house wire at an electrical counter"),
     None),
]
