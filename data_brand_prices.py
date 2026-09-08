# -*- coding: utf-8 -*-
"""Brand price-list pages built from the actual manufacturer / distributor
price lists held in the Mount Cable quote builder (Sep 2026).

Sources (all transcribed from the PDFs, page images cross-checked):
  Finolex  — Finolex Cables list price sheet wef 04 Sep 2026 (data_finolex_mrp.py).
             Published as Mount Cable NET selling prices only (owner rule).
  Legrand  — Legrand India Corp MPL 2026 (J9238). MRP inclusive of GST.
  Anchor   — Panasonic (Anchor) "Power for every home" pricelist, April 2026.
             Unit sale price = MRP per piece inclusive of taxes.
  Polycab  — Shree NM Electricals (Polycab distributor) price lists:
             house-wire coils wef 8 Jun 2026, flexible No.04 wef 15 Aug 2026,
             armoured wef 18 Aug 2026, telecom/coax wef 25 May 2026. Ex-GST.

Every page here is a dict in the PRICE_LISTS format understood by
build_price_list() in build.py, using the newer "cols" table shape.
"""
from data_finolex_mrp import (HOUSE_WIRE, LONG_LEN, FLEXIBLE, FLEXIBLE_FRLS_MULTI, TELEPHONE,
                              CCTV_FULL, COAXIAL_FULL, SPEAKER_100M, SPEAKER_25M, SOLAR_DC,
                              SOLAR_NOVA, LAN_FULL, FLAT_SUBMERSIBLE, FLAT_SUBMERSIBLE_XLPE,
                              EFFECTIVE_FROM, TAX_NOTE, offer)

W = "https://wa.me/918867676700"
PH = "88676 76700"


def rs(n):
    return "₹" + format(int(round(n)), ",d")


def dash():
    return "—"


CTA_NOTE = (f'<p><strong>Want your rate on any line?</strong> WhatsApp the list to <a href="{W}">{PH}</a>. '
            'Mount Cable India replies with an itemised quote within 60 minutes, and you are free to use it as a '
            'reference price anywhere.</p>')

# =====================================================================
# FINOLEX — net prices, every range on the 4 Sep 2026 list
# =====================================================================
SIZES = ["0.75", "1.0", "1.5", "2.5", "4.0", "6.0"]


def _hw(size, key):
    v = HOUSE_WIRE[size].get(key)
    return rs(offer(v, key)) if v else dash()


FINOLEX_TABLES = [
    {"title": "Finolex house wire, 90 m coils (single core FR / FR-LSH / HFFR)",
     "cols": ["Size", "Silver Pack FR", "Gold Pack FR", "Finoultra (HFFR)", "Flamegard FR-LSH"],
     "rows": [(f"{s} sq mm", _hw(s, "silver"), _hw(s, "gold"), _hw(s, "ultra"), _hw(s, "frls90")) for s in SIZES],
     "note": "<p>Silver Pack and Gold Pack are both IS 694 FR single-core house wire; Gold is the higher line. Finoultra is the e-beam cross-linked halogen-free (HFFR) range to IS 17048. Flamegard is the low-smoke FR-LSH grade. Read <a href=\"../blog/finolex-silver-vs-gold-90m.html\">Silver vs Gold</a> and <a href=\"../blog/fr-vs-frls-vs-finolex-ultra.html\">FR vs FR-LSH vs Finoultra</a> before choosing.</p>"},
    {"title": "Finolex 180 m project packing coils",
     "cols": ["Size", "FR 180 m", "FR-LSH 180 m"],
     "rows": [(f"{s} sq mm", _hw(s, "fr180"), _hw(s, "frls180")) for s in SIZES],
     "note": "<p>180 m coils are the site-pack size for builders and contractors: half the coil changes and fewer joints. See <a href=\"../blog/what-is-finolex-project-packing.html\">what Finolex project packing is</a>.</p>"},
    {"title": "Finolex long coils, 300 m and 200 m",
     "cols": ["Size", "Coil length", "FR", "FR-LSH"],
     "rows": [(f"{s} sq mm", LONG_LEN[s], _hw(s, "long"), _hw(s, "frls_long")) for s in SIZES],
     "note": "<p>0.75 to 2.5 sq mm ship as 300 m coils and 4.0 and 6.0 sq mm as 200 m coils. This is the lowest price per metre Finolex offers on house wire, and the packing we quote for apartment projects and bulk orders.</p>"},
    {"title": "Finolex 45 m coils (FR)",
     "cols": ["Size", "FR 45 m"],
     "rows": [(f"{s} sq mm", _hw(s, "fr45")) for s in SIZES if HOUSE_WIRE[s].get("fr45")]},
    {"title": "Finolex flexible cable, single core, 100 m coils",
     "cols": ["Size", "FR", "FRLS"],
     "rows": [(f"{s} sq mm", rs(offer(v[0])), rs(offer(v[1]))) for s, v in FLEXIBLE.items()],
     "note": "<p>Bright annealed bare copper Class 5 flexible cable to IS 694, colours red, black, blue, yellow, grey and green. Sizes above 6 sq mm are the heavy-duty single core. See the <a href=\"../blog/flexible-cable-submersible-pump-cable-guide.html\">flexible and submersible cable guide</a>.</p>"},
    {"title": "Finolex flexible multicore (round sheathed), 100 m coils, FR",
     "cols": ["Size", "2 core", "3 core", "4 core"],
     "rows": [(f"{s} sq mm", rs(offer(v[2])), rs(offer(v[3])), rs(offer(v[4]))) for s, v in FLEXIBLE.items() if v[2]]},
    {"title": "Finolex flexible multicore, 100 m coils, FRLS",
     "cols": ["Size", "2 core", "3 core", "4 core"],
     "rows": [(f"{s} sq mm", rs(offer(v[0])), rs(offer(v[1])), rs(offer(v[2]))) for s, v in FLEXIBLE_FRLS_MULTI.items()]},
    {"title": "Finolex telephone cable, 90 m coils",
     "cols": ["Pairs", "0.4 mm conductor", "0.5 mm conductor"],
     "rows": [(k, rs(offer(v[0])), rs(offer(v[1]))) for k, v in TELEPHONE.items()]},
    {"title": "Finolex co-axial cable (jelly filled)",
     "cols": ["Type", "Pack", "Price"],
     "rows": [(a, b, rs(offer(c))) for a, b, c in COAXIAL_FULL],
     "note": "<p>CU is solid electrolytic copper conductor; CCS is copper-clad steel; CCA is copper-clad aluminium. For DTH and cable TV runs inside a house the RG 6 CCS 100 m coil is the usual pick.</p>"},
    {"title": "Finolex CCTV cable",
     "cols": ["Type", "Pack", "Price"],
     "rows": [(a, b, rs(offer(c))) for a, b, c in CCTV_FULL]},
    {"title": "Finolex LAN cable (Cat 5e / Cat 6 / Cat 6A)",
     "cols": ["Description", "Pack", "Price"],
     "rows": [(a, b, rs(offer(c))) for a, b, c in LAN_FULL],
     "note": "<p>Cat 6 UTP in the 305 m box is the standard for a wired home network. See the <a href=\"../blog/cat6-lan-cable-home-networking-guide.html\">Cat 6 home networking guide</a>.</p>"},
    {"title": "Finolex speaker cable (transparent)",
     "cols": ["Size", "100 m coil", "25 m coil"],
     "rows": [(f"{s} sq mm", rs(offer(v)), rs(offer(SPEAKER_25M[s])) if s in SPEAKER_25M else dash()) for s, v in SPEAKER_100M.items()]},
    {"title": "Finolex 3-core flat submersible cable, per 100 m",
     "cols": ["Size", "PVC insulated", "XLPE insulated"],
     "rows": [(f"{s} sq mm", rs(offer(v)), rs(offer(FLAT_SUBMERSIBLE_XLPE[s]))) for s, v in FLAT_SUBMERSIBLE.items()],
     "note": "<p>Supplied in drums in continuous length; minimum order 500 m for non-standard lengths.</p>"},
    {"title": "Finolex solar DC cable, per 100 m",
     "cols": ["Size", "Solar DC (e-beam, tinned copper)", "Solar Nova"],
     "rows": [(k.split(" (")[0], rs(offer(v)), rs(offer(SOLAR_NOVA[k])) if k in SOLAR_NOVA else dash()) for k, v in SOLAR_DC.items()] +
             [("10 sq mm", dash(), rs(offer(SOLAR_NOVA["10 sq mm (per 100 m)"])))]},
]

FINOLEX_PAGE = {
    "slug": "finolex", "name": "Finolex", "kind": "brand", "group": "Wires & Cables",
    "title": "Finolex Wire Price List 2026 (Updated September 2026) — Every Range | Mount Cable India",
    "h1": "Finolex wire price list 2026, updated September 2026",
    "desc": "Complete Finolex wire price list for 2026, current to the 4 September 2026 Finolex list: Silver, Gold, Finoultra, FR-LSH, 45/90/180/300 m coils, flexible, multicore, telephone, co-axial, CCTV, LAN, speaker, submersible and solar cable. Mount Cable India, Bangalore.",
    "intro": f"These are Mount Cable India's selling prices for every Finolex line we stock, worked from the Finolex list price sheet effective {EFFECTIVE_FROM}. {TAX_NOTE} Larger quantities are priced better. We are one of the largest Finolex distributors in India, 35 years in Bangalore, and every coil is QR-verifiable at your site before you pay.",
    "badge": f"Finolex list wef {EFFECTIVE_FROM} · Our net prices",
    "effective": EFFECTIVE_FROM,
    "tables": FINOLEX_TABLES,
    "price_note": f"<p class=\"ptable-note\">All prices are Mount Cable India selling prices per coil or pack, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE} Finolex revises its list with copper and the rupee, so the figures move a few times a year; the date above tells you which list this is.</p>",
    "note": ("<h2>How to use this Finolex price list</h2>"
             "<p>Start from the size, not the range. Lighting circuits use 1.5 sq mm, 6A socket circuits 2.5 sq mm, geyser and 1.5-ton AC points 4.0 sq mm, and the main feed or a 2-ton AC 6.0 sq mm. Then pick the pack: <strong>Silver Pack</strong> for standard FR house wire, <strong>Gold Pack</strong> for the premium line, <strong>Flamegard FR-LSH</strong> for flats and enclosed stairwells where smoke matters, and <strong>Finoultra</strong> where a halogen-free specification is written. Work out how many metres you need with the <a href=\"../blog/how-much-wire-required-2bhk-3bhk-house.html\">2BHK/3BHK wire quantity guide</a> or the <a href=\"../tools/house-wiring-cost-calculator.html\">house wiring cost calculator</a>.</p>"
             "<h2>Why our Finolex price is lower than the shop near you</h2>"
             "<p>Finolex sells through distributors, and a distributor buys in truckloads directly from the company. A retailer buys a few cartons from a distributor and adds a margin on top. Mount Cable India is the distributor, so the price you see here is one step closer to the factory than a shop price. The catch in the wire trade is that a price far <em>below</em> a distributor's is not a bargain: it is short length, thin copper or a counterfeit carton. Read <a href=\"../blog/finolex-dealer-price-vs-retail-price.html\">dealer price vs retail price</a> and <a href=\"../original-finolex-wires.html\">how to verify original Finolex wire</a>.</p>"
             "<h2>Finolex price by size</h2>"
             "<p>Every size has its own page with the full pack table and what that size is used for: "
             "<a href=\"../blog/finolex-1-mm-wire-price.html\">1.0 sq mm</a>, "
             "<a href=\"../blog/finolex-1-5-mm-wire-price.html\">1.5 sq mm</a>, "
             "<a href=\"../blog/finolex-2-5-mm-wire-price.html\">2.5 sq mm</a>, "
             "<a href=\"../blog/finolex-4-mm-wire-price.html\">4.0 sq mm</a>, "
             "<a href=\"../blog/finolex-6-mm-wire-price.html\">6.0 sq mm</a> and "
             "<a href=\"../blog/finolex-0-75-mm-wire-price.html\">0.75 sq mm</a>. "
             "For the Gold Pack on its own see the <a href=\"finolex-gold-wire-price-list.html\">Finolex Gold wire price list</a>, and to order any line directly on WhatsApp use the <a href=\"../buy-finolex-wires.html\">buy Finolex wires page</a>.</p>"
             + CTA_NOTE),
    "related": [("finolex-gold-wire-price-list.html", "Finolex Gold wire price list 2026"),
                ("../buy-finolex-wires.html", "Buy Finolex wires online (WhatsApp ordering)"),
                ("../finolex-wire-scanner.html", "Finolex wire scanner: check a coil is original"),
                ("../blog/finolex-silver-vs-gold-90m.html", "Finolex Silver vs Gold: the difference"),
                ("polycab-price-list.html", "Polycab wire price list 2026"),
                ("../blog/finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html", "Finolex vs Polycab vs RR Kabel vs KEI")],
    "faqs": [
        ("What is the Finolex wire price list for 2026?",
         f"The table above is the complete Finolex price list current to {EFFECTIVE_FROM}, shown as Mount Cable India's selling prices. A 90 m Silver Pack coil is {_hw('1.0','silver')} in 1.0 sq mm, {_hw('1.5','silver')} in 1.5 sq mm, {_hw('2.5','silver')} in 2.5 sq mm, {_hw('4.0','silver')} in 4.0 sq mm and {_hw('6.0','silver')} in 6.0 sq mm, taxes extra."),
        ("What is the Finolex 1.5 mm wire price today?",
         f"A Finolex 1.5 sq mm 90 m coil is {_hw('1.5','silver')} in Silver Pack FR, {_hw('1.5','gold')} in Gold Pack FR and {_hw('1.5','frls90')} in Flamegard FR-LSH at Mount Cable India, current to {EFFECTIVE_FROM}, taxes extra."),
        ("What is the Finolex Gold wire price?",
         f"Finolex Gold Pack 90 m coils are {_hw('1.0','gold')} in 1.0 sq mm, {_hw('1.5','gold')} in 1.5 sq mm, {_hw('2.5','gold')} in 2.5 sq mm, {_hw('4.0','gold')} in 4.0 sq mm and {_hw('6.0','gold')} in 6.0 sq mm. The Gold page lists every size with Silver alongside it."),
        ("Is this the Finolex MRP or the selling price?",
         "These are Mount Cable India's selling prices, taxes extra as applicable. Finolex publishes a list price that trade buyers never pay; our price is worked from that list as a distributor. If another seller quotes far below these figures, verify the coil before paying."),
        ("How often do Finolex prices change?",
         f"Finolex revises its list price a few times a year with copper and the rupee. This page is built from the list effective {EFFECTIVE_FROM} and is regenerated whenever a new list arrives, so the date at the top tells you exactly which list you are looking at."),
        ("Do you supply Finolex flexible, LAN, co-axial and submersible cable too?",
         "Yes. Every line in the tables above is stocked at Jayanagar and Chickpete: flexible single core and multicore, telephone, co-axial, CCTV, Cat 6 LAN, speaker, 3-core flat submersible and solar DC cable, with free next-day delivery across Bangalore."),
        ("Can I check the price of a Finolex coil before I pay a shop?",
         f"Yes, that is what this page is for. Compare the shop's quote with the table, and if it is far lower, scan the coil with the Finolex wire scanner before paying. For a written reference quote, WhatsApp your list to {PH}."),
    ],
}

FINOLEX_GOLD_PAGE = {
    "slug": "finolex-gold-wire", "name": "Finolex Gold Wire", "kind": "sub", "parent": "finolex", "group": "Wires & Cables",
    "title": "Finolex Gold Wire Price List 2026 (Gold Pack 90 m) with Silver Alongside | Mount Cable India",
    "h1": "Finolex Gold wire price list 2026",
    "desc": f"Finolex Gold Pack 90 m coil prices for 0.75 to 6.0 sq mm, current to {EFFECTIVE_FROM}, with Silver Pack and FR-LSH alongside so you can see the difference per coil. Mount Cable India, Bangalore.",
    "intro": f"The Gold Pack is Finolex's premium FR house wire. Here is every size at Mount Cable India's selling price, current to the Finolex list effective {EFFECTIVE_FROM}, with the Silver Pack next to it so the extra cost per coil is visible. {TAX_NOTE}",
    "badge": f"Finolex list wef {EFFECTIVE_FROM} · Our net prices",
    "effective": EFFECTIVE_FROM,
    "tables": [
        {"title": "Finolex Gold Pack vs Silver Pack, 90 m coils",
         "cols": ["Size", "Gold Pack FR 90 m", "Silver Pack FR 90 m", "Gold costs more by"],
         "rows": [(f"{s} sq mm", _hw(s, "gold"), _hw(s, "silver"),
                   rs(offer(HOUSE_WIRE[s]["gold"], "gold") - offer(HOUSE_WIRE[s]["silver"], "silver"))) for s in SIZES]},
        {"title": "Other premium Finolex 90 m coils",
         "cols": ["Size", "Finoultra (HFFR)", "Flamegard FR-LSH"],
         "rows": [(f"{s} sq mm", _hw(s, "ultra"), _hw(s, "frls90")) for s in SIZES]},
    ],
    "price_note": f"<p class=\"ptable-note\">Mount Cable India selling prices per 90 m coil, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}</p>",
    "note": ("<h2>What you get for the difference</h2>"
             "<p>Both packs are IS 694 flame-retardant single-core copper wire from Finolex, and both carry the same QR verification. Gold is positioned as the premium pack with the higher insulation specification and the premium carton, and it is what most electricians in Bangalore ask for by name on a new house. Silver is the standard pack and is the right choice where the budget is tight or the run is short. The full argument, including what an electrician means when he says one is better, is in <a href=\"../blog/finolex-silver-vs-gold-90m.html\">Finolex Silver vs Gold 90 m</a>.</p>"
             "<h2>Gold Pack by size: what each is used for</h2>"
             "<ul><li><strong>1.0 sq mm</strong>: earth wire on lighting circuits and low-load points.</li>"
             "<li><strong>1.5 sq mm</strong>: lighting circuits and 6A socket points.</li>"
             "<li><strong>2.5 sq mm</strong>: 16A socket circuits, kitchen points, mixer and microwave.</li>"
             "<li><strong>4.0 sq mm</strong>: geyser and 1.5-ton AC points.</li>"
             "<li><strong>6.0 sq mm</strong>: 2-ton AC points and the main feed from meter to DB.</li></ul>"
             "<p>Gold Pack coils are 90 m only. If your run needs longer coils, the same wire in the FR 180 m project pack and 300 m / 200 m long coils is on the <a href=\"finolex-price-list.html\">full Finolex price list</a>.</p>"
             + CTA_NOTE),
    "related": [("finolex-price-list.html", "Full Finolex price list, every range"),
                ("../finolex-gold-90m-dealers.html", "Finolex Gold 90 m dealers in Bangalore"),
                ("../blog/finolex-silver-vs-gold-90m.html", "Finolex Silver vs Gold explained")],
    "faqs": [
        ("What is the Finolex Gold wire price for 1.5 sq mm?",
         f"A Finolex Gold Pack 1.5 sq mm 90 m coil is {_hw('1.5','gold')} at Mount Cable India, against {_hw('1.5','silver')} for the Silver Pack, current to {EFFECTIVE_FROM}, taxes extra."),
        ("Is Finolex Gold better than Finolex Silver?",
         "Gold is Finolex's premium FR pack and Silver is the standard FR pack. Both are genuine IS 694 copper wire with the same QR verification. Gold carries the higher specification and price; Silver is the value choice for the same sizes."),
        ("Does Finolex Gold come in 180 m or 300 m coils?",
         "No. The Gold Pack is a 90 m coil. The 180 m project pack and the 300 m / 200 m long coils are supplied as FR and FR-LSH wire, listed on the full Finolex price list."),
        ("Is a Finolex Gold coil sold far below this price genuine?",
         "Treat it with suspicion. Wire is a low-margin trade and Gold Pack cartons are the most copied. Scan both QR codes on the carton before paying, or bring the coil to us and we will check it at no charge."),
    ],
}

# =====================================================================
# LEGRAND — Corp MPL 2026, MRP inclusive of GST
# =====================================================================
def _mcb_rows(bands):
    """bands: list of (label, {pole: price})"""
    poles = ["SP", "SPN", "DP", "TP", "TPN", "FP"]
    return [(label,) + tuple(rs(d[p]) if d.get(p) else dash() for p in poles) for label, d in bands]

LEGRAND_MCB_C = [
    ("0.5 to 4 A", {"SP": 824, "SPN": 2041, "DP": 2299, "TP": 3386, "TPN": 4295, "FP": 4240}),
    ("6 to 32 A", {"SP": 494, "SPN": 1389, "DP": 1693, "TP": 2745, "TPN": 3579, "FP": 3729}),
    ("40 to 63 A", {"SP": 1180, "SPN": 2247, "DP": 2663, "TP": 4166, "TPN": 5119, "FP": 5306}),
]
LEGRAND_MCB_D = [
    ("0.5 to 4 A", {"SP": 830, "SPN": 2156, "DP": 2320, "TP": 3455, "TPN": 4321, "FP": 4382}),
    ("6 to 32 A", {"SP": 678, "DP": 1754, "TP": 2830, "FP": 3767}),
]
LEGRAND_MCB_HI = [
    ("80 A", {"SP": 4772, "DP": 11018, "TP": 17704, "FP": 22830}),
    ("100 A", {"SP": 5440, "DP": 11272, "TP": 18858, "FP": 23788}),
    ("125 A", {"SP": 5903, "DP": 12785, "TP": 20726, "FP": 26649}),
]
LEGRAND_ISOLATORS = [
    ("32 A", 874, 1574, 1726), ("40 A", 961, 1688, 2144), ("63 A", 1270, 2009, 2364),
    ("100 A", 1744, 2218, 2857), ("125 A", 1984, 2558, 3148),
]
LEGRAND_RCCB_AC = [
    ("25 A", 5478, 6034, 6137, 7870, 8298, 8547),
    ("40 A", 6360, 6968, 7320, 8068, 8396, 8673),
    ("63 A", 7818, 8297, 8330, 8976, 9875, 9909),
]
LEGRAND_RCBO_DP = [
    ("6 to 32 A", 6974, 8389, "8,656 (16 to 32 A)"),
    ("40 A", 8380, 9511, 9760),
    ("63 A", 10210, 10793, 10996),
]
LEGRAND_SPN_DB = [
    ("4 way", 4, 2405, 3150, 4285, 11016), ("8 way", 8, 2917, 4065, 4963, 13094),
    ("12 way", 12, 3447, 4884, 5665, 15042), ("16 way", 16, 4210, 6119, 7035, 15687),
    ("18 way", 18, 4897, 6430, 7837, 16887), ("20 way", 20, 5462, 7427, 8298, 18352),
]
LEGRAND_ETPN_DB = [
    ("4 way", "8+12", 7051, 8289, 10438, 26411), ("6 way", "8+18", 8746, 9990, 12760, 31781),
    ("8 way", "8+24", 10328, 11970, 15017, 34758), ("12 way", "8+36", 14726, 17751, 23260, 49460),
    ("16 way", "8+48", 17935, 22417, 28009, 58781), ("20 way", "8+60", 25031, 31234, 37865, 69930),
]
LEGRAND_VTPN_DB = [
    ("4 way", 18920, 19953, 25439, 40776), ("6 way", 20763, 22097, 27990, 44337),
    ("8 way", 23097, 24378, 32729, 49045), ("12 way", 33348, 34002, 43664, 63492),
]
LEGRAND_FLEXY = [("2 rows of 14 modules", 28, 8399, 10766, 11158), ("3 rows of 14 modules", 42, 10514, 12870, 13713),
                 ("4 rows of 14 modules", 56, 11658, 13953, 15536)]
LEGRAND_MIVAN = [("4 way", 3483), ("8 way", 4681), ("12 way", 5721), ("16 way", 6944), ("20 way", 8708)]
LEGRAND_ENCL = [("SP enclosure (1 module)", 829), ("DP enclosure (2 modules)", 1196), ("TP enclosure (3 modules)", 1196),
                ("FP enclosure (4 modules)", 1196), ("FP RCBO enclosure (8 modules)", 2000)]

# Switch ranges: (description, Britzy, Allzy white, Lyncus classic white, Myrius regular white)
LEGRAND_SWITCH_CMP = [
    ("6A one-way switch, 1 module", 56, 56, 100, 180),
    ("6A two-way switch, 1 module", 132, 126, 212, 326),
    ("16A one-way switch, 1 module", 190, 152, 246, 442),
    ("32A DP switch with indicator, 2 module", 382, 392, 718, 1510),
    ("6A bell push with indicator, 1 module", 160, 152, 250, None),
    ("6/16A socket with shutter, 2 module", 294, 284, 434, 684),
    ("TV co-axial socket, 1 module", 144, 144, None, 332),
    ("RJ45 Cat 6 socket, 1 module", 368, 788, 963, 1055),
    ("Fan regulator 100 W, 1 module", 650, 612, 734, None),
    ("Cover plate + frame, 4 module (white)", 190, None, 274, 376),
    ("Cover plate + frame, 8 module (white)", 326, None, 426, None),
    ("Cover plate + frame, 12 module (white)", 472, None, 620, 1126),
]
LEGRAND_BRITZY = [
    ("6734 01", "6A switch, SP, 1 way, 1 module", 56), ("6734 02", "6A switch, SP, 2 way, 1 module", 132),
    ("6734 03", "6A switch, 1 way with indicator, 1 module", 132), ("6734 11", "16A switch, SP, 1 way, 1 module", 190),
    ("6734 12", "16A switch, SP, 2 way, 1 module", 230), ("6734 13", "16A switch, 1 way with indicator, 1 module", 204),
    ("6734 25", "20A DP switch with indicator, 2 module", 318), ("6734 24", "25A SP switch with indicator, 1 module", 278),
    ("6734 26", "32A DP switch with indicator, 2 module", 382), ("6734 04", "6A bell push with indicator, 1 module", 160),
    ("6734 06", "6A bell push with indicator, 2 module", 240), ("6734 27", "6A 3-pin socket with shutter, ISI, 2 module", 168),
    ("6734 55", "6/16A socket with shutter, 3 pin, 2 module", 294), ("6734 41", "Telephone socket RJ11, 1 module", 158),
    ("6734 44", "Telephone socket double RJ11, 1 module", 228), ("6734 45", "RJ45 Cat 6 UTP socket with shutter, 1 module", 368),
    ("6734 46", "TV co-axial socket, 1 module", 144), ("6734 40", "Buzzer 230 V, 1 module", 392),
    ("6734 33", "Light dimmer 400 W, 1 module", 668), ("6734 31", "Fan regulator 100 W ISI, 1 module", 650),
    ("6734 30", "Fan regulator 100 W ISI, 2 module", 830), ("6734 38", "Fan regulator 8 step 100 W ISI, 2 module", 748),
    ("6734 90", "Blanking plate, 1 module", 40), ("6734 72", "Blanking plate, 2 module", 56),
]
LEGRAND_BRITZY_PLATES = [("1 module", 132), ("2 module", 132), ("3 module", 180), ("4 module", 190), ("6 module", 254),
                         ("8 module horizontal", 326), ("2 x 4 module vertical", 326), ("12 module", 472), ("16 module", 506), ("18 module", 622)]
LEGRAND_BOXES = [("1 and 2 module", 90), ("3 module", 118), ("4 module", 142), ("6 module", 226), ("8 module", 284),
                 ("8 (2 rows x 4) module", 284), ("12 (2 rows x 6) module", 394), ("16 (2 rows x 8) module", 444), ("18 module", 508)]
LEGRAND_ALLZY = [
    ("6811 00", "6A switch, SP, 1 way, 1 module", 56), ("6811 11", "6A switch, SP, 2 way, 1 module", 126),
    ("6811 02", "6A switch, 1 way with indicator, 1 module", 112), ("6811 74", "10A switch, 1 way, 1 module", 60),
    ("6811 75", "10A switch, 2 way, 1 module", 128), ("6811 01", "16A switch, SP, 1 way, 1 module", 152),
    ("6811 12", "16A switch, SP, 2 way, 1 module", 218), ("6811 05", "16A switch, 1 way with indicator, 1 module", 196),
    ("6811 07", "20A switch, SP, 1 way, 1 module", 180), ("6811 15", "20A DP switch with indicator, 2 module", 278),
    ("6811 06", "25A SP switch with indicator, 1 module", 252), ("6811 16", "32A DP switch with indicator, 2 module", 392),
    ("6811 09", "6A bell push, 1 module", 124), ("6811 10", "6A bell push with indicator, 1 module", 152),
    ("6811 22", "6/16A socket with shutter, ISI, 2 module", 284), ("6811 30", "Telephone socket RJ11 with shutter, 1 module", 150),
    ("6811 32", "RJ45 Cat 6 UTP socket with shutter, 1 module", 788), ("6811 33", "TV co-axial socket, 1 module", 144),
    ("6811 43", "Rotary dimmer 400 W, 1 module", 622), ("6811 40", "Fan regulator 4 step 100 W ISI, 1 module", 612),
    ("6811 41", "Fan regulator 100 W 360 degree ISI, 2 module", 708), ("6811 42", "Fan regulator 8 step 100 W ISI, 2 module", 772),
    ("6811 99", "Fan regulator BLDC, 2 module", 938), ("6811 39", "Buzzer 230 V, 1 module", 364),
    ("6811 38", "Flat indicator red, 1 module", 210), ("6811 66", "16A motor starter, 2 module", 714),
]
LEGRAND_LYNCUS = [
    ("6772 00", "6A switch, 1 way, 1 module", 100), ("6772 01", "6A switch, 2 way, 1 module", 212),
    ("6772 02", "6A switch, 1 way with indicator, 1 module", 212), ("6773 01", "10A switch, 1 way, 1 module", 110),
    ("6773 02", "10A switch, 2 way, 1 module", 216), ("6772 09", "16A switch, 1 way, 1 module", 246),
    ("6772 10", "16A switch, 2 way, 1 module", 302), ("6772 11", "16A switch, 1 way with indicator, 1 module", 312),
    ("6772 12", "20A switch, 1 way, 1 module", 360), ("6772 14", "20A DP switch with indicator, 2 module", 532),
    ("6772 16", "25A SP switch with indicator, 1 module", 372), ("6772 17", "32A DP switch with indicator, 2 module", 718),
    ("6772 20", "6A bell push, 1 module", 224), ("6772 35", "6A 3-pin socket with shutter, ISI, 2 module", 214),
    ("6772 30", "6/16A socket with shutter, ISI, 2 module", 434), ("6772 29", "6/16A socket with shutter, ISI, 3 module", 516),
    ("6772 36", "Rotary light dimmer 400 W, 1 module", 800), ("6772 39", "Fan regulator 100 W ISI, 1 module", 734),
    ("6772 40", "Fan regulator 100 W 360 degree ISI, 2 module", 912), ("6772 45", "Fan regulator BLDC, 2 module", 996),
    ("6774 60", "TV co-axial socket, 1 module (Chic Grey)", 278), ("6772 62", "Telephone socket RJ11, 1 module", 260),
    ("6772 65", "RJ45 Cat 6 UTP socket with shutter, 1 module", 963), ("6772 50", "Buzzer 230 V, 1 module", 752),
    ("6772 76", "Blanking plate, 1 module", 58), ("6772 77", "Blanking plate, 2 module", 76),
]
LEGRAND_LYNCUS_PLATES = [("1 module", 184, 234, 238), ("2 module", 184, 234, 238), ("3 module", 234, 328, 328), ("4 module", 274, 348, 356),
                         ("6 module", 332, 428, 452), ("8 module horizontal", 426, 584, 584), ("2 x 4 module vertical", 446, 584, 588),
                         ("9 module", 472, 628, 628), ("12 module", 620, 814, 830), ("16 module", 722, 938, 960), ("18 module", 974, 1280, 1318)]
LEGRAND_MYRIUS = [
    ("6730 00", "6A switch, 1 way, 1 module", 180), ("6730 01", "6A switch, 2 way, 1 module", 326),
    ("6730 08", "16A switch, 1 way, 1 module", 442), ("6730 16", "32A DP switch with indicator, 2 module", 1510),
    ("6730 45", "6/16A socket with shutter, ISI, 2 module", 684), ("6730 50", "TV co-axial socket, 1 module", 332),
    ("6730 55", "RJ45 Cat 6 UTP socket, 1 module", 1055), ("6731 64", "16A SP modular MCB, C curve, 1 module", 732),
    ("6731 65", "20A SP modular MCB, C curve, 1 module", 732), ("6731 30", "16A motor starter, 2 module", 1250),
]
LEGRAND_MYRIUS_PLATES = [("1 module", 306), ("2 module", 332), ("3 module", 350), ("4 module", 376), ("6 module", 676),
                         ("12 module", 1126), ("16 module", 1300), ("18 module", 1498)]

LEGRAND_NOTE_MRP = ("<p class=\"ptable-note\">Prices are Legrand India MRP per unit inclusive of all taxes including GST, "
                    "from the Legrand Corp MPL 2026. Mount Cable India's selling price is below MRP; WhatsApp your list for the rate.</p>")

LEGRAND_PAGE = {
    "slug": "legrand", "name": "Legrand", "kind": "brand", "group": "MCBs & Switchgear",
    "title": "Legrand Price List 2026 (India) — MCB, RCCB, DB, Myrius, Britzy, Lyncus, Allzy MRP | Mount Cable India",
    "h1": "Legrand price list 2026 for India",
    "desc": "Legrand price list 2026 from the Corp MPL: DX3 MCB and RCCB MRP by pole and rating, Ekinox SPN and TPN distribution boards, and Myrius, Britzy, Lyncus and Allzy modular switch and plate prices. Mount Cable India, authorised Legrand stockist in Bangalore.",
    "intro": "This is the Legrand India price list for 2026, taken from the Legrand Corp MPL 2026 and shown as MRP inclusive of GST. It covers the DX3 switchgear range (MCB, RCCB, RCBO, isolators), Ekinox distribution boards and the modular switch ranges Britzy, Allzy, Lyncus and Myrius. Mount Cable India stocks Legrand at Jayanagar and Chickpete in Bangalore and sells below MRP; the exact rate for your list comes on WhatsApp within 60 minutes.",
    "badge": "Legrand Corp MPL 2026 · MRP incl. GST",
    "effective": "Legrand Corp MPL 2026",
    "tables": [
        {"title": "Legrand DX3 MCB price list, C curve, 10 kA (MRP per unit)",
         "cols": ["Rating", "SP", "SPN", "DP", "TP", "TPN", "FP"],
         "rows": _mcb_rows(LEGRAND_MCB_C),
         "note": "<p>Every rating inside a band carries the same MRP: a 6A and a 32A single-pole DX3 are both ₹494. The full table with D curve, 80 to 125 A, DC MCBs and isolators is on the <a href=\"legrand-mcb-price-list.html\">Legrand MCB price list</a>.</p>"},
        {"title": "Legrand DX3 RCCB price list, AC type (MRP per unit)",
         "cols": ["Rating", "DP 30 mA", "DP 100 mA", "DP 300 mA", "FP 30 mA", "FP 100 mA", "FP 300 mA"],
         "rows": [(r[0],) + tuple(rs(x) for x in r[1:]) for r in LEGRAND_RCCB_AC]},
        {"title": "Legrand Ekinox SPN distribution boards (MRP per unit)",
         "cols": ["Ways", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
         "rows": [(r[0], rs(r[2]), rs(r[3]), rs(r[4]), rs(r[5])) for r in LEGRAND_SPN_DB],
         "note": "<p>RCBOs, isolators, TPN and vertical TPN boards, Flexy and Mivan DBs and metal enclosures are on the <a href=\"legrand-switchgear-price-list.html\">Legrand switchgear price list</a>.</p>"},
        {"title": "Legrand modular switch ranges compared (MRP per unit)",
         "cols": ["Item", "Britzy", "Allzy", "Lyncus", "Myrius"],
         "rows": [(d,) + tuple(rs(x) if x else dash() for x in (b, a, l, m)) for d, b, a, l, m in LEGRAND_SWITCH_CMP],
         "note": "<p>Britzy and Allzy are the entry ranges, Lyncus the mid range with metallic plate finishes, and Myrius the premium range. The full mechanism and plate lists for each are on the <a href=\"legrand-switches-price-list.html\">Legrand switches price list</a>.</p>"},
    ],
    "price_note": LEGRAND_NOTE_MRP,
    "note": ("<h2>How Legrand pricing works</h2>"
             "<p>Legrand publishes one MPL for India each year and revises it mid-year when needed. Every item has an MRP printed on the pack, and every dealer sells below that MRP; how far below depends on the range, the quantity and the dealer's own buying. That is why two shops can quote different figures for the same DX3 MCB and both be genuine. What no genuine dealer can do is sell a Legrand RCCB at a third of MRP: at that level the device is either a copy or a returned unit. <a href=\"../blog/how-to-identify-duplicate-legrand-mcb.html\">How to identify a duplicate Legrand MCB</a> covers the checks.</p>"
             "<h2>Which Legrand range for a house in Bangalore</h2>"
             "<p>For a typical 2BHK or 3BHK, a DX3 SPN or DP incomer with a 30 mA RCCB, 6 to 12 single-pole DX3 MCBs in an Ekinox SPN board, and Allzy or Lyncus switches with Lyncus plates for the living areas is the combination we quote most often. Use the <a href=\"../tools/mcb-selector.html\">MCB selector</a> to size each breaker and the <a href=\"../blog/distribution-board-selection-guide-home.html\">DB selection guide</a> for the board. If the budget allows, Myrius plates in the living room and Britzy in the utility areas is a common split.</p>"
             "<h2>Legrand vs Schneider vs Anchor for switchgear</h2>"
             "<p>Legrand and Schneider are the two European brands at the top of the Indian market and are priced close to each other. Anchor by Panasonic's UNO range sits well below on MRP with a 10 kA rating on the same sizes. The <a href=\"../blog/switchgear-brands-comparison-india.html\">switchgear brands comparison</a> sets them side by side, and the <a href=\"anchor-mcb-price-list.html\">Anchor MCB price list</a> gives the UNO figures.</p>"
             + CTA_NOTE),
    "related": [("legrand-mcb-price-list.html", "Legrand MCB price list 2026 (full DX3 table)"),
                ("legrand-switchgear-price-list.html", "Legrand switchgear price list: RCCB, RCBO, DB"),
                ("legrand-switches-price-list.html", "Legrand switches price list: Myrius, Britzy, Lyncus, Allzy"),
                ("schneider-price-list.html", "Schneider price list"),
                ("anchor-mcb-price-list.html", "Anchor UNO MCB price list"),
                ("../blog/how-to-identify-duplicate-legrand-switches.html", "How to identify duplicate Legrand switches")],
    "faqs": [
        ("What is the Legrand MCB price in 2026?",
         "A Legrand DX3 single-pole C-curve MCB from 6A to 32A has an MRP of ₹494 in the Corp MPL 2026; 40A to 63A is ₹1,180. Double pole is ₹1,693 for 6 to 32A, triple pole ₹2,745 and four pole ₹3,729. Dealers sell below MRP."),
        ("What is the Legrand RCCB price?",
         "A Legrand DX3 double-pole 30 mA RCCB is ₹5,478 MRP at 25A, ₹6,360 at 40A and ₹7,818 at 63A. Four-pole 30 mA units are ₹7,870, ₹8,068 and ₹8,976. HPI and Type S versions cost more."),
        ("What is the price of a Legrand 8-way SPN distribution board?",
         "An Ekinox SPN 8-way DB is ₹2,917 MRP in IP30, ₹4,065 with an IP43 metal door and ₹4,963 with an acrylic door. Twelve-way is ₹3,447, ₹4,884 and ₹5,665."),
        ("What is the Legrand Myrius switch price?",
         "A Myrius regular white 6A one-way switch is ₹180 MRP, a 16A one-way ₹442, a 6/16A socket ₹684 and a 4-module white plate ₹376. Britzy and Allzy 6A switches are ₹56 and Lyncus ₹100."),
        ("Is this Legrand price list the MRP or the dealer price?",
         "MRP inclusive of GST from the Legrand Corp MPL 2026. Mount Cable India sells below MRP; send your list on WhatsApp for the exact rate."),
        ("Where can I buy Legrand switchgear in Bangalore?",
         f"Mount Cable India stocks the Legrand DX3, Ekinox and modular switch ranges at Jayanagar and Chickpete with free next-day delivery across Bangalore. WhatsApp {PH} with your DB schedule."),
    ],
}

LEGRAND_MCB_PAGE = {
    "slug": "legrand-mcb", "name": "Legrand MCB", "kind": "sub", "parent": "legrand", "group": "MCBs & Switchgear",
    "title": "Legrand MCB Price List 2026 — DX3 SP, DP, TP, FP by Rating, C and D Curve, Isolators | Mount Cable India",
    "h1": "Legrand MCB price list 2026 (DX3)",
    "desc": "Legrand DX3 MCB price list 2026 with MRP for every pole and rating band: single pole, SPN, double pole, triple pole, TPN and four pole in C curve and D curve, 80 to 125 A breakers, DC MCBs and DX3 isolators. From the Legrand Corp MPL 2026.",
    "intro": "Every Legrand DX3 MCB with its MRP from the Corp MPL 2026. Legrand prices MCBs in rating bands, so a 6A and a 32A of the same pole cost the same, and the jump comes at 40A. Mount Cable India stocks the full DX3 range in Bangalore and sells below MRP.",
    "badge": "Legrand Corp MPL 2026 · MRP incl. GST",
    "effective": "Legrand Corp MPL 2026",
    "tables": [
        {"title": "DX3 MCB, C curve, 10 kA, IS/IEC 60898-1 (MRP per unit)",
         "cols": ["Rating", "Single pole", "SP + N", "Double pole", "Triple pole", "TP + N", "Four pole"],
         "rows": _mcb_rows(LEGRAND_MCB_C),
         "note": "<p>C curve is the standard for house wiring: lighting, sockets, AC and geyser circuits. Ratings available in each band: 0.5, 1, 2, 3, 4 A; 6, 10, 16, 20, 25, 32 A; 40, 50, 63 A.</p>"},
        {"title": "DX3 MCB, D curve, 10 kA (MRP per unit)",
         "cols": ["Rating", "Single pole", "SP + N", "Double pole", "Triple pole", "TP + N", "Four pole"],
         "rows": _mcb_rows(LEGRAND_MCB_D),
         "note": "<p>D curve breakers tolerate the high inrush of motors, pumps and transformers. 40 to 63 A D curve prices are on request.</p>"},
        {"title": "DX3 circuit breakers 80 to 125 A, 10 kA, IEC 60947-2 (MRP per unit)",
         "cols": ["Rating", "Single pole", "SP + N", "Double pole", "Triple pole", "TP + N", "Four pole"],
         "rows": _mcb_rows(LEGRAND_MCB_HI)},
        {"title": "DX3 DC MCBs, 6 kA, up to 63 A (MRP per unit)",
         "cols": ["Rating", "Single pole 250 V", "Double pole 250 V"],
         "rows": [("0.5 to 4 A", rs(1226), rs(2558)), ("6 to 32 A", rs(1015), rs(2372)), ("40 to 63 A", rs(1355), rs(2798))]},
        {"title": "DX3 isolators, up to 125 A (MRP per unit)",
         "cols": ["Rating", "Double pole 240 V", "Triple pole 415 V", "Four pole 415 V"],
         "rows": [(r[0], rs(r[1]), rs(r[2]), rs(r[3])) for r in LEGRAND_ISOLATORS]},
        {"title": "Myrius modular MCB for switch plates (MRP per unit)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [("6731 64", "16A SP modular MCB, C curve, 1 module", rs(732)), ("6731 65", "20A SP modular MCB, C curve, 1 module", rs(732))]},
    ],
    "price_note": LEGRAND_NOTE_MRP,
    "note": ("<h2>Reading the Legrand MCB price list</h2>"
             "<p>Three things decide the price of a DX3 breaker: the number of poles, the rating band and the curve. Poles are the big step, and that is where most house wiring money goes: a single pole for each outgoing circuit and a double pole or SPN for the incomer. The rating band matters only at 40A and above, so specifying a 32A where a 25A would do costs nothing extra, but specifying a 40A doubles the price. Curve is C for almost every residential circuit.</p>"
             "<h2>How many MCBs a house needs</h2>"
             "<p>A 2BHK typically needs one DP incomer, one 30 mA RCCB and 8 to 10 single-pole MCBs; a 3BHK 10 to 14. The <a href=\"../tools/mcb-selector.html\">MCB selector</a> picks the rating for each circuit from its load and wire size, and the <a href=\"../blog/mcb-rccb-rcbo-guide-for-homes.html\">MCB, RCCB and RCBO guide</a> explains which device does what.</p>"
             "<h2>Genuine DX3 vs copies</h2>"
             "<p>Legrand MCBs are copied because the brand carries a premium. A genuine DX3 has the integrated label holder, the biconnect lower terminals and the sliding bottom clamp described in the MPL, and a crisp laser-printed rating label. A soft, unevenly printed label or a breaker that feels light is the first warning. Our guide to <a href=\"../blog/how-to-identify-duplicate-legrand-mcb.html\">identifying a duplicate Legrand MCB</a> goes through it step by step.</p>"
             + CTA_NOTE),
    "related": [("legrand-price-list.html", "Legrand price list 2026 overview"),
                ("legrand-switchgear-price-list.html", "Legrand RCCB, RCBO and DB prices"),
                ("schneider-price-list.html", "Schneider MCB price list"),
                ("anchor-mcb-price-list.html", "Anchor UNO MCB price list"),
                ("../tools/mcb-selector.html", "MCB selector tool")],
    "faqs": [
        ("What is the Legrand DX3 single pole MCB price?",
         "₹494 MRP for 6A to 32A C curve, ₹824 for 0.5A to 4A and ₹1,180 for 40A to 63A, from the Legrand Corp MPL 2026. Mount Cable India sells below MRP."),
        ("What is the Legrand 32A DP MCB price?",
         "A DX3 double-pole 32A C-curve MCB is ₹1,693 MRP. The same price applies from 6A to 32A; 40A to 63A double pole is ₹2,663."),
        ("What is the Legrand 63A TP MCB price?",
         "A DX3 triple-pole 63A C-curve MCB is ₹4,166 MRP; 6A to 32A triple pole is ₹2,745. Four-pole 63A is ₹5,306."),
        ("What is the difference between C curve and D curve Legrand MCBs?",
         "C curve trips at 5 to 10 times rated current and suits lighting, sockets, ACs and geysers. D curve trips at 10 to 20 times and is for motors, pumps and transformers with high starting current. D curve costs more: ₹678 against ₹494 for a 6 to 32A single pole."),
        ("Does Legrand make an MCB that fits a modular switch plate?",
         "Yes, the Myrius modular MCB, 16A or 20A single pole C curve in 1 module, at ₹732 MRP. It is used for AC and geyser points where the breaker sits on the switchboard."),
    ],
}

LEGRAND_SWITCHGEAR_PAGE = {
    "slug": "legrand-switchgear", "name": "Legrand Switchgear", "kind": "sub", "parent": "legrand", "group": "MCBs & Switchgear",
    "title": "Legrand Switchgear Price List 2026 — RCCB, RCBO, Isolator, Ekinox DB, Enclosures MRP | Mount Cable India",
    "h1": "Legrand switchgear price list 2026: RCCB, RCBO and distribution boards",
    "desc": "Legrand switchgear price list 2026 with MRP for DX3 RCCBs (AC, Type S, HPI), RCBOs, isolators, Ekinox SPN, ETPN, vertical TPN, Flexy and Mivan distribution boards and metal enclosures, from the Legrand Corp MPL 2026.",
    "intro": "Legrand's protection and distribution range with MRP from the Corp MPL 2026: earth-leakage devices, combined RCBOs, isolators, and the Ekinox boards they go into. Mount Cable India stocks the DX3 and Ekinox ranges in Bangalore and sells below MRP.",
    "badge": "Legrand Corp MPL 2026 · MRP incl. GST",
    "effective": "Legrand Corp MPL 2026",
    "tables": [
        {"title": "DX3 RCCB, AC type, IS 12640-1 (MRP per unit)",
         "cols": ["Rating", "DP 30 mA", "DP 100 mA", "DP 300 mA", "FP 30 mA", "FP 100 mA", "FP 300 mA"],
         "rows": [(r[0],) + tuple(rs(x) for x in r[1:]) for r in LEGRAND_RCCB_AC],
         "note": "<p>30 mA is the sensitivity for shock protection in a home. 100 mA and 300 mA are for fire protection upstream of other RCDs.</p>"},
        {"title": "DX3 RCCB, Type S (delayed) and HPI (MRP per unit)",
         "cols": ["Rating", "DP Type S 300 mA", "FP Type S 300 mA", "DP HPI 30 mA", "FP HPI 30 mA"],
         "rows": [("25 A", rs(11323), rs(12750), rs(11688), rs(13240)), ("40 A", rs(11888), rs(12914), rs(12271), rs(13657)), ("63 A", rs(12233), rs(13493), rs(12627), rs(14010))],
         "note": "<p>HPI units resist nuisance tripping from inverters, computers and printers and detect faults with a DC component, which is why they are specified for homes with solar inverters.</p>"},
        {"title": "DX3 RCBO, double pole 240 V, AC type (MRP per unit)",
         "cols": ["Rating", "30 mA", "100 mA", "300 mA"],
         "rows": [(r[0], rs(r[1]), rs(r[2]), r[3] if isinstance(r[3], str) else rs(r[3])) for r in LEGRAND_RCBO_DP],
         "note": "<p>Four-pole RCBOs 16 to 32A are ₹9,337 at 30 mA and ₹10,946 at 300 mA; 63A four pole ₹11,242. The compact 2-module DP RCBO, 6 to 32A 6 kA, is ₹8,291 at 30 mA and ₹8,692 at 300 mA.</p>"},
        {"title": "DX3 isolators (MRP per unit)",
         "cols": ["Rating", "Double pole", "Triple pole", "Four pole"],
         "rows": [(r[0], rs(r[1]), rs(r[2]), rs(r[3])) for r in LEGRAND_ISOLATORS]},
        {"title": "Ekinox SPN distribution boards, 100 A busbar (MRP per unit)",
         "cols": ["Ways", "Modules", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
         "rows": [(r[0], str(r[1]), rs(r[2]), rs(r[3]), rs(r[4]), rs(r[5])) for r in LEGRAND_SPN_DB]},
        {"title": "Ekinox ETPN distribution boards (MRP per unit)",
         "cols": ["Ways", "Modules", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
         "rows": [(r[0], r[1], rs(r[2]), rs(r[3]), rs(r[4]), rs(r[5])) for r in LEGRAND_ETPN_DB]},
        {"title": "Ekinox vertical TPN boards, 100 A copper busbar per phase (MRP per unit)",
         "cols": ["Ways", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
         "rows": [(r[0], rs(r[1]), rs(r[2]), rs(r[3]), rs(r[4])) for r in LEGRAND_VTPN_DB]},
        {"title": "Ekinox Flexy DB (MRP per unit)",
         "cols": ["Size", "Modules", "IP30", "IP43 metal door", "IP43 acrylic door"],
         "rows": [(r[0], str(r[1]), rs(r[2]), rs(r[3]), rs(r[4])) for r in LEGRAND_FLEXY]},
        {"title": "Ekinox Mivan SPN DB, IP43 metal door (MRP per unit)",
         "cols": ["Ways", "MRP"],
         "rows": [(r[0], rs(r[1])) for r in LEGRAND_MIVAN],
         "note": "<p>Mivan boards are built with thicker sheet for aluminium-formwork construction; ETPN Mivan boards are ₹8,319 (4 way) to ₹20,203 (12 way).</p>"},
        {"title": "Ekinox metal enclosures for a single device (MRP per unit)",
         "cols": ["Enclosure", "MRP"],
         "rows": [(r[0], rs(r[1])) for r in LEGRAND_ENCL]},
    ],
    "price_note": LEGRAND_NOTE_MRP,
    "note": ("<h2>RCCB or RCBO</h2>"
             "<p>An RCCB protects a whole board against earth leakage and shock; it does not protect against overload, which the MCBs downstream do. An RCBO combines both in one device for one circuit, and is specified where a single leaky circuit should trip alone rather than darken the house. For most Bangalore homes one 30 mA DP RCCB as incomer plus MCBs per circuit is the standard, with an RCBO on the geyser or the outdoor circuit if the budget allows. The <a href=\"../blog/mcb-rccb-rcbo-guide-for-homes.html\">MCB, RCCB and RCBO guide</a> has the reasoning.</p>"
             "<h2>Choosing the Ekinox board</h2>"
             "<p>Count the outgoing circuits, add two spare ways, and that is the SPN size. IP43 with a metal door is the normal indoor specification; acrylic doors are chosen for looks in a living area; IP54 is for damp or dusty locations such as a basement or a terrace pump room. A three-phase connection needs an ETPN or vertical TPN board instead. See the <a href=\"../blog/distribution-board-selection-guide-home.html\">distribution board selection guide</a>.</p>"
             + CTA_NOTE),
    "related": [("legrand-price-list.html", "Legrand price list 2026 overview"),
                ("legrand-mcb-price-list.html", "Legrand MCB price list"),
                ("../blog/distribution-board-selection-guide-home.html", "How to choose a distribution board"),
                ("../switchgear-and-mcb.html", "Switchgear and MCB range")],
    "faqs": [
        ("What is the Legrand 40A RCCB price?",
         "A DX3 double-pole 40A 30 mA AC-type RCCB is ₹6,360 MRP; the four-pole 40A 30 mA is ₹8,068. HPI 40A units are ₹12,271 (DP) and ₹13,657 (FP)."),
        ("What is the Legrand RCBO price?",
         "A DX3 double-pole 30 mA RCBO is ₹6,974 MRP from 6A to 32A, ₹8,380 at 40A and ₹10,210 at 63A. The compact 2-module DP RCBO 6 to 32A is ₹8,291."),
        ("What is the Legrand 12-way SPN DB price?",
         "An Ekinox 12-way SPN DB is ₹3,447 MRP in IP30, ₹4,884 with an IP43 metal door, ₹5,665 with an acrylic door and ₹15,042 in IP54."),
        ("What is the price of a Legrand TPN distribution board?",
         "Ekinox ETPN boards start at ₹7,051 for 4 way IP30 and ₹8,289 with an IP43 metal door. Vertical TPN boards with a 100 A busbar per phase are ₹18,920 (4 way IP30) to ₹34,002 (12 way IP43 metal door)."),
        ("What is the difference between AC type, Type S and HPI RCCBs?",
         "AC type senses standard alternating leakage and is the residential default. Type S has a delayed trip so it coordinates with downstream RCDs. HPI has high immunity to nuisance tripping and detects DC-component faults from inverters and electronics."),
    ],
}

LEGRAND_SWITCHES_PAGE = {
    "slug": "legrand-switches", "name": "Legrand Switches", "kind": "sub", "parent": "legrand", "group": "Switches & Sockets",
    "title": "Legrand Switches Price List 2026 — Myrius, Britzy, Lyncus, Allzy Mechanisms and Plates MRP | Mount Cable India",
    "h1": "Legrand switches price list 2026: Myrius, Britzy, Lyncus and Allzy",
    "desc": "Legrand modular switch price list 2026 with MRP for Britzy, Allzy, Lyncus and Myrius switches, sockets, fan regulators, data sockets, cover plates and flush boxes, from the Legrand Corp MPL 2026.",
    "intro": "MRP for the four Legrand modular switch ranges most homes in Bangalore choose between, from the Corp MPL 2026: Britzy and Allzy at the entry level, Lyncus in the middle, Myrius at the top. Mechanisms and plates are priced separately in every Legrand range, so a switchboard price is the sum of its modules plus the plate.",
    "badge": "Legrand Corp MPL 2026 · MRP incl. GST",
    "effective": "Legrand Corp MPL 2026",
    "tables": [
        {"title": "The four ranges side by side (MRP per unit)",
         "cols": ["Item", "Britzy", "Allzy white", "Lyncus classic white", "Myrius regular white"],
         "rows": [(d,) + tuple(rs(x) if x else dash() for x in (b, a, l, m)) for d, b, a, l, m in LEGRAND_SWITCH_CMP]},
        {"title": "Legrand Britzy white mechanisms (MRP per unit)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in LEGRAND_BRITZY]},
        {"title": "Britzy white cover plates with support frame (MRP per unit)",
         "cols": ["Plate", "MRP"],
         "rows": [(a, rs(b)) for a, b in LEGRAND_BRITZY_PLATES]},
        {"title": "Legrand Allzy white mechanisms (MRP per unit)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in LEGRAND_ALLZY],
         "note": "<p>Allzy plates come in white, rose gold, gold, matt black and aluminium champagne. Matt black mechanisms (6812 series) run about 15 to 20 percent above white.</p>"},
        {"title": "Legrand Lyncus classic white mechanisms (MRP per unit)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in LEGRAND_LYNCUS]},
        {"title": "Lyncus cover plates with support frame (MRP per unit)",
         "cols": ["Plate", "Classic white", "Chic grey", "Alu sunset / champagne"],
         "rows": [(a, rs(b), rs(c), rs(d)) for a, b, c, d in LEGRAND_LYNCUS_PLATES],
         "note": "<p>Brushed silver plates are ₹242 (1 and 2 module) to ₹1,344 (18 module).</p>"},
        {"title": "Legrand Myrius regular white mechanisms (MRP per unit)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in LEGRAND_MYRIUS]},
        {"title": "Myrius regular white cover plates (MRP per unit)",
         "cols": ["Plate", "MRP"],
         "rows": [(a, rs(b)) for a, b in LEGRAND_MYRIUS_PLATES],
         "note": "<p>Myrius plates are also made in charcoal grey, ice white, ice black, pearl champagne, sonic silver and 3 mm toughened glass at higher MRPs.</p>"},
        {"title": "Legrand metal flush boxes, for all ranges (MRP per unit)",
         "cols": ["Box", "MRP"],
         "rows": [(a, rs(b)) for a, b in LEGRAND_BOXES]},
    ],
    "price_note": LEGRAND_NOTE_MRP,
    "note": ("<h2>How to price a Legrand switchboard</h2>"
             "<p>Add the mechanisms, then the plate, then the box. A typical bedroom board of two 6A switches, one fan regulator and one 6/16A socket in Lyncus is two at ₹100, one at ₹734 and one at ₹434 for the mechanisms, a 6-module classic white plate at ₹332 and a 6-module box at ₹226: ₹1,926 MRP for the board, before the dealer discount. The same board in Britzy is about ₹1,600 and in Myrius about ₹2,900. Multiply by the number of boards from the <a href=\"../tools/material-list-builder.html\">material list builder</a> and you have the switch budget for the house.</p>"
             "<h2>Which Legrand range to choose</h2>"
             "<p>Britzy and Allzy give you the Legrand mechanism at the lowest cost and are the right choice for rental flats, utility areas and budget builds. Lyncus adds a wider colour palette of plates, BLDC fan regulators and USB-C chargers at a moderate premium. Myrius is the range specified in premium apartments, with glass and metallic plates and the widest set of hospitality and automation modules. The <a href=\"../blog/best-modular-switch-brands-india-2026.html\">modular switch brands guide</a> compares Legrand with Anchor, Schneider and Greatwhite.</p>"
             + CTA_NOTE),
    "related": [("legrand-price-list.html", "Legrand price list 2026 overview"),
                ("anchor-panasonic-price-list.html", "Anchor Panasonic switch price list"),
                ("../blog/modular-switch-buying-guide-bangalore.html", "Modular switch buying guide"),
                ("../blog/how-to-identify-duplicate-legrand-switches.html", "Spotting duplicate Legrand switches")],
    "faqs": [
        ("What is the Legrand Myrius switch price?",
         "Myrius regular white: 6A one-way switch ₹180 MRP, 6A two-way ₹326, 16A one-way ₹442, 32A DP with indicator ₹1,510, 6/16A socket ₹684. Plates run from ₹306 for 1 module to ₹1,498 for 18 modules."),
        ("What is the Legrand Britzy switch price?",
         "Britzy: 6A one-way switch ₹56 MRP, 6A two-way ₹132, 16A one-way ₹190, 32A DP ₹382, 6/16A socket ₹294. White plates are ₹132 for 1 and 2 module up to ₹622 for 18 module."),
        ("What is the Legrand Lyncus switch price?",
         "Lyncus classic white: 6A one-way switch ₹100 MRP, 6A two-way ₹212, 16A one-way ₹246, 32A DP ₹718, 6/16A socket ₹434. Classic white plates are ₹184 (1 and 2 module) to ₹974 (18 module)."),
        ("What is the Legrand Allzy switch price?",
         "Allzy white: 6A one-way switch ₹56 MRP, 10A one-way ₹60, 16A one-way ₹152, 32A DP ₹392, 6/16A socket ₹284, BLDC fan regulator ₹938."),
        ("Are Legrand switch plates priced separately from the switches?",
         "Yes. Every Legrand range prices the mechanism, the cover plate with support frame and the flush box separately. A switchboard costs the sum of its modules plus the plate and box."),
    ],
}

# =====================================================================
# ANCHOR by Panasonic — April 2026 pricelist, MRP per piece
# =====================================================================
ANCHOR_NOTE = ("<p class=\"ptable-note\">Prices are Anchor by Panasonic MRP per piece inclusive of all taxes, from the "
               "Panasonic Power for Every Home pricelist, April 2026. Mount Cable India's selling price is below MRP.</p>")

ANCHOR_ROMA_URBAN = [
    ("66101", "10AX one-way switch, 1 module", 160), ("66111", "10AX one-way switch with indicator, 1 module", 242),
    ("66102", "10AX two-way switch, 1 module", 243), ("66201", "10AX one-way switch, 2 module", 251),
    ("66103", "10A bell push, 1 module", 243), ("66104", "20A one-way switch, 1 module", 272),
    ("66144", "20A one-way switch with indicator, 1 module", 329), ("66105", "20A two-way switch, 1 module", 304),
    ("66325", "25A SP switch with indicator, 1 module", 400), ("66332", "32A DP switch with indicator, 2 module", 510),
    ("66025", "25A motor starter switch, 2 module", 760), ("66402", "6A 3-pin socket with shutter, 2 module", 248),
    ("66404", "16A 3-pin socket with shutter, 2 module", 411), ("66455", "6/16A twin socket, 2 module", 504),
    ("66406", "6/16A twin socket, 3 module", 512), ("66501", "100 W step fan regulator, 1 module", 785),
    ("66503", "100 W step fan regulator ISI, 2 module", 1070), ("66508", "100 W 7-step fan regulator, 2 module", 1052),
    ("66505", "450 W dimmer, 1 module", 724), ("66507", "150 W LED dimmer, 2 module", 2306),
    ("66551", "RJ11 telephone jack with shutter, 1 module", 255), ("66557", "RJ45 Cat 6 computer socket, 1 module", 1055),
    ("66602", "TV socket outlet, 1 module", 260), ("66604", "Blank plate, 1 module", 64),
    ("66715", "USB-A charger 2.1A, 1 module", 1916), ("66717", "18 W USB-C PD charger, 1 module", 2243),
]
ANCHOR_ROMA_URBAN_PLATES = [("1 module", 226, 246), ("2 module", 226, 246), ("3 module", 290, 306), ("4 module", 343, 356),
                            ("6 module", 470, 498), ("8 module horizontal", 602, 643), ("8 module square", 602, 643),
                            ("9 module horizontal", 744, 791), ("12 module", 810, 868), ("16 module", 833, 890), ("18 module", 866, 921)]
ANCHOR_ROMA_CLASSIC = [
    ("21011", "10AX one-way switch", 77), ("21022", "10AX two-way switch", 186), ("21033", "10AX one-way switch with neon", 191),
    ("21044", "10A bell push", 193), ("21055", "10A bell push with neon", 206), ("21510", "Dura 10AX one-way switch", 196),
    ("21066", "20A one-way switch", 206), ("21088", "20A two-way switch", 235), ("21077", "20A one-way switch with neon", 245),
    ("22014", "25A SP one-way switch with neon", 314), ("21984", "32A DP one-way switch with neon", 406),
    ("20405", "25A motor starter switch", 587), ("21102", "6A 3-pin socket", 179), ("21124", "16A 3-pin socket", 292),
    ("30828", "6/16A twin socket", 319), ("22546", "Fan step regulator Tiny 100 W", 441), ("21496", "Fan step regulator Dura 100 W", 616),
    ("20507", "100 W fan regulator, 2 module, ISI", 677), ("22037", "7-step fan regulator, 2 module", 616),
    ("20799", "Dimmer Tiny 450 W", 545), ("30046", "150 W LED dimmer, 2 module", 1848), ("21157", "TV socket outlet", 204),
    ("20857", "RJ11 telephone jack with shutter", 204), ("35763", "RJ45 Cat 6 computer socket", 842),
    ("21598", "Blank plate single", 45), ("20462", "USB-A charger 2.1A, 1 module", 1480),
]
ANCHOR_PENTA_MOD = [
    ("65001", "6AX one-way switch, 1 module", 46), ("65002", "6AX two-way switch, 1 module", 106), ("65003", "6A bell push, 1 module", 111),
    ("65007", "16AX one-way switch, 1 module", 131), ("65008", "16AX two-way switch, 1 module", 172), ("65077", "16AX one-way switch with neon, 1 module", 144),
    ("65025", "25A SP one-way switch with neon, 1 module", 188), ("65032", "32A DP one-way switch with neon, 2 module", 263),
    ("65203", "6A 3-pin socket with shutter, 2 module", 149), ("65204", "16A 3-pin socket, 2 module", 237), ("65205", "6/16A twin socket, 2 module", 224),
    ("65503", "Blank plate, 1 module", 34), ("65504", "Neon indicator red, 1 module", 120), ("65710", "Buzzer, 2 module", 238),
    ("65125", "25A motor starter switch, 2 module", 510), ("65502", "TV socket outlet, 1 module", 143), ("65610", "RJ11 telephone jack with shutter, 1 module", 150),
    ("65611", "USB-A charger 2.1A, 1 module", 1373), ("65612", "18 W USB-C PD charger, 1 module", 1608),
    ("65171", "Zen 10AX one-way switch, 1 module", 61), ("65172", "Zen 10AX two-way switch, 1 module", 122), ("65173", "Zen 16AX one-way switch, 1 module", 151),
    ("65179", "Zen 32A DP switch with indicator, 2 module", 294), ("65141", "Flat 6AX one-way switch, 1 module", 81), ("65147", "Flat 16AX one-way switch, 1 module", 172),
]
ANCHOR_PENTA_PLATES = [("1 module", 108, 140), ("2 module", 108, 140), ("3 module", 152, 193), ("4 module", 168, 212), ("6 module", 244, 310),
                       ("8 module horizontal", 320, 408), ("8 module vertical", 320, 408), ("12 module", 383, 492), ("16 module", 407, 520), ("18 module", 429, 552)]
ANCHOR_PENTA_PIANO = [
    ("14125", "Penta Deluxe 6A one-way switch", 27), ("14112", "Penta Deluxe 6A two-way switch", 53), ("14113", "Penta Deluxe 6A bell push", 53),
    ("14126", "Penta Cherry 6A one-way switch", 28), ("14302", "6A 3-pin socket", 52), ("14401", "20A one-way switch", 140),
    ("14402", "20A two-way switch", 184), ("14404", "32A DP switch with neon", 297), ("14307", "6/16A universal socket", 156),
    ("52660", "25A motor starter SP", 511), ("14501", "100 W mini fan regulator, rotary step", 355), ("14502", "100 W deluxe fan regulator", 396),
    ("14503", "450 W mini dimmer", 341), ("14617", "6/16A Capton 5-in-1 combined unit", 336), ("14606", "TV outlet mini", 81),
    ("14602", "Mini telephone jack with shutter", 128), ("14601", "Neon indicator", 79), ("14609", "10A and 16A kit-kat fuse, flush", 94),
]
ANCHOR_UNO_MCB = [
    ("6 to 32 A", 308, 990, 1084, 1573, 2013, 2222), ("40 A", 732, 1551, 1628, 2503, 2926, 3075), ("63 A", 825, 1777, 1887, 2668, 3058, 3218),
]
ANCHOR_UNO_ISO = [("32 A", 620, None, None), ("40 A", 630, 925, 1386), ("63 A", 810, 1140, 1782), ("100 A", 1035, 1540, 2277), ("125 A", 1050, 1550, 2310)]
ANCHOR_UNO_RCCB = [("25 A", 3581, 3494, 3494, 4744, 4564, 4564), ("40 A", 3568, 3581, 3581, 4719, 4575, 4575), ("63 A", 5115, 5028, 5028, 5186, 5104, 5104),
                   ("80 A", 7703, 7703, 7703, 8347, 8347, 8347), ("100 A", 7839, 7839, 7839, 8554, 8554, 8554)]
ANCHOR_UNO_RCBO = [("6, 10, 20 A", 5700, 7132, 7132), ("16, 25 A", 5763, 6895, 7167), ("32 A", 6023, 6895, 7167), ("40 A", 6930, 7889, 8097), ("63 A", 8478, 9125, 9136)]
ANCHOR_UNO_COS = [("25 A", 1310, 2655), ("32 A", 1650, 3285), ("40 A", 1980, 4015), ("63 A", 2525, 4845)]
ANCHOR_UNO_DB = [("4 way", 1892, 5014, None, None), ("6 way", 2247, 6296, 2661, 8151), ("8 way", 2475, 8162, 2968, 10579),
                 ("12 way", 3069, 12132, 3673, None), ("16 way", 4123, None, 4918, None)]
ANCHOR_UNO_VTPN = [("4 way", 13324, 7431, 7839, 11013), ("6 way", 15068, 10907, 9328, 13404), ("8 way", 16817, 14231, 11284, 17527), ("12 way", 21825, 17660, None, 19366)]
ANCHOR_MINI_MCB = [("Roma Classic, Rider, Regent (white)", 365, 790), ("Roma Classic, Rider, Regent (matt black)", 395, 860),
                   ("Roma Urban (white)", 385, None), ("Roma Urban (black)", 420, None), ("Penta Modular (white)", 365, None), ("Ziva (white)", 365, None), ("Tiona (white)", 365, None), ("Roma Plus (white)", 365, None)]
ANCHOR_6KA = [("6 to 32 A", 240, 815, 885)]

ANCHOR_PAGE = {
    "slug": "anchor-panasonic", "name": "Anchor by Panasonic", "kind": "brand", "group": "Switches & Sockets",
    "title": "Anchor Panasonic Price List 2026 — Roma Urban, Roma Classic, Penta Switches, Plates, UNO MCB MRP | Mount Cable India",
    "h1": "Anchor Panasonic price list 2026",
    "desc": "Anchor by Panasonic price list 2026 (April 2026 pricelist): Roma Urban, Roma Classic, Penta Modular and Penta piano switch MRP, cover plates, sockets, fan regulators, USB chargers and a summary of UNO MCB and RCCB prices. Mount Cable India, authorised Anchor dealer, Bangalore.",
    "intro": "The Anchor by Panasonic price list for 2026, from the Panasonic Power for Every Home pricelist dated April 2026, shown as MRP per piece. It covers the switch ranges most Bangalore homes ask for, Roma Urban, Roma Classic, Penta Modular and the Penta piano range, along with plates and a summary of the UNO switchgear. Mount Cable India is an authorised Anchor dealer and sells below MRP.",
    "badge": "Panasonic pricelist April 2026 · MRP per piece",
    "effective": "Anchor pricelist April 2026",
    "tables": [
        {"title": "Anchor Roma Urban switches and modules (MRP per piece)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in ANCHOR_ROMA_URBAN]},
        {"title": "Roma Urban cover plates with base frame (MRP per piece)",
         "cols": ["Plate", "White", "Black, graphite black or silver"],
         "rows": [(a, rs(b), rs(c)) for a, b, c in ANCHOR_ROMA_URBAN_PLATES]},
        {"title": "Anchor Roma Classic switches and modules (MRP per piece)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in ANCHOR_ROMA_CLASSIC],
         "note": "<p>Roma Classic is the most widely fitted modular switch in India and the most copied. Check the ISI mark, the moulding and the packaging against our guide to <a href=\"../blog/how-to-identify-duplicate-anchor-switches.html\">identifying duplicate Anchor switches</a>.</p>"},
        {"title": "Anchor Penta Modular switches and modules (MRP per piece)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in ANCHOR_PENTA_MOD]},
        {"title": "Penta Modular regular plates (MRP per piece)",
         "cols": ["Plate", "White", "Black"],
         "rows": [(a, rs(b), rs(c)) for a, b, c in ANCHOR_PENTA_PLATES]},
        {"title": "Anchor Penta piano switches (non-modular) (MRP per piece)",
         "cols": ["Cat. no.", "Description", "MRP"],
         "rows": [(c, d, rs(p)) for c, d, p in ANCHOR_PENTA_PIANO],
         "note": "<p>Penta is the non-modular piano range for wooden boards, rentals and utility areas. Prices are for white; ivory and dark brown are listed at the same MRP.</p>"},
        {"title": "Anchor UNO 10 kA MCB, C curve (MRP per piece)",
         "cols": ["Rating", "SP", "SPN", "DP", "TP", "TPN", "FP"],
         "rows": [(r[0],) + tuple(rs(x) for x in r[1:]) for r in ANCHOR_UNO_MCB],
         "note": "<p>The full UNO switchgear list with RCCBs, RCBOs, isolators, changeovers, mini modular MCBs and distribution boards is on the <a href=\"anchor-mcb-price-list.html\">Anchor MCB price list</a>.</p>"},
    ],
    "price_note": ANCHOR_NOTE,
    "note": ("<h2>Which Anchor range to choose</h2>"
             "<p>Roma Classic is the value modular range: a 10AX switch at ₹77 MRP, familiar to every electrician in Bangalore, with the widest spares availability. Roma Urban is the current design range with the curved plate and 1-module and 2-module switch options at about double the price. Penta Modular sits below Roma Classic in price and above the piano Penta range, which is for wooden boards and budget builds. For a new house we usually quote Roma Urban in the living areas and Roma Classic or Penta Modular elsewhere. The <a href=\"../blog/which-switch-brand-should-you-buy.html\">switch brand guide</a> and <a href=\"../blog/greatwhite-vs-anchor-switches.html\">Greatwhite vs Anchor</a> compare it with the other brands we stock.</p>"
             "<h2>Anchor plates and the module system</h2>"
             "<p>Anchor prices the switch module and the cover plate separately. A 6-module Roma Urban board with three 10AX switches, a fan regulator and a 6/16A socket is three at ₹160, one at ₹785 and one at ₹504 plus a ₹470 plate: ₹2,239 MRP. The same in Roma Classic with a Tresa or Deko plate comes to about ₹1,500. Count your boards with the <a href=\"../tools/material-list-builder.html\">material list builder</a>.</p>"
             + CTA_NOTE),
    "related": [("anchor-mcb-price-list.html", "Anchor UNO MCB, RCCB and DB price list"),
                ("legrand-switches-price-list.html", "Legrand switches price list"),
                ("greatwhite-price-list.html", "Greatwhite price list"),
                ("../blog/greatwhite-vs-anchor-switches.html", "Greatwhite vs Anchor switches"),
                ("../blog/how-to-identify-duplicate-anchor-switches.html", "How to identify duplicate Anchor switches")],
    "faqs": [
        ("What is the Anchor Roma switch price in 2026?",
         "Roma Classic 10AX one-way switch ₹77 MRP, two-way ₹186, 16A socket ₹292, fan regulator ₹441 to ₹677. Roma Urban 10AX one-way ₹160, two-way ₹243, 6/16A twin socket ₹504, fan regulator ₹785 to ₹1,070."),
        ("What is the Anchor Penta switch price?",
         "Penta Modular 6AX one-way ₹46 MRP, 16AX one-way ₹131, 6/16A twin socket ₹224. The non-modular Penta Deluxe 6A one-way switch is ₹27 and the 6A socket ₹52."),
        ("What is the Anchor Roma Urban plate price?",
         "Roma Urban white cover plates: ₹226 for 1 and 2 module, ₹343 for 4 module, ₹470 for 6 module, ₹602 for 8 module, ₹810 for 12 module and ₹866 for 18 module. Black, graphite black and silver are about 8 percent more."),
        ("What is the Anchor MCB price?",
         "Anchor UNO 10 kA single-pole MCB 6 to 32A ₹308 MRP, 40A ₹732, 63A ₹825. Double pole 6 to 32A ₹1,084, triple pole ₹1,573, four pole ₹2,222. The 6 kA single pole is ₹240."),
        ("Is this the Anchor MRP or the selling price?",
         "MRP per piece inclusive of taxes from the April 2026 Panasonic pricelist. Mount Cable India sells below MRP; WhatsApp your list for the rate."),
        ("Where can I buy Anchor Panasonic switches in Bangalore?",
         f"Mount Cable India is an authorised Anchor dealer with showrooms at Jayanagar and Chickpete and free next-day delivery across Bangalore. WhatsApp {PH}."),
    ],
}

ANCHOR_MCB_PAGE = {
    "slug": "anchor-mcb", "name": "Anchor MCB", "kind": "sub", "parent": "anchor-panasonic", "group": "MCBs & Switchgear",
    "title": "Anchor MCB Price List 2026 — UNO MCB, RCCB, RCBO, Isolator, Distribution Board MRP | Mount Cable India",
    "h1": "Anchor MCB price list 2026 (UNO switchgear)",
    "desc": "Anchor by Panasonic UNO switchgear price list 2026: 10 kA and 6 kA MCB MRP by pole and rating, RCCB, RCBO, isolators, changeover switches, mini modular MCBs for switch plates and SPN/TPN distribution boards, from the April 2026 pricelist.",
    "intro": "Every Anchor UNO protection device with its MRP from the April 2026 Panasonic pricelist. UNO is the value switchgear range we quote against Legrand and Schneider for budget-conscious homes: the same 10 kA rating on MCBs at roughly two-thirds of the European MRP.",
    "badge": "Panasonic pricelist April 2026 · MRP per piece",
    "effective": "Anchor pricelist April 2026",
    "tables": [
        {"title": "Anchor UNO 10 kA MCB, C curve (MRP per piece)",
         "cols": ["Rating", "SP", "SPN", "DP", "TP", "TPN", "FP"],
         "rows": [(r[0],) + tuple(rs(x) for x in r[1:]) for r in ANCHOR_UNO_MCB],
         "note": "<p>B-curve single-pole 6 to 32A is also ₹308. Ratings inside the 6 to 32A band: 6, 10, 16, 20, 25, 32A.</p>"},
        {"title": "Anchor UNO 6 kA MCB, C curve (MRP per piece)",
         "cols": ["Rating", "SP", "SPN", "DP"],
         "rows": [(r[0], rs(r[1]), rs(r[2]), rs(r[3])) for r in ANCHOR_6KA]},
        {"title": "Anchor UNO RCCB (MRP per piece)",
         "cols": ["Rating", "DP 30 mA", "DP 100 mA", "DP 300 mA", "FP 30 mA", "FP 100 mA", "FP 300 mA"],
         "rows": [(r[0],) + tuple(rs(x) for x in r[1:]) for r in ANCHOR_UNO_RCCB]},
        {"title": "Anchor UNO SPN RCBO (MRP per piece)",
         "cols": ["Rating", "30 mA", "100 mA", "300 mA"],
         "rows": [(r[0], rs(r[1]), rs(r[2]), rs(r[3])) for r in ANCHOR_UNO_RCBO],
         "note": "<p>TPN RCBOs are ₹8,085 (6 to 25A, 30 mA) to ₹10,083 (63A, 300 mA).</p>"},
        {"title": "Anchor UNO isolators (MRP per piece)",
         "cols": ["Rating", "DP", "TP", "FP"],
         "rows": [(r[0], rs(r[1]), rs(r[2]) if r[2] else dash(), rs(r[3]) if r[3] else dash()) for r in ANCHOR_UNO_ISO]},
        {"title": "Anchor UNO changeover switches (MRP per piece)",
         "cols": ["Rating", "DP", "FP"],
         "rows": [(r[0], rs(r[1]), rs(r[2])) for r in ANCHOR_UNO_COS]},
        {"title": "Anchor mini modular MCBs for switch plates, 6 to 32A (MRP per piece)",
         "cols": ["Switch range", "SP", "DP"],
         "rows": [(a, rs(b), rs(c) if c else dash()) for a, b, c in ANCHOR_MINI_MCB],
         "note": "<p>These fit inside the modular switch plate for AC and geyser points; the mini MCB is chosen to match the switch range.</p>"},
        {"title": "Anchor UNO distribution boards, double door (MRP per piece)",
         "cols": ["Ways", "SPN metal", "TPN metal", "SPN acrylic", "TPN acrylic"],
         "rows": [(r[0],) + tuple(rs(x) if x else dash() for x in r[1:]) for r in ANCHOR_UNO_DB],
         "note": "<p>Ornet Plus DBs are ₹1,903 (6 way) to ₹2,486 (12 way). SPN single-door DBs start at ₹1,034 (4 way) and transparent-door SPN at ₹1,235 (4 way) to ₹2,396 (16 way).</p>"},
        {"title": "Anchor UNO TPN vertical and per-phase-isolation boards (MRP per piece)",
         "cols": ["Ways", "TPN vertical", "Vertical PPI (4 tier)", "Horizontal PPI", "Eight segment"],
         "rows": [(r[0],) + tuple(rs(x) if x else dash() for x in r[1:]) for r in ANCHOR_UNO_VTPN]},
    ],
    "price_note": ANCHOR_NOTE,
    "note": ("<h2>Anchor UNO against Legrand and Schneider</h2>"
             "<p>On MRP, a UNO 10 kA single-pole MCB at ₹308 is about 60 percent of a Legrand DX3 at ₹494, and the UNO 40A DP 30 mA RCCB at ₹3,568 is well under the DX3's ₹6,360. Both carry the ISI mark and the same 10 kA breaking capacity. The difference is in the build, the terminal design and the accessories range. For a rental flat or a budget home the UNO is a sound choice; for a premium build most buyers stay with the European brands. The <a href=\"legrand-mcb-price-list.html\">Legrand MCB price list</a> and <a href=\"../blog/switchgear-brands-comparison-india.html\">switchgear comparison</a> give the full picture.</p>"
             "<h2>Sizing the board</h2>"
             "<p>Use the <a href=\"../tools/mcb-selector.html\">MCB selector</a> for each circuit and the <a href=\"../tools/load-calculator.html\">load calculator</a> for the incomer, then add two spare ways. An 8-way SPN metal DB at ₹2,475 MRP covers a typical 2BHK; a 12-way at ₹3,069 a 3BHK.</p>"
             + CTA_NOTE),
    "related": [("anchor-panasonic-price-list.html", "Anchor switch price list"),
                ("legrand-mcb-price-list.html", "Legrand MCB price list"),
                ("../blog/mcb-rccb-rcbo-guide-for-homes.html", "MCB, RCCB and RCBO guide for homes"),
                ("../tools/mcb-selector.html", "MCB selector")],
    "faqs": [
        ("What is the Anchor UNO MCB price?",
         "Single pole 6 to 32A ₹308 MRP, 40A ₹732, 63A ₹825. SPN ₹990, DP ₹1,084, TP ₹1,573, TPN ₹2,013, FP ₹2,222 for 6 to 32A. The 6 kA single pole is ₹240."),
        ("What is the Anchor RCCB price?",
         "UNO DP 30 mA RCCB ₹3,581 at 25A, ₹3,568 at 40A and ₹5,115 at 63A; FP 30 mA ₹4,744, ₹4,719 and ₹5,186. Higher-rating 80A and 100A DP units are ₹7,703 and ₹7,839."),
        ("What is the Anchor 32A DP MCB price?",
         "₹1,084 MRP for the UNO 10 kA double-pole 32A C-curve MCB. The mini modular 32A DP that fits inside a Roma switch plate is ₹790."),
        ("What is the Anchor DB price?",
         "UNO SPN metal double-door DBs: ₹1,892 (4 way), ₹2,247 (6 way), ₹2,475 (8 way), ₹3,069 (12 way), ₹4,123 (16 way). TPN metal: ₹5,014 (4 way) to ₹12,132 (12 way)."),
        ("Is Anchor UNO switchgear as safe as Legrand?",
         "Both are ISI-marked 10 kA MCBs to IS/IEC 60898-1 and both trip on the same overload and short-circuit curves. Legrand offers more refined terminals, accessories and a wider range. For residential use either protects the circuit correctly when correctly sized."),
    ],
}

# =====================================================================
# POLYCAB — Shree NM Electricals distributor lists, ex-GST
# =====================================================================
POLYCAB_NOTE = ("<p class=\"ptable-note\">Prices are Polycab list prices from the Shree NM Electricals (Polycab distributor) "
                "price lists: house-wire coils wef 8 June 2026, flexible cable list no. 04 wef 15 August 2026, armoured cable wef "
                "18 August 2026, telecom and co-axial wef 25 May 2026. Rates exclusive of GST. Mount Cable India's selling price is "
                "below list; WhatsApp your requirement for the rate.</p>")
POLYCAB_90M = [("0.75 sq mm", "7 A", 2155, 2300, 2130, 2000), ("1.0 sq mm", "12 A", 2890, 3100, 2705, 2590), ("1.5 sq mm", "16 A", 4225, 4525, 3975, 3820),
               ("2.5 sq mm", "22 A", 6680, 7100, 6335, 6095), ("4.0 sq mm", "29 A", 9775, 10360, 9715, 9115), ("6.0 sq mm", "37 A", 14610, 15550, 14570, 14015)]
POLYCAB_LONG = [("0.75 sq mm", "300 m", 9555, 9735, 10680), ("1.0 sq mm", "300 m", 12265, 12490, 13420), ("1.5 sq mm", "300 m", 17970, 18325, 19535),
                ("2.5 sq mm", "300 m", 29830, 30330, 32460), ("4.0 sq mm", "200 m", 31010, 31410, 33360), ("6.0 sq mm", "200 m", 46425, 47000, 49920),
                ("10 sq mm", "200 m", 79885, 80815, 85795), ("16 sq mm", "200 m", 125685, 126935, 135020)]
POLYCAB_FLEX = [("0.5 sq mm", "5 A", 20.90, 54.05, 75.80, 98.45), ("0.75 sq mm", "8 A", 30.20, 76.95, 106.10, 139.00), ("1.0 sq mm", "13 A", 38.75, 96.15, 137.10, 179.00),
                ("1.5 sq mm", "17 A", 56.10, 134.60, 192.25, 254.50), ("2.5 sq mm", "24 A", 93.45, 216.25, 305.50, 414.00), ("4.0 sq mm", "30 A", 148.00, 326.00, 476.00, 625.00),
                ("6.0 sq mm", "38 A", 221.00, 483.50, 705.00, 932.00), ("10 sq mm", "52 A", 378.00, 828.00, 1217.00, 1604.00)]
POLYCAB_FRLS = [("0.5 sq mm", 21.30, 57.65, 78.85, 101.50), ("0.75 sq mm", 30.70, 79.95, 109.00, 142.40), ("1.0 sq mm", 39.50, 99.05, 140.50, 181.85),
                ("1.5 sq mm", 56.85, 138.00, 195.25, 258.25), ("2.5 sq mm", 95.10, 219.50, 309.75, 420.25), ("4.0 sq mm", 151.10, 332.00, 484.00, 633.50),
                ("6.0 sq mm", 223.00, 490.00, 714.00, 941.00), ("10 sq mm", 382.00, 842.00, 1230.00, 1619.00), ("16 sq mm", 594.00, 1271.00, 1861.00, 2461.00),
                ("25 sq mm", 964.00, 2133.00, 3119.00, 4136.00), ("35 sq mm", 1321.00, 2964.00, 4351.00, 5765.00), ("50 sq mm", 1884.00, 4206.00, 6198.00, 8195.00),
                ("70 sq mm", 2643.00, 5906.00, 8624.00, 11441.00)]
POLYCAB_TEL = [("1 pair", 15.90, 11.60), ("2 pair", 30.20, 19.70), ("3 pair", 43.00, 28.75), ("4 pair", 57.05, 38.55), ("5 pair", 71.35, 50.25),
               ("10 pair", 142.65, None), ("20 pair", 279.25, None), ("50 pair", 733.35, None), ("100 pair", 1466.70, None)]
POLYCAB_SUB = [("1.5 sq mm", 134.15), ("2.5 sq mm", 217.15), ("4.0 sq mm", 336.10), ("6.0 sq mm", 491.90), ("10 sq mm", 860.00), ("16 sq mm", 1275.95), ("25 sq mm", 2085.80), ("35 sq mm", 2920.80)]
POLYCAB_COAX = [("RG-59", 4015, 12250), ("RG-6 CCS", 2785, 8500), ("RG-6", 4105, 12520), ("RG-11", 9700, 29575), ("RG-11 CCS", 5460, 16650)]
POLYCAB_ALU = [("2.5 sq mm", None, 224, 241, None, 266), ("4 sq mm", None, 241, 284, None, 315), ("6 sq mm", None, 303, 353, None, 395), ("10 sq mm", None, 349, 417, None, 546),
               ("16 sq mm", 242, 406, 464, None, 592), ("25 sq mm", 302, 418, 556, 653, 702), ("35 sq mm", 376, 536, 761, 843, 960), ("50 sq mm", 479, 723, 986, 1124, 1266),
               ("70 sq mm", 608, 921, 1323, 1532, 1717), ("95 sq mm", 744, 1192, 1702, 1941, 2264), ("120 sq mm", 891, 1468, 2083, 2433, 2771), ("150 sq mm", 1061, 1797, 2580, 2837, 3348),
               ("185 sq mm", 1288, 2194, 3192, 3589, 4217), ("240 sq mm", 1600, 2776, 4130, 4575, 5454), ("300 sq mm", 1945, 3414, 5107, 5674, 6741), ("400 sq mm", 2511, 4475, 6481, 7200, 8667)]
POLYCAB_CU_ARM = [("4 sq mm", 549, 761, 990), ("6 sq mm", 781, 1102, 1433), ("10 sq mm", 1266, 1803, 2386), ("16 sq mm", 1791, 2679, 3519)]


def rsd(v):
    """Rupees with paise for per-metre rates."""
    if v is None:
        return dash()
    return "₹" + (format(v, ",.2f") if v != int(v) else format(int(v), ",d"))


POLYCAB_PAGE = {
    "slug": "polycab", "name": "Polycab", "kind": "brand", "group": "Wires & Cables",
    "title": "Polycab Wire Price List 2026 — Etira, Primma, Optima, Maxima Coils, Flexible, Armoured, LAN | Mount Cable India",
    "h1": "Polycab wire price list 2026",
    "desc": "Polycab wire price list 2026 from the distributor list: Etira, Primma, Optima and Maxima 90 m house-wire coils, 200 m and 300 m FRLF, FRLS-H and HFFR coils, flexible single and multicore per metre, FRLS, telephone, submersible, co-axial, LAN, CCTV, speaker, solar, welding and armoured cable. Mount Cable India, Bangalore.",
    "intro": "Polycab list prices for 2026 from the current Shree NM Electricals distributor lists (house-wire coils effective 8 June 2026, flexible cable list no. 04 effective 15 August 2026, armoured cable effective 18 August 2026, telecom and co-axial effective 25 May 2026), rates exclusive of GST. Mount Cable India stocks the full Polycab range in Bangalore and sells below list; message your requirement for the rate.",
    "badge": "Polycab list wef 15 Aug 2026 · Ex-GST list prices",
    "effective": "Polycab distributor lists, June to August 2026",
    "tables": [
        {"title": "Polycab house wire, 90 m coils (list price per coil)",
         "cols": ["Size", "Rating", "Optima FRLF", "Maxima HR-FR", "Primma FRLF", "Etira FR"],
         "rows": [(r[0], r[1], rs(r[2]), rs(r[3]), rs(r[4]), rs(r[5])) for r in POLYCAB_90M],
         "note": "<p>Etira is the standard FR house wire, Primma and Optima are flame-retardant low-flame (FRLF) grades, and Maxima is the heat-resistant HR-FR premium line. For the same size, a Polycab Etira coil lists a little above a Finolex Silver Pack coil; the <a href=\"finolex-price-list.html\">Finolex price list</a> has the comparison figures.</p>"},
        {"title": "Polycab industrial cable long coils, 200 m and 300 m (list price per coil)",
         "cols": ["Size", "Coil", "FRLF", "FRLS-H", "HFFR"],
         "rows": [(r[0], r[1], rs(r[2]), rs(r[3]), rs(r[4])) for r in POLYCAB_LONG]},
        {"title": "Polycab FR flexible cable, per metre (list price)",
         "cols": ["Size", "Rating", "Single core", "2 core", "3 core", "4 core"],
         "rows": [(r[0], r[1], rsd(r[2]), rsd(r[3]), rsd(r[4]), rsd(r[5])) for r in POLYCAB_FLEX],
         "note": "<p>Polycab lists flexible cable per metre; multiply by 100 for the coil. Single core 16 to 70 sq mm and multicore 5 to 24 core are on the FRLS list below and on request.</p>"},
        {"title": "Polycab FRLS flexible cable, per metre (list price)",
         "cols": ["Size", "Single core", "2 core", "3 core", "4 core"],
         "rows": [(r[0], rsd(r[1]), rsd(r[2]), rsd(r[3]), rsd(r[4])) for r in POLYCAB_FRLS]},
        {"title": "Polycab telephone and switchboard cable, per metre (list price)",
         "cols": ["Pairs", "0.5 mm unarmoured", "0.4 mm unarmoured"],
         "rows": [(r[0], rsd(r[1]), rsd(r[2])) for r in POLYCAB_TEL],
         "note": "<p>Jelly-filled armoured telephone cable (0.5 mm): 5 pair ₹220, 10 pair ₹338, 20 pair ₹596, 50 pair ₹1,319, 100 pair ₹2,517 per metre.</p>"},
        {"title": "Polycab 3-core flat submersible cable, per metre (list price)",
         "cols": ["Size", "Per metre"],
         "rows": [(r[0], rsd(r[1])) for r in POLYCAB_SUB]},
        {"title": "Polycab co-axial cable (list price per coil)",
         "cols": ["Type", "100 m", "305 m"],
         "rows": [(r[0], rs(r[1]), rs(r[2])) for r in POLYCAB_COAX],
         "note": "<p>Armoured RG-6 is ₹97.85 per metre and armoured RG-11 ₹178.45 per metre.</p>"},
        {"title": "Polycab LAN, CCTV, speaker and solar cable (list price)",
         "cols": ["Item", "Pack", "List price"],
         "rows": [("Cat 5e UTP 4 pair", "305 m box", rs(18585)), ("Cat 6 UTP 4 pair", "305 m box", rs(18585)), ("Cat 6 armoured", "per metre", rsd(122.33)),
                  ("CCTV 3+1", "90 m coil", rs(4725)), ("CCTV 4+1", "90 m coil", rs(5460)), ("CCTV 4+1 armoured", "per metre", rsd(138.02)),
                  ("Speaker wire 23/36", "90 m", rs(2565)), ("Speaker wire 40/36", "90 m", rs(4095)), ("Speaker wire 70/36", "90 m", rs(6090)),
                  ("Speaker wire 1.0 sq mm", "90 m", rs(6005)), ("Speaker wire 1.5 sq mm", "90 m", rs(8550)), ("Speaker wire 2.5 sq mm", "90 m", rs(14190)),
                  ("Solar cable 4 sq mm, tinned copper", "100 m", rs(14605)), ("Solar cable 6 sq mm, tinned copper", "100 m", rs(21635)),
                  ("Welding cable 16 sq mm", "per metre", rs(723)), ("Welding cable 25 sq mm", "per metre", rs(1107)), ("Welding cable 35 sq mm", "per metre", rs(1554)),
                  ("Welding cable 50 sq mm", "per metre", rs(2197)), ("Welding cable 70 sq mm", "per metre", rs(3102)), ("Welding cable 95 sq mm", "per metre", rs(4092))]},
        {"title": "Polycab aluminium armoured cable, PVC/XLPE, 1.1 kV, per metre (list price)",
         "cols": ["Size", "1 core", "2 core", "3 core", "3.5 core", "4 core"],
         "rows": [(r[0],) + tuple(rsd(x) for x in r[1:]) for r in POLYCAB_ALU],
         "note": "<p>Armoured aluminium is the usual choice for the service cable from the meter to the building DB and for underground runs to a pump house or gate.</p>"},
        {"title": "Polycab copper armoured cable, small sizes, per metre (list price)",
         "cols": ["Size", "2 core", "3 core", "4 core"],
         "rows": [(r[0], rs(r[1]), rs(r[2]), rs(r[3])) for r in POLYCAB_CU_ARM],
         "note": "<p>Copper control cable 1.5 sq mm runs from ₹283 (2 core) to ₹6,354 (61 core) per metre; 2.5 sq mm from ₹398 to ₹9,955. Large copper YFY 25 to 400 sq mm and 6.6 to 33 kV HT XLPE aluminium cable are quoted on request.</p>"},
    ],
    "price_note": POLYCAB_NOTE,
    "note": ("<h2>Reading the Polycab price list</h2>"
             "<p>Polycab publishes several lists rather than one: a coil list for house wire, a per-metre list for flexible and FRLS cable, a per-coil list for co-axial and speaker cable, and a per-metre list for armoured power cable. That is why the units change between the tables above. When you compare Polycab with Finolex, compare coil to coil: a 90 m Etira coil against a 90 m Finolex Silver Pack coil of the same size. The <a href=\"../blog/finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html\">four-brand wire comparison</a> and <a href=\"../blog/rr-kabel-vs-polycab-vs-finolex-wire.html\">RR Kabel vs Polycab vs Finolex</a> do this size by size.</p>"
             "<h2>Which Polycab range for a house</h2>"
             "<p>Etira FR is the standard house wire and the one most electricians mean when they say Polycab. Primma and Optima add the low-flame FRLF property for flats and enclosed spaces, and Maxima HR-FR adds heat resistance for kitchens, geyser points and long AC runs. For apartment projects the 300 m and 200 m coils bring the per-metre cost down by roughly 10 percent against 90 m coils.</p>"
             "<h2>Polycab duplicates</h2>"
             "<p>Polycab is the largest wire brand in India and the second most copied after Finolex. Every genuine Polycab coil carries the brand, size, ISI mark and a batch code printed along the wire, and the carton carries a hologram and a verification code. A list-price coil offered at half the figures above is the clearest warning. Our guide to <a href=\"../blog/how-to-identify-duplicate-polycab-wire.html\">identifying duplicate Polycab wire</a> walks through the checks.</p>"
             + CTA_NOTE),
    "related": [("finolex-price-list.html", "Finolex price list 2026"),
                ("../blog/how-to-identify-duplicate-polycab-wire.html", "Polycab original vs duplicate"),
                ("../blog/rr-kabel-vs-polycab-vs-finolex-wire.html", "RR Kabel vs Polycab vs Finolex"),
                ("../blog/finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html", "Four-brand wire comparison"),
                ("../brands/polycab.html", "Polycab range at Mount Cable")],
    "faqs": [
        ("What is the Polycab wire price list for 2026?",
         "From the June 2026 coil list, a Polycab Etira FR 90 m coil lists at ₹2,590 in 1.0 sq mm, ₹3,820 in 1.5 sq mm, ₹6,095 in 2.5 sq mm, ₹9,115 in 4.0 sq mm and ₹14,015 in 6.0 sq mm, ex-GST. Primma, Optima and Maxima are priced above Etira. Mount Cable India sells below list."),
        ("What is the Polycab 1.5 mm wire price?",
         "A Polycab 1.5 sq mm 90 m coil lists at ₹3,820 in Etira FR, ₹3,975 in Primma FRLF, ₹4,225 in Optima FRLF and ₹4,525 in Maxima HR-FR, ex-GST."),
        ("What is the Polycab 2.5 mm wire price?",
         "A Polycab 2.5 sq mm 90 m coil lists at ₹6,095 in Etira FR, ₹6,335 in Primma, ₹6,680 in Optima and ₹7,100 in Maxima, ex-GST. The 300 m FRLF coil is ₹29,830."),
        ("What is the difference between Polycab Etira, Primma, Optima and Maxima?",
         "Etira is standard FR house wire. Primma and Optima are FRLF (flame retardant low flame) grades with better fire performance. Maxima is HR-FR, heat resistant for kitchens, geysers and long AC runs. All are IS 694 copper wire in 90 m coils."),
        ("Is Polycab cheaper than Finolex?",
         "Coil for coil the list prices are close. A Polycab Etira 1.5 sq mm 90 m coil lists at ₹3,820 against a Finolex Silver Pack list of ₹3,640, and dealer prices on both are well below list. Choose on the range and grade you want rather than on a small list-price gap."),
        ("Are these Polycab prices the MRP?",
         "They are Polycab distributor list prices exclusive of GST, which is how Polycab publishes wire pricing. Mount Cable India's selling price is below list; WhatsApp your list for the rate."),
    ],
}

BRAND_PRICE_PAGES = [FINOLEX_PAGE, FINOLEX_GOLD_PAGE, POLYCAB_PAGE, ANCHOR_PAGE, ANCHOR_MCB_PAGE,
                     LEGRAND_PAGE, LEGRAND_MCB_PAGE, LEGRAND_SWITCHGEAR_PAGE, LEGRAND_SWITCHES_PAGE]


def merge_price_lists(price_lists):
    """Replace the old approximate-range entries for these brands with the real
    lists, keeping hub order, and slot the sub-pages after their parent."""
    override = {p["slug"]: p for p in BRAND_PRICE_PAGES if p["kind"] == "brand"}
    subs = {}
    for p in BRAND_PRICE_PAGES:
        if p["kind"] == "sub":
            subs.setdefault(p["parent"], []).append(p)
    out = []
    for p in price_lists:
        q = override.get(p["slug"], p)
        out.append(q)
        out.extend(subs.get(q["slug"], []))
    return out
