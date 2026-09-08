# -*- coding: utf-8 -*-
"""Legrand cluster: a dealer pillar page, five intent pages and four posts,
written for the Legrand queries Search Console shows landing on the site
(legrand price list 2026 is the top-clicked query, plus legrand mcb price list
2026, legrand switchgear price list 2026, legrand price list 2026 india).

Facts used come from the Legrand Corp MPL 2026 held in the quote builder:
range names, cat-number format, DX3 features (integrated label holder,
biconnect lower terminals, sliding bottom clamp, IP20 terminals, ISI mark to
IS/IEC 60898-1), packing quantities, the "bold cat nos are normally available
with stockists, others 4-8 weeks" rule, and the 10-year manufacturing-defect
replacement policy printed under Myrius and Britzy. Prices are MRP inclusive
of GST from the same MPL and are rendered from data_brand_prices so they
cannot drift from the price-list pages. Mount Cable's own selling price is
never published for Legrand; "best price" is argued as below-MRP dealer
pricing plus a reference quote, never as a percentage.
"""
from data_brand_prices import (LEGRAND_DISCOUNT, lnet, with_net, LEGRAND_MCB_C, LEGRAND_RCCB_AC, LEGRAND_SPN_DB, LEGRAND_SWITCH_CMP,
                               LEGRAND_ISOLATORS, LEGRAND_BRITZY_PLATES, LEGRAND_LYNCUS_PLATES,
                               LEGRAND_MYRIUS_PLATES, _mcb_rows, rs)

D = ("2026-09-08", "September 8, 2026")
W = "https://wa.me/918867676700"
PH = "88676 76700"

CTA = (f'<p class="muted"><strong>Get your Legrand price.</strong> WhatsApp the list, the DB schedule or a photo of the '
       f'electrician\'s memo to <a href="{W}">{PH}</a>. Mount Cable India replies with an itemised Legrand quote within '
       '60 minutes, and you can use it as a reference price anywhere in Bangalore. No obligation to buy from us.</p>')


def _tbl(cols, rows):
    head = "".join(f"<th>{c}</th>" for c in cols)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return with_net(f'<div class="ptable-wrap"><table class="ptable"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')


MCB_TABLE = _tbl(["Rating", "SP", "SPN", "DP", "TP", "TPN", "FP"], _mcb_rows(LEGRAND_MCB_C))
RCCB_TABLE = _tbl(["Rating", "DP 30 mA", "DP 100 mA", "DP 300 mA", "FP 30 mA", "FP 100 mA", "FP 300 mA"],
                  [(r[0],) + tuple(rs(x) for x in r[1:]) for r in LEGRAND_RCCB_AC])
DB_TABLE = _tbl(["Ways", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
                [(r[0], rs(r[2]), rs(r[3]), rs(r[4]), rs(r[5])) for r in LEGRAND_SPN_DB])
SWITCH_TABLE = _tbl(["Item", "Britzy", "Allzy", "Lyncus", "Myrius"],
                    [(d,) + tuple(rs(x) if x else "—" for x in (b, a, l, m)) for d, b, a, l, m in LEGRAND_SWITCH_CMP])
ISO_TABLE = _tbl(["Rating", "DP", "TP", "FP"], [(r[0], rs(r[1]), rs(r[2]), rs(r[3])) for r in LEGRAND_ISOLATORS])
MRP_LINE = '<p class="ptable-note">Struck-through figures are Legrand MRP per unit inclusive of GST, Corp MPL 2026. Bold figures are Mount Cable India\'s price at <strong>65% off MRP</strong>, one of the highest Legrand discounts in Bangalore, on every Legrand product.</p>'

# A 3BHK DB costed at MRP so the "where the money goes" argument uses real figures.
DB_EXAMPLE = _tbl(["Item", "Qty", "MRP each", "MRP total"], [
    ("DX3 DP isolator 40 A (incomer)", "1", rs(961), rs(961)),
    ("DX3 DP RCCB 40 A 30 mA", "1", rs(6360), rs(6360)),
    ("DX3 SP MCB 6 to 32 A, C curve", "10", rs(494), rs(4940)),
    ("Ekinox SPN 12-way DB, IP43 metal door", "1", rs(4884), rs(4884)),
    ("Total at MRP", "", "", rs(961 + 6360 + 4940 + 4884)),
])

BOARD_EXAMPLE = _tbl(["6-module bedroom board", "Britzy", "Lyncus", "Myrius"], [
    ("2 x 6A one-way switch", rs(112), rs(200), rs(360)),
    ("Fan regulator 100 W (1 module)", rs(650), rs(734), "Myrius 1432 (6794 39)"),
    ("6/16A socket with shutter (2 module)", rs(294), rs(434), rs(684)),
    ("6-module plate with frame, white", rs(254), rs(332), rs(676)),
    ("6-module metal flush box", rs(226), rs(226), rs(226)),
    ("Board total at MRP", rs(112 + 650 + 294 + 254 + 226), rs(200 + 734 + 434 + 332 + 226), rs(360 + 1432 + 684 + 676 + 226)),
])

RANGES = _tbl(["Category", "Legrand range", "What it is", "Price page"], [
    ("MCBs", "DX3 AC MCBs, C and D curve, 0.5 to 63 A; 80 to 125 A breakers; DC MCBs", "10 kA ISI-marked breakers for every circuit in a home or building", '<a href="price-lists/legrand-mcb-price-list.html">Legrand MCB price list</a>'),
    ("Earth leakage", "DX3 RCCBs (AC, Type S, HPI) and RCBOs", "Shock and fire protection, 25 to 63 A, 30 to 300 mA", '<a href="price-lists/legrand-switchgear-price-list.html">Legrand switchgear price list</a>'),
    ("Isolation and control", "DX3 isolators, changeover switches, CX3 contactors, time switches, twilight switches", "Incomers, generator changeover, pump and lighting control", '<a href="price-lists/legrand-switchgear-price-list.html">Legrand switchgear price list</a>'),
    ("Distribution boards", "Ekinox3 SPN, ETPN, vertical TPN, Flexy, Mivan, PPI, NEO; metal enclosures; cable end boxes", "Boards for single-phase homes to three-phase buildings", '<a href="price-lists/legrand-switchgear-price-list.html">Legrand switchgear price list</a>'),
    ("Surge protection", "T1, T1+T2 and T2 SPDs, PV and DC SPDs", "Lightning and surge protection at the main and sub boards", '<a href="price-lists/legrand-switchgear-price-list.html">Legrand switchgear price list</a>'),
    ("MCCBs and metering", "DPX3 160 / 250 / 630 MCCBs, DRX, EMDX3 meters", "Building incomers and energy monitoring", "On request"),
    ("Modular switches, entry", "Britzy, Allzy", "Everyday switches with a 10-year manufacturing-defect replacement on switches and sockets", '<a href="price-lists/legrand-switches-price-list.html">Legrand switches price list</a>'),
    ("Modular switches, mid", "Lyncus, Mylinc", "Contemporary plates in white, grey, silver, champagne and metallics; USB-C and BLDC modules", '<a href="price-lists/legrand-switches-price-list.html">Legrand switches price list</a>'),
    ("Modular switches, premium", "Myrius, Myrius glass and antibacterial, Arteor, Arteor Advance", "Premium residences, hotels and offices; IoT and KNX automation", '<a href="price-lists/legrand-switches-price-list.html">Legrand switches price list</a>'),
    ("Cable management", "Trunking, DLP, floor boxes, Soluclip", "Office and commercial wiring accessories", "On request"),
])

LEGRAND_SEO_PAGES = [

# ---------------------------------------------------------------- pillar
{"slug": "legrand-dealer-bangalore", "cluster": "legrand",
 "title": "Legrand Dealer in Bangalore — Original Legrand Switches, MCBs, RCCBs and DBs at the Best Price | Mount Cable India",
 "desc": "Legrand dealer in Bangalore: every Legrand range in stock, DX3 MCBs and RCCBs, Ekinox DBs, Myrius, Lyncus, Allzy and Britzy switches, 100% original at 65% off MRP, one of the highest Legrand discounts in the city. MPL 2026 prices, free next-day delivery, pay after checking. Mount Cable India, Jayanagar and Chickpete.",
 "h1": "Legrand dealer in Bangalore: original switches, MCBs and DBs at the best price",
 "badge": "Full Legrand range in stock · 65% off MRP · Verify before you pay",
 "intro": "Mount Cable India stocks the complete Legrand range in Bangalore, bought through Legrand's authorised distribution and sold at 65% off MRP, one of the highest Legrand discounts in the city: DX3 MCBs, RCCBs and RCBOs, Ekinox distribution boards, and the Myrius, Lyncus, Allzy and Britzy modular switch ranges. Send your list to WhatsApp for an itemised Legrand quote within 60 minutes, take free next-day delivery anywhere in Bangalore, and pay after you have checked every piece at your site.",
 "answer": "Mount Cable India is a Legrand stockist in Bangalore with the DX3 switchgear, Ekinox distribution board and Myrius, Lyncus, Allzy and Britzy switch ranges in stock at Jayanagar and Chickpete. Every item is original, bought through Legrand's authorised distribution, and sold at 65% off the MPL 2026 MRP, one of the highest Legrand discounts in Bangalore. WhatsApp 88676 76700 for a Legrand quote within 60 minutes.",
 "hero": ("electrician-installing-mcb-distribution-board.jpg", "Electrician fitting Legrand DX3 MCBs into an Ekinox distribution board in a Bangalore home"),
 "sections": [
  ("Why buy Legrand from a stockist rather than a shop",
   "<p>Legrand sells in India through authorised distributors, and dealers buy from them. Most electrical shops in Bangalore keep a handful of Legrand MCBs and one switch range and order the rest, which means a wait, a substitution, or a piece that came from somewhere other than the Legrand chain. A stockist holds the range: every DX3 pole and rating, the RCCB sensitivities, the Ekinox board sizes, and the plates in every module count for each switch range. That is the difference between a DB that is finished on Tuesday and one that waits three weeks for a four-pole RCCB.</p>"
   "<p>It also settles the originality question. Legrand switchgear is copied because the brand carries a premium, and a copied MCB is the one product in a house that fails silently: it looks fine until the day it does not trip. Buying from a stockist whose invoice chain runs back to Legrand's distributor is the simplest protection. Ask us for it; we will show it. The checks you can do yourself are in <a href=\"original-legrand-mcb.html\">Legrand MCB 100% original</a>.</p>"),
  ("What is in stock",
   "<p>All of it, in the ranges below. Items printed in bold in the Legrand MPL are the ones Legrand keeps with its stockists; those are on our shelves. The non-bold items, mostly special ratings, Arteor automation and cable management, are 4 to 8 weeks from Legrand and we order them against your requirement.</p>" + RANGES.replace('href="price-lists/', 'href="price-lists/')),
  ("Legrand prices: MRP, and what best price means",
   "<p>Every Legrand product has an MRP printed on the pack from the Corp MPL 2026, and every dealer sells below it, because Legrand's MRP is a list price set well above what the trade pays. How far below depends on the range, the quantity and how the dealer buys. A stockist buying by the carton from the distributor has the most room, and Mount Cable India gives <strong>65% off MRP on every Legrand product</strong>, one of the highest Legrand discounts available in Bangalore: a ₹494 DX3 single-pole MCB is ₹173, a ₹6,360 RCCB is ₹2,226. That is close to the floor for original stock. A quote well below it is a copy, a returned unit or grey stock without warranty. Use our price as your reference: if another price is far under it, ask why.</p>"
   "<p>The MRP tables for every range are on the <a href=\"price-lists/legrand-price-list.html\">Legrand price list 2026</a>, the <a href=\"price-lists/legrand-mcb-price-list.html\">MCB price list</a>, the <a href=\"price-lists/legrand-switchgear-price-list.html\">switchgear price list</a> and the <a href=\"price-lists/legrand-switches-price-list.html\">switches price list</a>. A snapshot of the items most homes buy:</p>"
   + _tbl(["Item", "MRP"], [("DX3 SP MCB 6 to 32 A, C curve", rs(494)), ("DX3 DP MCB 6 to 32 A", rs(1693)), ("DX3 DP RCCB 40 A 30 mA", rs(6360)),
                             ("DX3 DP isolator 40 A", rs(961)), ("Ekinox SPN 8-way DB, IP43 metal door", rs(4065)), ("Ekinox SPN 12-way DB, IP43 metal door", rs(4884)),
                             ("Britzy 6A one-way switch", rs(56)), ("Lyncus 6A one-way switch", rs(100)), ("Myrius 6A one-way switch", rs(180)), ("Lyncus 6/16A socket", rs(434))])
   + MRP_LINE),
  ("How we prove every piece is original",
   "<ul><li><strong>Invoice chain.</strong> Our Legrand stock is bought from Legrand's authorised distributor, and the invoice carries the cat numbers you receive.</li>"
   "<li><strong>Cat number check.</strong> Every Legrand item has a six-digit cat number printed on the product and the pack, in the MPL format such as 4085 90 for a 10 A single-pole DX3. We match the pack, the product and the invoice line.</li>"
   "<li><strong>Check at delivery.</strong> Open the packs, compare the laser-printed rating label and the DX3 features against the MPL, and pay only when satisfied. The checklist is on the <a href=\"original-legrand-mcb.html\">original Legrand MCB page</a>.</li>"
   "<li><strong>Manufacturer replacement.</strong> Legrand replaces Myrius and Britzy switches and power sockets with a manufacturing defect for 10 years, and we handle the claim.</li></ul>"),
  ("Legrand for a house in Bangalore: what we usually quote",
   "<p>For a 2BHK or 3BHK the standard Legrand schedule is a DX3 double-pole isolator or SPN MCB as incomer, a 30 mA double-pole RCCB, 8 to 14 single-pole DX3 MCBs in an Ekinox SPN board with a metal door, Lyncus or Allzy switches through the house and Myrius plates in the living room if the budget allows. Costed at MRP a 3BHK DB comes to about ₹17,000 before the dealer price; the working is on <a href=\"legrand-mcb-best-price.html\">Legrand MCB best price</a>, and the switch side is on <a href=\"legrand-switches-best-price.html\">Legrand switches best price</a>. Size the breakers with the <a href=\"tools/mcb-selector.html\">MCB selector</a> and count the boards with the <a href=\"tools/material-list-builder.html\">material list builder</a>.</p>"),
  ("Delivery across Bangalore", "<p>Free next-day delivery, usually same day for Legrand switchgear, to every area of the city:</p>{areas}"),
 ],
 "faqs": [
  ("Is Mount Cable an authorised Legrand dealer in Bangalore?", "Mount Cable India stocks the full Legrand range at Jayanagar and Chickpete, bought through Legrand's authorised distribution, and can show the invoice chain for any item. Every piece is original and sold at 65% off MRP."),
  ("What Legrand products do you keep in stock?", "DX3 MCBs (all poles, C and D curve), RCCBs and RCBOs, isolators and changeovers, Ekinox SPN, TPN and vertical TPN distribution boards, SPDs, and the Myrius, Lyncus, Allzy and Britzy switch ranges with plates in every module count. Arteor, MCCBs and cable management are ordered against requirement."),
  ("What is the Legrand MCB price in Bangalore?", "A DX3 single-pole 6 to 32 A C-curve MCB is ₹494 MRP; double pole ₹1,693; a 40 A DP 30 mA RCCB ₹6,360; an Ekinox 8-way SPN DB ₹4,065 with a metal door. At Mount Cable India's 65% off MRP those are ₹173, ₹593, ₹2,226 and ₹1,423."),
  ("How do I get the best price on Legrand switches and MCBs?", "Send the complete list at once, with plate module counts and the DB schedule, so it can be quoted as one Legrand order. Mount Cable India gives 65% off MRP on every Legrand item and quotes within 60 minutes."),
  ("How do I know the Legrand MCB is original?", "Check the cat number on the product and pack against the invoice, the laser-printed rating label, the DX3 features such as the integrated label holder and biconnect terminals, and the price against MRP. Mount Cable India lets you do all of this at delivery before paying."),
  ("Do you deliver Legrand outside Bangalore?", "Yes. WhatsApp the list with your address and we quote the material and the transport. Karnataka towns are served by road, usually within two to three days."),
 ]},

# ---------------------------------------------------------------- original MCB
{"slug": "original-legrand-mcb", "cluster": "legrand",
 "title": "Legrand MCB 100% Original — 7 Checks, Why Fakes Exist, and Where to Buy in Bangalore | Mount Cable India",
 "desc": "How to confirm a Legrand DX3 MCB is 100% original: cat number, laser rating label, integrated label holder, biconnect terminals, ISI mark, packing and the price test against MRP. Why duplicate Legrand MCBs exist, what a fake does in a fault, and Mount Cable India's check-before-you-pay guarantee.",
 "h1": "Legrand MCB 100% original: how to be sure, and where to buy in Bangalore",
 "badge": "Check every MCB at delivery · Pay after",
 "intro": "A miniature circuit breaker is the one product in a house you cannot test by using it. A counterfeit Legrand MCB switches the light on just like the real one; the difference shows only in a fault, when the copy may not trip. This page gives the seven checks that separate a genuine DX3 from a copy, explains why the copies exist, and describes how Mount Cable India lets you run every check at your site before you pay.",
 "answer": "A genuine Legrand DX3 MCB carries a six-digit Legrand cat number on the product and the pack that matches the invoice, a crisp laser-printed rating label, the integrated label holder and biconnect lower terminals of the DX3 design, the ISI mark to IS/IEC 60898-1, and comes packed 10 to a box for single pole. A price well below a stockist's net, which at Mount Cable India's 65% off MRP is ₹173 for a 6 to 32 A single pole, is the strongest warning of a copy.",
 "hero": ("homeowner-electrician-discussing-switchboard.jpg", "Homeowner and electrician checking Legrand DX3 MCBs against the invoice before fitting the distribution board"),
 "sections": [
  ("Why Legrand MCBs are copied",
   "<p>Legrand is the most specified switchgear brand in premium Indian housing, and a specification is exactly what a counterfeiter needs: the buyer has already decided on the brand and is looking only at price. A copy of a ₹494 single-pole DX3 costs a fraction of that to make, looks identical on the outside, and is sold into the gap between the MRP and the honest dealer price. The buyer thinks he has found a better deal on the same product. The <a href=\"original-vs-duplicate-electrical-products.html\">original vs duplicate guide</a> explains how the trade works across brands; the Legrand-specific tells are below.</p>"),
  ("Seven checks for an original Legrand DX3 MCB",
   "<ol>"
   "<li><strong>Cat number.</strong> Every Legrand item has a six-digit catalogue number printed as two groups, for example 4085 90 for a 10 A single-pole C-curve DX3, 4086 33 for a 16 A double pole, 4118 52 for a 40 A DP 30 mA RCCB. The number is on the product face, on the pack and on the dealer's invoice. All three must agree. A pack with no cat number, or a number that is not in the Legrand MPL, is a copy.</li>"
   "<li><strong>Rating label.</strong> Legrand laser-prints the rating, curve and standard on the front of the breaker: for instance C16, 240/415 V, 10 kA, IS/IEC 60898-1. The print is sharp and level. Ink-jet, smudged or slightly tilted text is the most common fault in copies.</li>"
   "<li><strong>DX3 design features.</strong> The MPL lists them: an integrated label holder on the front, a sliding bottom clamp for DIN-rail removal, biconnect lower terminals that take a cable and a busbar comb together, IP20 protected terminals with sliding shutters, and colour-coded on/off indication on the dolly. Copies usually get one or two of these wrong or omit them.</li>"
   "<li><strong>ISI mark and standard.</strong> DX3 AC MCBs up to 63 A are ISI marked to IS/IEC 60898-1; RCCBs to IS 12640-1; RCBOs to IS 12640-2. The mark and the standard number are moulded or printed on the device.</li>"
   "<li><strong>Weight and feel.</strong> A genuine DX3 single pole has a solid, dense feel and a crisp dolly action with a definite snap. Copies are lighter, the dolly is soft, and the moulding seams are rough.</li>"
   "<li><strong>Packing.</strong> Single-pole DX3 MCBs come 1/10/120: one per inner pack, ten per box, 120 per carton. SPN units 1/5/60, DP 1/40, TP and FP 1/32. A single pole sold in a box of 12, or loose without a Legrand pack, did not come through the Legrand chain.</li>"
   "<li><strong>Price against MRP.</strong> The MPL 2026 MRP for a 6 to 32 A single pole is ₹494, for a 40 to 63 A single pole ₹1,180, for a DP 6 to 32 A ₹1,693. Legrand's MRP is a list price and the trade sells far below it; Mount Cable India's 65% off MRP puts the single pole at ₹173. That is close to the floor for original stock. A price well under a stockist's net, or a seller who cannot show the invoice chain behind such a price, means the product is not what the box says.</li>"
   "</ol>"
   "<p>The full list of DX3 MCB prices, so you can run the seventh check on any quote, is on the <a href=\"price-lists/legrand-mcb-price-list.html\">Legrand MCB price list</a>. Our step-by-step guide with photographs of the tells is <a href=\"blog/how-to-identify-duplicate-legrand-mcb.html\">how to identify a duplicate Legrand MCB</a>.</p>"),
  ("Legrand DX3 MCB MRP, for the price test", MCB_TABLE + MRP_LINE),
  ("What a counterfeit MCB does in a fault",
   "<p>An MCB has two jobs: trip on a sustained overload through a thermal element, and trip instantly on a short circuit through a magnetic element rated to the breaking capacity, 10 kA for a DX3. A copy is built to switch, not to break. Its thermal element may be miscalibrated so a 16 A circuit carries 30 A until the wire insulation softens; its magnetic element and arc chutes may not clear a short at all, so the breaker welds shut and the fault runs until the utility fuse blows or the wire burns. The <a href=\"blog/mcb-rccb-rcbo-guide-for-homes.html\">MCB, RCCB and RCBO guide</a> explains what each device is supposed to do; a copy does none of it reliably.</p>"),
  ("Our guarantee: check every piece before you pay",
   "<p>Every Legrand item Mount Cable India delivers can be opened and checked at your site against the seven points above, with our delivery staff present, before payment. The invoice carries the cat number of each line so the pack, the product and the paper can be matched on the spot. Anything that fails any check is taken back on the spot and replaced. Legrand's own manufacturing-defect replacement, 10 years on Myrius and Britzy switches and sockets, is handled by us. Buy on the <a href=\"legrand-dealer-bangalore.html\">Legrand dealer page</a> or send the list to WhatsApp.</p>"),
  ("Original Legrand switches too",
   "<p>The same trade copies Legrand switches, especially Myrius plates and 6A modules. The checks are similar: cat number on the module back and the pack, Legrand moulded on the rocker, the plate's support frame with the Legrand mark, and the price against MRP. See <a href=\"blog/how-to-identify-duplicate-legrand-switches.html\">how to identify duplicate Legrand switches</a> and the <a href=\"legrand-switches-best-price.html\">Legrand switches best price page</a>.</p>"),
 ],
 "faqs": [
  ("How can I check if a Legrand MCB is original?", "Match the six-digit cat number on the product, the pack and the invoice; look for the crisp laser-printed rating label, the integrated label holder and biconnect terminals of the DX3 design, the ISI mark to IS/IEC 60898-1, the 1/10/120 packing on single poles, and compare the price with the ₹494 MRP for a 6 to 32 A single pole."),
  ("Does Legrand have a QR code or app to verify MCBs?", "Legrand relies on cat numbers, laser-printed labels, design features and its authorised distribution chain rather than a consumer QR check. The reliable route is to buy from a stockist that can show the invoice chain and to check the seven points at delivery."),
  ("What is the MRP of a Legrand DX3 MCB?", "₹494 for a 6 to 32 A single pole C curve, ₹824 for 0.5 to 4 A, ₹1,180 for 40 to 63 A; double pole ₹1,693 (6 to 32 A); triple pole ₹2,745; four pole ₹3,729. From the Legrand Corp MPL 2026."),
  ("What happens if a duplicate MCB is installed?", "It switches normally but may not trip on overload or short circuit. The wire overheats or the fault runs until something upstream fails, which is the fire scenario an MCB exists to prevent."),
  ("Can I return a Legrand MCB that fails the checks?", "At Mount Cable India, yes, at the door: every piece is checked at delivery before payment and anything that fails is replaced on the spot."),
  ("Where can I buy original Legrand MCBs in Bangalore?", "Mount Cable India, Jayanagar and Chickpete, with the full DX3 range in stock, free next-day delivery across Bangalore and payment after inspection. WhatsApp 88676 76700."),
 ]},

# ---------------------------------------------------------------- switches best price
{"slug": "legrand-switches-best-price", "cluster": "legrand",
 "title": "Best Price on Legrand Switches in Bangalore — Myrius, Lyncus, Allzy, Britzy at 65% Off MRP | Mount Cable India",
 "desc": "Best price on Legrand modular switches in Bangalore: Myrius, Lyncus, Allzy and Britzy mechanisms, plates and boxes sold at 65% off MPL 2026 MRP. How Legrand switch pricing works, a costed switchboard in each range, how to send a list for the lowest quote, and the 10-year replacement policy.",
 "h1": "Best price on Legrand switches in Bangalore: Myrius, Lyncus, Allzy and Britzy",
 "badge": "All four ranges in stock · 65% off MRP · 10-year replacement on switches and sockets",
 "intro": "Legrand prices every switch range as a kit of parts: the mechanism, the cover plate with its support frame, and the flush box. The best price on a Legrand switchboard therefore comes from quoting the whole board, and the whole house, as one list. Mount Cable India stocks Myrius, Lyncus, Allzy and Britzy in every module count at 65% off MRP, one of the highest Legrand discounts in Bangalore; send the board count and the quote comes back within 60 minutes.",
 "answer": "Mount Cable India sells Legrand switches at 65% off the MPL 2026 MRP. A 6A one-way switch is ₹56 MRP in Britzy and Allzy, ₹100 in Lyncus and ₹180 in Myrius, which is ₹20, ₹35 and ₹63 net; a 6-module white plate is ₹254, ₹332 and ₹676 MRP, or ₹89, ₹116 and ₹237 net. WhatsApp 88676 76700 for the full list within 60 minutes.",
 "hero": ("happy-electrician-installing-modular-switch.jpg", "Electrician fitting a Legrand Lyncus modular switch plate in a Bangalore apartment"),
 "sections": [
  ("How Legrand switch pricing works",
   "<p>Three parts, three prices. The mechanism is the switch, socket, regulator or data module, priced per module. The cover plate comes with its support frame and is priced by module count and finish. The flush box is metal or plastic and is priced by module count. A four-range comparison of the pieces most boards use:</p>" + SWITCH_TABLE + MRP_LINE
   + "<p>The complete mechanism and plate lists for each range are on the <a href=\"price-lists/legrand-switches-price-list.html\">Legrand switches price list</a>.</p>"),
  ("A bedroom board costed in each range",
   "<p>Two switches, a fan regulator and a 6/16A socket on a 6-module plate, at MRP:</p>" + BOARD_EXAMPLE
   + "<p>Multiply by the number of boards in the house and the switch budget appears. A 3BHK typically has 18 to 24 boards, so the gap between Britzy and Myrius across a house is several tens of thousands of rupees at MRP, and the dealer discount applies to all of it. The <a href=\"tools/material-list-builder.html\">material list builder</a> produces the board list from the room count.</p>"),
  ("How to get the lowest Legrand switch price",
   "<ol><li><strong>Send the full house in one list</strong>: every board with its module count and the modules on it. One order is priced better than five visits.</li>"
   "<li><strong>State the range and the plate finish</strong> for each area. Mixing Myrius in the living room with Lyncus elsewhere is normal and we quote it that way.</li>"
   "<li><strong>Include the boxes.</strong> Legrand metal flush boxes are priced separately and are often forgotten until the electrician asks.</li>"
   "<li><strong>Ask for the DB on the same quote.</strong> Legrand MCBs and switches together make one Legrand order, which is how a stockist buys and prices.</li>"
   "<li><strong>Use the quote as a reference.</strong> 65% off MRP is close to the floor for original Legrand. If a shop beats it by a lot, the plates or modules are not what the pack says. See <a href=\"blog/how-to-identify-duplicate-legrand-switches.html\">how to identify duplicate Legrand switches</a>.</li></ol>"),
  ("Which range to choose",
   "<p>Britzy and Allzy give the Legrand mechanism at the lowest cost and suit rental flats, utility areas and budget builds; Allzy adds coloured plates and a BLDC fan regulator. Lyncus is the mid range most Bangalore homes settle on, with plates in white, chic grey, brushed silver, alu sunset and champagne and modules such as 20 W and 45 W USB-C chargers. Myrius is the premium range with glass and metallic plates, the antibacterial series and the widest hospitality and automation set. The full argument is in <a href=\"blog/legrand-myrius-vs-lyncus-vs-allzy-vs-britzy.html\">Myrius vs Lyncus vs Allzy vs Britzy</a>.</p>"),
  ("The 10-year replacement policy",
   "<p>Legrand's MPL states that the company will, at its discretion, replace Myrius and Britzy switches (without LED lamp) and power sockets with a manufacturing defect within 10 years, and other wiring accessories in those ranges within a shorter period. That policy applies to product bought through the Legrand chain with a dealer invoice, which is one more reason to buy from a stockist rather than a loose box. We keep the invoice and handle the claim.</p>"),
  ("Plates in every module count, in stock",
   "<p>The most common reason a Legrand board is delayed is a missing 8-module vertical or 12-module plate in the chosen finish. We stock the plate ranges in full. Lyncus classic white, for example, runs from ₹184 for 1 and 2 module to ₹974 for 18 module at MRP; Britzy from ₹132 to ₹622; Myrius regular white from ₹306 to ₹1,498. The tables are on the switches price list. Delivery is free next day across Bangalore, and boards are checked at your site before payment. The main <a href=\"legrand-dealer-bangalore.html\">Legrand dealer page</a> has the rest of the range.</p>"),
 ],
 "faqs": [
  ("What is the best price for Legrand switches in Bangalore?", "65% off MRP at Mount Cable India, on every Legrand switch, plate and box. A 6A one-way switch is ₹56 MRP in Britzy and Allzy, ₹100 in Lyncus and ₹180 in Myrius, so ₹20, ₹35 and ₹63 net. The full list is quoted within 60 minutes."),
  ("What is the Legrand Myrius switch price?", "Myrius regular white at MRP: 6A one-way ₹180, 6A two-way ₹326, 16A one-way ₹442, 32A DP ₹1,510, 6/16A socket ₹684; white plates ₹306 (1 module) to ₹1,498 (18 module). Dealers sell below these figures."),
  ("What is the Legrand Lyncus switch price?", "Lyncus classic white at MRP: 6A one-way ₹100, 16A one-way ₹246, 32A DP ₹718, 6/16A socket ₹434, fan regulator ₹734; plates ₹184 to ₹974."),
  ("Are Legrand plates and switches priced separately?", "Yes. Mechanism, cover plate with support frame and flush box are three separate prices in every Legrand range. A board costs the sum of its modules plus the plate and box."),
  ("Which Legrand switch range is best value?", "Allzy for the lowest cost with coloured plates, Lyncus for most homes, Myrius for a premium interior. Britzy matches Allzy on price with fewer plate finishes."),
  ("Do Legrand switches have a warranty?", "Legrand replaces Myrius and Britzy switches and power sockets with a manufacturing defect for 10 years at its discretion, on product bought through its chain with an invoice. Mount Cable India handles the claim."),
 ]},

# ---------------------------------------------------------------- MCB best price
{"slug": "legrand-mcb-best-price", "cluster": "legrand",
 "title": "Best Price on Legrand MCB, RCCB and DB in Bangalore — DX3 and Ekinox at 65% Off MRP | Mount Cable India",
 "desc": "Best pricing on Legrand DX3 MCBs, RCCBs, RCBOs, isolators and Ekinox distribution boards in Bangalore. MPL 2026 MRP tables, a 3BHK DB costed at MRP, how to send a DB schedule for the lowest quote, and where the money goes. Mount Cable India, Legrand stockist.",
 "h1": "Best price on Legrand MCBs, RCCBs and distribution boards in Bangalore",
 "badge": "Every DX3 pole and rating in stock · 65% off MRP · Check at delivery",
 "intro": "The best price on Legrand switchgear comes from sending the distribution board schedule as one list: incomer, RCCB, every outgoing MCB by rating and pole, and the Ekinox board itself. Mount Cable India stocks the complete DX3 and Ekinox ranges in Bangalore at 65% off MRP, one of the highest Legrand discounts in the city, quotes within 60 minutes, and lets you check every breaker at your site before you pay.",
 "answer": "Mount Cable India sells Legrand switchgear at 65% off the MPL 2026 MRP: a DX3 6 to 32 A single pole is ₹494 MRP and ₹173 net, a double pole ₹1,693 and ₹593, a 40 A DP 30 mA RCCB ₹6,360 and ₹2,226, a 12-way Ekinox SPN DB with metal door ₹4,884 and ₹1,709. A 3BHK board is about ₹17,000 at MRP and about ₹6,000 net. WhatsApp 88676 76700 with the schedule.",
 "hero": ("electrician-installing-mcb-distribution-board.jpg", "Legrand DX3 MCBs and RCCB being fitted into an Ekinox SPN distribution board"),
 "sections": [
  ("Legrand DX3 MCB MRP", "<p>Legrand prices MCBs in rating bands, so a 6 A and a 32 A of the same pole cost the same and the step comes at 40 A. C curve, 10 kA:</p>" + MCB_TABLE + MRP_LINE),
  ("Legrand RCCB and isolator MRP", RCCB_TABLE + "<p>Isolators, for the incomer position:</p>" + ISO_TABLE + MRP_LINE),
  ("Legrand Ekinox SPN distribution board MRP", DB_TABLE + MRP_LINE + "<p>RCBOs, TPN and vertical TPN boards, Flexy and Mivan boards and enclosures are on the <a href=\"price-lists/legrand-switchgear-price-list.html\">Legrand switchgear price list</a>.</p>"),
  ("A 3BHK distribution board costed at MRP",
   DB_EXAMPLE + "<p>Three things decide the number. The RCCB is the single largest item, so choose the rating you need (40 A covers most homes) and the AC type unless you run a solar inverter, where the HPI type is worth its premium. Every outgoing MCB from 6 to 32 A costs the same ₹494, so there is no saving in under-sizing a circuit and no penalty in sizing it correctly. The board price steps up with the door: IP30 for a cupboard, IP43 metal door for the usual indoor position, acrylic for looks, IP54 for damp locations. The <a href=\"tools/mcb-selector.html\">MCB selector</a> gives the rating for each circuit and the <a href=\"blog/distribution-board-selection-guide-home.html\">DB selection guide</a> the number of ways.</p>"),
  ("How to get the lowest Legrand switchgear price",
   "<ol><li><strong>Send the DB schedule</strong>, or a photo of the electrician's list: incomer rating, RCCB rating and sensitivity, each outgoing MCB by rating and pole, and the DB size and door.</li>"
   "<li><strong>Add the switches</strong> so the house is one Legrand order. Stockists buy Legrand by the carton and price a full order better than a DB alone.</li>"
   "<li><strong>Ask for stock items.</strong> C-curve DX3 in standard ratings, AC-type RCCBs and Ekinox SPN boards are stocked and priced best; special ratings and D-curve above 32 A are ordered from Legrand.</li>"
   "<li><strong>Compare on MRP.</strong> Every quote you get should be readable against the tables above. Our price is 65% off MRP on every line, close to the floor for original stock; a quote far below it is not a better deal on the same product. Read <a href=\"original-legrand-mcb.html\">Legrand MCB 100% original</a>.</li></ol>"),
  ("Legrand against the alternatives on price",
   "<p>Schneider is priced close to Legrand and the choice between them is usually availability and the look of the board; the <a href=\"blog/legrand-vs-schneider-mcb-and-switches.html\">Legrand vs Schneider</a> comparison goes through it. Anchor by Panasonic's UNO range is the budget alternative with the same 10 kA rating at roughly 60 percent of the MRP; its figures are on the <a href=\"price-lists/anchor-mcb-price-list.html\">Anchor MCB price list</a>. For a premium home or any building where the specification names Legrand, the DX3 and Ekinox combination is what we quote, and the <a href=\"legrand-dealer-bangalore.html\">Legrand dealer page</a> has the rest of the range.</p>"),
 ],
 "faqs": [
  ("What is the best price for a Legrand MCB in Bangalore?", "65% off the ₹494 MRP, so ₹173 for a 6 to 32 A single-pole DX3 at Mount Cable India, quoted on the whole DB schedule within 60 minutes on WhatsApp."),
  ("What is the Legrand RCCB price?", "DX3 double-pole 30 mA AC type: ₹5,478 at 25 A, ₹6,360 at 40 A, ₹7,818 at 63 A MRP. Four pole 30 mA: ₹7,870, ₹8,068 and ₹8,976. HPI and Type S cost more."),
  ("How much does a Legrand DB for a 3BHK cost?", "About ₹17,000 at MRP for a 40 A DP isolator, a 40 A 30 mA RCCB, ten single-pole DX3 MCBs and a 12-way Ekinox SPN board with metal door. The dealer price is below that."),
  ("Is a Legrand 32A MCB more expensive than a 16A?", "No. Legrand prices DX3 MCBs in bands: every rating from 6 A to 32 A of the same pole has the same MRP. The step is at 40 A."),
  ("Do you stock four-pole Legrand MCBs and RCCBs?", "Yes, DX3 TP, TPN and FP MCBs and FP RCCBs are stocked at Jayanagar and Chickpete along with the Ekinox ETPN and vertical TPN boards they go into."),
  ("Can I check the MCBs before paying?", "Yes. Every Legrand item is delivered in its pack with the cat number on the invoice, and you check the product, pack and paper at your site before payment."),
 ]},

# ---------------------------------------------------------------- all products
{"slug": "legrand-products-bangalore", "cluster": "legrand",
 "title": "All Legrand Products Available in Bangalore — Complete Range: DX3, Ekinox, Myrius, Lyncus, Allzy, Britzy, Arteor | Mount Cable India",
 "desc": "The complete Legrand product range available in Bangalore from Mount Cable India: DX3 MCBs, RCCBs, RCBOs, isolators, contactors and timers, Ekinox distribution boards, SPDs, DPX3 MCCBs, and the Britzy, Allzy, Lyncus, Mylinc, Myrius and Arteor switch ranges. Stock items, order items and how to order by cat number.",
 "h1": "All Legrand products available in Bangalore: the complete range",
 "badge": "Every Legrand range · Stock and order items · Original",
 "intro": "Legrand's Indian catalogue runs to more than 360 pages, from a 6 A single-pole MCB to KNX home automation. This page lists the whole of it as it is available from Mount Cable India in Bangalore: what is on the shelf at Jayanagar and Chickpete, what is ordered from Legrand against your requirement, and how to order any item by its cat number so that you get exactly the product the specification names.",
 "answer": "Mount Cable India stocks the full Legrand range in Bangalore: DX3 MCBs, RCCBs and RCBOs, isolators and changeovers, Ekinox SPN, TPN and vertical TPN distribution boards, SPDs, and the Britzy, Allzy, Lyncus and Myrius modular switch ranges with plates and boxes. Arteor, Arteor Advance, Mylinc, DPX3 MCCBs, EMDX3 meters and cable management are ordered from Legrand against requirement. Every item is original and sold at 65% off MRP.",
 "hero": ("wire-coils-warehouse-electrical-distributor.jpg", "Legrand switchgear and switch stock on the shelves at Mount Cable India, Bangalore"),
 "sections": [
  ("The Legrand range, category by category", RANGES),
  ("Stock items and order items",
   "<p>Legrand marks the items it keeps with its stockists in bold in the MPL, and states that the rest are delivered within 4 to 8 weeks from the date of order. In practice that means:</p>"
   "<ul><li><strong>On our shelf:</strong> DX3 C-curve MCBs in every pole from 6 to 63 A, DX3 AC-type RCCBs at 25, 40 and 63 A in 30 and 100 mA, DP and FP isolators, Ekinox SPN boards in every size and door, ETPN and vertical TPN boards in the common sizes, and the Britzy, Allzy, Lyncus and Myrius mechanisms and plates in every module count and the main finishes.</li>"
   "<li><strong>Ordered from Legrand:</strong> D-curve MCBs above 32 A, DC MCBs, Type S and HPI RCCBs in some ratings, 80 to 125 A breakers, SPDs, contactors and time switches, DPX3 MCCBs, Arteor and Arteor Advance, Mylinc, Myrius glass and IoT, cable management, and any plate finish outside the main ones.</li></ul>"
   "<p>If your specification names an order item, send it early; we place the order with Legrand and hold the stock items until the whole list is ready to deliver together.</p>"),
  ("How to order by cat number",
   "<p>Every Legrand product has a six-digit cat number printed as two groups of digits, and it is the only reliable way to specify an item across the range: 4085 90 is a 10 A single-pole C-curve DX3, 4118 52 a 40 A DP 30 mA RCCB, 5076 12 a 12-way IP43 SPN Ekinox board, 6772 00 a Lyncus 6A one-way switch, 6775 06 a Lyncus 6-module classic white plate. Consultants' BOMs and builders' specifications carry these numbers. Send the list as it is and we quote line by line against the MPL, with the MRP shown for each cat number and our price below it. If a list is written in words instead, we translate it to cat numbers on the quote so there is no substitution.</p>"),
  ("Prices for every range",
   "<p>MRP for the whole range, from the Corp MPL 2026, is published on our price pages: the <a href=\"price-lists/legrand-price-list.html\">Legrand price list 2026 overview</a>, the <a href=\"price-lists/legrand-mcb-price-list.html\">MCB price list</a>, the <a href=\"price-lists/legrand-switchgear-price-list.html\">switchgear and DB price list</a> and the <a href=\"price-lists/legrand-switches-price-list.html\">switches price list</a>. Mount Cable India sells all of it at 65% off MRP; see <a href=\"legrand-mcb-best-price.html\">best price on Legrand MCBs</a> and <a href=\"legrand-switches-best-price.html\">best price on Legrand switches</a> for how to get the lowest quote.</p>"),
  ("Projects, builders and electricians",
   "<p>For apartment projects and villas we supply Legrand against the consultant's schedule, floor by floor, with cat numbers on every invoice line and delivery timed to the electrician's programme. Bulk orders of DX3 MCBs, Ekinox boards and Lyncus or Myrius plates are priced as one Legrand order. Electricians and contractors get the same range, the same originality checks and trade pricing on repeat business. The main <a href=\"legrand-dealer-bangalore.html\">Legrand dealer page</a> has the delivery areas and the originality guarantee.</p>"),
 ],
 "faqs": [
  ("Which Legrand products are available in Bangalore from Mount Cable?", "The complete range: DX3 MCBs, RCCBs, RCBOs, isolators, changeovers, contactors and timers, Ekinox distribution boards, SPDs, DPX3 MCCBs, EMDX3 meters, Britzy, Allzy, Lyncus, Mylinc, Myrius and Arteor switches, and cable management. Stock items are on the shelf; the rest is ordered from Legrand in 4 to 8 weeks."),
  ("Do you keep Legrand Arteor in stock?", "Arteor and Arteor Advance are ordered from Legrand against your requirement, usually within 4 to 8 weeks. Myrius, Lyncus, Allzy and Britzy are stocked."),
  ("Can I order Legrand by catalogue number?", "Yes, and it is the best way. Send the six-digit cat numbers from the specification and the quote comes back line by line against the MPL with MRP and our price."),
  ("Are all your Legrand products original?", "Yes. Stock is bought through Legrand's authorised distribution, the invoice carries the cat number of each line, and every item can be checked at delivery before payment."),
  ("Do you supply Legrand for apartment projects?", "Yes, against the consultant's schedule, delivered floor by floor with cat numbers on every invoice line and priced as one Legrand order."),
  ("What is the Legrand price list for 2026?", "The Legrand Corp MPL 2026 MRP for every range is on our Legrand price list pages, with Mount Cable India's price at 65% off beside each figure."),
 ]},

# ---------------------------------------------------------------- best prices of Legrand products (broad)
{"slug": "legrand-best-price-bangalore", "cluster": "legrand",
 "title": "Best Prices on Legrand Products in Bangalore — MCB, RCCB, DB and Switches at 65% Off MRP | Mount Cable India",
 "desc": "Best prices on Legrand products in Bangalore from a stockist: DX3 MCBs and RCCBs, Ekinox DBs and the Myrius, Lyncus, Allzy and Britzy switch ranges sold at 65% off MPL 2026 MRP. Why a stockist's price is lower, what a too-low price means, a whole-house Legrand budget at MRP, and how to get a quote in 60 minutes.",
 "h1": "Best prices on Legrand products in Bangalore",
 "badge": "65% off MRP on every Legrand product · Quote in 60 minutes",
 "intro": "Legrand publishes an MRP for every product and every dealer sells below it, so the question is not whether you can get a discount but who can give the largest one on original stock. Mount Cable India gives 65% off MRP on every Legrand product, one of the highest Legrand discounts in Bangalore, because a stockist buying by the carton from the authorised distributor has room a shop buying a box at a time does not. The full Legrand range is at Jayanagar and Chickpete, with free next-day delivery and payment after you have checked the goods.",
 "answer": "The best price on Legrand products in Bangalore comes from a stockist that buys by the carton through Legrand's authorised distribution and quotes the whole house as one order. Mount Cable India sells every Legrand range at 65% off the MPL 2026 MRP, one of the highest Legrand discounts in Bangalore, delivers free the next day across the city, and lets you check each item before paying. WhatsApp 88676 76700 for a quote within 60 minutes.",
 "hero": ("contractor-checking-price-list-phone.jpg", "Contractor comparing a Legrand quote from Mount Cable India against the MRP on his phone"),
 "sections": [
  ("Why a stockist's Legrand price is lower",
   "<p>Legrand's Indian channel is manufacturer, authorised distributor, dealer, buyer. A stockist buys from the distributor in carton quantities across the range and turns the stock quickly, so the buying price is lower and the margin needed per piece is smaller. A shop that keeps a few Legrand boxes buys them from the same distributor, or from a stockist, in small lots, and each piece carries more cost. Both sell below MRP; the stockist sells further below. That is the whole of the argument, and it is why Mount Cable India can give 65% off MRP on every Legrand product, one of the highest Legrand discounts a Bangalore buyer will find for original stock.</p>"),
  ("What a too-low Legrand price means",
   "<p>There is a floor under every genuine Legrand price: the distributor's price to the dealer. Our 65% off MRP sits close to that floor, and nobody sells original DX3 or Myrius much below it for long. A quote well under a stockist's net price is therefore one of three things: a copy, which is common for DX3 MCBs and Myrius plates; returned or damaged stock; or grey stock that came from outside the Indian channel and carries no replacement policy. The <a href=\"original-legrand-mcb.html\">Legrand MCB 100% original page</a> gives the checks; the price test against MRP is the fastest of them.</p>"),
  ("Legrand MRP for the items a house buys",
   "<p>Struck-through figures are MRP per unit inclusive of GST from the Corp MPL 2026; bold figures are our price at 65% off.</p>"
   + _tbl(["Item", "MRP"], [("DX3 SP MCB 6 to 32 A", rs(494)), ("DX3 SP MCB 40 to 63 A", rs(1180)), ("DX3 DP MCB 6 to 32 A", rs(1693)), ("DX3 DP isolator 40 A", rs(961)),
                             ("DX3 DP RCCB 40 A 30 mA", rs(6360)), ("DX3 DP RCBO 6 to 32 A 30 mA", rs(6974)), ("Ekinox SPN 8-way DB, IP43 metal door", rs(4065)), ("Ekinox SPN 12-way DB, IP43 metal door", rs(4884)),
                             ("Britzy 6A one-way switch", rs(56)), ("Allzy 6A one-way switch", rs(56)), ("Lyncus 6A one-way switch", rs(100)), ("Myrius 6A one-way switch", rs(180)),
                             ("Lyncus 6/16A socket with shutter", rs(434)), ("Lyncus fan regulator 100 W", rs(734)), ("Lyncus 6-module plate, classic white", rs(332)), ("Myrius 6-module plate, white", rs(676))])
   + MRP_LINE),
  ("A whole-house Legrand budget at MRP",
   "<p>Every figure here is MRP, and Mount Cable India takes 65% off all of it. For a 3BHK: the distribution board at about ₹17,000 (worked on the <a href=\"legrand-mcb-best-price.html\">MCB best price page</a>), plus 20 switchboards. In Lyncus a typical board of two switches, a regulator and a socket on a 6-module plate is ₹1,926 at MRP including the box, so 20 boards are roughly ₹38,000; in Britzy about ₹31,000; in Myrius about ₹68,000. A Lyncus house with a DX3 board therefore lands near ₹55,000 at MRP, which is about ₹19,000 at our 65% off. Send the board count and the DB schedule together and it is quoted as one order.</p>"),
  ("How to get the quote",
   "<ol><li>WhatsApp the list, the DB schedule, the consultant's BOM with cat numbers, or a photo of the electrician's memo to " + PH + ".</li>"
   "<li>Say which switch range and plate finish goes where; mixing ranges by room is normal.</li>"
   "<li>Receive an itemised quote within 60 minutes with MRP and our price on each line.</li>"
   "<li>Use it as a reference anywhere. If you buy from us, delivery is free the next day across Bangalore and you pay after checking each pack at your site.</li></ol>"
   "<p>The full range is on <a href=\"legrand-products-bangalore.html\">all Legrand products available</a>, the MRP tables on the <a href=\"price-lists/legrand-price-list.html\">Legrand price list 2026</a>, and the rest of the story on the <a href=\"legrand-dealer-bangalore.html\">Legrand dealer page</a>.</p>"),
 ],
 "faqs": [
  ("Who gives the best price on Legrand in Bangalore?", "Mount Cable India, which stocks the full range and gives 65% off MRP on every Legrand product, one of the highest Legrand discounts in Bangalore for original stock bought through Legrand's authorised distribution."),
  ("How much below MRP are Legrand products sold?", "Mount Cable India sells every Legrand product at 65% off MRP. Send the list and the quote shows MRP and the net price on each line."),
  ("What is a fair price for a Legrand DX3 MCB?", "₹173, which is 65% off the ₹494 MRP, for a 6 to 32 A single pole at Mount Cable India. That is close to the floor for original stock; a price well under it is a copy or grey stock."),
  ("What does a Legrand house cost?", "Around ₹55,000 at MRP for a 3BHK with a DX3 distribution board and 20 Lyncus switchboards; about ₹48,000 in Britzy and ₹85,000 in Myrius. At Mount Cable India's 65% off MRP those are roughly ₹19,000, ₹17,000 and ₹30,000."),
  ("Do you give better prices on bulk Legrand orders?", "Yes. Project quantities of DX3 MCBs, Ekinox boards and plates are priced as one Legrand order, and repeat trade customers get trade pricing."),
  ("How fast is a Legrand quote?", "Within 60 minutes on WhatsApp during working hours, itemised with MRP and our price on every line."),
 ]},
]

# ---------------------------------------------------------------- posts
LEGRAND_BLOG = [

("legrand-myrius-vs-lyncus-vs-allzy-vs-britzy",
 "Legrand Myrius vs Lyncus vs Allzy vs Britzy: Which Switch Range for Your Home",
 "The four Legrand modular switch ranges compared on price from the MPL 2026, plate finishes, modules available, warranty and where each belongs in a Bangalore house.",
 "Comparison",
 """<p><strong>Britzy and Allzy are Legrand's entry ranges at the same mechanism price, with Allzy adding coloured plates;
Lyncus is the mid range with the widest plate palette and the most modern modules; Myrius is the premium range with
glass, metallic and antibacterial options. For most Bangalore homes, Lyncus through the house with Myrius in the
living room is the combination that balances looks and budget.</strong></p>

<h2>The four ranges on price</h2>
""" + SWITCH_TABLE + MRP_LINE + """
<p>Every range prices the mechanism, the cover plate with support frame and the flush box separately. The full lists are on
the <a href="../price-lists/legrand-switches-price-list.html">Legrand switches price list</a>.</p>

<h2>Britzy</h2>
<p>The everyday range: white mechanisms, white plates from 1 to 18 modules, a 6A switch at ₹56 MRP and a 6/16A socket at
₹294. Fan regulators, an 8-step regulator, RJ45 and TV sockets and hotel functions are all there. What it lacks is plate
finishes; Britzy is white. It carries the same 10-year replacement policy on switches and sockets as Myrius.</p>

<h2>Allzy</h2>
<p>Allzy matches Britzy on the 6A switch (₹56) and adds a 10A switch line at ₹60, a BLDC fan regulator at ₹938, and plates
in white, rose gold, gold, matt black and aluminium champagne. Matt black mechanisms cost about 15 to 20 percent more than
white. For a budget build that still wants a black or metallic plate in the hall, Allzy is the answer.</p>

<h2>Lyncus</h2>
<p>Lyncus is where most of our Legrand switch orders land. The 6A switch is ₹100, the 6/16A socket ₹434, the fan
regulator ₹734, and the modules include USB-C chargers at 20, 30, 45 and 65 W, a Bluetooth sound receiver, a BLDC
regulator and a rotary LED dimmer. Plates come in classic white, chic grey, brushed silver, alu sunset and champagne,
from ₹184 to ₹974 for white and a little more for the metallics. Mylinc, with its white dove and matt grey mechanisms,
sits alongside it.</p>

<h2>Myrius</h2>
<p>The premium range: the 6A switch is ₹180, the socket ₹684, and the plates run from ₹306 for white to ₹1,498 for 18
module, with charcoal grey, ice white, ice black, pearl champagne, sonic silver and 3 mm toughened glass above that. Myrius
adds the antibacterial series with silver-ion surfaces, a modular MCB that sits in the plate, the full hospitality set,
and the IoT and connected modules. It is what architects specify for premium apartments and villas.</p>

<h2>Where each belongs</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Area or situation</th><th>Range</th></tr></thead>
<tbody>
<tr><td>Rental flat, utility, store, servant room</td><td>Britzy or Allzy</td></tr>
<tr><td>Budget home wanting a coloured plate in the hall</td><td>Allzy</td></tr>
<tr><td>Family home, all rooms</td><td>Lyncus</td></tr>
<tr><td>Living and dining in a family home</td><td>Myrius plates on Lyncus budget elsewhere</td></tr>
<tr><td>Premium apartment, villa, designer interior</td><td>Myrius, or Arteor if specified</td></tr>
<tr><td>Hotel and hospitality</td><td>Myrius or Arteor</td></tr>
</tbody></table></div>

<h2>What is common to all four</h2>
<p>The mechanisms are Legrand's own, ISI-marked where the standard applies, with the same 230 V ratings and the same
Legrand support. The metal flush boxes are shared across ranges. And the price test is the same: a plate or module far
below the MRP above is not the Legrand product. The <a href="../legrand-switches-best-price.html">Legrand switches best
price page</a> explains how to send a list for the lowest quote, and <a href="how-to-identify-duplicate-legrand-switches.html">how to
identify duplicate Legrand switches</a> covers the checks.</p>
""" + CTA,
 D,
 [("Which Legrand switch range is the cheapest?", "Britzy and Allzy, both at ₹56 MRP for a 6A one-way switch. Allzy adds coloured plates and a BLDC regulator; Britzy is white only."),
  ("Is Legrand Lyncus better than Myrius?", "Myrius is the premium range with more plate finishes, glass, the antibacterial series and automation modules. Lyncus offers the most modern modules at a mid price. Lyncus is better value; Myrius is better looking and more specified."),
  ("What is the difference between Legrand Allzy and Britzy?", "Same mechanism price on the 6A switch. Allzy adds a 10A switch line, a BLDC fan regulator and plates in rose gold, gold, matt black and aluminium champagne; Britzy is white only."),
  ("Can I mix Legrand ranges in one house?", "Yes, and most homes do: Lyncus or Allzy through the house and Myrius plates in the living room. Boxes are shared; plates and mechanisms must match within a board."),
  ("Which Legrand range do architects specify?", "Myrius for premium residences and Arteor or Arteor Advance for luxury and hospitality projects. Lyncus is increasingly specified for mid-range apartments."),
  ("Where can I see Legrand switch samples in Bangalore?", f"At Mount Cable India's showrooms at Jayanagar and Chickpete, where all four ranges and the plate finishes are on display. WhatsApp {PH} for a quote on any combination.")],
 ("woman-homeowner-choosing-modular-switches.jpg", "Homeowner comparing Legrand Myrius, Lyncus, Allzy and Britzy switch plates"),
 None),

("legrand-vs-schneider-mcb-and-switches",
 "Legrand vs Schneider: MCBs, RCCBs and Switches Compared for Indian Homes",
 "The two European switchgear brands at the top of the Indian market compared on ranges, MRP from the Legrand MPL 2026, availability in Bangalore and where each one is the better choice.",
 "Comparison",
 """<p><strong>Legrand and Schneider Electric are equals on protection: both make 10 kA ISI-marked MCBs and IS 12640 RCCBs
that do the same job to the same standard, and both are priced at the top of the Indian market. The choice comes down to
availability of the exact item, the look of the switch range, and which brand the consultant or electrician knows. In
Bangalore, Legrand's DX3 and Lyncus are stocked more deeply, which is often the deciding factor.</strong></p>

<h2>Switchgear</h2>
<p>Legrand's DX3 range covers AC MCBs from 0.5 to 63 A in C and D curve, breakers to 125 A, DC MCBs, AC, Type S and HPI
RCCBs, assembled and compact RCBOs, isolators and changeovers, with Ekinox3 distribution boards from 4-way SPN to
vertical TPN. Schneider's residential range covers the same ground with its own MCB, RCCB and RCBO lines and its own
distribution boards. On breaking capacity, standards and terminal design the two are alike; the differences are in
accessories such as auxiliaries and add-on modules, and in which ratings sit on a dealer's shelf.</p>
<p>Legrand MRP from the Corp MPL 2026 for reference:</p>
""" + MCB_TABLE + MRP_LINE + """
<p>Schneider does not publish a list we hold, so we will not print figures for it; in our trade its MCB and RCCB
prices land close to Legrand's for the same rating and pole, sometimes a little above, sometimes below. The
<a href="switchgear-brands-comparison-india.html">switchgear brands comparison</a> covers the wider field including
Anchor, HPL and Havells.</p>

<h2>Switches</h2>
<p>Legrand runs four residential ranges, Britzy, Allzy, Lyncus and Myrius, plus Arteor for premium and hospitality
work. Schneider's Indian residential ranges include Livia and Zencelo. Both brands price mechanism, plate and box
separately. Legrand's strength is the depth of plate finishes and module options in Lyncus and Myrius; Schneider's is
the design of Zencelo, which many architects specify for its flat rocker. Legrand's 10-year replacement policy on Myrius
and Britzy switches and sockets is written into its MPL.</p>

<h2>Availability in Bangalore</h2>
<p>This is where the brands separate in practice. Legrand DX3 in every pole and rating, DX3 RCCBs, Ekinox boards and
the Lyncus and Myrius plates in every module count are stocked by Mount Cable India at Jayanagar and Chickpete. Schneider
is stocked too, but the range on the shelf is narrower and more items are ordered against requirement. For a DB that
must be finished this week, Legrand is usually the faster answer.</p>

<h2>Where each is the better choice</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Situation</th><th>Pick</th></tr></thead>
<tbody>
<tr><td>Consultant's specification names one brand</td><td>That brand, by cat number</td></tr>
<tr><td>DB needed quickly with unusual poles or ratings</td><td>Legrand, for depth of stock</td></tr>
<tr><td>Architect wants the Zencelo look</td><td>Schneider</td></tr>
<tr><td>Wide plate palette and USB-C, BLDC modules</td><td>Legrand Lyncus or Myrius</td></tr>
<tr><td>Home with a solar inverter (nuisance tripping)</td><td>Either, in the HPI or equivalent RCCB type</td></tr>
<tr><td>Budget build</td><td>Neither; see Anchor UNO</td></tr>
</tbody></table></div>

<p>Both brands are copied, and both are checked the same way: cat number against pack and invoice, laser label,
design features, ISI mark and the price test. For Legrand the checks are on <a href="../original-legrand-mcb.html">Legrand
MCB 100% original</a>; for Schneider, <a href="how-to-identify-duplicate-schneider-switches.html">how to identify
duplicate Schneider switches</a>. Prices for the budget alternative are on the
<a href="../price-lists/anchor-mcb-price-list.html">Anchor MCB price list</a>.</p>
""" + CTA,
 D,
 [("Which is better, Legrand or Schneider MCB?", "Both are 10 kA ISI-marked MCBs to the same standard and protect a circuit equally when correctly sized. Legrand is stocked more deeply in Bangalore; Schneider is chosen when specified or for its switch designs. Price is close."),
  ("Is Schneider cheaper than Legrand?", "Not materially. Both are priced at the top of the Indian market and dealer prices for the same rating and pole land close together. A Legrand DX3 6 to 32 A single pole is ₹494 MRP."),
  ("Which has better switches, Legrand or Schneider?", "Legrand offers more ranges and plate finishes (Britzy, Allzy, Lyncus, Myrius, Arteor); Schneider's Zencelo is specified for its flat design. Both price plates separately from mechanisms."),
  ("Can I use Schneider MCBs in a Legrand DB?", "Both fit standard 35 mm DIN rail and 17.5 mm module pitch, so mechanically yes. Mixing brands in one board is usually avoided for busbar comb compatibility and warranty; keep the DB in one brand."),
  ("Which brand do consultants specify in Bangalore?", "Both appear in specifications for premium projects. Where a brand is named, buy that brand by cat number; substitution is the commonest route for copies to enter a project."),
  ("Do you stock both Legrand and Schneider?", f"Yes. Legrand in full depth and Schneider's main ranges, at Jayanagar and Chickpete. WhatsApp {PH} for a quote in either or both.")],
 ("electrician-installing-mcb-distribution-board.jpg", "Electrician comparing Legrand and Schneider MCBs while wiring a distribution board"),
 None),

("legrand-dx3-mcb-selection-guide-home",
 "Legrand DX3 MCB Selection Guide: Which Breaker for Each Circuit in a House",
 "How to pick the Legrand DX3 MCB, RCCB and isolator for every circuit in an Indian home: rating, pole, curve and sensitivity, with the MRP of each choice from the Legrand MPL 2026.",
 "Buying Guide",
 """<p><strong>A house needs one incomer (a DX3 double-pole isolator or SPN MCB), one 30 mA double-pole RCCB, and one
single-pole C-curve DX3 MCB per circuit: 6 A for lighting, 16 A for socket circuits, 20 A for a geyser or 1.5-ton AC,
25 A for a 2-ton AC, sized to the wire behind it. Every DX3 single pole from 6 to 32 A costs the same ₹494 MRP, so the
right rating never costs more than the wrong one.</strong></p>

<h2>Rating: match the wire, not the load</h2>
<p>An MCB protects the wire, so its rating must not exceed what the wire can carry: 1.5 sq mm takes a 10 A breaker at
most, 2.5 sq mm 16 to 20 A, 4 sq mm 25 A, 6 sq mm 32 A. Within that limit choose the rating that comfortably covers
the load. The <a href="../tools/mcb-selector.html">MCB selector</a> works it out from watts and wire size, and the
<a href="house-wiring-wire-size-guide.html">wire size guide</a> gives the wire behind each circuit.</p>

<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Circuit</th><th>Wire</th><th>DX3 MCB</th><th>Cat no. (C curve SP)</th><th>MRP</th></tr></thead>
<tbody>
<tr><td>Lighting and fans, per room group</td><td>1.5 sq mm</td><td>6 A or 10 A SP</td><td>4085 87 / 4085 90</td><td>₹494</td></tr>
<tr><td>6A socket circuits</td><td>1.5 or 2.5 sq mm</td><td>10 A SP</td><td>4085 90</td><td>₹494</td></tr>
<tr><td>16A socket circuits, kitchen</td><td>2.5 sq mm</td><td>16 A SP</td><td>4085 92</td><td>₹494</td></tr>
<tr><td>Geyser, 1.5-ton AC</td><td>4 sq mm</td><td>20 A SP</td><td>4085 93</td><td>₹494</td></tr>
<tr><td>2-ton AC</td><td>4 or 6 sq mm</td><td>25 A SP</td><td>4085 94</td><td>₹494</td></tr>
<tr><td>Water pump (single phase)</td><td>4 sq mm</td><td>16 or 20 A SP, D curve if it trips on start</td><td>4085 92 / 4087 16</td><td>₹494 / ₹678</td></tr>
<tr><td>Incomer, single phase</td><td>6 or 10 sq mm</td><td>40 A DP isolator, or 40 A SPN MCB</td><td>4065 01 / 4086 18</td><td>₹961 / ₹2,247</td></tr>
<tr><td>Earth leakage, whole board</td><td></td><td>40 A DP RCCB 30 mA</td><td>4118 52</td><td>₹6,360</td></tr>
</tbody></table></div>
""" + MRP_LINE + """

<h2>Poles</h2>
<p>Outgoing circuits in a single-phase home use single-pole MCBs; the neutral runs through the neutral bar. The incomer
is double pole so both live and neutral are broken, which is why a DP isolator or an SPN MCB sits at the head of the
board. Three-phase homes and buildings use TP or TPN MCBs and FP RCCBs, in an ETPN or vertical TPN Ekinox board.</p>

<h2>Curve</h2>
<p>C curve for everything in a house: lighting, sockets, ACs, geysers, ovens. D curve only where a motor's starting
current keeps tripping a C-curve breaker, typically a borewell pump or a lift. D curve costs more (₹678 against ₹494 for a
single pole) and gives less protection against small overloads, so it is not a default.</p>

<h2>RCCB sensitivity and type</h2>
<p>30 mA for shock protection, which is what a home needs; 100 mA and 300 mA are upstream fire-protection devices for
larger installations. AC type for a standard home. HPI type if the house runs a solar inverter, a large UPS or a lot of
electronics, because those cause nuisance trips on AC-type RCCBs; the HPI 40 A DP is ₹12,271 against ₹6,360 for the AC
type. Type S only where one RCCB must coordinate with another downstream. The <a href="mcb-rccb-rcbo-guide-for-homes.html">MCB,
RCCB and RCBO guide</a> has the reasoning.</p>

<h2>RCBO or RCCB plus MCBs</h2>
<p>An RCCB for the board plus an MCB per circuit is the standard and the cheapest. A DX3 RCBO (₹6,974 for 6 to 32 A DP at
30 mA) combines both in one device for one circuit, so a leak on that circuit trips only that circuit. It is worth it
for the geyser, an outdoor circuit or a home office, not for every circuit.</p>

<h2>Counting the board</h2>
<p>List the circuits, add two spare ways, and that is the Ekinox SPN size: 8 way for a 2BHK, 12 way for a 3BHK, 16 or
18 way for a large house. IP43 with a metal door is the normal indoor choice at ₹4,065 (8 way) and ₹4,884 (12 way).
The whole board costed at MRP is on <a href="../legrand-mcb-best-price.html">Legrand MCB best price</a>, and the
<a href="distribution-board-selection-guide-home.html">DB selection guide</a> covers the board itself.</p>
""" + CTA,
 D,
 [("Which Legrand MCB should I use for lighting?", "A 6 A or 10 A single-pole C-curve DX3 (cat 4085 87 or 4085 90) on 1.5 sq mm wire. Both are ₹494 MRP."),
  ("Which Legrand MCB for a 1.5-ton AC?", "A 20 A single-pole C-curve DX3 (4085 93) on 4 sq mm wire; a 2-ton AC takes 25 A (4085 94) on 4 or 6 sq mm. Both ₹494 MRP."),
  ("Which Legrand MCB for a geyser?", "A 20 A single-pole C-curve DX3 on 4 sq mm wire, or a 20 A RCBO if you want the geyser on its own earth-leakage protection."),
  ("Should I use C curve or D curve Legrand MCBs at home?", "C curve for everything in a house. D curve only for a motor such as a borewell pump that trips a C-curve breaker on starting."),
  ("What RCCB rating do I need for a house?", "A 40 A double-pole 30 mA RCCB (4118 52, ₹6,360 MRP) covers most single-phase homes; 63 A for a large house with a 63 A incomer. Use the HPI type if you run a solar inverter."),
  ("Does a higher-rated Legrand MCB cost more?", "Not from 6 to 32 A: every DX3 single pole in that band is ₹494 MRP. 40 to 63 A steps up to ₹1,180.")],
 ("electrician-installing-mcb-distribution-board.jpg", "Electrician selecting Legrand DX3 MCB ratings for each circuit of a new house"),
 None),

("why-legrand-switchgear-costs-more",
 "Why Legrand Switchgear Costs More, and When It Is Worth Paying",
 "What you actually get for the Legrand premium over Anchor or HPL on MCBs, RCCBs and DBs, where the difference matters in a home, and where a budget brand does the same job.",
 "Buying Guide",
 """<p><strong>A Legrand DX3 single-pole MCB is ₹494 MRP against ₹308 for an Anchor UNO of the same 10 kA rating. Both
trip on the same curves to the same standard. The premium buys terminal and mechanism design, accessories, a deeper
range and the brand's specification value. It is worth paying in a premium home, in any building that will be
inspected against a specification, and on the RCCB, which is the device that protects people. It is not worth paying
where the budget is tight and the board is a simple single-phase DB, where Anchor UNO protects the circuits just as
well.</strong></p>

<h2>Where the money goes</h2>
<ul>
<li><strong>Terminals and clamps.</strong> DX3 has biconnect lower terminals that take a cable and a busbar comb together,
IP20 shuttered terminals, and a sliding bottom clamp for removing one breaker from a live rail without disturbing its
neighbours. These make the board faster to wire and safer to service.</li>
<li><strong>Accessories.</strong> Auxiliary contacts, shunt trips, undervoltage releases and motorised controls clip
onto DX3 for remote monitoring and control. A budget range has none of this.</li>
<li><strong>Range depth.</strong> Ratings from 0.5 A, D curve, DC MCBs, HPI and Type S RCCBs, compact RCBOs, and boards
from a 4-way SPN to a 12-way vertical TPN with a 100 A busbar. When a specification asks for something unusual, Legrand
has it.</li>
<li><strong>Consistency and finish.</strong> The moulding, the laser labels and the fit in an Ekinox board are the
reason consultants specify it and the reason it is copied.</li>
</ul>

<h2>Where it does not matter</h2>
<p>Breaking capacity, curve and standard are the same on a 10 kA ISI-marked MCB from any serious brand. A correctly
sized Anchor UNO MCB clears a short circuit in a house the same way a DX3 does. If the board is a straightforward
single-phase DB with an RCCB and ten single poles, and nobody is going to inspect it against a specification, the ₹186
per breaker saved across ten breakers and the ₹2,800 saved on the RCCB are real money that can go into better wire or a
better MCB board enclosure.</p>

<h2>The comparison in numbers</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Item</th><th>Legrand DX3 / Ekinox MRP</th><th>Anchor UNO MRP</th></tr></thead>
<tbody>
<tr><td>SP MCB 6 to 32 A, 10 kA</td><td>₹494</td><td>₹308</td></tr>
<tr><td>DP MCB 6 to 32 A</td><td>₹1,693</td><td>₹1,084</td></tr>
<tr><td>DP RCCB 40 A 30 mA</td><td>₹6,360</td><td>₹3,568</td></tr>
<tr><td>DP isolator 40 A</td><td>₹961</td><td>₹630</td></tr>
<tr><td>SPN 12-way DB, metal double door</td><td>₹4,884 (IP43)</td><td>₹3,069</td></tr>
<tr><td>3BHK board (isolator, RCCB, 10 SP, 12-way DB)</td><td>₹17,145</td><td>₹10,278</td></tr>
</tbody></table></div>
<p class="ptable-note">MRP from the Legrand Corp MPL 2026 and the Anchor Panasonic pricelist April 2026. Mount Cable India sells Legrand at 65% off MRP, so the DX3 single pole is ₹173 net and the 3BHK board about ₹6,000; Anchor is also sold below MRP, so compare net quotes rather than MRPs.</p>

<h2>When to pay for Legrand</h2>
<ul>
<li>A premium apartment or villa, where the board will be seen and the brand will be asked about at resale.</li>
<li>Any project with a consultant's specification: substitution is where copies enter, and matching the cat numbers is
the cheapest insurance.</li>
<li>The RCCB, always. It is the device that protects people rather than wire, and the HPI option matters in homes with
inverters.</li>
<li>Three-phase and commercial boards, where the DX3 accessories and Ekinox TPN range earn their cost.</li>
</ul>

<h2>When a budget brand does the job</h2>
<ul>
<li>A rental flat, a small independent house, a shop or a farmhouse with a simple single-phase board.</li>
<li>A tight budget where the wire is being compromised to afford the switchgear; genuine wire in the wall matters
more than the badge on the board.</li>
</ul>
<p>Whichever you choose, buy it original. Legrand MCBs are copied precisely because of the premium; the checks are on
<a href="../original-legrand-mcb.html">Legrand MCB 100% original</a>, and the budget alternative's figures are on the
<a href="../price-lists/anchor-mcb-price-list.html">Anchor MCB price list</a>. Both are stocked at Mount Cable India, Legrand at 65% off MRP; see the <a href="../legrand-dealer-bangalore.html">Legrand dealer page</a>.</p>
""" + CTA,
 D,
 [("Why is Legrand MCB so expensive?", "Because of terminal and mechanism design, clip-on accessories, range depth and the brand's specification value. A DX3 single pole is ₹494 MRP against ₹308 for an Anchor UNO of the same 10 kA rating."),
  ("Is Legrand MCB better than Anchor?", "On breaking capacity, curve and standard they are equal: both are 10 kA ISI-marked breakers. Legrand adds better terminals, accessories and range depth, which matter in premium and specified work."),
  ("Is it worth buying a Legrand RCCB?", "Yes, more than any other item on the board: the RCCB protects people, and Legrand's AC, HPI and Type S options cover situations, such as solar inverters, that a budget range does not."),
  ("How much more does a Legrand DB cost than Anchor?", "About ₹17,145 against ₹10,278 at MRP for a 3BHK board with isolator, RCCB, ten single poles and a 12-way DB. Dealer prices are below both."),
  ("Can I use Legrand for the RCCB and Anchor for the MCBs?", "Mechanically yes, on the same DIN rail. Most electricians keep a board in one brand for busbar comb fit and a single warranty, but a Legrand RCCB with budget MCBs is a reasonable compromise on a tight budget."),
  ("Where can I buy Legrand and Anchor switchgear in Bangalore?", f"Mount Cable India, Jayanagar and Chickpete, stocks both ranges in full and quotes both below MRP. WhatsApp {PH} with the DB schedule.")],
 ("electrical-shop-counter-happy-customer.jpg", "Customer discussing Legrand and Anchor switchgear options at Mount Cable India's counter"),
 None),
]

LEGRAND_CLUSTER = [p[0] for p in LEGRAND_BLOG] + [
    "how-to-identify-duplicate-legrand-mcb",
    "how-to-identify-duplicate-legrand-switches",
    "switchgear-brands-comparison-india",
    "best-modular-switch-brands-india-2026",
    "mcb-rccb-rcbo-guide-for-homes",
    "distribution-board-selection-guide-home",
    "modular-switch-buying-guide-bangalore",
    "which-switch-brand-should-you-buy",
]

LEGRAND_PAGE_LINKS = [
    ("legrand-dealer-bangalore.html", "Legrand dealer in Bangalore"),
    ("original-legrand-mcb.html", "Legrand MCB 100% original"),
    ("legrand-mcb-best-price.html", "Best price on Legrand MCBs and DBs"),
    ("legrand-switches-best-price.html", "Best price on Legrand switches"),
    ("legrand-best-price-bangalore.html", "Best prices on Legrand products"),
    ("legrand-products-bangalore.html", "All Legrand products available"),
    ("price-lists/legrand-price-list.html", "Legrand price list 2026"),
    ("price-lists/legrand-mcb-price-list.html", "Legrand MCB price list"),
    ("price-lists/legrand-switchgear-price-list.html", "Legrand switchgear price list"),
    ("price-lists/legrand-switches-price-list.html", "Legrand switches price list"),
    ("brands/legrand.html", "Legrand brand page"),
    ("knowledge/legrand-guide.html", "Legrand brand guide"),
]
