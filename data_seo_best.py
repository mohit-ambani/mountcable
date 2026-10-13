# -*- coding: utf-8 -*-
""""Which is best" cluster (Oct 2026, owner brief): question-intent landing pages
for which switch / wire / brand is best, safest and best quality.

Owner positioning: Legrand for switches (and MCBs), Finolex for wires.

Discipline (same as data_blog_vs / data_blog_compare):
  - The recommendation is ours and is argued with reasons, never presented as
    an independent ranking or a test result.
  - Other brands are described fairly: the major wire brands all make IS 694
    copper wire; the major switch brands all make ISI switches. Never assert a
    named brand is unsafe, fake or inferior in a way we cannot show.
  - Product facts used are the ones already verified elsewhere on the site:
    Finolex grades (FR, Flamegard FR-LSH, Finoultra e-beam HFFR to IS 17048),
    the two-QR carton check, Legrand DX3 10 kA ISI breakers, the 10-year
    manufacturing-defect replacement on Myrius / Britzy switches and sockets.
  - Prices render from the price data so they never drift: Finolex net only,
    Legrand MRP struck through with the 65% net (with_net).
"""
from data_finolex_mrp import HOUSE_WIRE, offer, EFFECTIVE_FROM
from data_brand_prices import rs, lnet, with_net, LEGRAND_SWITCH_CMP, LEGRAND_MCB_C, LEGRAND_RCCB_AC

W = "https://wa.me/918867676700"
PH = "88676 76700"


def _hw(size, key):
    return rs(offer(HOUSE_WIRE[size][key], key))


def _tbl(cols, rows, net=False):
    head = "".join(f"<th>{c}</th>" for c in cols)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    t = f'<div class="ptable-wrap"><table class="ptable"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
    return with_net(t) if net else t


CTA = (f'<p class="muted"><strong>Not sure yet?</strong> WhatsApp your electrician\'s list or a photo of the memo to '
       f'<a href="{W}">{PH}</a>. Mount Cable India replies within 60 minutes with the right grade and brand for each '
       'point and an itemised price. No obligation to buy from us.</p>')

MRP_LINE = ('<p class="ptable-note">Struck-through figures are Legrand MRP per unit inclusive of GST (Corp MPL 2026). '
            'Bold figures are Mount Cable India\'s price at 65% off MRP.</p>')
FIN_LINE = (f'<p class="ptable-note">Mount Cable India selling prices per 90 m coil, current to the Finolex list '
            f'effective {EFFECTIVE_FROM}. Taxes extra as applicable.</p>')

# Finolex grade ladder, 90 m coils.
FINOLEX_GRADES = _tbl(
    ["Finolex grade", "What it adds", "1.5 sq mm", "2.5 sq mm", "Best for"],
    [("Silver Pack FR", "Flame retardant (IS 694)", _hw("1.5", "silver"), _hw("2.5", "silver"), "Standard house wiring on a budget"),
     ("Gold Pack FR", "Premium FR pack", _hw("1.5", "gold"), _hw("2.5", "gold"), "Independent houses, the electrician's usual pick"),
     ("Flamegard FR-LSH", "Low smoke, low halogen in a fire", _hw("1.5", "frls90"), _hw("2.5", "frls90"), "Flats, bedrooms, kids' rooms, stairwells"),
     ("Finoultra (HFFR)", "E-beam, halogen-free, higher heat resistance", _hw("1.5", "ultra"), _hw("2.5", "ultra"), "Premium homes, AC and geyser runs")]) + FIN_LINE

LEGRAND_RANGES = _tbl(
    ["Legrand range", "Level", "6A switch", "6/16A socket", "Best for"],
    [("Britzy", "Value", rs(56), rs(294), "Rental flats, utility areas, budget builds"),
     ("Allzy", "Value, coloured plates", rs(56), rs(284), "Budget homes that want colour"),
     ("Lyncus", "Mid", rs(100), rs(434), "Most Bangalore homes"),
     ("Myrius", "Premium", rs(180), rs(684), "Villas, premium apartments")], net=True) + MRP_LINE

SIZE_GUIDE = _tbl(
    ["Circuit", "Wire size", "Finolex 90 m coil (Flamegard FR-LSH)"],
    [("Lighting and fans", "1.5 sq mm", _hw("1.5", "frls90")),
     ("6A sockets", "1.5 or 2.5 sq mm", _hw("2.5", "frls90") + " (2.5)"),
     ("16A sockets, kitchen", "2.5 sq mm", _hw("2.5", "frls90")),
     ("Geyser, 1.5-ton AC", "4.0 sq mm", _hw("4.0", "frls90")),
     ("2-ton AC, main feed", "6.0 sq mm", _hw("6.0", "frls90"))]) + FIN_LINE

MCB_ROW = _tbl(["Legrand DX3", "MRP", "Mount Cable price"],
               [("SP MCB 6 to 32 A, C curve", rs(494), rs(lnet(494))),
                ("DP RCCB 40 A 30 mA", rs(6360), rs(lnet(6360)))])

TWO_QR = ("<p>Finolex cartons carry <strong>two QR codes</strong>: an outer code on the carton label and an inner code you reach only after opening. "
          "The outer one proves the carton is registered with Finolex; the inner one proves the contents are what Finolex packed. "
          "Scan both, at your site, before you pay. Our <a href=\"finolex-wire-scanner.html\">Finolex wire scanner</a> does it in the browser.</p>")


def _page(slug, title, desc, h1, badge, intro, answer, hero, sections, faqs):
    return {"slug": slug, "cluster": "best", "title": title, "desc": desc, "h1": h1, "badge": badge,
            "intro": intro, "answer": answer, "hero": hero, "sections": sections + [("Talk to us before you buy", CTA)],
            "faqs": faqs}


BEST_SEO_PAGES = [

_page("best-switch-brand-in-india",
  "Which Switch Brand Is Best in India? Our Answer: Legrand (2026) | Mount Cable India",
  "Which modular switch brand is best in India for a home? Our recommendation is Legrand, and why: mechanism quality, ISI shuttered sockets, a 10-year replacement on switches, four ranges from budget to premium, and 65% off MRP in Bangalore.",
  "Which switch brand is best in India?",
  "Recommendation · Legrand for switches",
  "Every switchboard in your house will be pressed thousands of times a year for twenty years or more. That makes the switch brand one of the few electrical choices you notice every day. After 35 years of supplying Bangalore homes, our answer is Legrand.",
  "Legrand is the best switch brand for most Indian homes. It combines a reliable mechanism, ISI-marked shuttered sockets, a 10-year manufacturing-defect replacement on Myrius and Britzy switches and sockets, and four ranges from budget Britzy to premium Myrius, so every room can be Legrand. At Mount Cable India it is sold at 65% off MRP.",
  ("woman-homeowner-choosing-modular-switches.jpg", "Homeowner choosing Legrand modular switches for her new house in Bangalore"),
  [("Why Legrand",
    "<ul><li><strong>The mechanism.</strong> Legrand is a global specialist in electrical wiring devices. The switch action is crisp and consistent, and it stays that way, which is what you feel every day.</li>"
    "<li><strong>Safety where it matters.</strong> Shuttered sockets keep children's fingers and stray objects out, and the sockets are ISI marked.</li>"
    "<li><strong>A written replacement policy.</strong> Legrand states a 10-year manufacturing-defect replacement on Myrius and Britzy switches and power sockets, bought through its chain with an invoice.</li>"
    "<li><strong>One brand for every budget.</strong> Britzy and Allzy cost about what local brands do, Lyncus suits most homes, Myrius is premium. You never have to mix brands to stay on budget.</li>"
    "<li><strong>Switches and MCBs from one maker.</strong> Legrand DX3 breakers and Ekinox boards sit behind the same switches.</li></ul>"),
   ("Legrand's four ranges, priced",
    "<p>Prices for the two parts every board has, from the Legrand Corp MPL 2026:</p>" + LEGRAND_RANGES
    + "<p>Full lists: <a href=\"price-lists/legrand-britzy-price-list.html\">Britzy</a>, <a href=\"price-lists/legrand-allzy-price-list.html\">Allzy</a>, <a href=\"price-lists/legrand-lyncus-price-list.html\">Lyncus</a>, <a href=\"price-lists/legrand-myrius-price-list.html\">Myrius</a>.</p>"),
   ("What about the other brands?",
    "<p>Anchor by Panasonic, GM, Hi-Fi and others make good ISI-marked switches, and we stock several of them. Anchor is a sensible value choice and GM is known for colours and finishes. Our recommendation for a house you will live in for decades is still Legrand, because at 65% off MRP its entry ranges cost about the same as the alternatives, and its premium ranges are a real step up.</p>"),
  ],
  [("Which switch brand is best for home in India?", "We recommend Legrand. It offers a reliable mechanism, ISI shuttered sockets, a 10-year manufacturing-defect replacement on Myrius and Britzy switches and sockets, and four ranges from budget to premium."),
   ("Is Legrand better than Anchor?", "Both are reputable. Anchor is a good value brand. Legrand has the better mechanism and premium ranges, and at 65% off MRP its Britzy and Allzy ranges cost about the same as Anchor at a shop, which is why we recommend Legrand."),
   ("Which Legrand range should I buy?", "Lyncus for most homes, Myrius for a premium interior, Britzy or Allzy for budget builds, rental flats and utility areas."),
   ("Are Legrand switches expensive?", "At MRP they look expensive. Mount Cable India sells every Legrand product at 65% off MRP, so a Britzy 6A switch is ₹20 and a Lyncus 6A switch ₹35.")]),

_page("best-wire-brand-in-india",
  "Which Wire Brand Is Best in India? Our Answer: Finolex (2026) | Mount Cable India",
  "Which electrical wire brand is best for house wiring in India? Our recommendation is Finolex, and why: IS 694 copper, FR-LSH and halogen-free grades, a two-QR check on every carton, and net prices from one of India's largest Finolex distributors.",
  "Which wire brand is best in India?",
  "Recommendation · Finolex for wires",
  "Wire goes inside the walls and is never seen again. You cannot replace it without breaking plaster, so the brand you choose has to be right the first time. After 35 years of wiring Bangalore homes, our answer is Finolex.",
  "Finolex is the best wire brand for most Indian homes. Its house wire is IS 694 copper in FR, low-smoke FR-LSH (Flamegard) and halogen-free (Finoultra) grades, every carton carries two QR codes you can scan at site before paying, and it is the wire most Bangalore electricians ask for by name.",
  ("electrician-scanning-qr-code-wire-coil.jpg", "Electrician scanning the QR code on a Finolex wire coil at a Bangalore house site"),
  [("Why Finolex",
    "<ul><li><strong>Copper and insulation to standard.</strong> Finolex house wire is IS 694 flame-retardant copper wire, with a full grade ladder up to halogen-free.</li>"
    "<li><strong>You can verify it.</strong> Wire is the most counterfeited electrical product in India. Finolex's two-code carton check lets you prove the coil is genuine at your own site.</li>"
    "<li><strong>A grade for every room.</strong> Silver and Gold FR for standard circuits, Flamegard FR-LSH where smoke matters, Finoultra where you want the best.</li>"
    "<li><strong>Electricians trust it.</strong> It is the most specified house wire in Bangalore, so your electrician knows how it handles and strips.</li></ul>"),
   ("The Finolex grades, priced", FINOLEX_GRADES
    + "<p>Every range and coil length: <a href=\"price-lists/finolex-price-list.html\">Finolex price list</a>, <a href=\"price-lists/finolex-frls-wire-price-list.html\">FRLS</a>, <a href=\"price-lists/finolex-ultra-wire-price-list.html\">Finoultra</a>, <a href=\"price-lists/finolex-silver-wire-price-list.html\">Silver</a>.</p>"),
   ("How to make sure it is real Finolex", TWO_QR),
   ("What about Polycab, KEI and RR Kabel?",
    "<p>They are large, reputable makers of IS 694 copper wire, and Polycab is a brand we stock. Correctly sized, any of them will outlast the house. We recommend Finolex because it is the easiest to verify, the easiest to buy genuine in Bangalore, and its FR-LSH grade gives low-smoke safety at a small premium. The <a href=\"blog/finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html\">four-brand comparison</a> goes size by size.</p>"),
  ],
  [("Which wire brand is best for house wiring in India?", "We recommend Finolex: IS 694 copper wire in FR, FR-LSH and halogen-free grades, with a two-QR check on every carton so you can prove it is genuine at site."),
   ("Is Finolex better than Polycab?", "Both make good IS 694 copper wire and list prices are close. We recommend Finolex for house wiring because it is easier to verify at site and its Flamegard FR-LSH grade is a small step up in price for low-smoke safety."),
   ("Which Finolex wire is best for a house?", "Flamegard FR-LSH for most homes, especially flats and bedrooms. Silver or Gold FR on a tighter budget. Finoultra for premium homes and heavy AC and geyser runs."),
   ("What is the Finolex 1.5 sq mm price?", f"A 90 m coil is {_hw('1.5','silver')} in Silver Pack, {_hw('1.5','gold')} in Gold and {_hw('1.5','frls90')} in Flamegard FR-LSH at Mount Cable India, taxes extra.")]),

_page("which-electrical-brand-to-buy",
  "Which Electrical Brand to Buy for a New House? Finolex Wires, Legrand Switches | Mount Cable India",
  "Building a house and not sure which electrical brands to buy? Our straight answer: Finolex for wires and Legrand for switches, MCBs and distribution boards, with the grade and range for each room and real prices.",
  "Which electrical brand should you buy for your house?",
  "Our answer · Finolex wires + Legrand switches",
  "A new house needs wires, switches, MCBs, a distribution board and lighting, and a shop will happily sell you five brands. Our advice to every house builder who walks into our showroom is simpler.",
  "Buy Finolex for every wire in the house and Legrand for switches, sockets, MCBs, RCCBs and the distribution board. Finolex is the wire you can verify coil by coil; Legrand gives you one maker behind every switch and breaker, from budget Britzy to premium Myrius, at 65% off MRP.",
  ("happy-homeowner-couple-new-house-wiring.jpg", "Homeowner couple planning electrical brands for their new house in Bangalore"),
  [("The short list",
    _tbl(["What", "Brand", "Grade or range", "Why"],
         [("House wire", "Finolex", "Flamegard FR-LSH (or Silver / Gold FR on a budget)", "Verifiable, low smoke in a fire"),
          ("Switches and sockets", "Legrand", "Lyncus for most rooms, Myrius where it shows", "Mechanism, shuttered sockets, 10-year replacement"),
          ("MCBs and RCCB", "Legrand", "DX3, 30 mA RCCB on the incomer", "10 kA ISI breakers"),
          ("Distribution board", "Legrand", "Ekinox SPN, IP43", "Built for the DX3 breakers"),
          ("LAN and TV cable", "Finolex", "Cat 6 UTP, RG 6", "Same verifiable brand")])),
   ("Why one wire brand and one switch brand",
    "<p>Mixing brands is how duplicates get in. When the whole order is two brands from one distributor, every carton can be checked and every warranty claim has one place to go. It also makes price comparison honest: you are comparing like with like.</p>"),
   ("What it costs",
    "<p>Wire, the biggest line, priced by grade:</p>" + FINOLEX_GRADES
    + "<p>Switches, by Legrand range:</p>" + LEGRAND_RANGES
    + "<p>For a full estimate use the <a href=\"tools/house-wiring-cost-calculator.html\">house wiring cost calculator</a> or send us the list.</p>"),
  ],
  [("Which brand is best for electrical items for a house?", "Finolex for wires and Legrand for switches, sockets, MCBs, RCCBs and the distribution board. That is what we recommend to every house builder."),
   ("Should I use the same brand for wires and switches?", "No single maker leads in both. Finolex is the wire specialist and Legrand the switch and switchgear specialist; using one of each keeps the order simple and verifiable."),
   ("Which MCB brand is best for a house?", "Legrand DX3. They are 10 kA ISI-marked breakers, and Mount Cable India sells them at 65% off MRP.")]),

_page("safest-electrical-brand",
  "Which Is the Safest Electrical Brand for Your Home? Finolex and Legrand | Mount Cable India",
  "Which electrical brand is safest for a home? What actually makes wiring safe, and why we recommend Finolex FR-LSH wire with Legrand switches, shuttered sockets, DX3 MCBs and a 30 mA RCCB.",
  "Which is the safest electrical brand for your home?",
  "Safety · Finolex wire + Legrand protection",
  "Electrical safety is not one product. It is the wire that does not spread fire or smoke, the breaker that trips before the wire overheats, the RCCB that trips before a shock hurts someone, and the socket that keeps little fingers out. Here is how we build a safe house, and the brands we use.",
  "For safety we recommend Finolex Flamegard FR-LSH or Finoultra wire, which limit flame spread and give off far less smoke in a fire, with Legrand protection: DX3 MCBs sized to the wire, a 30 mA Legrand RCCB on the incomer, and Legrand shuttered sockets. Above all, buy genuine: a counterfeit of any brand is the least safe product in the house.",
  ("electrician-installing-mcb-distribution-board.jpg", "Electrician installing Legrand MCBs and RCCB in a home distribution board"),
  [("The four layers of a safe installation",
    "<ol><li><strong>Wire that resists fire and smoke:</strong> Finolex Flamegard FR-LSH or Finoultra.</li>"
    "<li><strong>Breakers that protect the wire:</strong> Legrand DX3 MCBs, each sized to the wire on its circuit.</li>"
    "<li><strong>Protection for people:</strong> a 30 mA Legrand RCCB, which trips on earth leakage in milliseconds.</li>"
    "<li><strong>Safe points:</strong> Legrand shuttered sockets and a proper earth pit.</li></ol>"),
   ("Genuine is the biggest safety factor",
    "<p>A duplicate wire has less copper than the label says, so it runs hot on a load it should carry. A duplicate MCB may not trip at all. That is why we tell buyers to verify every Finolex coil with both QR codes and to buy Legrand from a stockist at a sensible price.</p>" + TWO_QR),
   ("What safe protection costs", MCB_ROW
    + "<p>A full 3BHK DB with an isolator, a 30 mA RCCB and ten MCBs is costed on <a href=\"legrand-mcb-best-price.html\">best price on Legrand MCBs</a>.</p>"),
  ],
  [("Which electrical brand is safest?", "No brand is safe if it is counterfeit or wrongly sized. We recommend Finolex FR-LSH wire and Legrand MCBs, RCCB and shuttered sockets, bought genuine and installed to the right sizes."),
   ("Is an RCCB necessary in a house?", "Yes. A 30 mA RCCB is the device that protects people from electric shock. MCBs protect the wire, not the person."),
   ("Which wire is safest for a house?", "Finolex Flamegard FR-LSH, or Finoultra for halogen-free. Both resist flame spread and give off much less smoke than standard FR wire.")]),

_page("safest-wire-for-house",
  "Which Wire Is Safest for House Wiring? FR vs FRLS vs Halogen-Free | Mount Cable India",
  "Which electrical wire is the safest for a house? FR, FR-LSH (FRLS) and halogen-free (HFFR) explained, why we recommend Finolex Flamegard or Finoultra, the right size per circuit, and current prices.",
  "Which wire is the safest for house wiring?",
  "Safety · Finolex Flamegard and Finoultra",
  "In a house fire, most injuries come from smoke, not flame. That single fact decides which wire is safest.",
  "The safest house wire is a low-smoke grade: Finolex Flamegard FR-LSH, or Finolex Finoultra, which is halogen-free with e-beam insulation. Both stop flame running along the cable and give off much less smoke and fewer toxic gases than standard FR wire. Size it correctly for each circuit and verify it is genuine.",
  ("electrician-hands-stripping-wire-closeup.jpg", "Electrician stripping Finolex FR-LSH house wire for a safe installation"),
  [("FR, FR-LSH and halogen-free, plainly",
    "<ul><li><strong>FR (flame retardant):</strong> the wire will not carry a flame along its length. The standard for house wire.</li>"
    "<li><strong>FR-LSH (often FRLS):</strong> FR plus low smoke and low halogen gas when it burns. Finolex calls it Flamegard.</li>"
    "<li><strong>HFFR (halogen-free):</strong> no halogen in the insulation at all. Finolex Finoultra uses e-beam cross-linked insulation, which also handles heat better.</li></ul>"
    + FINOLEX_GRADES),
   ("The right size is part of safety",
    "<p>A wire that is too thin for its load runs hot for years. These are the sizes we supply for each circuit:</p>" + SIZE_GUIDE
    + "<p>Check any circuit with the <a href=\"tools/wire-size-calculator.html\">wire size calculator</a>.</p>"),
   ("A counterfeit is never safe", TWO_QR),
  ],
  [("Which wire is safest for home?", "A low-smoke grade: Finolex Flamegard FR-LSH, or Finolex Finoultra, which is halogen-free. Both resist flame spread and give off far less smoke than standard FR wire."),
   ("Is FRLS wire safer than FR?", "Yes. Both resist flame spread, but FRLS (FR-LSH) also gives off much less smoke and fewer halogen gases, which is what harms people in a fire."),
   ("Is Finolex wire safe?", "Yes, genuine Finolex is IS 694 copper wire with FR, FR-LSH and halogen-free grades. Verify both QR codes on the carton to be sure the coil is genuine."),
   ("What is the safest wire for AC and geyser?", "4.0 sq mm Finolex Flamegard FR-LSH or Finoultra for geysers and 1.5-ton ACs, 6.0 sq mm for 2-ton ACs, each on its own MCB.")]),

_page("best-quality-switches",
  "Which Switches Are the Best Quality? Legrand Modular Switches | Mount Cable India",
  "Which modular switches have the best quality? What quality means in a switch (mechanism, contacts, plate, socket shutters) and why we recommend Legrand Myrius and Lyncus, with prices at 65% off MRP.",
  "Which switches are the best quality?",
  "Quality · Legrand Myrius and Lyncus",
  "Two switches can look identical in a showroom. Quality shows after five years: whether the rocker still clicks cleanly, whether the plate has yellowed, whether the socket still grips a plug.",
  "For the best quality switches we recommend Legrand, and within Legrand the Myrius and Lyncus ranges. The mechanism stays crisp, sockets are ISI marked with shutters, the plates keep their finish, and Legrand states a 10-year manufacturing-defect replacement on Myrius and Britzy switches and sockets.",
  ("homeowner-electrician-discussing-switchboard.jpg", "Homeowner and electrician comparing Legrand Myrius and Lyncus switch quality"),
  [("What quality means in a switch",
    "<ul><li><strong>The mechanism:</strong> a consistent, positive click that does not soften with use.</li>"
    "<li><strong>The contacts:</strong> rated for the load, so a 16A socket does not heat up under a geyser or AC.</li>"
    "<li><strong>The socket:</strong> ISI marked, shuttered, and gripping the plug firmly.</li>"
    "<li><strong>The plate:</strong> a finish that does not yellow, scratch or loosen.</li>"
    "<li><strong>The warranty:</strong> a written replacement promise from the maker.</li></ul>"),
   ("Legrand ranges by quality and price", LEGRAND_RANGES
    + "<p>Myrius is the top of the line; Lyncus is our pick for most homes. Compare them on the <a href=\"price-lists/legrand-switches-price-list.html\">Legrand switches price list</a> and <a href=\"blog/legrand-myrius-vs-lyncus-vs-allzy-vs-britzy.html\">Myrius vs Lyncus vs Allzy vs Britzy</a>.</p>"),
   ("Check before you pay",
    "<p>Copies of premium switches are common. Buy from a stockist, keep the invoice, and see <a href=\"blog/how-to-identify-duplicate-legrand-switches.html\">how to identify duplicate Legrand switches</a>.</p>"),
  ],
  [("Which switch is best quality in India?", "We recommend Legrand, especially Myrius and Lyncus, for the mechanism, ISI shuttered sockets, plate finish and the 10-year replacement on Myrius and Britzy switches and sockets."),
   ("Is Legrand Myrius good quality?", "Yes. Myrius is Legrand's premium range, specified in high-end apartments and villas, with glass and metallic plate options."),
   ("Is Lyncus or Myrius better?", "Myrius is the premium range with more finishes; Lyncus is the mid range most homes choose. Both use Legrand mechanisms.")]),

_page("best-mcb-brand",
  "Which MCB Brand Is Best for a House? Legrand DX3 | Mount Cable India",
  "Which MCB brand is best for home? Why we recommend Legrand DX3 MCBs and RCCBs: 10 kA ISI breakers, C and D curves, matching Ekinox boards, and 65% off MRP in Bangalore.",
  "Which MCB brand is best for a house?",
  "Recommendation · Legrand DX3",
  "An MCB has one job: trip before the wire overheats. You only find out whether it does that on the day it matters, so the brand has to be one you trust without testing.",
  "We recommend Legrand DX3 MCBs with a 30 mA Legrand RCCB. DX3 breakers are 10 kA ISI-marked MCBs in C and D curves, they fit Legrand's Ekinox distribution boards, and at Mount Cable India they cost 65% off MRP.",
  ("electrician-installing-mcb-distribution-board.jpg", "Electrician fitting Legrand DX3 MCBs in an Ekinox distribution board"),
  [("Why Legrand DX3",
    "<ul><li><strong>10 kA breaking capacity</strong>, ISI marked to IS/IEC 60898-1.</li>"
    "<li><strong>C and D curves</strong> from 0.5 to 63 A, and 80 to 125 A breakers for large incomers.</li>"
    "<li><strong>RCCBs, RCBOs and isolators</strong> in the same family, and Ekinox boards built for them.</li></ul>"),
   ("Prices", MCB_ROW
    + "<p>Full tables: <a href=\"price-lists/legrand-mcb-price-list.html\">Legrand MCB</a>, <a href=\"price-lists/legrand-rccb-price-list.html\">Legrand RCCB</a>, <a href=\"price-lists/legrand-distribution-board-price-list.html\">Legrand DB</a>.</p>"),
   ("Size the MCB to the wire",
    "<p>The breaker protects the wire, so it is chosen from the wire size: 6 or 10 A on 1.5 sq mm lighting, 16 A on 2.5 sq mm sockets, 20 or 25 A on 4.0 sq mm geyser and AC circuits. Use the <a href=\"tools/mcb-selector.html\">MCB selector</a>.</p>"),
  ],
  [("Which MCB is best for home use?", "Legrand DX3, with a 30 mA Legrand RCCB on the incomer. They are 10 kA ISI breakers and Mount Cable India sells them at 65% off MRP."),
   ("What is the Legrand MCB price?", f"A DX3 SP MCB 6 to 32 A, C curve, is ₹494 MRP, {rs(lnet(494))} at Mount Cable India."),
   ("Which MCB curve for a house?", "C curve for almost every household circuit. D curve is for motors and loads with a high starting current.")]),

_page("best-wire-for-house-wiring",
  "Best Wire for House Wiring in 2026: Brand, Grade and Size | Mount Cable India",
  "The best wire for house wiring: Finolex, in the right grade (Flamegard FR-LSH for most homes) and the right size for each circuit, with a size table, current prices and how to verify the coil.",
  "Best wire for house wiring: brand, grade and size",
  "Recommendation · Finolex Flamegard FR-LSH",
  "Choosing house wire comes down to three questions: which brand, which grade, which size. Here is our answer to all three.",
  "The best wire for house wiring is Finolex Flamegard FR-LSH in the correct size for each circuit: 1.5 sq mm for lights and fans, 2.5 sq mm for sockets, 4.0 sq mm for geysers and 1.5-ton ACs, 6.0 sq mm for 2-ton ACs and the main feed. Choose Finoultra for a premium home, or Silver or Gold FR on a tighter budget.",
  ("house-under-construction-conduit-wiring.jpg", "House under construction in Bangalore with Finolex wiring run through conduits"),
  [("Size by circuit", SIZE_GUIDE),
   ("Grade by budget", FINOLEX_GRADES),
   ("How much you need",
    "<p>A 2BHK typically uses 8 to 12 coils across sizes; a 3BHK 12 to 18. Work it out with the <a href=\"blog/how-much-wire-required-2bhk-3bhk-house.html\">wire quantity guide</a> or the <a href=\"tools/wire-quantity-calculator.html\">wire quantity calculator</a>.</p>"),
   ("Verify every coil", TWO_QR),
  ],
  [("Which wire is best for house wiring?", "Finolex Flamegard FR-LSH, correctly sized: 1.5 sq mm for lights, 2.5 for sockets, 4.0 for geysers and 1.5-ton ACs, 6.0 for 2-ton ACs and the main feed."),
   ("Which is better, FR or FRLS wire?", "FRLS (FR-LSH) gives off much less smoke in a fire, at a small extra cost per coil. We recommend it for most homes."),
   ("Is copper wire better than aluminium for houses?", "Yes. Copper is the standard for house wiring; aluminium is used for large service cables, not internal circuits.")]),

_page("is-finolex-wire-good",
  "Is Finolex Wire Good? An Honest Answer from a Finolex Distributor | Mount Cable India",
  "Is Finolex wire good for house wiring? What Finolex does well, its grades, how it compares with Polycab, KEI and RR Kabel, how to make sure your coil is genuine, and current prices.",
  "Is Finolex wire good?",
  "Honest answer · Finolex distributor, 35 years",
  "We are one of India's largest Finolex distributors, so you should weigh our answer accordingly. Here are the facts we base it on.",
  "Yes. Finolex wire is IS 694 copper house wire with FR, low-smoke FR-LSH and halogen-free Finoultra grades, it is the most specified house wire among Bangalore electricians, and every carton can be verified with two QR codes. The one real risk is buying a counterfeit, which you can rule out at site.",
  ("shop-owner-explaining-wire-quality.jpg", "Mount Cable India explaining Finolex wire quality to a customer"),
  [("What Finolex does well",
    "<ul><li>A complete grade ladder, from Silver Pack FR to halogen-free Finoultra.</li>"
    "<li>A two-code carton check that lets a buyer prove the coil is genuine.</li>"
    "<li>Every size and coil length, from 45 m repair coils to 300 m project coils, plus flexible, LAN, CCTV, submersible and solar cable.</li></ul>"
    + FINOLEX_GRADES),
   ("How it compares",
    "<p>Polycab, KEI and RR Kabel also make good IS 694 copper wire, and list prices are close. Finolex's advantage is verification and availability. See <a href=\"blog/kei-vs-finolex-wire-which-is-better.html\">KEI vs Finolex</a>, <a href=\"blog/rr-kabel-vs-finolex-wire-which-is-better.html\">RR Kabel vs Finolex</a> and the <a href=\"blog/finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html\">four-brand comparison</a>.</p>"),
   ("Make sure it is genuine", TWO_QR),
  ],
  [("Is Finolex a good brand for wires?", "Yes. It is IS 694 copper house wire with FR, FR-LSH and halogen-free grades, widely specified by electricians, and verifiable with two QR codes on every carton."),
   ("Is Finolex wire pure copper?", "Finolex house wire uses an electrolytic-grade copper conductor. Counterfeits do not, which is why verifying the carton matters."),
   ("Which Finolex wire is best?", "Flamegard FR-LSH for most homes; Finoultra for premium homes; Silver or Gold FR on a budget.")]),

_page("is-legrand-good-for-home",
  "Are Legrand Switches Good for Home? An Honest Answer | Mount Cable India",
  "Are Legrand switches and MCBs good for a home? What Legrand does well, its four switch ranges and DX3 breakers, the 10-year replacement, how to avoid copies, and prices at 65% off MRP.",
  "Are Legrand switches good for home?",
  "Honest answer · Legrand stockist",
  "Legrand is a premium name, and premium names attract two worries: is it worth the price, and is the one I am buying real? Here are both answered.",
  "Yes. Legrand switches have a reliable mechanism, ISI shuttered sockets and plates that keep their finish, and Legrand states a 10-year manufacturing-defect replacement on Myrius and Britzy switches and sockets. Its DX3 MCBs are 10 kA ISI breakers. At 65% off MRP, Legrand's entry ranges cost about what other brands do at a shop.",
  ("happy-electrician-installing-modular-switch.jpg", "Electrician installing a Legrand modular switch in a Bangalore home"),
  [("Worth the price?", LEGRAND_RANGES
    + "<p>At Mount Cable India's price a Britzy 6A switch is ₹20 and a Lyncus 6A switch ₹35, so the question is less about cost than about which range you prefer.</p>"),
   ("Switches and breakers from one maker",
    "<p>Legrand also makes the DX3 MCBs, RCCBs and Ekinox boards behind the switches. See <a href=\"best-mcb-brand.html\">which MCB brand is best</a>.</p>"),
   ("Avoiding copies",
    "<p>Buy from a stockist, keep the invoice, and treat a price far below a stockist's net as a warning. See <a href=\"original-legrand-mcb.html\">Legrand MCB 100% original</a> and <a href=\"blog/how-to-identify-duplicate-legrand-switches.html\">duplicate Legrand switches</a>.</p>"),
  ],
  [("Is Legrand a good brand for switches?", "Yes. Reliable mechanism, ISI shuttered sockets, durable plates, and a 10-year manufacturing-defect replacement on Myrius and Britzy switches and sockets."),
   ("Is Legrand worth the money?", "At 65% off MRP, yes. A Legrand Britzy 6A switch is ₹20 and a Lyncus 6A switch ₹35 at Mount Cable India."),
   ("Is Legrand an Indian brand?", "Legrand is a French group and one of the largest electrical wiring-device makers in the world, with manufacturing in India.")]),
]

BEST_PAGE_LINKS = [
    ("which-electrical-brand-to-buy.html", "Which electrical brand to buy"),
    ("best-switch-brand-in-india.html", "Which switch brand is best"),
    ("best-wire-brand-in-india.html", "Which wire brand is best"),
    ("safest-electrical-brand.html", "Safest electrical brand"),
    ("safest-wire-for-house.html", "Safest wire for a house"),
    ("best-quality-switches.html", "Best quality switches"),
    ("best-mcb-brand.html", "Best MCB brand"),
    ("best-wire-for-house-wiring.html", "Best wire for house wiring"),
    ("is-finolex-wire-good.html", "Is Finolex wire good?"),
    ("is-legrand-good-for-home.html", "Are Legrand switches good?"),
]

# ---------------------------------------------------------------- Oct 2026 batch 2: Legrand MCB + comparisons
from data_brand_prices import ANCHOR_ROMA_URBAN, ANCHOR_PENTA_MOD, LEGRAND_MCB_D

CIRCUIT_MCB = _tbl(
    ["Circuit", "Finolex wire", "Legrand DX3 MCB", "MCB MRP", "Mount Cable price"],
    [("Lighting and fans", "1.5 sq mm", "SP 6 or 10 A, C curve", rs(494), rs(lnet(494))),
     ("6A and 16A sockets", "2.5 sq mm", "SP 16 A, C curve", rs(494), rs(lnet(494))),
     ("Geyser", "4.0 sq mm", "DP 20 A, C curve", rs(1693), rs(lnet(1693))),
     ("1.5-ton AC", "4.0 sq mm", "DP 20 or 25 A, C curve", rs(1693), rs(lnet(1693))),
     ("2-ton AC", "6.0 sq mm", "DP 32 A, C curve", rs(1693), rs(lnet(1693))),
     ("Borewell or sump pump", "Submersible / 2.5 to 4.0 sq mm", "DP, D curve, rated to the motor", rs(1754), rs(lnet(1754))),
     ("Main incomer, single phase", "6.0 to 10 sq mm", "DP 40 or 63 A + 30 mA RCCB", rs(2663), rs(lnet(2663)))])
CIRCUIT_NOTE = ('<p class="ptable-note">MCB prices are Legrand MRP inclusive of GST (Corp MPL 2026) and Mount Cable India\'s '
                'price at 65% off. Final ratings depend on the appliance and run length; send us the load list to confirm.</p>')

BEST_SEO_PAGES += [

_page("legrand-mcb-for-house",
  "Which Legrand MCB for Each Circuit in a House? Rating, Curve and Price | Mount Cable India",
  "Which Legrand DX3 MCB to use for lights, sockets, geyser, AC, pump and the main incomer, with the matching Finolex wire size, the RCCB, and MRP and net prices at 65% off.",
  "Which Legrand MCB for each circuit in a house",
  "Legrand DX3 · matched to Finolex wire sizes",
  "An MCB is chosen from the wire it protects. Get that pairing right and every circuit in the house is protected; get it wrong and the MCB either trips all day or never trips at all.",
  "Use a Legrand DX3 C curve SP MCB of 6 or 10 A for lights on 1.5 sq mm wire and 16 A for sockets on 2.5 sq mm, a DP 20 or 25 A for geysers and 1.5-ton ACs on 4.0 sq mm, a DP 32 A for 2-ton ACs on 6.0 sq mm, a D curve for pumps, and a DP 40 or 63 A incomer with a 30 mA RCCB.",
  ("electrician-installing-mcb-distribution-board.jpg", "Legrand DX3 MCBs matched to circuits in a home distribution board"),
  [("Circuit by circuit", CIRCUIT_MCB + CIRCUIT_NOTE),
   ("Do not skip the RCCB",
    "<p>The MCB protects the wire from overload and short circuit. Only an RCCB protects a person from shock. Every home needs a 30 mA RCCB on the incomer, or RCBOs on wet-area circuits. Prices are on the <a href=\"price-lists/legrand-rccb-price-list.html\">Legrand RCCB price list</a>.</p>"),
   ("Every Legrand MCB price list",
    "<p><a href=\"price-lists/legrand-mcb-price-list.html\">All Legrand MCBs</a> · <a href=\"price-lists/legrand-dp-mcb-price-list.html\">DP MCB</a> · <a href=\"price-lists/legrand-4-pole-mcb-price-list.html\">4 pole and TPN</a> · <a href=\"price-lists/legrand-d-curve-mcb-price-list.html\">D curve</a> · <a href=\"price-lists/legrand-distribution-board-price-list.html\">Distribution boards</a>. Check any circuit with the <a href=\"tools/mcb-selector.html\">MCB selector</a>.</p>"),
  ],
  [("Which MCB is used for a geyser?", "A Legrand DX3 DP 20 A C curve MCB on 4.0 sq mm Finolex wire for a typical 2 to 3 kW geyser."),
   ("Which MCB for a 1.5-ton AC?", "A DX3 DP 20 or 25 A C curve MCB on 4.0 sq mm wire."),
   ("Which MCB for a 2-ton AC?", "A DX3 DP 32 A C curve MCB on 6.0 sq mm wire."),
   ("Which MCB for lights?", "A DX3 SP 6 or 10 A C curve MCB on 1.5 sq mm wire.")]),

_page("wire-and-mcb-for-ac-geyser",
  "Which Wire and MCB for AC and Geyser? Finolex Size + Legrand MCB | Mount Cable India",
  "The right wire size and MCB for an AC or geyser: Finolex 4.0 or 6.0 sq mm FR-LSH with a Legrand DX3 DP MCB, with prices for both.",
  "Which wire and MCB for an AC and geyser",
  "Finolex wire + Legrand MCB",
  "ACs and geysers are the heaviest loads in a house and the circuits most often under-wired. Here is the pairing we supply.",
  "For a geyser or 1.5-ton AC use 4.0 sq mm Finolex Flamegard FR-LSH on a Legrand DX3 DP 20 or 25 A C curve MCB. For a 2-ton AC use 6.0 sq mm on a DP 32 A. Each heavy appliance gets its own circuit.",
  ("electrician-testing-socket-multimeter.jpg", "Electrician testing an AC point wired with Finolex 4 sq mm wire"),
  [("The pairing", _tbl(["Appliance", "Finolex FR-LSH 90 m coil", "Legrand DX3 MCB"],
      [("Geyser 2 to 3 kW", "4.0 sq mm, " + _hw("4.0", "frls90"), "DP 20 A C curve"),
       ("1.5-ton AC", "4.0 sq mm, " + _hw("4.0", "frls90"), "DP 20 or 25 A C curve"),
       ("2-ton AC", "6.0 sq mm, " + _hw("6.0", "frls90"), "DP 32 A C curve")]) + FIN_LINE + MCB_ROW),
   ("Why heat matters here",
    "<p>These circuits carry high current for hours. That is where an under-sized or counterfeit wire runs hot, so it is where the wire grade, the size and a genuine coil matter most. For the longest runs, Finoultra's heat-resistant e-beam insulation is worth considering.</p>" + TWO_QR),
  ],
  [("Which wire is used for AC?", "4.0 sq mm Finolex FR-LSH for a 1.5-ton AC and 6.0 sq mm for a 2-ton AC, each on its own Legrand DP MCB."),
   ("Which wire for a geyser?", "4.0 sq mm Finolex FR-LSH on a Legrand DX3 DP 20 A MCB."),
   ("Is 2.5 sq mm wire enough for an AC?", "We do not recommend it for a 1.5-ton or larger AC. Use 4.0 sq mm, or 6.0 sq mm for 2-ton.")]),

_page("legrand-vs-anchor-switches",
  "Legrand vs Anchor Switches: Which Is Better for Your Home? | Mount Cable India",
  "Legrand vs Anchor by Panasonic modular switches compared on range, price at MRP, sockets and replacement policy. Both are stocked at Mount Cable India; we recommend Legrand, and explain why.",
  "Legrand vs Anchor switches: which is better?",
  "Fair comparison · we stock both",
  "Anchor by Panasonic and Legrand are the two switch brands Bangalore buyers ask us about most, and we sell both. Here is a fair comparison, and our recommendation.",
  "Both are reputable, ISI-marked switch brands. Anchor is a familiar value choice. We recommend Legrand because its mechanism and premium ranges are a step up, Legrand states a 10-year manufacturing-defect replacement on Myrius and Britzy switches and sockets, and at Mount Cable India's 65% off MRP Legrand costs about the same as Anchor.",
  ("woman-homeowner-choosing-modular-switches.jpg", "Comparing Legrand and Anchor modular switches in a Bangalore showroom"),
  [("MRP compared, like for like",
    _tbl(["Item (MRP)", "Legrand Britzy", "Anchor Penta modular", "Legrand Lyncus", "Anchor Roma Urban"],
         [("One-way switch, 1 module", rs(56) + " (6A)", rs(46) + " (6AX)", rs(100) + " (6A)", rs(160) + " (10AX)"),
          ("Two-way switch, 1 module", rs(132), rs(106), rs(212), rs(243)),
          ("32A DP switch with indicator", rs(382), rs(263), rs(718), rs(510))])
    + '<p class="ptable-note">MRP inclusive of GST: Legrand Corp MPL 2026, Anchor by Panasonic pricelist April 2026. Ratings differ slightly between ranges, as shown. Legrand is sold at 65% off MRP at Mount Cable India.</p>'),
   ("Where each fits",
    "<p>Anchor Penta and Roma are long-established, widely available ranges and a sensible budget choice. Legrand's ladder runs from Britzy and Allzy to Lyncus and Myrius, so one brand covers every room from utility to living room, with Legrand DX3 MCBs behind them.</p>"),
   ("Our recommendation",
    "<p>Legrand, for the mechanism, the premium ranges and the written replacement policy, especially because the price difference largely disappears at our Legrand discount. If you prefer Anchor we will supply it genuine. Price lists: <a href=\"price-lists/legrand-switches-price-list.html\">Legrand switches</a>, <a href=\"price-lists/anchor-panasonic-price-list.html\">Anchor</a>.</p>"),
  ],
  [("Which is better, Legrand or Anchor switches?", "Both are reputable. We recommend Legrand for its mechanism, premium ranges and 10-year replacement on Myrius and Britzy switches and sockets; at 65% off MRP it costs about the same as Anchor."),
   ("Is Anchor cheaper than Legrand?", "At MRP, Anchor's mid ranges are often cheaper. At Mount Cable India's 65% off Legrand MRP, Legrand Britzy and Lyncus cost about what Anchor does."),
   ("Is Anchor a good brand?", "Yes. Anchor by Panasonic is a well-established ISI-marked switch brand and a good value choice.")]),

_page("finolex-vs-polycab-wire",
  "Finolex vs Polycab Wire: Which Is Better for House Wiring? | Mount Cable India",
  "Finolex vs Polycab house wire compared on grades, list price, verification and availability. We stock both and recommend Finolex for house wiring, with the reasons.",
  "Finolex vs Polycab wire: which is better?",
  "Fair comparison · we stock both",
  "Finolex and Polycab are the two wire brands most Bangalore homes choose between, and we supply both. Here is a fair comparison and our recommendation.",
  "Both make good IS 694 copper house wire, and coil list prices are close. We recommend Finolex for house wiring because every carton can be checked with two QR codes at site, its Flamegard FR-LSH grade gives low-smoke safety at a small premium, and it is the house wire most Bangalore electricians ask for.",
  ("wire-coils-warehouse-electrical-distributor.jpg", "Finolex and Polycab wire coils at a Bangalore electrical distributor"),
  [("List price, coil to coil",
    _tbl(["90 m coil, list price", "Finolex Silver Pack FR", "Polycab Etira FR"],
         [("1.5 sq mm", rs(HOUSE_WIRE["1.5"]["silver"]), rs(3820)),
          ("2.5 sq mm", rs(HOUSE_WIRE["2.5"]["silver"]), rs(6095)),
          ("4.0 sq mm", rs(HOUSE_WIRE["4.0"]["silver"]), rs(9115))])
    + f'<p class="ptable-note">Manufacturer list prices before dealer pricing: Finolex list wef {EFFECTIVE_FROM}, Polycab distributor coil list June 2026 (ex-GST). Nobody pays list; compare dealer quotes on the same basis.</p>'),
   ("Grades side by side",
    "<p>Finolex: Silver and Gold FR, Flamegard FR-LSH, Finoultra halogen-free. Polycab: Etira FR, Primma and Optima FRLF, Maxima HR-FR. Both brands cover the same needs; the names differ.</p>"),
   ("Why we recommend Finolex", TWO_QR
    + "<p>Polycab is the right pick if you want one brand across wires, fans and lighting. For house wire alone, Finolex. See <a href=\"price-lists/finolex-price-list.html\">Finolex prices</a> and <a href=\"price-lists/polycab-price-list.html\">Polycab prices</a>.</p>"),
  ],
  [("Which is better, Finolex or Polycab wire?", "Both make good IS 694 copper wire. We recommend Finolex for house wiring for its two-QR verification and low-smoke Flamegard grade; Polycab suits buyers who want one brand across wires, fans and lighting."),
   ("Is Polycab cheaper than Finolex?", "List prices are close: a 1.5 sq mm 90 m coil lists at ₹3,820 for Polycab Etira and ₹3,640 for Finolex Silver Pack. Dealer prices on both are below list."),
   ("Which is best, Finolex FR-LSH or Polycab FRLF?", "Both are low-smoke safety grades for homes and flats. We supply Finolex Flamegard FR-LSH as our default.")]),
]

BEST_PAGE_LINKS += [
    ("legrand-mcb-for-house.html", "Which Legrand MCB for each circuit"),
    ("wire-and-mcb-for-ac-geyser.html", "Wire and MCB for AC and geyser"),
    ("legrand-vs-anchor-switches.html", "Legrand vs Anchor switches"),
    ("finolex-vs-polycab-wire.html", "Finolex vs Polycab wire"),
]
