# -*- coding: utf-8 -*-
"""Range-level price-list pages for Finolex (wires) and Legrand (switches and
switchgear), one page per search intent ("finolex frls wire price list",
"legrand myrius price list" ...). Oct 2026.

Every figure is rendered from the same data the parent pages use
(data_finolex_mrp / data_brand_prices), so nothing can drift:
  Finolex  — NET selling prices only, never the list price or a percentage.
  Legrand  — MRP struck through with the 65%-off net beside it (the page key
             "discount" makes build_price_list apply with_net()).
"""
from data_finolex_mrp import (HOUSE_WIRE, LONG_LEN, FLEXIBLE, FLEXIBLE_FRLS_MULTI, CCTV_FULL, COAXIAL_FULL,
                              SOLAR_DC, SOLAR_NOVA, LAN_FULL, FLAT_SUBMERSIBLE, FLAT_SUBMERSIBLE_XLPE,
                              EFFECTIVE_FROM, TAX_NOTE, offer)
from data_brand_prices import (rs, dash, lnet, CTA_NOTE, SIZES, LEGRAND_DISCOUNT, LEGRAND_NOTE_MRP,
                               LEGRAND_MYRIUS, LEGRAND_MYRIUS_PLATES, LEGRAND_LYNCUS, LEGRAND_LYNCUS_PLATES,
                               LEGRAND_ALLZY, LEGRAND_BRITZY, LEGRAND_BRITZY_PLATES, LEGRAND_BOXES,
                               LEGRAND_RCCB_AC, LEGRAND_RCBO_DP, LEGRAND_ISOLATORS, LEGRAND_SPN_DB,
                               LEGRAND_ETPN_DB, LEGRAND_VTPN_DB, LEGRAND_FLEXY, LEGRAND_MIVAN, LEGRAND_ENCL,
                               LEGRAND_MCB_C, LEGRAND_MCB_D, LEGRAND_MCB_HI)


def _hw(size, key):
    v = HOUSE_WIRE[size].get(key)
    return rs(offer(v, key)) if v else dash()


def _n(v):
    return rs(offer(v))


FIN_BADGE = f"Finolex list wef {EFFECTIVE_FROM} · Our net prices"
FIN_NOTE = (f"<p class=\"ptable-note\">Mount Cable India selling prices per coil or pack, current to the Finolex list "
            f"effective {EFFECTIVE_FROM}. {TAX_NOTE} Larger quantities are priced better.</p>")
LEG_BADGE = "Legrand Corp MPL 2026 · 65% off MRP at Mount Cable"

FIN_RELATED = [("../finolex-best-price-bangalore.html", "Best price for Finolex in Bangalore"),
               ("finolex-price-list.html", "Full Finolex price list, every range"),
               ("../buy-finolex-wires.html", "Buy Finolex wires (WhatsApp ordering)"),
               ("../finolex-wire-scanner.html", "Finolex wire scanner: check a coil is original"),
               ("../best-wire-brand-in-india.html", "Which wire brand is best?")]
LEG_RELATED = [("../legrand-best-price-bangalore.html", "Best price for Legrand in Bangalore"),
               ("legrand-price-list.html", "Legrand price list 2026 overview"),
               ("legrand-switches-price-list.html", "All Legrand switch ranges side by side"),
               ("../legrand-dealer-bangalore.html", "Legrand dealer in Bangalore"),
               ("../best-switch-brand-in-india.html", "Which switch brand is best?")]


def _fin(slug, name, title, h1, desc, intro, tables, note, faqs, related=None):
    return {"slug": slug, "name": name, "kind": "sub", "parent": "finolex", "group": "Wires & Cables",
            "title": title, "h1": h1, "desc": desc, "intro": intro, "badge": FIN_BADGE,
            "effective": EFFECTIVE_FROM, "tables": tables, "price_note": FIN_NOTE,
            "note": note + CTA_NOTE, "related": (related or []) + FIN_RELATED, "faqs": faqs}


def _leg(slug, name, group, title, h1, desc, intro, tables, note, faqs, related=None):
    return {"slug": slug, "name": name, "kind": "sub", "parent": "legrand", "group": group,
            "title": title, "h1": h1, "desc": desc, "intro": intro, "badge": LEG_BADGE,
            "discount": LEGRAND_DISCOUNT, "effective": "Legrand Corp MPL 2026", "tables": tables,
            "price_note": LEGRAND_NOTE_MRP, "note": note + CTA_NOTE,
            "related": (related or []) + LEG_RELATED, "faqs": faqs}


def _mp(mrp):
    """'₹180 MRP, ₹63 at Mount Cable' for FAQ text."""
    return f"{rs(mrp)} MRP ({rs(lnet(mrp))} at Mount Cable)"


# =====================================================================
# FINOLEX
# =====================================================================
SILVER = _fin(
    "finolex-silver-wire", "Finolex Silver Wire",
    "Finolex Silver Wire Price List 2026 (Silver Pack FR, 45/90/180/300 m) | Mount Cable India",
    "Finolex Silver wire price list 2026",
    f"Finolex Silver Pack FR house wire prices for 0.75 to 6.0 sq mm in 45 m, 90 m, 180 m and 300/200 m coils, current to the Finolex list of {EFFECTIVE_FROM}. Net prices at Mount Cable India, Bangalore.",
    f"Silver Pack is Finolex's standard IS 694 flame-retardant (FR) house wire and the coil most Bangalore homes are wired with. Below is every size and coil length at Mount Cable India's selling price, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex Silver Pack FR, 90 m coils",
      "cols": ["Size", "Silver Pack FR 90 m", "Typical use"],
      "rows": [(f"{s} sq mm", _hw(s, "silver"), u) for s, u in zip(SIZES, [
          "Bell, indicator and control wiring", "Earth wire on lighting circuits", "Lighting and 6A socket circuits",
          "16A sockets, kitchen points", "Geyser and 1.5-ton AC points", "2-ton AC and the main feed"])]},
     {"title": "Same FR wire in other coil lengths",
      "cols": ["Size", "FR 45 m", "FR 180 m", "FR long coil", "Long coil length"],
      "rows": [(f"{s} sq mm", _hw(s, "fr45"), _hw(s, "fr180"), _hw(s, "long"), LONG_LEN[s]) for s in SIZES]}],
    ("<h2>Silver Pack or a longer coil?</h2>"
     "<p>For a single house the 90 m Silver Pack is the convenient size: an electrician can carry it, and a 2BHK uses a handful of coils per size. For apartments and row houses the 180 m project pack and the 300 m / 200 m long coils cut the price per metre and the number of joints. The 45 m coil is for repairs, extensions and one-room jobs.</p>"
     "<h2>Silver or Gold?</h2>"
     "<p>Both are genuine IS 694 FR copper house wire with the same two-QR verification on the carton. Gold is Finolex's premium pack and costs a little more per coil; the per-size gap is on the <a href=\"finolex-gold-wire-price-list.html\">Finolex Gold price list</a> and explained in <a href=\"../blog/finolex-silver-vs-gold-90m.html\">Silver vs Gold</a>.</p>"),
    [("What is the Finolex Silver wire price for 1.5 sq mm?",
      f"A Finolex Silver Pack 1.5 sq mm 90 m coil is {_hw('1.5','silver')} at Mount Cable India, current to {EFFECTIVE_FROM}, taxes extra. The 180 m coil is {_hw('1.5','fr180')}."),
     ("What is the Finolex Silver wire price for 2.5 sq mm?",
      f"A Finolex Silver Pack 2.5 sq mm 90 m coil is {_hw('2.5','silver')}, and the 300 m long coil is {_hw('2.5','long')}, taxes extra."),
     ("Is Finolex Silver good for house wiring?",
      "Yes. Silver Pack is IS 694 flame-retardant copper house wire, and it is what most homes in Bangalore are wired with. Choose Flamegard FR-LSH instead if you want low smoke in a fire, which we recommend for flats and bedrooms."),
     ("Is a Finolex Silver coil far below this price genuine?",
      "Be careful. Wire is a 3 to 5 percent margin trade, so a coil far below a distributor's price is usually short in length, thin in copper or counterfeit. Scan both QR codes on the carton before you pay.")])

FRLS = _fin(
    "finolex-frls-wire", "Finolex FRLS Wire",
    "Finolex FRLS Wire Price List 2026 — Flamegard FR-LSH 90/180/300 m | Mount Cable India",
    "Finolex FRLS (Flamegard FR-LSH) wire price list 2026",
    f"Finolex Flamegard FR-LSH (FRLS) house wire prices for 0.75 to 6.0 sq mm in 90 m, 180 m and 300/200 m coils, current to {EFFECTIVE_FROM}, with Silver FR alongside. Net prices at Mount Cable India, Bangalore.",
    f"Flamegard is Finolex's flame-retardant, low-smoke and low-halogen (FR-LSH, often written FRLS) house wire. In a fire, smoke is what hurts people first, so this is the grade we recommend for flats, bedrooms, children's rooms and enclosed stairwells. Every size and coil length below is at Mount Cable India's selling price, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex Flamegard FR-LSH, all coil lengths",
      "cols": ["Size", "FR-LSH 90 m", "FR-LSH 180 m", "FR-LSH long coil", "Long coil length"],
      "rows": [(f"{s} sq mm", _hw(s, "frls90"), _hw(s, "frls180"), _hw(s, "frls_long"), LONG_LEN[s]) for s in SIZES]},
     {"title": "What the safety upgrade costs per 90 m coil",
      "cols": ["Size", "Silver Pack FR", "Flamegard FR-LSH", "Extra for FR-LSH"],
      "rows": [(f"{s} sq mm", _hw(s, "silver"), _hw(s, "frls90"),
                rs(offer(HOUSE_WIRE[s]["frls90"], "frls90") - offer(HOUSE_WIRE[s]["silver"], "silver"))) for s in SIZES]}],
    ("<h2>Why we recommend FR-LSH for most homes</h2>"
     "<p>FR wire stops a flame from running along the cable. FR-LSH does that and also gives off much less smoke and fewer halogen gases when it burns, which keeps a corridor or stairwell visible and breathable for longer. The table above shows the extra cost per coil is small, and across a whole house it is usually a few thousand rupees. Read <a href=\"../blog/fr-vs-frls-vs-finolex-ultra.html\">FR vs FR-LSH vs Finoultra</a> and <a href=\"../safest-wire-for-house.html\">which wire is safest for a house</a>.</p>"),
    [("What is the Finolex FRLS wire price for 1.5 sq mm?",
      f"A Finolex Flamegard FR-LSH 1.5 sq mm 90 m coil is {_hw('1.5','frls90')} at Mount Cable India, current to {EFFECTIVE_FROM}, taxes extra. The 180 m coil is {_hw('1.5','frls180')}."),
     ("What is the Finolex FRLS wire price for 2.5 sq mm?",
      f"A Finolex Flamegard FR-LSH 2.5 sq mm 90 m coil is {_hw('2.5','frls90')}, and the 300 m long coil is {_hw('2.5','frls_long')}, taxes extra."),
     ("Is FRLS wire better than FR wire?",
      "For safety, yes. Both resist flame spread; FR-LSH also gives off much less smoke and fewer halogen gases in a fire. For a house or flat it is the grade we recommend, and the extra cost per coil is small."),
     ("Is Flamegard the same as FRLS?",
      "Yes. Flamegard is Finolex's brand name for its FR-LSH house wire, which electricians and shops usually call FRLS.")])

ULTRA = _fin(
    "finolex-ultra-wire", "Finolex Ultra (Finoultra) Wire",
    "Finolex Ultra (Finoultra) Wire Price List 2026 — E-Beam Halogen-Free | Mount Cable India",
    "Finolex Ultra (Finoultra) wire price list 2026",
    f"Finolex Finoultra e-beam halogen-free house wire prices, 0.75 to 6.0 sq mm 90 m coils, current to {EFFECTIVE_FROM}, compared with Gold and Flamegard FR-LSH. Net prices at Mount Cable India, Bangalore.",
    f"Finoultra is Finolex's top house wire: electron-beam (e-beam) cross-linked, halogen-free insulation to IS 17048, with better heat resistance and the lowest smoke and halogen emission in the Finolex range. Here is every size at Mount Cable India's selling price with the Gold and Flamegard packs alongside, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex premium 90 m coils compared",
      "cols": ["Size", "Finoultra (HFFR)", "Gold Pack FR", "Flamegard FR-LSH"],
      "rows": [(f"{s} sq mm", _hw(s, "ultra"), _hw(s, "gold"), _hw(s, "frls90")) for s in SIZES]}],
    ("<h2>When Finoultra is worth it</h2>"
     "<p>Choose Finoultra where a halogen-free specification is written (premium apartments, villas, offices), for long AC and geyser runs where heat resistance matters, and anywhere you want the best Finolex makes. For a standard home, Flamegard FR-LSH gives most of the smoke-safety benefit at a lower price. The full comparison is in <a href=\"../blog/fr-vs-frls-vs-finolex-ultra.html\">FR vs FR-LSH vs Finoultra</a>.</p>"),
    [("What is the Finolex Ultra wire price for 1.5 sq mm?",
      f"A Finolex Finoultra 1.5 sq mm 90 m coil is {_hw('1.5','ultra')} at Mount Cable India, current to {EFFECTIVE_FROM}, taxes extra."),
     ("What is the Finolex Ultra wire price for 2.5 sq mm?",
      f"A Finolex Finoultra 2.5 sq mm 90 m coil is {_hw('2.5','ultra')}, taxes extra."),
     ("What is Finolex Ultra wire?",
      "Finoultra is Finolex's premium house wire with electron-beam cross-linked, halogen-free insulation to IS 17048. It has better heat resistance and the lowest smoke and halogen emission in the Finolex range."),
     ("Is Finolex Ultra better than Finolex Gold?",
      "On safety and heat resistance, yes. Gold is a premium FR wire; Finoultra adds halogen-free e-beam insulation. The price gap per coil is in the table above.")])

FLEX = _fin(
    "finolex-flexible-cable", "Finolex Flexible Cable",
    "Finolex Flexible Cable Price List 2026 — Single Core and Multicore, FR and FRLS | Mount Cable India",
    "Finolex flexible cable price list 2026",
    f"Finolex flexible cable prices: single core 0.5 to 70 sq mm and 2, 3 and 4 core round sheathed in FR and FRLS, per 100 m coil, current to {EFFECTIVE_FROM}. Net prices at Mount Cable India, Bangalore.",
    f"Finolex flexible cable uses a fine-stranded Class 5 copper conductor to IS 694, for appliance leads, panel wiring, extension boards and machine connections. Single core and round-sheathed multicore, in FR and FRLS, at Mount Cable India's selling price per 100 m coil, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex flexible single core, 100 m coils",
      "cols": ["Size", "FR", "FRLS"],
      "rows": [(f"{s} sq mm", _n(v[0]), _n(v[1])) for s, v in FLEXIBLE.items()]},
     {"title": "Finolex flexible multicore (round sheathed), FR, 100 m coils",
      "cols": ["Size", "2 core", "3 core", "4 core"],
      "rows": [(f"{s} sq mm", _n(v[2]), _n(v[3]), _n(v[4])) for s, v in FLEXIBLE.items() if v[2]]},
     {"title": "Finolex flexible multicore, FRLS, 100 m coils",
      "cols": ["Size", "2 core", "3 core", "4 core"],
      "rows": [(f"{s} sq mm", _n(a), _n(b), _n(c)) for s, (a, b, c) in FLEXIBLE_FRLS_MULTI.items()]}],
    ("<h2>Flexible cable or house wire?</h2>"
     "<p>Concealed wiring in conduit uses single-core house wire. Flexible cable is for anything that moves or is handled: appliance leads, extension boards, panel wiring, motors. Three-core flexible is the usual choice for a washing machine or water purifier point fed from a socket. For pumps see the <a href=\"finolex-submersible-cable-price-list.html\">Finolex submersible cable price list</a>.</p>"),
    [("What is the Finolex 3 core 1.5 sq mm flexible cable price?",
      f"Finolex 3 core 1.5 sq mm flexible cable is {_n(FLEXIBLE['1.5'][3])} per 100 m coil in FR and {_n(FLEXIBLE_FRLS_MULTI['1.5'][1])} in FRLS at Mount Cable India, taxes extra."),
     ("What is the Finolex 3 core 2.5 sq mm flexible cable price?",
      f"Finolex 3 core 2.5 sq mm flexible cable is {_n(FLEXIBLE['2.5'][3])} per 100 m coil in FR and {_n(FLEXIBLE_FRLS_MULTI['2.5'][1])} in FRLS, taxes extra."),
     ("Is flexible cable sold by the metre?",
      "Finolex packs flexible cable in 100 m coils, and that is how it is priced here. For a cut length, WhatsApp the size, cores and length for a quote.")])

LANP = _fin(
    "finolex-lan-cable", "Finolex LAN Cable",
    "Finolex LAN Cable Price List 2026 — Cat 6, Cat 6A, Cat 5e 305 m Box | Mount Cable India",
    "Finolex LAN cable price list 2026: Cat 6, Cat 6A and Cat 5e",
    f"Finolex LAN cable prices for Cat 6 UTP, Cat 6 Lite, Cat 6A, Cat 5e and armoured Cat 6 per box, current to {EFFECTIVE_FROM}. Net prices at Mount Cable India, Bangalore.",
    f"Wired networking for a home office, CCTV recorder or smart TV runs best on Cat 6. These are Mount Cable India's selling prices for every Finolex LAN cable on the list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex LAN cable",
      "cols": ["Description", "Pack", "Price"],
      "rows": [(a, b, _n(c)) for a, b, c in LAN_FULL]}],
    ("<h2>Which LAN cable for a house</h2>"
     "<p>Cat 6 UTP solid copper is the right default: it carries gigabit to every room and leaves headroom. Cat 6A is for 10-gigabit runs and offices. Avoid CCA (copper-clad aluminium) for runs inside walls; it is cheaper but loses signal and cannot carry PoE power reliably. The <a href=\"../blog/cat6-lan-cable-home-networking-guide.html\">Cat 6 home networking guide</a> covers sockets and layout.</p>"),
    [("What is the Finolex Cat 6 cable price?",
      f"A 305 m box of Finolex Cat 6 UTP 0.5 x 4 pair is {_n(17905)} at Mount Cable India, current to {EFFECTIVE_FROM}, taxes extra."),
     ("Is Finolex Cat 6 copper?",
      "The standard Finolex Cat 6 UTP is solid copper. Finolex also lists a Cat 6 CCA (copper-clad aluminium) version at a lower price, shown separately in the table."),
     ("Do you sell LAN cable by the metre?",
      "LAN cable is packed in 305 m boxes (some lines in 100 m and 250 m). For a smaller length, WhatsApp the requirement and we will quote.")])

CCTV = _fin(
    "finolex-cctv-cable", "Finolex CCTV and Co-axial Cable",
    "Finolex CCTV Cable and Co-axial Cable Price List 2026 — 3+1, 4+1, RG6, RG59 | Mount Cable India",
    "Finolex CCTV and co-axial cable price list 2026",
    f"Finolex CCTV cable (3+1, 4+1, Gen Z, RG59 combo) and co-axial cable (RG6, RG11, RG59 in CU, CCS, CCA) prices, current to {EFFECTIVE_FROM}. Net prices at Mount Cable India, Bangalore.",
    f"Finolex CCTV and co-axial cable at Mount Cable India's selling price, from the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex CCTV cable",
      "cols": ["Type", "Pack", "Price"],
      "rows": [(a, b, _n(c)) for a, b, c in CCTV_FULL]},
     {"title": "Finolex co-axial cable (jelly filled)",
      "cols": ["Type", "Pack", "Price"],
      "rows": [(a, b, _n(c)) for a, b, c in COAXIAL_FULL]}],
    ("<h2>Reading the table</h2>"
     "<p>3+1 and 4+1 CCTV cable carries video on a co-axial core plus 3 or 4 power cores, for analogue HD cameras. For IP cameras use Cat 6 from the <a href=\"finolex-lan-cable-price-list.html\">Finolex LAN cable price list</a>. In co-axial cable, CU is solid copper, CCS copper-clad steel and CCA copper-clad aluminium; for DTH and TV points inside a house, RG 6 CCS is the usual pick.</p>"),
    [("What is the Finolex 3+1 CCTV cable price?",
      f"A 90 m coil of Finolex CCTV cable Gen Z 3+1 is {_n(2565)}, and the standard 3+1 is {_n(2930)}, at Mount Cable India, taxes extra."),
     ("What is the Finolex RG6 cable price?",
      f"Finolex RG 6 CCS is {_n(1760)} per 100 m and RG 6 CU (copper) is {_n(3270)} per 100 m, taxes extra.")])

SUB = _fin(
    "finolex-submersible-cable", "Finolex Submersible Cable",
    "Finolex Submersible Cable Price List 2026 — 3 Core Flat PVC and XLPE | Mount Cable India",
    "Finolex submersible cable price list 2026",
    f"Finolex 3-core flat submersible pump cable prices, 1.5 to 35 sq mm, PVC and XLPE insulated, per 100 m, current to {EFFECTIVE_FROM}. Net prices at Mount Cable India, Bangalore.",
    f"Borewell and openwell pumps run on 3-core flat submersible cable. Finolex makes it in PVC and in XLPE insulation, which handles heat better on long, heavily loaded runs. Mount Cable India's selling prices per 100 m, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex 3-core flat submersible cable, per 100 m",
      "cols": ["Size", "PVC insulated", "XLPE insulated"],
      "rows": [(f"{s} sq mm", _n(v), _n(FLAT_SUBMERSIBLE_XLPE[s])) for s, v in FLAT_SUBMERSIBLE.items()],
      "note": "<p>Supplied in continuous drum lengths; minimum order 500 m for non-standard lengths.</p>"}],
    ("<h2>Sizing a submersible cable</h2>"
     "<p>The size depends on the pump's horsepower and the depth: a deep borewell needs a larger size than the motor's current alone suggests, because of voltage drop over the length. Check it with the <a href=\"../tools/voltage-drop-calculator.html\">voltage drop calculator</a>, or WhatsApp the pump HP and depth and we will size it.</p>"),
    [("What is the Finolex 2.5 sq mm submersible cable price?",
      f"Finolex 3-core flat 2.5 sq mm submersible cable is {_n(FLAT_SUBMERSIBLE['2.5'])} per 100 m in PVC and {_n(FLAT_SUBMERSIBLE_XLPE['2.5'])} in XLPE at Mount Cable India, taxes extra."),
     ("PVC or XLPE submersible cable?",
      "XLPE handles heat better and suits long, heavily loaded or deep borewell runs. PVC is fine for shallower, lighter-duty pumps.")])

SOLAR = _fin(
    "finolex-solar-cable", "Finolex Solar Cable",
    "Finolex Solar DC Cable Price List 2026 — 4 sq mm, 6 sq mm Tinned Copper | Mount Cable India",
    "Finolex solar DC cable price list 2026",
    f"Finolex solar DC cable prices for 2.5, 4, 6 and 10 sq mm tinned-copper e-beam cable per 100 m, current to {EFFECTIVE_FROM}. Net prices at Mount Cable India, Bangalore.",
    f"Rooftop solar strings run on DC cable built for sun, heat and decades outdoors: tinned copper conductor and electron-beam cross-linked insulation. Mount Cable India's selling prices per 100 m, current to the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE}",
    [{"title": "Finolex solar DC cable, per 100 m",
      "cols": ["Size", "Solar DC (e-beam, tinned copper)", "Solar Nova"],
      "rows": [(k.split(" (")[0], _n(v), _n(SOLAR_NOVA[k]) if k in SOLAR_NOVA else dash()) for k, v in SOLAR_DC.items()]
              + [("10 sq mm", dash(), _n(SOLAR_NOVA["10 sq mm (per 100 m)"]))]}],
    ("<h2>Which size for a rooftop system</h2>"
     "<p>4 sq mm is the usual string cable for home rooftop systems; 6 sq mm for longer runs from the roof to the inverter. Never use ordinary house wire on the DC side: it is not rated for UV and outdoor heat.</p>"),
    [("What is the Finolex 4 sq mm solar cable price?",
      f"Finolex 4 sq mm solar DC cable is {_n(SOLAR_DC['4.0 sq mm (per 100 m)'])} per 100 m at Mount Cable India, taxes extra."),
     ("What is the Finolex 6 sq mm solar cable price?",
      f"Finolex 6 sq mm solar DC cable is {_n(SOLAR_DC['6.0 sq mm (per 100 m)'])} per 100 m, taxes extra.")])

# =====================================================================
# LEGRAND
# =====================================================================
def _mech(rows):
    return [(c, d, rs(p)) for c, d, p in rows]


_BOX_TABLE = {"title": "Legrand metal flush boxes, for all ranges (MRP per unit)",
              "cols": ["Box", "MRP"], "rows": [(a, rs(b)) for a, b in LEGRAND_BOXES]}

MYRIUS = _leg(
    "legrand-myrius", "Legrand Myrius", "Switches & Sockets",
    "Legrand Myrius Price List 2026 — Switches, Sockets and Plates at 65% Off MRP | Mount Cable India",
    "Legrand Myrius price list 2026",
    "Legrand Myrius switch, socket, MCB module and cover plate prices from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP beside every line.",
    "Myrius is Legrand's premium modular switch range, specified in high-end apartments and villas, with the widest choice of plate finishes. Every line below shows the Legrand MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand Myrius regular white mechanisms",
      "cols": ["Cat. no.", "Description", "Price"], "rows": _mech(LEGRAND_MYRIUS)},
     {"title": "Myrius regular white cover plates",
      "cols": ["Plate", "Price"], "rows": [(a, rs(b)) for a, b in LEGRAND_MYRIUS_PLATES],
      "note": "<p>Myrius plates also come in charcoal grey, ice white, ice black, pearl champagne, sonic silver and 3 mm toughened glass at higher MRPs. Ask for the finish you want.</p>"},
     _BOX_TABLE],
    ("<h2>Is Myrius worth it?</h2>"
     "<p>Myrius is where Legrand's look and feel are at their best, and Legrand states a 10-year manufacturing-defect replacement on Myrius switches and power sockets. At 65% off MRP a Myrius 6A switch costs about what a mid-range brand's switch does at a shop. Compare all four Legrand ranges on the <a href=\"legrand-switches-price-list.html\">Legrand switches price list</a>.</p>"),
    [("What is the Legrand Myrius 6A switch price?", f"A Myrius 6A one-way switch is {_mp(180)}; the 6A two-way is {_mp(326)}."),
     ("What is the Legrand Myrius socket price?", f"A Myrius 6/16A socket with shutter is {_mp(684)}."),
     ("What is the Legrand Myrius plate price?", f"Myrius regular white plates run from {_mp(306)} for 1 module to {_mp(1498)} for 18 modules.")])

LYNCUS = _leg(
    "legrand-lyncus", "Legrand Lyncus", "Switches & Sockets",
    "Legrand Lyncus Price List 2026 — Switches, Sockets, Regulators and Plates at 65% Off MRP | Mount Cable India",
    "Legrand Lyncus price list 2026",
    "Legrand Lyncus switch, socket, fan regulator, data socket and cover plate prices (classic white, chic grey, alu finishes) from the Corp MPL 2026, with Mount Cable India's 65%-off net price beside every line.",
    "Lyncus is the Legrand range most Bangalore homes settle on: a clean modern look, plates in white, chic grey, silver and metallic finishes, and BLDC fan regulators. Every line shows the Legrand MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand Lyncus classic white mechanisms",
      "cols": ["Cat. no.", "Description", "Price"], "rows": _mech(LEGRAND_LYNCUS)},
     {"title": "Lyncus cover plates with support frame",
      "cols": ["Plate", "Classic white", "Chic grey", "Alu sunset / champagne"],
      "rows": [(a, rs(b), rs(c), rs(d)) for a, b, c, d in LEGRAND_LYNCUS_PLATES]},
     _BOX_TABLE],
    ("<h2>Pricing a Lyncus board</h2>"
     "<p>A bedroom board of two 6A switches, a fan regulator and a 6/16A socket on a 6-module classic white plate with box is ₹1,926 at MRP, about ₹674 at 65% off. Use the <a href=\"../tools/material-list-builder.html\">material list builder</a> to count boards for the whole house.</p>"),
    [("What is the Legrand Lyncus 6A switch price?", f"A Lyncus 6A one-way switch is {_mp(100)}; the 6A two-way is {_mp(212)}."),
     ("What is the Legrand Lyncus fan regulator price?", f"The Lyncus 1-module 100 W fan regulator is {_mp(734)}, and the BLDC regulator is {_mp(996)}."),
     ("What is the Legrand Lyncus plate price?", f"Classic white plates run from {_mp(184)} for 1 and 2 module to {_mp(974)} for 18 module.")])

ALLZY = _leg(
    "legrand-allzy", "Legrand Allzy", "Switches & Sockets",
    "Legrand Allzy Price List 2026 — Switches, Sockets and Regulators at 65% Off MRP | Mount Cable India",
    "Legrand Allzy price list 2026",
    "Legrand Allzy switch, socket, fan regulator (including BLDC) and accessory prices from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP.",
    "Allzy brings genuine Legrand mechanisms at entry-level prices, with coloured plates (white, rose gold, gold, matt black and champagne) and a BLDC fan regulator. Every line shows the Legrand MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand Allzy white mechanisms",
      "cols": ["Cat. no.", "Description", "Price"], "rows": _mech(LEGRAND_ALLZY),
      "note": "<p>Matt black mechanisms (6812 series) run about 15 to 20 percent above white.</p>"},
     _BOX_TABLE],
    ("<h2>Allzy or Britzy?</h2>"
     "<p>Both are Legrand's entry ranges at near-identical prices. Allzy has more plate colours, 10A switches and a BLDC regulator; Britzy has a simpler plate range. See the <a href=\"legrand-britzy-price-list.html\">Britzy price list</a> to compare.</p>"),
    [("What is the Legrand Allzy 6A switch price?", f"An Allzy 6A one-way switch is {_mp(56)}; the 16A one-way is {_mp(152)}."),
     ("What is the Legrand Allzy socket price?", f"The Allzy 6/16A socket with shutter is {_mp(284)}."),
     ("Does Allzy have a BLDC fan regulator?", f"Yes, 2 module, {_mp(938)}.")])

BRITZY = _leg(
    "legrand-britzy", "Legrand Britzy", "Switches & Sockets",
    "Legrand Britzy Price List 2026 — Switches, Sockets and Plates at 65% Off MRP | Mount Cable India",
    "Legrand Britzy price list 2026",
    "Legrand Britzy switch, socket, regulator and cover plate prices from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP beside every line.",
    "Britzy is Legrand's value range: genuine Legrand mechanisms, a 10-year manufacturing-defect replacement on switches and power sockets, and the lowest price in the Legrand family. Every line shows the Legrand MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand Britzy white mechanisms",
      "cols": ["Cat. no.", "Description", "Price"], "rows": _mech(LEGRAND_BRITZY)},
     {"title": "Britzy white cover plates with support frame",
      "cols": ["Plate", "Price"], "rows": [(a, rs(b)) for a, b in LEGRAND_BRITZY_PLATES]},
     _BOX_TABLE],
    ("<h2>Why Britzy is the smart budget choice</h2>"
     "<p>At 65% off MRP a Britzy 6A switch costs less than many local brands at a shop, and you still get Legrand's mechanism and Legrand's replacement policy. It is the range we suggest for rental flats, utility areas and budget builds.</p>"),
    [("What is the Legrand Britzy 6A switch price?", f"A Britzy 6A one-way switch is {_mp(56)}; the 16A one-way is {_mp(190)}."),
     ("What is the Legrand Britzy socket price?", f"The Britzy 6/16A socket with shutter is {_mp(294)}."),
     ("What is the Legrand Britzy plate price?", f"Britzy white plates run from {_mp(132)} for 1 and 2 module to {_mp(622)} for 18 module.")])

RCCB = _leg(
    "legrand-rccb", "Legrand RCCB and RCBO", "MCBs & Switchgear",
    "Legrand RCCB and RCBO Price List 2026 — DX3 25 to 63 A at 65% Off MRP | Mount Cable India",
    "Legrand RCCB and RCBO price list 2026",
    "Legrand DX3 RCCB (DP and FP, 30/100/300 mA, 25 to 63 A) and RCBO prices from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP.",
    "An RCCB is the device that saves a life in a shock: it trips in milliseconds when current leaks to earth. Every Legrand DX3 RCCB and RCBO below shows MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand DX3 RCCB, AC type",
      "cols": ["Rating", "DP 30 mA", "DP 100 mA", "DP 300 mA", "FP 30 mA", "FP 100 mA", "FP 300 mA"],
      "rows": [(r[0],) + tuple(rs(x) for x in r[1:]) for r in LEGRAND_RCCB_AC]},
     {"title": "Legrand DX3 RCBO, DP",
      "cols": ["Rating", "30 mA", "100 mA", "300 mA"],
      "rows": [(r[0],) + tuple(rs(x) if isinstance(x, int) else x for x in r[1:]) for r in LEGRAND_RCBO_DP]}],
    ("<h2>Which RCCB for a house</h2>"
     "<p>A single-phase home needs a 2-pole (DP) 30 mA RCCB, rated at or above the main MCB: 40 A for most homes, 63 A for large villas. A three-phase home needs a 4-pole (FP). The <a href=\"../blog/mcb-rccb-rcbo-guide-for-homes.html\">MCB, RCCB and RCBO guide</a> explains the difference.</p>"),
    [("What is the Legrand RCCB 40 A 30 mA price?", f"The Legrand DX3 DP 40 A 30 mA RCCB is {_mp(6360)}; the FP version is {_mp(8068)}."),
     ("What is the Legrand RCCB 63 A price?", f"The DX3 DP 63 A 30 mA RCCB is {_mp(7818)}."),
     ("RCCB or RCBO?", "An RCCB protects against earth leakage only and sits with MCBs. An RCBO combines both in one device, protecting a single circuit.")])

DB = _leg(
    "legrand-distribution-board", "Legrand Distribution Board", "MCBs & Switchgear",
    "Legrand Distribution Board Price List 2026 — Ekinox SPN, TPN, Flexy, Isolators at 65% Off MRP | Mount Cable India",
    "Legrand distribution board (DB) price list 2026",
    "Legrand Ekinox SPN and TPN distribution boards, vertical TPN, Flexy, Mivan boards, enclosures and DX3 isolators from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP.",
    "The distribution board holds every MCB in the house, so it should be built for it. Legrand Ekinox boards, enclosures and DX3 isolators below show MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand Ekinox SPN DB (single phase)",
      "cols": ["Ways", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
      "rows": [(r[0], rs(r[2]), rs(r[3]), rs(r[4]), rs(r[5])) for r in LEGRAND_SPN_DB]},
     {"title": "Legrand Ekinox TPN DB (three phase)",
      "cols": ["Ways", "Modules", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
      "rows": [(r[0], r[1], rs(r[2]), rs(r[3]), rs(r[4]), rs(r[5])) for r in LEGRAND_ETPN_DB]},
     {"title": "Legrand vertical TPN DB",
      "cols": ["Ways", "IP30", "IP43 metal door", "IP43 acrylic door", "IP54"],
      "rows": [(r[0],) + tuple(rs(x) for x in r[1:]) for r in LEGRAND_VTPN_DB]},
     {"title": "Legrand Flexy boards",
      "cols": ["Size", "Modules", "IP30", "IP43 metal door", "IP43 acrylic door"],
      "rows": [(r[0], r[1], rs(r[2]), rs(r[3]), rs(r[4])) for r in LEGRAND_FLEXY]},
     {"title": "Legrand Mivan DB", "cols": ["Ways", "Price"], "rows": [(a, rs(b)) for a, b in LEGRAND_MIVAN]},
     {"title": "Legrand modular enclosures", "cols": ["Enclosure", "Price"], "rows": [(a, rs(b)) for a, b in LEGRAND_ENCL]},
     {"title": "Legrand DX3 isolators", "cols": ["Rating", "DP", "TP", "FP"],
      "rows": [(r[0], rs(r[1]), rs(r[2]), rs(r[3])) for r in LEGRAND_ISOLATORS]}],
    ("<h2>Choosing the board size</h2>"
     "<p>Count the circuits, add the incomer and RCCB, then leave 20 to 30 percent spare ways. A 2BHK is usually an 8 or 12-way SPN board, a 3BHK 12 or 16-way. For the breakers see the <a href=\"legrand-mcb-price-list.html\">Legrand MCB price list</a> and the <a href=\"../blog/distribution-board-selection-guide-home.html\">DB selection guide</a>.</p>"),
    [("What is the Legrand 8-way DB price?", f"A Legrand Ekinox SPN 8-way DB is {_mp(2917)} in IP30 and {_mp(4065)} with an IP43 metal door."),
     ("What is the Legrand 12-way DB price?", f"An Ekinox SPN 12-way DB is {_mp(3447)} in IP30 and {_mp(4884)} with an IP43 metal door."),
     ("What is the Legrand isolator price?", f"A DX3 DP 40 A isolator is {_mp(961)}; the 63 A DP is {_mp(1270)}.")])

def _pole(pole):
    rows = []
    for curve, bands in (("C curve", LEGRAND_MCB_C), ("D curve", LEGRAND_MCB_D), ("C curve", LEGRAND_MCB_HI)):
        for label, d in bands:
            if d.get(pole):
                rows.append((label, curve, rs(d[pole])))
    return rows


_MCB_REL = [("../legrand-best-price-bangalore.html", "Best price for Legrand in Bangalore"),
            ("legrand-mcb-price-list.html", "Legrand MCB price list, every pole and curve"),
            ("legrand-rccb-price-list.html", "Legrand RCCB and RCBO price list"),
            ("legrand-distribution-board-price-list.html", "Legrand distribution board price list"),
            ("../best-mcb-brand.html", "Which MCB brand is best?")]

DP_MCB = _leg(
    "legrand-dp-mcb", "Legrand DP MCB", "MCBs & Switchgear",
    "Legrand DP MCB Price List 2026 — DX3 2 Pole 6 to 125 A at 65% Off MRP | Mount Cable India",
    "Legrand DP (2 pole) MCB price list 2026",
    "Legrand DX3 double pole (DP) MCB prices from 0.5 to 125 A in C and D curve, from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP.",
    "A double pole MCB switches both live and neutral, which is why it is used as the main switch of a single-phase home and for AC and geyser circuits. Every Legrand DX3 DP MCB below shows MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand DX3 DP MCB", "cols": ["Rating", "Curve", "Price"], "rows": _pole("DP")}],
    ("<h2>Where a DP MCB goes</h2>"
     "<p>As the incomer of a single-phase DB (40 or 63 A), and on dedicated AC and geyser circuits where isolating both conductors is safer for servicing. For ordinary lighting and socket circuits an SP MCB is enough.</p>"),
    [("What is the Legrand 32 A DP MCB price?", f"A Legrand DX3 DP MCB 6 to 32 A, C curve, is {_mp(1693)}."),
     ("What is the Legrand 63 A DP MCB price?", f"A DX3 DP MCB 40 to 63 A, C curve, is {_mp(2663)}."),
     ("C or D curve for a DP MCB?", "C curve for homes. D curve for motors, pumps and compressors with a high starting current.")],
    related=_MCB_REL)

FP_MCB = _leg(
    "legrand-4-pole-mcb", "Legrand 4 Pole MCB", "MCBs & Switchgear",
    "Legrand 4 Pole (FP) and TPN MCB Price List 2026 — DX3 at 65% Off MRP | Mount Cable India",
    "Legrand 4 pole (FP) and TPN MCB price list 2026",
    "Legrand DX3 four pole (FP), TPN and TP MCB prices from 0.5 to 125 A, from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP.",
    "Three-phase homes, villas and buildings need a three or four pole incomer. Every Legrand DX3 TP, TPN and FP MCB below shows MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand DX3 FP (4 pole) MCB", "cols": ["Rating", "Curve", "Price"], "rows": _pole("FP")},
     {"title": "Legrand DX3 TPN MCB", "cols": ["Rating", "Curve", "Price"], "rows": _pole("TPN")},
     {"title": "Legrand DX3 TP MCB", "cols": ["Rating", "Curve", "Price"], "rows": _pole("TP")}],
    ("<h2>TP, TPN or FP?</h2>"
     "<p>TP switches the three phases; TPN and FP also switch the neutral, which is what most three-phase homes use as the incomer. Match it with a 4-pole 30 mA RCCB from the <a href=\"legrand-rccb-price-list.html\">Legrand RCCB price list</a>.</p>"),
    [("What is the Legrand 4 pole MCB price?", f"A Legrand DX3 FP MCB 6 to 32 A, C curve, is {_mp(3729)}; 40 to 63 A is {_mp(5306)}."),
     ("What is the Legrand 63 A FP MCB price?", f"{_mp(5306)} for the DX3 FP 40 to 63 A, C curve.")],
    related=_MCB_REL)

D_MCB = _leg(
    "legrand-d-curve-mcb", "Legrand D Curve MCB", "MCBs & Switchgear",
    "Legrand D Curve MCB Price List 2026 — DX3 SP, DP, TP, FP at 65% Off MRP | Mount Cable India",
    "Legrand D curve MCB price list 2026",
    "Legrand DX3 D curve MCB prices for SP, SPN, DP, TP, TPN and FP from 0.5 to 32 A, from the Corp MPL 2026, with Mount Cable India's net price at 65% off MRP.",
    "D curve MCBs ride through the high starting current of motors, pumps and compressors without nuisance tripping. Every Legrand DX3 D curve MCB below shows MRP and Mount Cable India's price at 65% off.",
    [{"title": "Legrand DX3 D curve MCB", "cols": ["Rating", "SP", "SPN", "DP", "TP", "TPN", "FP"],
      "rows": [(label,) + tuple(rs(d[p]) if d.get(p) else dash() for p in ["SP", "SPN", "DP", "TP", "TPN", "FP"]) for label, d in LEGRAND_MCB_D]}],
    ("<h2>When to use D curve</h2>"
     "<p>Borewell and sump pumps, lifts, compressors and workshop machines. Every other household circuit, including ACs with inverter compressors, normally takes a C curve MCB.</p>"),
    [("What is the Legrand D curve MCB price?", f"A Legrand DX3 SP D curve MCB 6 to 32 A is {_mp(678)}; the DP is {_mp(1754)}."),
     ("Should a pump use a D curve MCB?", "Usually yes: a motor's starting current can trip a C curve MCB. Size the rating to the motor and the cable.")],
    related=_MCB_REL)

MORE_PRICE_PAGES = [DP_MCB, FP_MCB, D_MCB, SILVER, FRLS, ULTRA, FLEX, LANP, CCTV, SUB, SOLAR, MYRIUS, LYNCUS, ALLZY, BRITZY, RCCB, DB]
