# -*- coding: utf-8 -*-
"""2026 blog expansion for Mount Cable India — brands, electrical products and
pricing guides. Tuple format used by build.py:

    (slug, title, excerpt, tag, body_html, (iso_date, display_date), faqs, hero)

faqs = [(question, answer), ...]   hero = (image filename in assets/img/people, alt text)
"""

D = ("2026-08-01", "August 1, 2026")

W = "https://wa.me/918867676700"
PH = "88676 76700"


def _cta(text="Send your list on WhatsApp for an exact quote within 60 minutes."):
    return (f'<p class="muted"><strong>{text}</strong> '
            f'Approximate ranges on this page are for planning; WhatsApp <a href="{W}">{PH}</a> '
            f'for today\'s firm rate, with no pressure to buy.</p>')


BLOG_2026 = [

# ---------------------------------------------------------------- 1
("electrical-material-list-for-new-house-bangalore",
 "The Complete Electrical Material List for a New House in Bangalore",
 "Everything you actually need to buy to wire a new house — wires, conduit, switches, MCBs, DB, earthing, fans and lights — with approximate quantities and budget bands for 2BHK and 3BHK homes.",
 "Buying Guide",
 """<p>Most first-time house builders in Bangalore discover the electrical list only when the contractor hands them a scribbled page and asks for money. This guide is that list, written out properly, so you know what you are buying before anyone quotes you for it.</p>

<h2>The seven things a house needs electrically</h2>
<ol>
<li><strong>Conduit and accessories</strong> — the pipes buried in the wall before plastering.</li>
<li><strong>House wire</strong> — the copper that runs inside the conduit.</li>
<li><strong>Switches, sockets and plates</strong> — the visible layer, chosen last.</li>
<li><strong>Switchgear</strong> — MCBs, RCCB and the distribution board.</li>
<li><strong>Earthing</strong> — electrode, strip and chemical compound.</li>
<li><strong>Fans, lights and accessories</strong>.</li>
<li><strong>Special cables</strong> — submersible pump cable, LAN, TV coaxial, doorbell.</li>
</ol>
<p>They are bought in that order too, because conduit goes in before plastering and switches go in at the very end.</p>

<h2>Approximate quantities by house size</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Item</th><th>2BHK (~900–1,100 sq ft)</th><th>3BHK (~1,400–1,700 sq ft)</th></tr></thead>
<tbody>
<tr><td>1.0 sq mm wire (lights, fans)</td><td>3–4 coils of 90m</td><td>5–7 coils</td></tr>
<tr><td>1.5 sq mm wire (light and 6A circuits)</td><td>4–6 coils</td><td>7–10 coils</td></tr>
<tr><td>2.5 sq mm wire (power sockets)</td><td>3–5 coils</td><td>5–8 coils</td></tr>
<tr><td>4.0 sq mm wire (AC, geyser)</td><td>1–2 coils</td><td>2–4 coils</td></tr>
<tr><td>6.0 sq mm wire (mains, meter to DB)</td><td>1 coil</td><td>1–2 coils</td></tr>
<tr><td>Earth wire (green, 1.5 / 2.5 sq mm)</td><td>2–3 coils</td><td>4–5 coils</td></tr>
<tr><td>PVC conduit 20mm / 25mm</td><td>250–350 m</td><td>400–600 m</td></tr>
<tr><td>Modular switch points</td><td>60–90 points</td><td>100–150 points</td></tr>
<tr><td>MCBs</td><td>10–14</td><td>16–24</td></tr>
<tr><td>Distribution board</td><td>1 × 8–12 way</td><td>1 × 12–16 way (or 2 DBs)</td></tr>
<tr><td>RCCB</td><td>1 × 40A 30mA</td><td>1–2 × 40/63A 30mA</td></tr>
</tbody></table></div>
<p class="ptable-note">Quantities vary with layout, number of floors and how far the meter is from the distribution board. A long meter-to-DB run alone can add a full coil of 6.0 sq mm.</p>

<h2>Approximate budget bands (2026, Bangalore)</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Package</th><th>2BHK</th><th>3BHK</th></tr></thead>
<tbody>
<tr><td>Economy — reputed brand, basic switches</td><td>₹90,000 – ₹1,30,000</td><td>₹1,50,000 – ₹2,10,000</td></tr>
<tr><td>Standard — FR wire, good modular switches</td><td>₹1,30,000 – ₹1,90,000</td><td>₹2,10,000 – ₹3,00,000</td></tr>
<tr><td>Premium — FRLS wire, premium switches, automation-ready</td><td>₹2,00,000 – ₹3,00,000+</td><td>₹3,20,000 – ₹5,00,000+</td></tr>
</tbody></table></div>
<p>These are <strong>material</strong> bands only — labour is charged separately, usually per point or as a percentage. The single biggest swing factor is the switch range: the same house can take ₹35,000 or ₹1,60,000 of modular switches depending on the series chosen.</p>

<h2>Where builders lose money on this list</h2>
<ul>
<li><strong>Buying wire on a "with material" contract.</strong> The contractor buys, and the temptation to substitute duplicate wire is enormous — it is invisible inside the wall and the margin is his. Buy wire yourself; let him do the labour.</li>
<li><strong>Undersizing AC and geyser circuits</strong> to save two coils of 4.0 sq mm. It is the most expensive ₹6,000 you will ever save.</li>
<li><strong>Paying for points you will never use</strong> — 150 points in a 2BHK is a contractor's revenue, not your convenience.</li>
<li><strong>Skipping the RCCB.</strong> It is the one device that protects a person rather than the wiring.</li>
<li><strong>Buying loose wire without a carton.</strong> No box means no QR, no batch, no warranty and no way to prove what you bought.</li>
</ul>

<h2>Buy it in the right sequence</h2>
<p>Conduit and boxes go in before plastering. Wire goes in after plastering and before painting. Switches, plates, MCBs, DB, fans and lights go in at the end, after painting. Buying the visible layer too early means it sits on site collecting dust and damage for three months — and modular plates scratch easily.</p>

<p>Full brand-wise reference rates are on our <a href="../price-lists.html">price list pages</a>, and you can size everything yourself with the <a href="../tools.html">free calculators</a>.</p>
""" + _cta(),
 D,
 [("What electrical material is needed for a new house?", "Conduit and accessories, house wire in 1.0 to 6.0 sq mm sizes, earth wire, modular switches and sockets, MCBs, an RCCB, a distribution board, earthing electrode and strip, fans, lights, and special cables such as submersible pump cable, LAN and coaxial. They are bought in that order because conduit goes in before plastering and switches at the very end."),
  ("How much does electrical material cost for a 2BHK house in Bangalore?", "Approximately ₹90,000 to ₹1,30,000 for an economy specification, ₹1,30,000 to ₹1,90,000 for a standard build with FR wire and good modular switches, and ₹2,00,000 upwards for a premium specification. These are material costs only; wiring labour is charged separately, usually per point."),
  ("How much electrical material does a 3BHK house need?", "Roughly 15 to 25 coils of house wire across sizes, 400 to 600 metres of conduit, 100 to 150 switch points, 16 to 24 MCBs, one or two distribution boards and one or two RCCBs. Exact quantities depend on layout, number of floors and the distance from the meter to the distribution board."),
  ("Should I buy electrical material myself or let the contractor buy it?", "Buy the wire and switchgear yourself. On a with-material contract the contractor keeps the difference, and duplicate wire is invisible once it is inside the wall. Let the contractor handle labour and small consumables, and keep the high-value, quality-critical items in your own name with your own bills."),
  ("What is the biggest mistake in a house electrical list?", "Undersizing the AC and geyser circuits to save a couple of coils of 4.0 sq mm wire. Those are the highest-load circuits in a home, they run continuously in Bangalore summers, and correcting an undersized concealed circuit later means breaking finished walls."),
  ("Do I need an RCCB in a house?", "Yes. MCBs protect the wiring from overload and short circuit; an RCCB protects a person from electric shock by tripping on earth leakage. A 40A or 63A, 30mA RCCB is standard for a home and is the single most important safety device on the list.")],
 ("happy-house-builder-electrical-delivery.jpg", "A house builder in Bangalore receiving a delivery of electrical material at his site")),

# ---------------------------------------------------------------- 2
("how-much-wire-required-2bhk-3bhk-house",
 "How Much Wire Is Required for a 2BHK or 3BHK House?",
 "A practical method to calculate house wire quantity — how many 90m coils of 1.0, 1.5, 2.5, 4.0 and 6.0 sq mm you need, why contractors over-order, and how to check the estimate you were given.",
 "Buying Guide",
 """<p>Wire is the second-largest line on a house electrical bill and the easiest one to over-order. Contractors quote coils generously because leftover wire belongs to them, not to you. Here is how to work out the real number.</p>

<h2>The method: count points, not square feet</h2>
<p>Square footage is a poor predictor because a compact 3BHK and a spread-out 2BHK can need the same wire. Count circuits instead:</p>
<ul>
<li><strong>Light and fan points</strong> — run on 1.0 or 1.5 sq mm.</li>
<li><strong>5A/6A socket points</strong> — 1.5 sq mm.</li>
<li><strong>16A power sockets</strong> — 2.5 sq mm.</li>
<li><strong>AC, geyser, oven</strong> — 4.0 sq mm.</li>
<li><strong>Meter to distribution board</strong> — 6.0 sq mm, occasionally 10.0.</li>
</ul>
<p>Each point needs wire from the DB to the point and back, plus vertical drops, plus roughly 15% for bends, loops and wastage.</p>

<h2>The quick estimate</h2>
<p>A working rule for Bangalore homes: <strong>average run length per point is 9–14 metres</strong> of each conductor. Multiply points by run length, by the number of conductors (phase, neutral and earth — so three), then divide by 90 to get coils.</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Wire size</th><th>2BHK (~70 points)</th><th>3BHK (~110 points)</th><th>Typical use</th></tr></thead>
<tbody>
<tr><td>1.0 sq mm</td><td>3–4 coils</td><td>5–7 coils</td><td>Lights, fans</td></tr>
<tr><td>1.5 sq mm</td><td>4–6 coils</td><td>7–10 coils</td><td>Light circuits, 6A sockets</td></tr>
<tr><td>2.5 sq mm</td><td>3–5 coils</td><td>5–8 coils</td><td>16A power sockets, kitchen</td></tr>
<tr><td>4.0 sq mm</td><td>1–2 coils</td><td>2–4 coils</td><td>AC, geyser, oven</td></tr>
<tr><td>6.0 sq mm</td><td>1 coil</td><td>1–2 coils</td><td>Mains, meter to DB</td></tr>
<tr><td>Earth (green)</td><td>2–3 coils</td><td>4–5 coils</td><td>All circuits</td></tr>
</tbody></table></div>
<p class="ptable-note">A 90m coil is the standard house-wire pack in India. Some brands also sell 180m and 300m coils, which cost less per metre and are worth it on larger houses.</p>

<h2>Why 90m coils, and when to buy bigger</h2>
<p>The 90m coil is the industry standard and the easiest size to verify, return and account for. If your house needs four or more coils of a single size, ask for 180m or 300m coils instead — the per-metre rate drops and there is less joint wastage. We explain the trade-off in our guide on <a href="why-buy-finolex-90m-coils.html">why 90m coils are the safe default</a>.</p>

<h2>Three checks on the estimate you were given</h2>
<ol>
<li><strong>Does the coil count roughly match the point count?</strong> If a 2BHK estimate shows 20 coils, ask which circuits need them.</li>
<li><strong>Is 4.0 sq mm present at all?</strong> An estimate with no 4.0 sq mm means the ACs and geyser are being run on 2.5 — which is undersized for most installations.</li>
<li><strong>Is earth wire quantity roughly equal to the phase wire?</strong> Every circuit needs an earth conductor; a low earth-wire number usually means earthing is being skipped on socket circuits.</li>
</ol>

<h2>Buy slightly short, top up later</h2>
<p>Order about 90% of your estimate and top up once the electrician has actually pulled the first floor. Wire is available next day across Bangalore, so there is no reason to carry three spare coils — and unused coils have a way of leaving site.</p>

<p>Use the <a href="../tools/wire-quantity-calculator.html">wire quantity calculator</a> to run your own numbers, and the <a href="../tools/wire-size-calculator.html">wire size calculator</a> to confirm which size each circuit needs.</p>
""" + _cta(),
 D,
 [("How many coils of wire are needed for a 2BHK house?", "Typically 12 to 20 coils of 90m in total: 3–4 coils of 1.0 sq mm, 4–6 of 1.5, 3–5 of 2.5, 1–2 of 4.0, one of 6.0 and 2–3 coils of earth wire. The exact number depends on point count, floor layout and the distance from the meter to the distribution board."),
  ("How many coils of wire does a 3BHK house need?", "Usually 24 to 36 coils of 90m across all sizes, for roughly 110 points. Larger or multi-floor homes with long cable runs from the meter can go higher, and houses with many air conditioners need noticeably more 4.0 sq mm."),
  ("How do I calculate house wire quantity myself?", "Count the points on each circuit type, assume an average run of 9 to 14 metres per point, multiply by three conductors for phase, neutral and earth, add about 15% for bends and wastage, then divide by 90 to get the number of coils per size."),
  ("Is a 90m coil the standard wire pack in India?", "Yes, the 90m coil is the standard house-wire pack and the easiest size to verify and account for. Brands also sell 180m and 300m coils, which cost less per metre and are worth buying when a single size needs four or more coils."),
  ("Should I buy extra wire to be safe?", "No. Order about 90% of your estimate and top up after the first floor is pulled. Wire is delivered next day across Bangalore, so surplus coils only tie up money and have a habit of disappearing from site."),
  ("How can I tell if my contractor over-quoted the wire?", "Check three things: whether the coil count is proportionate to the point count, whether 4.0 sq mm appears at all for AC and geyser circuits, and whether earth wire quantity is roughly comparable to the phase wire. A missing 4.0 sq mm line or very little earth wire indicates corners being cut, not savings.")],
 ("wire-coils-warehouse-electrical-distributor.jpg", "Coils of house wiring cable stacked on racks at an electrical distributor warehouse in Bangalore")),

# ---------------------------------------------------------------- 3
("copper-price-and-wire-rates-explained",
 "Why Wire Prices Keep Changing: Copper Rates Explained for House Builders",
 "Wire prices move with the copper market, not with the shop. Here is how copper pricing works, why every honest dealer quotes ranges, and how to use price movement to time your purchase.",
 "Pricing",
 """<p>Every week someone asks us why the wire rate we gave last month is different today. The answer has nothing to do with the shop and everything to do with a commodity traded on international exchanges.</p>

<h2>A wire coil is mostly copper</h2>
<p>In a house wire, the conductor is electrolytic-grade copper and the insulation is PVC. By value, copper is the dominant component — which means the price of a coil tracks the copper market far more closely than it tracks anything a dealer decides. When copper moves several percent in a month, wire prices follow within weeks.</p>

<h2>What actually moves the price</h2>
<ul>
<li><strong>International copper prices</strong>, set on global exchanges and quoted in dollars.</li>
<li><strong>The rupee-dollar rate</strong>, because copper is imported and priced in dollars. A weaker rupee raises wire prices even when copper itself is flat.</li>
<li><strong>PVC and additive costs</strong>, which follow crude oil and matter more for FRLS and specialty ranges.</li>
<li><strong>Manufacturer MRP revisions</strong>, which happen periodically and reset the whole price band at once.</li>
<li><strong>Season</strong> — construction demand peaks after the monsoon and before the festive season.</li>
</ul>

<h2>Why every honest dealer quotes a range</h2>
<p>This is the part worth understanding before you compare sellers. A published fixed price for house wire is almost always stale. Any dealer actually moving stock knows the rate changes, which is why our <a href="../price-lists.html">price list pages</a> show approximate bands and why we ask you to WhatsApp for today's exact figure. A website quoting a single precise rupee figure for a wire coil is either not selling wire or is quoting a number from months ago.</p>

<h2>The 3–5% margin rule, and what it tells you</h2>
<p>Genuine branded wire runs on roughly 3–5% dealer margin. That single fact is the most useful price test available to a house builder:</p>
<ul>
<li>A discount of 5–8% off the market band is aggressive but possible on a large order.</li>
<li>A discount of 15% or more on a branded coil is not a discount. It is a different product — under-weight copper, shorter length, or an outright duplicate.</li>
</ul>
<p>Copper shortfall is the common trick: a coil marked 1.5 sq mm carrying 1.2 sq mm of copper looks identical, weighs slightly less, and overheats under load. You cannot see it, which is why our <a href="../original-vs-duplicate-electrical-products.html">original versus duplicate guide</a> exists.</p>

<h2>Can you time your purchase?</h2>
<p>Marginally, and only if your schedule allows it. Practical advice:</p>
<ol>
<li><strong>Buy all your wire in one go</strong> rather than floor by floor. You lock one rate and get a better price on the full list.</li>
<li><strong>Do not delay for a price fall.</strong> A 3% saving on ₹1,50,000 of wire is ₹4,500 — less than a week of delayed construction costs.</li>
<li><strong>Do get a written quote with a validity window.</strong> Ours is valid for a stated period, which protects you from mid-project movement.</li>
<li><strong>Ignore "scheme" pricing that seems disconnected from the market.</strong> The market does not have secrets; it has margins.</li>
</ol>

<h2>How to use a reference price</h2>
<p>Send your full list to <a href="{W}">{PH}</a> and use our quote as a reference band, whether or not you buy from us. If another seller is within a few percent, they are quoting honestly. If they are far below, ask to see the carton, the batch number and the QR code before you pay.</p>
""".replace("{W}", W).replace("{PH}", PH) + _cta(),
 D,
 [("Why do wire prices change so often in India?", "Because a wire coil is mostly copper, and copper is an internationally traded commodity priced in dollars. Wire rates follow the copper market and the rupee-dollar exchange rate, with PVC costs, periodic manufacturer MRP revisions and construction season adding further movement."),
  ("Why do dealers only give approximate wire prices online?", "Because a fixed published figure goes stale within weeks. Any dealer genuinely moving stock knows the rate changes, so honest price lists show approximate bands and give an exact figure on request. A website quoting one precise rupee figure for a wire coil is usually months out of date."),
  ("How much discount is realistic on branded wire?", "Genuine branded wire runs on roughly 3–5% dealer margin, so 5–8% off the market band is aggressive but possible on a large order. A discount of 15% or more is not a discount — it usually indicates under-weight copper, short coil length or duplicate stock."),
  ("What is copper shortfall in house wire?", "It is when a coil marked 1.5 sq mm actually carries less copper than that, for example 1.2 sq mm. The coil looks identical and weighs only slightly less, but it overheats under load and cannot carry its rated current. It is invisible without measurement, which is why buying from an authorised seller matters."),
  ("Should I wait for copper prices to fall before buying wire?", "Generally no. A 3% saving on ₹1,50,000 of wire is about ₹4,500, which is less than the cost of a week of delayed construction. Buy all your wire in one order to lock a single rate and get better pricing on the full list."),
  ("How do I know if a wire price I was quoted is fair?", "Get a reference quote for the same list from an established distributor and compare. Quotes within a few percent of each other are honest market pricing. Anything far below the band should be checked against the carton, batch number and QR verification before payment.")],
 ("shop-owner-explaining-wire-quality.jpg", "An electrical shop owner explaining copper wire quality to a customer at the counter")),

# ---------------------------------------------------------------- 4
("mcb-rccb-rcbo-guide-for-homes",
 "MCB, RCCB and RCBO: What Each One Does and What Your Home Needs",
 "A plain-language guide to home switchgear — what an MCB protects, why an RCCB saves lives, when an RCBO is worth it, correct ratings for Indian homes and how to spot duplicate breakers.",
 "Product Guide",
 """<p>Switchgear is the part of a house electrical list that people understand least and question most. It is also the part where a wrong choice is genuinely dangerous rather than merely expensive.</p>

<h2>The three devices, in one line each</h2>
<ul>
<li><strong>MCB (Miniature Circuit Breaker)</strong> — protects the <em>wiring</em> from overload and short circuit. Trips when too much current flows.</li>
<li><strong>RCCB (Residual Current Circuit Breaker)</strong> — protects the <em>person</em> from electric shock. Trips when current leaks to earth, for example through a human body or damp wall.</li>
<li><strong>RCBO</strong> — one device doing both jobs for a single circuit.</li>
</ul>
<p>The critical point: an MCB will not save you from a shock, and an RCCB will not protect your wiring from overload. A home needs both.</p>

<h2>Ratings for a typical Indian home</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Circuit</th><th>Wire size</th><th>MCB rating</th><th>Curve</th></tr></thead>
<tbody>
<tr><td>Lights and fans</td><td>1.0 / 1.5 sq mm</td><td>6A</td><td>B</td></tr>
<tr><td>6A socket circuits</td><td>1.5 sq mm</td><td>10A</td><td>B</td></tr>
<tr><td>16A power sockets, kitchen</td><td>2.5 sq mm</td><td>16A</td><td>C</td></tr>
<tr><td>Geyser</td><td>2.5 / 4.0 sq mm</td><td>16A / 20A</td><td>C</td></tr>
<tr><td>Air conditioner (1.5 ton)</td><td>4.0 sq mm</td><td>20A</td><td>C</td></tr>
<tr><td>Main incomer</td><td>6.0 / 10.0 sq mm</td><td>40A / 63A</td><td>C</td></tr>
<tr><td>RCCB (whole house)</td><td>—</td><td>40A / 63A, 30mA</td><td>—</td></tr>
</tbody></table></div>
<p class="ptable-note">Curve B trips faster and suits resistive loads such as lights and heaters. Curve C tolerates the brief inrush of motors and compressors, which is why ACs, pumps and fridges belong on C.</p>

<h2>The MCB must match the wire, not the appliance</h2>
<p>This is the single most misunderstood rule in home wiring. The breaker exists to protect the cable, so its rating must be at or below what the cable can safely carry. Fitting a 32A MCB on a 2.5 sq mm circuit because "the AC keeps tripping" removes the protection entirely — the wire will now overheat before the breaker notices. If a breaker trips repeatedly, the fix is a bigger cable or a separate circuit, never a bigger breaker.</p>

<h2>Is 30mA the right RCCB sensitivity?</h2>
<p>For personal protection in homes, yes — 30mA is the standard. 100mA and 300mA devices exist but protect equipment and fire risk rather than people. In houses that suffer nuisance tripping, the usual cause is genuine leakage from an old geyser element or damp wiring, not an oversensitive RCCB. Splitting the house across two RCCBs makes faults easier to isolate and stops one leaky appliance from blacking out the whole home.</p>

<h2>When an RCBO is worth the money</h2>
<p>An RCBO gives one circuit both overload and leakage protection independently. It costs several times an MCB, so it is not for every circuit — but it is genuinely worth it for a geyser, an outdoor or garden circuit, a borewell pump, or any circuit that has a history of nuisance tripping. Protecting those individually keeps the rest of the house on when they fault.</p>

<h2>Duplicate breakers are common — and dangerous</h2>
<p>A counterfeit MCB looks identical and may even click convincingly, but its trip characteristics are unverified and its breaking capacity is often a fraction of what is printed. It is the one duplicate item that fails precisely when you need it. Buy switchgear only in sealed boxes from an authorised source, check the printing quality and the KA rating, and verify the QR where the brand provides one. We cover the specific tells in our guides on <a href="how-to-identify-duplicate-legrand-mcb.html">identifying duplicate MCBs</a>.</p>

<p>Reference rates are on the <a href="../switchgear-and-mcb.html">switchgear and MCB page</a>, and the <a href="../tools/mcb-selector.html">MCB selector tool</a> will suggest ratings for your circuits.</p>
""" + _cta(),
 D,
 [("What is the difference between an MCB and an RCCB?", "An MCB protects the wiring by tripping on overload and short circuit. An RCCB protects people by tripping when current leaks to earth, such as through a body or a damp wall. They do different jobs and a home needs both — an MCB will not prevent an electric shock and an RCCB will not stop a cable overheating."),
  ("What MCB rating should I use for an air conditioner?", "A 1.5 ton air conditioner is typically run on a 4.0 sq mm circuit with a 20A Curve C MCB. Curve C matters because it tolerates the brief inrush current when a compressor starts, whereas a Curve B breaker on the same load will nuisance trip."),
  ("Is a 30mA RCCB right for a house?", "Yes. 30mA is the standard sensitivity for personal shock protection in homes. Higher ratings such as 100mA or 300mA protect equipment and reduce fire risk but do not reliably protect a person. Splitting a house across two 30mA RCCBs helps isolate faults without blacking out the whole home."),
  ("Can I fit a higher rated MCB if it keeps tripping?", "No. The MCB rating must match the cable, not the appliance, because its whole purpose is to protect the wiring. Fitting a larger breaker removes the protection and lets the cable overheat before the breaker reacts. Repeated tripping means the circuit needs a larger cable or a separate circuit."),
  ("When should I use an RCBO instead of an MCB?", "When a single circuit deserves its own leakage protection — a geyser, an outdoor or garden circuit, a borewell pump, or any circuit with a history of nuisance tripping. An RCBO costs several times an MCB, so it is used selectively rather than throughout the board."),
  ("How do I know if an MCB is genuine?", "Buy only sealed boxes from an authorised seller, check that the printing is sharp and correctly aligned, confirm that the breaking capacity in kA is clearly marked, and scan the QR code where the brand provides one. Counterfeit breakers look convincing but have unverified trip characteristics and often a fraction of the stated breaking capacity.")],
 ("electrician-installing-mcb-distribution-board.jpg", "An electrician wiring miniature circuit breakers into a home distribution board")),

# ---------------------------------------------------------------- 5
("distribution-board-selection-guide-home",
 "How to Choose a Distribution Board for Your Home",
 "Sizing a DB by way count, single vs double door, IP rating, busbar quality, separate DBs per floor, and the brands worth considering — with approximate price bands for Bangalore.",
 "Product Guide",
 """<p>The distribution board is the one component in a house that nobody looks at again for twenty years, which is exactly why it is worth choosing properly the first time.</p>

<h2>Sizing: count ways, then add 30%</h2>
<p>A "way" is one module position. Count every MCB you need, add the incomer and RCCB (which occupy two modules each), then add roughly 30% spare capacity for future circuits — an added AC, an EV charger, an inverter changeover.</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Home</th><th>Typical MCB count</th><th>DB size to buy</th></tr></thead>
<tbody>
<tr><td>1BHK / small flat</td><td>6–8</td><td>8-way single door</td></tr>
<tr><td>2BHK</td><td>10–14</td><td>12-way double door</td></tr>
<tr><td>3BHK</td><td>16–20</td><td>16-way double door, or 12-way + sub-DB</td></tr>
<tr><td>Duplex / independent house</td><td>20–30</td><td>Main DB + one sub-DB per floor</td></tr>
</tbody></table></div>
<p class="ptable-note">Approximate DB price bands in Bangalore: 8-way ₹1,200–₹2,800, 12-way ₹1,800–₹4,500, 16-way ₹2,600–₹6,500, depending on brand and whether it is single or double door.</p>

<h2>Single door, double door or IP-rated?</h2>
<ul>
<li><strong>Single door</strong> — MCB toggles are exposed when the door is open. Cheapest, fine for a utility area.</li>
<li><strong>Double door</strong> — an inner cover hides the wiring and only the toggles show. Safer with children in the house and much neater. This is the right default for a home.</li>
<li><strong>IP43 / IP54 enclosures</strong> — dust and splash protected, for semi-outdoor locations, utility balconies or borewell points.</li>
</ul>

<h2>What actually differs between a cheap DB and a good one</h2>
<p>From the outside they look the same. The differences that matter are inside:</p>
<ol>
<li><strong>Busbar quality and current rating.</strong> A thin or plated-steel busbar heats up under sustained load. Good boards use properly rated tinned copper.</li>
<li><strong>Terminal quality</strong> on the neutral and earth links — the most common source of loose connections and warm terminals years later.</li>
<li><strong>Sheet thickness and powder coating,</strong> which decides whether the enclosure rusts in a humid utility area.</li>
<li><strong>DIN rail alignment,</strong> which decides whether MCBs from your chosen brand actually sit flush.</li>
</ol>
<p>The price difference between a poor board and a good one on a 12-way is a couple of thousand rupees, spread across a device that carries the entire house load for two decades. It is not the place to economise.</p>

<h2>One DB or several?</h2>
<p>For anything larger than a compact 2BHK, split the load. A main DB near the meter with the incomer and RCCB, plus a sub-DB per floor, gives you shorter circuit runs, easier fault isolation and far less disruption when something needs work. In an independent house it also means an electrician does not have to work at the main board with the whole house live.</p>

<h2>Keep the same brand for DB and MCBs</h2>
<p>Mixing brands inside a board is common and usually works, but module widths, DIN rail heights and busbar comb designs differ slightly between manufacturers. Matching the DB and the breakers avoids gaps, forced fits and comb busbars that do not seat properly. It also keeps warranty responsibility with one manufacturer.</p>

<h2>Label the board</h2>
<p>Ask your electrician to label every way — kitchen, bedroom 1 lights, AC hall, geyser. It takes ten minutes and saves an hour of guesswork every time something trips for the next twenty years. Photograph the labelled board and keep the picture; it is the most useful electrical document a homeowner can own.</p>

<p>See approximate rates on the <a href="../switchgear-and-mcb.html">switchgear page</a>, and use the <a href="../tools/load-calculator.html">load calculator</a> to check your incomer rating.</p>
""" + _cta(),
 D,
 [("What size distribution board do I need for a 2BHK?", "A 12-way double door board is the usual choice for a 2BHK with 10 to 14 MCBs, once you allow two modules each for the incomer and the RCCB plus around 30% spare capacity for future circuits such as an extra air conditioner or an EV charger."),
  ("Should I choose a single door or double door distribution board?", "Double door for a home. The inner cover hides the wiring so only the MCB toggles are exposed, which is safer with children in the house and considerably neater. Single door boards are cheaper and acceptable in a utility area where appearance and access do not matter."),
  ("What is the difference between a cheap and a good distribution board?", "Mostly what you cannot see: busbar material and current rating, the quality of the neutral and earth terminals, sheet thickness and powder coating, and DIN rail alignment. A thin busbar heats under sustained load and poor terminals become loose warm connections years later."),
  ("Should the distribution board and MCBs be from the same brand?", "Ideally yes. Module widths, DIN rail heights and comb busbar designs vary slightly between manufacturers, so matching them avoids gaps, forced fits and busbars that do not seat correctly. It also keeps warranty responsibility with a single manufacturer."),
  ("Do I need more than one distribution board in a house?", "For anything larger than a compact 2BHK, yes. A main board near the meter carrying the incomer and RCCB, plus a sub-board on each floor, shortens circuit runs, makes faults easier to isolate and avoids an electrician having to work at the main board with the whole house live."),
  ("How much does a distribution board cost in Bangalore?", "Approximately ₹1,200 to ₹2,800 for an 8-way, ₹1,800 to ₹4,500 for a 12-way and ₹2,600 to ₹6,500 for a 16-way, depending on brand and whether it is single or double door. These are indicative bands; WhatsApp your requirement for today's exact rate.")],
 ("electrician-installing-mcb-distribution-board.jpg", "A distribution board being wired and labelled in a Bangalore home")),

# ---------------------------------------------------------------- 6
("modular-switch-buying-guide-bangalore",
 "Modular Switch Buying Guide: Ranges, Price Bands and What Actually Matters",
 "How modular switch ranges are priced in India, what separates an entry series from a premium one, plate materials, socket types you actually need, and how many points a house really requires.",
 "Product Guide",
 """<p>Modular switches are the only electrical product in the house your family will touch every day and the only one guests will notice. They are also where the electrical budget swings most — the same house can take ₹35,000 or ₹1,60,000 of switches depending on the series.</p>

<h2>How the ranges are structured</h2>
<p>Almost every brand sells three or four tiers built on the same modular frame, so plates and modules are interchangeable within a brand:</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Tier</th><th>Approx per point</th><th>What you get</th></tr></thead>
<tbody>
<tr><td>Entry</td><td>₹180 – ₹350</td><td>Basic polycarbonate plates, standard rockers, limited colours</td></tr>
<tr><td>Mid</td><td>₹350 – ₹700</td><td>Better plate finish, softer switch action, wider module range</td></tr>
<tr><td>Premium</td><td>₹700 – ₹1,500</td><td>Metal or glass-finish plates, silent or feather-touch action, matching accessories</td></tr>
<tr><td>Designer / touch</td><td>₹1,500 – ₹4,000+</td><td>Glass, touch panels, dimmers, automation-ready</td></tr>
</tbody></table></div>
<p class="ptable-note">"Per point" here includes the module, its share of the plate and the mounting box. A 3BHK with 120 points is therefore roughly ₹45,000 at entry level and ₹1,20,000 at premium.</p>

<h2>What actually differs between tiers</h2>
<ul>
<li><strong>Contact material and rating.</strong> The metal inside the switch decides how many thousand operations it survives. This is the real difference, and it is invisible.</li>
<li><strong>Switch action.</strong> Premium ranges use a different mechanism that stays consistent for years rather than becoming loose and rattly.</li>
<li><strong>Plate material.</strong> Polycarbonate yellows slowly in sunlight; better polymers and metal finishes do not.</li>
<li><strong>Module availability.</strong> Higher ranges have fan regulators, dimmers, USB sockets, bell push, TV and data modules that match visually.</li>
<li><strong>Colour consistency</strong> across batches — relevant if you extend the wiring two years later.</li>
</ul>

<h2>How many points does a house really need?</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Room</th><th>Sensible point count</th></tr></thead>
<tbody>
<tr><td>Living room</td><td>2 light, 1 fan, 4–6 sockets, 1 TV point</td></tr>
<tr><td>Master bedroom</td><td>2 light, 1 fan, 4 sockets, 1 AC point</td></tr>
<tr><td>Other bedrooms</td><td>1–2 light, 1 fan, 3 sockets, 1 AC point</td></tr>
<tr><td>Kitchen</td><td>2 light, 5–7 sockets (16A for major appliances)</td></tr>
<tr><td>Bathroom</td><td>1 light, 1 exhaust, 1 geyser point</td></tr>
<tr><td>Balcony / utility</td><td>1 light, 1–2 sockets, washing machine point</td></tr>
</tbody></table></div>
<p>That lands a 2BHK at roughly 60–90 points and a 3BHK at 100–150. Beyond this, extra points are usually contractor revenue rather than convenience — though a few well-placed extra sockets are the cheapest future-proofing you will ever buy, so spend them on the kitchen and beside the bed rather than on additional light points.</p>

<h2>Socket types worth specifying</h2>
<ul>
<li><strong>6A sockets</strong> for phones, lamps, chargers — the bulk of your points.</li>
<li><strong>16A sockets</strong> for microwave, fridge, washing machine, AC. These need 2.5 or 4.0 sq mm wiring, so they must be planned before wiring, not chosen at the end.</li>
<li><strong>USB modules</strong> beside beds and in the living room. Genuinely useful; specify the amperage rather than assuming.</li>
<li><strong>Fan regulators</strong> — step-type is reliable and cheap; electronic is smoother and works better with BLDC fans.</li>
</ul>

<h2>Choose the brand before wiring, the colour at the end</h2>
<p>Box sizes and module widths differ between brands, so the mounting boxes fitted during wiring commit you to a brand family. Decide the brand and series before the conduit and boxes go in; the plate colour and finish can be chosen months later, at painting stage. And buy switches last — they scratch, and three months on a dusty site does them no favours.</p>

<p>See our comparison of <a href="best-modular-switch-brands-india-2026.html">the best modular switch brands</a>, <a href="which-switch-brand-should-you-buy.html">which switch brand to buy</a>, and approximate rates on the <a href="../switches-and-sockets.html">switches and sockets page</a>.</p>
""" + _cta(),
 D,
 [("How much do modular switches cost per point in India?", "Roughly ₹180 to ₹350 per point for entry ranges, ₹350 to ₹700 for mid ranges, ₹700 to ₹1,500 for premium and ₹1,500 upwards for designer, glass or touch ranges. Per point includes the module, its share of the plate and the mounting box."),
  ("How many switch points does a 3BHK house need?", "Typically 100 to 150 points. A sensible allocation is two light points, one fan and three to four sockets per bedroom with an AC point, five to seven sockets in the kitchen, four to six in the living room, and a light, exhaust and geyser point in each bathroom."),
  ("What is the real difference between cheap and expensive modular switches?", "Mostly the contact material inside the switch, which decides how many operations it survives, and the switch mechanism, which decides whether the action stays crisp or becomes loose after a few years. Plate material, module range and colour consistency across batches also improve with tier."),
  ("When should I choose the modular switch brand?", "Before wiring starts. Mounting box sizes and module widths differ between brands, so the boxes fitted during the conduit stage commit you to a brand family. The plate colour and finish can be decided much later, at painting stage."),
  ("Should I buy 6A or 16A sockets?", "Both. Use 6A sockets for phones, lamps and chargers, which is most of the house, and 16A sockets for the microwave, fridge, washing machine and air conditioners. 16A points need 2.5 or 4.0 sq mm wiring, so they must be planned before the wiring goes in."),
  ("When should modular switches be bought and installed?", "Last, after painting. Modular plates scratch easily and three months on a dusty construction site damages them. Only the mounting boxes go in early, during the conduit stage.")],
 ("woman-homeowner-choosing-modular-switches.jpg", "A homeowner choosing modular switches and sockets from a display board in an electrical showroom")),

# ---------------------------------------------------------------- 7
("led-lighting-buying-guide-home-bangalore",
 "LED Lighting for Homes: Types, Lumens, Colour Temperature and Price Bands",
 "How to choose home LED lighting — panel vs COB vs strip, how many lumens each room needs, warm vs cool white, driver quality, and approximate Bangalore price bands by type.",
 "Product Guide",
 """<p>Lighting is bought last and planned first — the conduit and points for a false-ceiling scheme must go in months before anyone chooses a fixture. Here is what to decide, and when.</p>

<h2>The five fixture types used in Indian homes</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Type</th><th>Approx price</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>LED bulb (B22 / E27)</td><td>₹70 – ₹350</td><td>Existing holders, utility areas, retrofit</td></tr>
<tr><td>Surface panel / downlight</td><td>₹250 – ₹1,200</td><td>General ceiling light without false ceiling</td></tr>
<tr><td>Recessed panel (false ceiling)</td><td>₹300 – ₹1,600</td><td>Even, glare-free general lighting</td></tr>
<tr><td>COB spotlight</td><td>₹400 – ₹2,000</td><td>Focused accent light on walls, art, kitchen counters</td></tr>
<tr><td>LED strip / cove (per metre)</td><td>₹90 – ₹450</td><td>Cove lighting, indirect and ambient layers</td></tr>
</tbody></table></div>

<h2>How much light each room needs</h2>
<p>Lighting is measured in lumens, not watts. A useful rule for Indian homes is lumens per square foot:</p>
<ul>
<li><strong>Living room</strong> — 20–30 lumens per sq ft general, plus accent layers.</li>
<li><strong>Bedroom</strong> — 15–20 lumens per sq ft, with a lower-level bedside layer.</li>
<li><strong>Kitchen</strong> — 40–60 lumens per sq ft, and under-cabinet light over the counter is worth more than any ceiling fixture.</li>
<li><strong>Bathroom</strong> — 30–40 lumens per sq ft, plus a dedicated mirror light.</li>
<li><strong>Study or work area</strong> — 50–70 lumens per sq ft at the desk.</li>
</ul>
<p>A modern LED delivers roughly 90–110 lumens per watt, so a 12ft × 12ft bedroom needing about 2,800 lumens is served by roughly 28–32W of good LED.</p>

<h2>Colour temperature: get this right or regret it daily</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Temperature</th><th>Appearance</th><th>Where it belongs</th></tr></thead>
<tbody>
<tr><td>2700K – 3000K (warm white)</td><td>Yellow, restful</td><td>Bedrooms, living room, dining</td></tr>
<tr><td>4000K (neutral)</td><td>Balanced</td><td>Kitchen, bathroom, corridors</td></tr>
<tr><td>6500K (cool daylight)</td><td>Blue-white, clinical</td><td>Utility, garage, work areas</td></tr>
</tbody></table></div>
<p>The most common mistake in Indian homes is 6500K everywhere because it looks brighter in the shop. It makes a living room feel like an office. Mix deliberately: warm in living and sleeping areas, neutral where you work.</p>

<h2>What separates a good LED from a cheap one</h2>
<ol>
<li><strong>The driver.</strong> Most LED failures are driver failures, not LED failures. A good driver has proper surge protection — which matters in areas with unstable supply.</li>
<li><strong>Heat sinking.</strong> LEDs die from heat. A fixture with a real aluminium heat sink lasts years longer than a plastic-bodied equivalent at the same lumen output.</li>
<li><strong>CRI (Colour Rendering Index).</strong> CRI above 80 makes skin, food and fabric look natural. Cheap fixtures at CRI 65–70 make everything look slightly grey.</li>
<li><strong>Honest lumen claims.</strong> Wattage is easy to print; lumens are easy to overstate. Buy brands that publish both.</li>
<li><strong>Flicker.</strong> Cheap drivers flicker at a rate you do not consciously see but which causes eye strain over hours.</li>
</ol>

<h2>Plan the wiring before the ceiling</h2>
<p>Cove and recessed lighting need conduit, driver locations and switching decided before the false ceiling goes up. Decide at that stage how many switch groups you want — a living room on a single switch is a design failure you cannot fix later without opening the ceiling. Three groups (general, cove, accent) is a good default.</p>

<p>Approximate rates are on our <a href="../lighting.html">lighting page</a>, and the <a href="../tools/load-calculator.html">load calculator</a> will tell you what all of it adds up to.</p>
""" + _cta(),
 D,
 [("How many lumens does a room need?", "Around 20 to 30 lumens per square foot for a living room, 15 to 20 for a bedroom, 40 to 60 for a kitchen, 30 to 40 for a bathroom and 50 to 70 at a desk. A modern LED gives roughly 90 to 110 lumens per watt, so a 12 by 12 foot bedroom needs about 28 to 32 watts of good quality LED."),
  ("Which colour temperature is best for a home?", "Warm white at 2700K to 3000K for bedrooms, living and dining areas, neutral 4000K for kitchens, bathrooms and corridors, and cool 6500K only in utility areas, garages and workspaces. Using 6500K throughout is the most common mistake and makes living areas feel like an office."),
  ("Why do LED lights fail early?", "Usually the driver fails rather than the LED itself, often due to voltage surges, and heat is the second cause. Fixtures with a proper aluminium heat sink and a driver with surge protection last considerably longer than plastic-bodied fixtures at the same claimed output."),
  ("What is CRI and does it matter?", "CRI is the Colour Rendering Index, a measure of how naturally a light source shows colours. Above 80 makes skin, food and fabrics look natural. Cheap fixtures at CRI 65 to 70 give everything a slightly grey cast, which is noticeable in kitchens and dressing areas."),
  ("How much does home LED lighting cost in Bangalore?", "Approximately ₹70 to ₹350 for an LED bulb, ₹250 to ₹1,200 for a surface panel, ₹300 to ₹1,600 for a recessed panel, ₹400 to ₹2,000 for a COB spotlight and ₹90 to ₹450 per metre for LED strip. These bands vary widely with brand and output."),
  ("When should lighting be planned in a house build?", "The layout, conduit, driver locations and switch grouping must be decided before the false ceiling goes up, even though the fixtures themselves are bought at the very end. A living room wired to a single switch cannot be corrected later without opening the ceiling.")],
 ("warm-led-lighting-living-room-family.jpg", "A living room lit by warm LED ceiling lights in an Indian home in the evening")),

# ---------------------------------------------------------------- 8
("ceiling-fan-buying-guide-bldc-vs-induction",
 "Ceiling Fan Buying Guide: BLDC vs Ordinary, Sweep Size and Price Bands",
 "Whether a BLDC fan is worth the extra money, how sweep size and air delivery actually work, star ratings, what to check before buying, and approximate 2026 price bands in Bangalore.",
 "Product Guide",
 """<p>Ceiling fans are the appliance Indian homes run the most hours per year, which makes them the one place where a small efficiency difference compounds into real money.</p>

<h2>BLDC versus ordinary induction fans</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th></th><th>Ordinary induction</th><th>BLDC</th></tr></thead>
<tbody>
<tr><td>Power draw (1200mm)</td><td>70–80 W</td><td>28–35 W</td></tr>
<tr><td>Approx price</td><td>₹1,300 – ₹3,000</td><td>₹2,800 – ₹6,500</td></tr>
<tr><td>Remote / speed control</td><td>Wall regulator</td><td>Remote, usually with timer and modes</td></tr>
<tr><td>Inverter backup friendly</td><td>Poor</td><td>Excellent — runs far longer per battery charge</td></tr>
<tr><td>Noise</td><td>Slight hum at low speeds</td><td>Generally quieter</td></tr>
<tr><td>Repairability</td><td>Any local technician</td><td>Needs brand service for the controller</td></tr>
</tbody></table></div>

<h2>Does the payback actually work?</h2>
<p>Take a fan running 10 hours a day for 8 months a year. The difference between 75W and 32W is 43W, which is about 105 units a year per fan. At Bangalore domestic tariffs that is roughly ₹700–₹900 a year saved per fan. On a ₹1,800 price premium, payback lands around two to two and a half years — and with five fans in a house, the household saves meaningfully every year after that.</p>
<p>The case is strongest where fans run long hours and where there is an inverter, because a BLDC fan more than doubles backup runtime. It is weakest in a guest room used twice a year, where an ordinary fan is the rational purchase.</p>

<h2>Sweep size by room</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Room size</th><th>Sweep</th></tr></thead>
<tbody>
<tr><td>Up to 55 sq ft</td><td>900mm</td></tr>
<tr><td>55–110 sq ft</td><td>1200mm — the standard Indian size</td></tr>
<tr><td>110–160 sq ft</td><td>1400mm</td></tr>
<tr><td>Above 160 sq ft or high ceilings</td><td>1400mm+, or two fans</td></tr>
</tbody></table></div>
<p>Two smaller fans in a large hall move air more evenly than one oversized fan, and they let you run only half when the room is half occupied.</p>

<h2>Read air delivery, not just watts</h2>
<p>Air delivery is measured in cubic metres per minute and is the number that tells you whether the fan actually cools. A 1200mm fan should deliver around 210–230 CMM. A very low-wattage fan with poor air delivery is not efficient — it is simply weak. Look at the ratio: CMM per watt is the honest efficiency measure, and BIS star ratings are based on it.</p>

<h2>Practical checks before buying</h2>
<ul>
<li><strong>Downrod length</strong> — the blades should sit roughly 2.4 to 2.7 metres above the floor. High ceilings need a longer downrod, and false ceilings need a shorter one.</li>
<li><strong>Canopy and hook compatibility</strong> — the ceiling hook must be properly embedded, especially for heavier fans.</li>
<li><strong>Regulator type</strong> — BLDC fans use their own remote or controller and do not work with an ordinary wall regulator, so plan the switch point accordingly.</li>
<li><strong>Warranty on the controller</strong>, not just the motor. The controller is the part that fails on a BLDC.</li>
<li><strong>Blade material</strong> — metal blades hold their pitch; very cheap plastic blades can warp in Bangalore's summer attic heat.</li>
</ul>

<h2>What to buy</h2>
<p>For rooms in daily use, and especially in homes with an inverter, BLDC is the better purchase despite the higher upfront cost. For occasional rooms, a good ordinary 1200mm fan from a reputable brand is entirely sensible. In both cases buy from a source that will honour the warranty — fan warranty claims are common, and a fan bought from an unauthorised seller is a warranty you cannot use.</p>

<p>Check what your fans and lights add up to with the <a href="../tools/load-calculator.html">load calculator</a>.</p>
""" + _cta(),
 D,
 [("Is a BLDC fan worth the extra cost?", "For rooms used daily, yes. A 1200mm BLDC fan draws about 28 to 35 watts against 70 to 80 watts for an ordinary fan, saving roughly ₹700 to ₹900 a year per fan at Bangalore tariffs when run 10 hours a day. Payback on the price premium is around two to two and a half years, and it is faster in homes with an inverter."),
  ("What sweep size ceiling fan do I need?", "900mm for rooms up to about 55 square feet, 1200mm for 55 to 110 square feet which covers most Indian bedrooms, and 1400mm for 110 to 160 square feet. For large halls, two smaller fans distribute air more evenly than one oversized fan and let you run only half when needed."),
  ("What is air delivery in a ceiling fan?", "Air delivery is measured in cubic metres per minute and indicates how much air the fan actually moves. A 1200mm fan should deliver roughly 210 to 230 CMM. A very low wattage fan with poor air delivery is weak rather than efficient — the honest measure is CMM per watt, which is what BIS star ratings are based on."),
  ("Do BLDC fans work with normal wall regulators?", "No. BLDC fans use their own electronic controller and remote, and connecting them through an ordinary wall regulator can damage the controller. Plan the switch point as a plain on-off switch and keep the regulator module out of that circuit."),
  ("How much do ceiling fans cost in Bangalore?", "Approximately ₹1,300 to ₹3,000 for an ordinary induction fan and ₹2,800 to ₹6,500 for a BLDC fan, depending on brand, sweep and finish. Designer and decorative ranges go considerably higher."),
  ("What should I check before installing a ceiling fan?", "That the blades will sit roughly 2.4 to 2.7 metres above the floor, which decides downrod length, that the ceiling hook is properly embedded for the fan's weight, and that the warranty covers the electronic controller and not only the motor — on a BLDC fan the controller is the part that usually fails.")],
 ("happy-family-new-home-lights-on.jpg", "A family in the living room of their new home with fans and lights running")),

# ---------------------------------------------------------------- 9
("house-earthing-guide-cost-bangalore",
 "House Earthing in Bangalore: Types, Materials and What It Costs",
 "Why earthing matters more than most people realise, the difference between conventional and chemical earthing, electrode types, earth resistance targets, and approximate material costs.",
 "Product Guide",
 """<p>Earthing is invisible, buried, and the first thing cut when a contractor wants to save money. It is also the system that decides whether a fault kills an appliance or a person.</p>

<h2>What earthing actually does</h2>
<p>An earthing system gives fault current a deliberate low-resistance path to ground. When a live wire touches an appliance body, the current runs to earth rather than through whoever touches it, and the resulting surge trips the MCB or RCCB. Without a good earth, that appliance body simply stays live and waits.</p>
<p>It also gives surge and lightning protection a discharge path, and gives sensitive electronics a stable reference — a poor earth is behind a surprising number of unexplained equipment failures.</p>

<h2>Conventional versus chemical earthing</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th></th><th>Conventional (pipe/plate)</th><th>Chemical / maintenance-free</th></tr></thead>
<tbody>
<tr><td>Method</td><td>GI or copper pipe or plate in a pit with salt and charcoal</td><td>Filled electrode with backfill compound</td></tr>
<tr><td>Approx material cost</td><td>₹3,500 – ₹9,000 per pit</td><td>₹6,500 – ₹18,000 per pit</td></tr>
<tr><td>Maintenance</td><td>Needs periodic watering and inspection</td><td>Effectively maintenance free</td></tr>
<tr><td>Resistance stability</td><td>Varies with soil moisture and season</td><td>Stable through the year</td></tr>
<tr><td>Life</td><td>8–15 years depending on soil</td><td>15–25 years</td></tr>
</tbody></table></div>
<p class="ptable-note">Bangalore's rocky, often dry soil makes resistance harder to achieve than in alluvial regions, which is why chemical earthing has become the practical default for independent houses here.</p>

<h2>How many earth pits does a house need?</h2>
<ul>
<li><strong>Apartment or small flat</strong> — the building's earthing serves you; verify continuity at your sockets.</li>
<li><strong>Independent house</strong> — at least two pits: one for the neutral/body earth and one separate earth. Three is common on larger homes.</li>
<li><strong>With solar or a borewell pump</strong> — an additional dedicated pit is usually specified.</li>
<li><strong>With sensitive electronics or a home office</strong> — a clean, dedicated earth is worth the extra pit.</li>
</ul>

<h2>Target resistance and how to verify it</h2>
<p>For domestic installations, aim for an earth resistance below 5 ohms, and below 1 ohm where sensitive equipment or solar is involved. This is measurable — an earth resistance tester gives a number in minutes. Ask your electrician to test and record it, and to retest after the monsoon. An earthing system that has never been measured is an assumption, not a protection.</p>

<h2>What the material list looks like</h2>
<ul>
<li>Earth electrode — GI pipe, copper-bonded rod or chemical electrode.</li>
<li>Earth strip — GI or copper, sized to the installation.</li>
<li>Backfill compound or salt and charcoal.</li>
<li>Earth pit chamber with a removable cover, so it can actually be inspected later.</li>
<li>Earth wire — green, run to every socket and appliance point.</li>
<li>Clamps, bolts and a test link at the board.</li>
</ul>

<h2>Where earthing goes wrong</h2>
<ol>
<li><strong>The pit is covered permanently</strong> under a driveway or tile, so it can never be inspected or watered.</li>
<li><strong>Earth continuity is not run to every socket</strong> — common in older homes and in cost-cut new ones. Every 6A and 16A socket needs an earth conductor.</li>
<li><strong>Neutral and earth are bridged</strong> at the board as a shortcut. This defeats the RCCB and is genuinely dangerous.</li>
<li><strong>Resistance is never measured</strong>, so nobody knows whether the system works.</li>
<li><strong>Copper strip is substituted with thinner material</strong> once the pit is closed and no one is looking.</li>
</ol>

<p>See the full range and approximate rates on our <a href="../earthing-products.html">earthing products page</a>.</p>
""" + _cta(),
 D,
 [("How much does house earthing cost in Bangalore?", "Approximately ₹3,500 to ₹9,000 of material per pit for conventional pipe or plate earthing, and ₹6,500 to ₹18,000 per pit for chemical or maintenance-free earthing, plus digging and installation labour. Most independent houses need at least two pits."),
  ("What is the difference between conventional and chemical earthing?", "Conventional earthing uses a GI or copper pipe or plate in a pit packed with salt and charcoal, and needs periodic watering as its resistance varies with soil moisture. Chemical earthing uses a filled electrode with a backfill compound, holds resistance stable through the year and is effectively maintenance free, at roughly twice the material cost."),
  ("How many earth pits does a house need?", "An independent house needs at least two — one for the neutral or body earth and one separate earth — with three common on larger homes. A borewell pump or a solar installation usually calls for an additional dedicated pit. Flats rely on the building's earthing, so the check there is socket continuity."),
  ("What earth resistance is acceptable for a home?", "Below 5 ohms for a domestic installation, and below 1 ohm where solar or sensitive electronics are involved. It is measurable with an earth resistance tester in minutes, so ask your electrician to test and record the value, and to retest after the monsoon."),
  ("Why is earthing important in a house?", "It gives fault current a deliberate low-resistance path to ground, so that when a live wire touches an appliance body the current flows to earth and trips the breaker instead of passing through whoever touches it. It also provides a discharge path for surges and a stable reference for sensitive electronics."),
  ("What are the common mistakes in house earthing?", "Sealing the pit permanently under a driveway so it can never be inspected, failing to run earth continuity to every socket, bridging neutral and earth at the board as a shortcut which defeats the RCCB, never measuring the resistance, and substituting thinner strip once the pit is closed.")],
 ("earthing-rod-installation-house-site.jpg", "Workers installing a copper earthing electrode beside a newly built house")),

# ---------------------------------------------------------------- 10
("cat6-lan-cable-home-networking-guide",
 "Home Networking Cable Guide: Cat6, Coaxial and What to Lay Before Plastering",
 "How to wire a house for internet — Cat6 versus Cat6a, how many drops you need, where the router goes, coaxial and CCTV cabling, and approximate Bangalore price bands.",
 "Product Guide",
 """<p>Almost every homeowner who skips structured cabling regrets it within two years, usually while looking at a Wi-Fi extender plugged into a corridor socket. Network cable is cheap; running it after plastering is not.</p>

<h2>Why wired still matters in a Wi-Fi house</h2>
<p>Wi-Fi is a shared radio medium and Indian homes are built of concrete and brick, which is close to worst case for signal. The practical answer is not more powerful Wi-Fi — it is wired backhaul to two or three well-placed access points. That needs Cat6 in the walls, decided before plastering.</p>

<h2>Cat6, Cat6a or Cat5e?</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Cable</th><th>Speed / distance</th><th>Approx price (305m box)</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Cat5e</td><td>1 Gbps to 100m</td><td>₹3,500 – ₹6,500</td><td>Adequate today, poor future-proofing</td></tr>
<tr><td>Cat6</td><td>1 Gbps to 100m, 10 Gbps to ~55m</td><td>₹6,000 – ₹12,000</td><td>The right default for homes</td></tr>
<tr><td>Cat6a</td><td>10 Gbps to 100m</td><td>₹11,000 – ₹22,000</td><td>Worth it only for long runs or a home office</td></tr>
</tbody></table></div>
<p class="ptable-note">Insist on solid-conductor pure copper for in-wall runs. Copper-clad aluminium is widely sold, is noticeably cheaper, and fails on longer runs and with power-over-ethernet devices such as cameras and access points.</p>

<h2>How many drops, and where</h2>
<ul>
<li><strong>Two drops behind the TV</strong> — TV and set-top box or console.</li>
<li><strong>One drop per bedroom</strong>, near the desk or bedside.</li>
<li><strong>Two drops at ceiling level</strong> in the corridor or living area, for Wi-Fi access points. This is the one most people miss and the one that matters most.</li>
<li><strong>One drop at the work desk</strong>, plus a spare.</li>
<li><strong>All returning to one central point</strong> — a small cabinet or a deep enclosure near the meter or in a utility area, with a power socket in it.</li>
</ul>
<p>A 2BHK typically needs 6–8 drops and a 3BHK 10–14. At roughly ₹25–45 per metre installed, the whole job is a small fraction of the electrical budget.</p>

<h2>Put the router in the right place</h2>
<p>The most common Indian networking mistake is the router sitting inside the meter cupboard by the front door, because that is where the fibre arrives. Bring the fibre to the cupboard, then run Cat6 from there to a central access point location. A router in a metal cupboard behind a concrete wall is a router working at a fraction of its capability.</p>

<h2>Coaxial, CCTV and doorbell cabling</h2>
<ul>
<li><strong>RG-6 coaxial</strong> for cable TV and dish — still worth running one to the TV wall even in a streaming household.</li>
<li><strong>CCTV</strong> — modern IP cameras run on the same Cat6 with power over ethernet, so plan camera positions as network drops rather than separate cabling. Analogue systems still use RG-59 with a power pair.</li>
<li><strong>Video doorbell / intercom</strong> — a Cat6 drop to the main door serves almost every current system.</li>
<li><strong>Keep data cable separated from power cable</strong> — a parallel run alongside mains in the same conduit induces noise. Cross at right angles where they must meet, and use separate conduit.</li>
</ul>

<h2>Terminate properly</h2>
<p>Use keystone jacks in modular plates at the room end and a patch panel at the central point, rather than crimping plugs directly onto solid cable. Solid conductor is designed to be punched down, not crimped, and directly crimped plugs on solid cable are the single most common cause of intermittent home network faults.</p>

<p>See the full range on our <a href="../internet-networking.html">internet and networking page</a>.</p>
""" + _cta(),
 D,
 [("Should I use Cat6 or Cat6a cable at home?", "Cat6 is the right default for a home — it carries 1 Gbps over the full 100 metres and 10 Gbps over shorter runs, which covers every realistic domestic need. Cat6a is worth the extra cost only for unusually long runs or a serious home office. Cat5e still works but offers poor future-proofing for the small saving."),
  ("How many network points does a house need?", "Typically six to eight drops in a 2BHK and ten to fourteen in a 3BHK. Include two behind the TV, one per bedroom, one at the work desk and — most importantly — two at ceiling level in central locations for Wi-Fi access points, all returning to one enclosure with a power socket in it."),
  ("What is copper-clad aluminium LAN cable?", "It is cable with an aluminium core thinly coated in copper, sold at a noticeably lower price than pure copper. It performs poorly on long runs and fails with power-over-ethernet devices such as IP cameras and access points. For in-wall runs, insist on solid-conductor pure copper."),
  ("Where should the router be placed in a house?", "Not in the meter cupboard by the front door, which is where fibre usually arrives and where a metal enclosure behind concrete cripples the signal. Bring fibre to that point, then run Cat6 to a central location and place the router or an access point there."),
  ("Can network cable run in the same conduit as power cable?", "It should not. A long parallel run alongside mains cable induces noise into the data pair. Use separate conduit, and where the two must meet, cross them at right angles rather than running them together."),
  ("How much does home networking cable cost in Bangalore?", "Approximately ₹6,000 to ₹12,000 for a 305m box of Cat6 and ₹11,000 to ₹22,000 for Cat6a, with installed cost working out around ₹25 to ₹45 per metre including conduit, keystone jacks and termination. For most homes the whole job is a small fraction of the electrical budget.")],
 ("networking-cable-installation-home-office.jpg", "A technician terminating a Cat6 network cable into a wall data socket in a home office")),

# ---------------------------------------------------------------- 11
("flexible-cable-submersible-pump-cable-guide",
 "Flexible Cable and Submersible Pump Cable: Sizes, Types and Prices",
 "Choosing multi-core flexible cable and submersible pump cable — 2, 3 and 4 core, flat versus round, how to size for pump horsepower and depth, and approximate Bangalore price bands.",
 "Product Guide",
 """<p>House wire covers the walls; flexible and submersible cable covers everything else — appliances, pumps, motors and outdoor runs. It is a smaller line on the bill and a common place to get the sizing wrong.</p>

<h2>Flexible cable versus house wire</h2>
<p>House wire is single-core with relatively few strands, built to sit still inside a conduit for decades. Flexible cable has many fine strands and a tough outer sheath, built to bend, move and survive handling. Use flexible cable for appliance leads, pump connections, extension boards, submersible pumps and any run that is not fixed inside a wall.</p>

<h2>Core count: what each is for</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Type</th><th>Used for</th></tr></thead>
<tbody>
<tr><td>2 core</td><td>Single-phase appliances without earthing, lighting circuits in temporary use</td></tr>
<tr><td>3 core</td><td>Single-phase with earth — the standard for appliances, single-phase pumps, extensions</td></tr>
<tr><td>4 core</td><td>Three-phase equipment — three-phase motors, larger pumps, ACs on three-phase supply</td></tr>
<tr><td>3 core flat</td><td>Submersible borewell pumps — the flat profile fits alongside the delivery pipe</td></tr>
</tbody></table></div>

<h2>Sizing submersible pump cable</h2>
<p>Two things decide the size: motor current and cable length down the borewell. Voltage drop over depth is the factor that catches people out — a cable that is adequate at 100 feet may starve the motor at 400 feet.</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Pump</th><th>Up to 150 ft</th><th>150–300 ft</th><th>300–500 ft</th></tr></thead>
<tbody>
<tr><td>0.5 – 1 HP</td><td>3 core 1.5 sq mm</td><td>3 core 2.5 sq mm</td><td>3 core 4.0 sq mm</td></tr>
<tr><td>1.5 – 2 HP</td><td>3 core 2.5 sq mm</td><td>3 core 4.0 sq mm</td><td>3 core 6.0 sq mm</td></tr>
<tr><td>3 – 5 HP</td><td>3 core 4.0 sq mm</td><td>3 core 6.0 sq mm</td><td>3 core 10.0 sq mm</td></tr>
</tbody></table></div>
<p class="ptable-note">Indicative only — confirm against the pump manufacturer's chart for your exact motor rating and depth. Approximate rates run about ₹55–₹95 per metre for 3 core 1.5 sq mm flat, ₹90–₹150 for 2.5 sq mm and ₹140–₹240 for 4.0 sq mm.</p>

<h2>What "submersible grade" actually means</h2>
<p>A borewell cable sits permanently in water under pressure. Genuine submersible cable uses water-resistant insulation and a sheath rated for continuous immersion, with tight extrusion that does not allow water to travel along the cable. Ordinary flexible cable pushed down a borewell will absorb water within months, fail insulation and, in the worst case, energise the water column. This is one of the few places where using the correct product is not a matter of longevity but of safety.</p>

<h2>Practical points</h2>
<ul>
<li><strong>Never joint a submersible cable inside the borewell</strong> unless it is a proper heat-shrink jointing kit, correctly applied. Buy one continuous length.</li>
<li><strong>Include a separate earth</strong> to the pump body and to the borewell casing.</li>
<li><strong>Use a control panel with dry-run and overload protection</strong> — most pump failures are protection failures, not motor failures.</li>
<li><strong>Buy 10% extra length</strong> for the surface run to the panel; a cable that just reaches is a cable under tension.</li>
<li><strong>Check the copper.</strong> Under-weight submersible cable is common and, at depth, produces exactly the voltage drop that burns motors.</li>
</ul>

<h2>Flexible cable for appliances and outdoor use</h2>
<p>For appliance leads and extension boards, 3 core 1.0 or 1.5 sq mm covers most needs, with 2.5 sq mm for anything drawing over about 2,000 watts. For outdoor runs to a garden light or gate motor, use sheathed cable in conduit and keep joints inside proper enclosures — outdoor joints in a wall niche are the commonest cause of monsoon earth leakage and RCCB tripping.</p>

<p>See the full range on our <a href="../wires-and-cables.html">wires and cables page</a>.</p>
""" + _cta(),
 D,
 [("What size cable does a submersible pump need?", "It depends on both motor rating and borewell depth. A 1 HP pump typically needs 3 core 1.5 sq mm up to 150 feet, 2.5 sq mm to 300 feet and 4.0 sq mm beyond that, because voltage drop increases with depth. Always confirm against the pump manufacturer's chart for your exact motor."),
  ("What is the difference between flexible cable and house wire?", "House wire is single-core with relatively few strands and is designed to sit still inside a conduit for decades. Flexible cable has many fine strands and a tough outer sheath so it can bend and be handled, which makes it right for appliance leads, extension boards, pumps and any run that is not fixed inside a wall."),
  ("Can ordinary cable be used in a borewell?", "No. A borewell cable sits permanently in water under pressure, so it needs water-resistant insulation and a sheath rated for continuous immersion. Ordinary flexible cable absorbs water within months, fails insulation and can energise the water column. This is a safety requirement, not a longevity preference."),
  ("What is the difference between 3 core and 4 core cable?", "Three core carries phase, neutral and earth and is the standard for single-phase appliances and pumps. Four core carries three phases plus neutral or earth and is used for three-phase motors, larger pumps and equipment on a three-phase supply."),
  ("Why is submersible cable flat instead of round?", "The flat profile sits neatly alongside the delivery pipe inside the borewell casing, where a round cable would take up more radial space and risk being pinched or abraded against the casing as the pump assembly is lowered."),
  ("How much does submersible pump cable cost?", "Approximately ₹55 to ₹95 per metre for 3 core 1.5 sq mm flat, ₹90 to ₹150 for 2.5 sq mm and ₹140 to ₹240 for 4.0 sq mm, moving with copper rates. Buy one continuous length rather than jointing inside the borewell, and add about 10% extra for the surface run.")],
 ("electrician-hands-stripping-wire-closeup.jpg", "Close-up of an electrician stripping the insulation from a copper cable")),

# ---------------------------------------------------------------- 12
("wire-price-comparison-brands-bangalore",
 "Wire Price Comparison: Finolex, Polycab, KEI, RR Kabel and V-Guard in Bangalore",
 "An approximate side-by-side of house wire price bands across the major brands in Bangalore, what actually differs between them, and how to compare quotes without being misled by discounts.",
 "Pricing",
 """<p>Every house builder eventually lines up four quotes and finds they are not comparable — different brands, different grades, different coil lengths. This page puts the major brands side by side so you can at least compare like with like.</p>

<h2>Approximate 90m coil price bands (Bangalore, 2026)</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Brand</th><th>1.5 sq mm FR</th><th>2.5 sq mm FR</th><th>4.0 sq mm FR</th></tr></thead>
<tbody>
<tr><td>Finolex</td><td>₹1,950 – ₹2,250</td><td>₹3,150 – ₹3,650</td><td>₹4,700 – ₹5,400</td></tr>
<tr><td>Polycab</td><td>₹1,900 – ₹2,300</td><td>₹3,100 – ₹3,700</td><td>₹4,650 – ₹5,500</td></tr>
<tr><td>KEI</td><td>₹1,850 – ₹2,200</td><td>₹3,000 – ₹3,550</td><td>₹4,500 – ₹5,300</td></tr>
<tr><td>RR Kabel</td><td>₹1,850 – ₹2,250</td><td>₹3,050 – ₹3,600</td><td>₹4,550 – ₹5,350</td></tr>
<tr><td>V-Guard</td><td>₹1,800 – ₹2,200</td><td>₹2,950 – ₹3,500</td><td>₹4,450 – ₹5,250</td></tr>
</tbody></table></div>
<p class="ptable-note">Approximate ranges that move with copper. The overlap between brands is the real story — the honest spread between major brands is single-digit percent, not the 20–30% that some quotes suggest.</p>

<h2>What actually differs between the major brands</h2>
<p>Less than marketing implies. All the brands above use electrolytic-grade copper and meet the same IS standards. The genuine differences:</p>
<ul>
<li><strong>Insulation formulation and grade names.</strong> Each brand's premium range (FRLS, low-smoke, halogen-free) has its own name and its own price step.</li>
<li><strong>Coil length options.</strong> 90m is universal; 180m and 300m availability varies by brand and region.</li>
<li><strong>Colour range and consistency</strong> across batches, which matters if you extend wiring later.</li>
<li><strong>Local availability and replacement speed</strong> — genuinely important, and where a strong local distributor makes more practical difference than the brand name.</li>
<li><strong>Counterfeit exposure.</strong> The most heavily copied brands are the most popular ones, which is an argument for buying from an authorised source rather than for avoiding the brand.</li>
</ul>

<h2>How to compare quotes properly</h2>
<ol>
<li><strong>Compare the same grade.</strong> FR against FR, FRLS against FRLS. An FR quote will always undercut an FRLS quote, and the two are not the same product.</li>
<li><strong>Compare per metre, not per coil.</strong> A 180m coil quoted against a 90m coil is not a cheaper price.</li>
<li><strong>Check the size mix.</strong> A cheaper total often means less 4.0 sq mm — which is a specification change, not a saving.</li>
<li><strong>Ask what happens if a coil is short or faulty.</strong> Replacement policy is worth more than 2% on price.</li>
<li><strong>Treat outliers with suspicion.</strong> On a 3–5% margin business, a quote 15% below the pack is not competitive pricing.</li>
</ol>

<h2>So which brand should you buy?</h2>
<p>For a house, any of the major brands above, bought genuine from an authorised source, will serve you well for decades. The choice that actually affects your outcome is not the brand — it is whether the coil in your hand is real, correctly sized for the circuit, and installed properly. Pick the brand your electrician knows and your local distributor stocks deeply, so replacements and additions are simple.</p>

<p>Brand-wise reference rates: <a href="../price-lists/finolex-price-list.html">Finolex</a>, <a href="../price-lists/polycab-price-list.html">Polycab</a>, <a href="../price-lists/kei-price-list.html">KEI</a>, <a href="../price-lists/rr-kabel-price-list.html">RR Kabel</a>, <a href="../price-lists/v-guard-price-list.html">V-Guard</a>. Our detailed head-to-head is in <a href="finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html">the four-brand wire comparison</a>.</p>
""" + _cta(),
 D,
 [("Which wire brand is cheapest in Bangalore?", "The honest spread between Finolex, Polycab, KEI, RR Kabel and V-Guard is single-digit percent on comparable grades, with the bands overlapping heavily. V-Guard and KEI often sit slightly lower and Finolex and Polycab slightly higher, but the difference on a full house is small compared with the effect of getting the size mix or the grade right."),
  ("Is there a real quality difference between major wire brands?", "Not much on the fundamentals. All the major brands use electrolytic-grade copper and meet the same IS standards. The genuine differences are in premium insulation formulations, coil length options, colour consistency across batches, and local availability and replacement speed."),
  ("How do I compare wire quotes from different shops?", "Compare the same grade — FR against FR, not FR against FRLS — compare per metre rather than per coil since coil lengths differ, check that the size mix is identical especially the 4.0 sq mm quantity, and ask about the replacement policy for a short or faulty coil."),
  ("Why is one shop's wire quote much cheaper than the others?", "On a 3 to 5% margin business, a quote 15% below the rest is not competitive pricing. It usually indicates a different grade, a shorter coil, copper shortfall, or duplicate stock. Ask to see the carton, the batch number and the QR code before paying."),
  ("Which wire brand should I buy for my house?", "Any of the major brands bought genuine from an authorised seller will serve a house for decades. The choice that actually affects your outcome is whether the coil is genuine, correctly sized for the circuit and properly installed. Prefer the brand your electrician knows and your local distributor stocks deeply."),
  ("Do wire prices differ between Bangalore areas?", "Not meaningfully for genuine stock, since prices are MRP-linked and margins are thin. What varies is delivery cost, credit terms and replacement service. A large local distributor generally quotes closer to the market band than a small shop buying in small lots.")],
 ("contractor-checking-price-list-phone.jpg", "An electrical contractor comparing wire price quotations on his phone at a construction site")),

# ---------------------------------------------------------------- 13
("switchgear-brands-comparison-india",
 "Switchgear Brands Compared: Schneider, Legrand, HPL, GreatWhite and Anchor",
 "How the major Indian switchgear brands compare on range, price band, availability and where each fits — plus what to look for beyond the brand name when buying MCBs and distribution boards.",
 "Brand Guide",
 """<p>Switchgear is bought once and relied on for twenty years, so the brand decision matters more here than in almost any other category in a house. Here is an honest comparison of what is actually available in Bangalore.</p>

<h2>Where each brand sits</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Brand</th><th>Price band</th><th>Strength</th><th>Best suited to</th></tr></thead>
<tbody>
<tr><td>Schneider Electric</td><td>Premium</td><td>Deep technical range, strong RCBO and industrial crossover</td><td>Larger homes, home offices, installations wanting a wide protection range</td></tr>
<tr><td>Legrand</td><td>Premium</td><td>Design consistency across switches and switchgear, good enclosures</td><td>Homes matching switchgear to a premium switch range</td></tr>
<tr><td>HPL</td><td>Mid</td><td>Broad domestic range, widely available, good value</td><td>Mainstream residential builds</td></tr>
<tr><td>GreatWhite</td><td>Mid</td><td>Strong modular switch and switchgear pairing, good availability</td><td>Homes buying switches and switchgear together</td></tr>
<tr><td>Anchor by Panasonic</td><td>Entry to mid</td><td>Very wide distribution, familiar to every electrician</td><td>Budget-conscious builds and replacements</td></tr>
</tbody></table></div>
<p class="ptable-note">Approximate single-pole MCB bands: entry ₹150–₹280, mid ₹250–₹450, premium ₹400–₹800. RCCBs run roughly ₹1,800–₹5,500 depending on rating and brand.</p>

<h2>What to look at beyond the brand</h2>
<ol>
<li><strong>Breaking capacity (kA).</strong> 10kA is standard for domestic MCBs in India; some cheaper ranges are 6kA. It is printed on the device — check it rather than assuming.</li>
<li><strong>Trip curve.</strong> B and C curves must be available across the ratings you need. Some entry ranges only stock C.</li>
<li><strong>RCBO availability.</strong> If you want individual leakage protection on the geyser or the pump, confirm the brand's RCBO range covers your ratings before committing to the board.</li>
<li><strong>Isolator and changeover range,</strong> if you are installing an inverter or generator.</li>
<li><strong>Local spares.</strong> A brand your area's electricians do not stock means a two-day wait for a ₹300 part.</li>
</ol>

<h2>Match the board to the breakers</h2>
<p>Distribution boards and MCBs are designed as a system — module widths, DIN rail heights and comb busbars differ slightly by manufacturer. Mixing usually works but can leave gaps, forced fits and busbars that do not seat cleanly, and it splits warranty responsibility. Choose one brand for the board and the breakers inside it.</p>

<h2>Counterfeit switchgear is the real risk</h2>
<p>The differences between these brands are modest; the difference between genuine and fake switchgear is total. A counterfeit MCB may click convincingly and do nothing under actual fault current, and its printed kA rating is meaningless. This is the item where buying from an authorised distributor matters most, because it is the one component whose failure mode is a fire that nobody traces back to a ₹250 part.</p>
<p>What to check: sealed box, sharp and correctly aligned printing, a clearly marked breaking capacity, consistent moulding with no flash or misaligned seams, a firm and defined toggle action, and a QR code that verifies where the brand provides one. Our guides on <a href="how-to-identify-duplicate-legrand-mcb.html">duplicate Legrand MCBs</a> and <a href="how-to-identify-duplicate-indo-asian-mcb.html">duplicate MCBs generally</a> go into the specific tells.</p>

<h2>A sensible default</h2>
<p>For most Bangalore homes: a mid-range board and MCBs from one brand, a 30mA RCCB from the same family, RCBOs on the geyser and any outdoor circuit, and everything bought in sealed boxes from an authorised source. Spending up to premium is defensible if you want the wider protection range or are matching a premium switch series; spending down to the cheapest available is not, because this is the category where the saving is smallest and the consequence largest.</p>

<p>Brand pages: <a href="../brands/schneider.html">Schneider</a>, <a href="../brands/legrand.html">Legrand</a>, <a href="../brands/hpl.html">HPL</a>, <a href="../brands/greatwhite.html">GreatWhite</a>, <a href="../brands/anchor-panasonic.html">Anchor by Panasonic</a>.</p>
""" + _cta(),
 D,
 [("Which switchgear brand is best for a home in India?", "For most homes a mid-range board and MCBs from a single brand such as HPL or GreatWhite is entirely adequate. Schneider and Legrand are worth the premium if you want a deeper protection range or are matching a premium switch series. The brand matters less than buying genuine product in sealed boxes from an authorised source."),
  ("What breaking capacity should a domestic MCB have?", "10kA is the standard for domestic MCBs in India, though some cheaper ranges are rated 6kA. The figure is printed on the device, so check it rather than assuming. On a counterfeit breaker the printed rating is meaningless, which is another reason to buy from an authorised seller."),
  ("How much does an MCB cost in India?", "Approximately ₹150 to ₹280 for entry-range single-pole MCBs, ₹250 to ₹450 for mid-range and ₹400 to ₹800 for premium. RCCBs run roughly ₹1,800 to ₹5,500 depending on current rating, sensitivity and brand."),
  ("Can I mix MCB brands in one distribution board?", "It usually works but is not advisable. Module widths, DIN rail heights and comb busbar designs vary slightly between manufacturers, so mixing can leave gaps, forced fits and busbars that do not seat properly, and it splits warranty responsibility between two companies."),
  ("How do I spot a counterfeit MCB?", "Check for a sealed box, sharp and correctly aligned printing, a clearly marked breaking capacity in kA, consistent moulding with no flash or misaligned seams, and a firm defined toggle action. Scan the QR code where the brand provides one. A counterfeit may click convincingly and still do nothing under real fault current."),
  ("Is expensive switchgear worth it for a house?", "Spending up to a premium brand is defensible if you want a wider protection range, better enclosures or matching design with a premium switch series. Spending down to the cheapest available is not, because switchgear is the category where the saving is smallest and the consequence of failure is largest.")],
 ("electrician-installing-mcb-distribution-board.jpg", "Switchgear being installed in a residential distribution board")),

# ---------------------------------------------------------------- 14
("ac-geyser-wiring-wire-size-mcb-guide",
 "Wiring for ACs and Geysers: Wire Size, MCB Rating and Common Mistakes",
 "How to wire high-load appliances correctly — wire size for 1, 1.5 and 2 ton ACs and for geysers, MCB and RCBO selection, dedicated circuits, stabiliser points and what goes wrong.",
 "Product Guide",
 """<p>Air conditioners and geysers are the two highest-load appliances in an Indian home and the two most often wired incorrectly, because both are frequently added after the house is built.</p>

<h2>Wire size and protection by appliance</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Appliance</th><th>Approx load</th><th>Wire size</th><th>MCB</th></tr></thead>
<tbody>
<tr><td>1 ton AC</td><td>~1,000–1,200 W</td><td>2.5 sq mm (4.0 for long runs)</td><td>16A, Curve C</td></tr>
<tr><td>1.5 ton AC</td><td>~1,500–1,800 W</td><td>4.0 sq mm</td><td>20A, Curve C</td></tr>
<tr><td>2 ton AC</td><td>~2,000–2,400 W</td><td>4.0 sq mm</td><td>20A / 25A, Curve C</td></tr>
<tr><td>Geyser 15L / 2000W</td><td>~2,000 W</td><td>2.5 sq mm</td><td>16A, Curve C</td></tr>
<tr><td>Geyser 25L / 3000W</td><td>~3,000 W</td><td>4.0 sq mm</td><td>20A, Curve C</td></tr>
<tr><td>Instant geyser 4500W</td><td>~4,500 W</td><td>4.0 sq mm</td><td>25A, Curve C</td></tr>
</tbody></table></div>
<p class="ptable-note">Sizes assume normal run lengths. Runs beyond about 20 metres from the board need the next size up to keep voltage drop within limits — check with the <a href="../tools/voltage-drop-calculator.html">voltage drop calculator</a>.</p>

<h2>Every AC and geyser needs its own circuit</h2>
<p>Not a spur off the bedroom socket circuit — a dedicated run from the distribution board with its own MCB. Three reasons: the load is too high to share, a fault on a shared circuit takes out the whole room, and an individual MCB lets you isolate the appliance for service without killing anything else. This is also why adding an AC to an existing house properly means running a new cable, not tapping the nearest 16A socket.</p>

<h2>Curve C, not Curve B</h2>
<p>Compressor motors draw a large inrush current for a fraction of a second at startup. A Curve B breaker sees that as a fault and trips. Curve C tolerates the inrush while still protecting against a genuine overload. Nuisance tripping every time the AC starts is almost always a curve problem, and the correct fix is the right curve, never a higher rating.</p>

<h2>RCBO on the geyser</h2>
<p>A geyser is an electric heating element immersed in water in a wet room — which is the highest shock-risk appliance in a house. Element leakage is a common failure and often develops slowly. An RCBO on the geyser circuit gives it both overload and leakage protection independently, so a failing element trips its own circuit instead of the whole-house RCCB, and you find out early rather than by touching a tap.</p>

<h2>Stabilisers and the socket question</h2>
<ul>
<li><strong>Modern inverter ACs</strong> mostly have wide input voltage tolerance and are marketed as stabiliser-free. In areas with genuinely unstable supply a stabiliser is still worth having — check the manufacturer's stated voltage range against local conditions.</li>
<li><strong>If a stabiliser is used,</strong> it needs its own point at an accessible height, wired on the same dedicated circuit.</li>
<li><strong>Use a 16A or 20A point,</strong> not a 6A socket with an adapter. Adapters on high-load appliances are the single most common cause of burnt sockets in Indian homes.</li>
<li><strong>Position the AC point</strong> close to the indoor unit, high on the wall, so the appliance lead is not run across the room.</li>
</ul>

<h2>The five mistakes we see most</h2>
<ol>
<li><strong>ACs and geysers run on 2.5 sq mm because "it works".</strong> It works until the cable is warm all summer and its insulation ages a decade in two years.</li>
<li><strong>A higher MCB fitted to stop tripping,</strong> which removes the protection instead of fixing the cause.</li>
<li><strong>No earth run to the appliance point,</strong> especially on retrofit circuits.</li>
<li><strong>Copper joints inside the wall</strong> on a retrofitted AC line, made in a junction box that later gets plastered over.</li>
<li><strong>Adding a second AC to a circuit sized for one.</strong> Two 1.5 ton units on a single 20A circuit is an overload waiting for a hot afternoon.</li>
</ol>

<p>Size your own circuits with the <a href="../tools/wire-size-calculator.html">wire size calculator</a> and the <a href="../tools/mcb-selector.html">MCB selector</a>.</p>
""" + _cta(),
 D,
 [("What wire size is needed for a 1.5 ton AC?", "4.0 sq mm on a dedicated circuit with a 20A Curve C MCB, for normal run lengths. Runs longer than about 20 metres from the distribution board may need the next size up to keep voltage drop within limits. A 1 ton unit can use 2.5 sq mm on short runs but 4.0 sq mm is safer."),
  ("What wire size does a geyser need?", "2.5 sq mm with a 16A MCB for a 2000W storage geyser, and 4.0 sq mm with a 20A MCB for a 3000W unit. Instant geysers around 4500W need 4.0 sq mm with a 25A breaker. Every geyser should be on its own dedicated circuit, ideally protected by an RCBO."),
  ("Why does my AC trip the MCB every time it starts?", "Almost always because the circuit uses a Curve B breaker. Compressor motors draw a large inrush current for a fraction of a second at startup, which a Curve B breaker reads as a fault. The fix is a Curve C breaker of the correct rating, never a higher rated breaker on the same cable."),
  ("Does an air conditioner need a dedicated circuit?", "Yes. The load is too high to share, a fault on a shared circuit takes out the whole room, and a dedicated MCB lets you isolate the unit for service. Adding an AC to an existing house properly means running a new cable from the board, not tapping the nearest 16A socket."),
  ("Should a geyser have an RCBO?", "It is strongly advisable. A geyser is a heating element immersed in water in a wet room, which makes it the highest shock-risk appliance in a house, and element leakage often develops slowly. An RCBO gives that circuit its own overload and leakage protection so a failing element trips itself rather than the whole house."),
  ("Do inverter ACs need a stabiliser?", "Most modern inverter air conditioners have a wide input voltage tolerance and are marketed as stabiliser-free. In areas where the supply genuinely swings outside the manufacturer's stated range, a stabiliser is still worth fitting, on its own accessible point wired to the same dedicated circuit.")],
 ("happy-electrician-installing-modular-switch.jpg", "An electrician completing a high-load appliance point in a Bangalore home")),

]
