# -*- coding: utf-8 -*-
"""Finolex list prices — transcribed from the Finolex Cables list price sheet
"List Price wef. 04 Sep 2026" (the copy held in the Mount Cable quote builder,
data/pricelists/finolex_cables). All figures are MANUFACTURER LIST PRICE in
rupees, per pack, taxes extra.

⚠ CRITICAL FRAMING — do not break this anywhere on the site.
The rest of mountcable.com argues, correctly, that a discount of 15%+ off the
*market* rate signals copper shortfall, a short coil or counterfeit stock. Our
own offer is 35%+ off *list price*, which is a different baseline entirely:
Indian wire list prices are set well above the transacted trade price. So the
offer is genuine and consistent — but ONLY if every price is labelled as our
selling price. Never write "35% below market price"; that would contradict the
site's own trust argument and read exactly like the sellers we warn buyers about.
The site publishes the NET price only — never the percentage, never the list
price alongside it.

Coil lengths: SILVER / GOLD / FRLS-90 are 90m. FR-180 / FRLS-180 are 180m.
The long-coil column is 300m for 0.75-2.5 sq mm and 200m for 4.0 and 6.0 sq mm.
"""

EFFECTIVE_FROM = "4 September 2026"
# Per-range discount off list price, set by the owner (3 Aug 2026). The site
# publishes the NET price only — never the percentage, never the list price.
DISCOUNT = {
    "silver":    38,
    "gold":      37,
    "ultra":     35,
    "long":      45,   # the 300 m / 200 m long coil
    "frls90":    38,
    "frls180":   38,
    "frls_long": 44,   # FRLS 300 m / 200 m long coil
    "fr180":     38,
    "fr45":      38,   # 45 m Silver Pack coil
}
DEFAULT_DISCOUNT = 35      # anything not in the map above
TAX_NOTE = "Taxes extra as applicable."
MRP_IMAGES = []


def offer(mrp, pack=None, pct=None):
    """Net selling price for a pack, rounded to the nearest rupee.

    Always call with the pack key so the correct per-range discount applies.
    """
    if pct is None:
        pct = DISCOUNT.get(pack, DEFAULT_DISCOUNT)
    return int(round(mrp * (100 - pct) / 100))


# ---------------------------------------------------------------- house wire
# size -> dict of pack -> list price (Rs per coil)
HOUSE_WIRE = {
    "0.75": {"silver": 1960,  "gold": 2025,  "ultra": 2095,  "fr180": 3715,  "long": 6310,  "frls90": 1990,  "frls180": 3755,  "frls_long": 6375},
    "1.0":  {"silver": 2480,  "gold": 2770,  "ultra": 2700,  "fr180": 4855,  "long": 8255,  "frls90": 2515,  "frls180": 4905,  "frls_long": 8340,  "fr45": 1215},
    "1.5":  {"silver": 3640,  "gold": 4025,  "ultra": 3795,  "fr180": 7030,  "long": 11960, "frls90": 3695,  "frls180": 7100,  "frls_long": 12080, "fr45": 1800},
    "2.5":  {"silver": 5940,  "gold": 6400,  "ultra": 6155,  "fr180": 11590, "long": 19730, "frls90": 6030,  "frls180": 11705, "frls_long": 19925, "fr45": 2960},
    "4.0":  {"silver": 9020,  "gold": 9390,  "ultra": 9790,  "fr180": 18065, "long": 20505, "frls90": 9155,  "frls180": 18245, "frls_long": 20710, "fr45": 4510},
    "6.0":  {"silver": 13700, "gold": 14085, "ultra": 14515, "fr180": 27135, "long": 30815, "frls90": 13905, "frls180": 27405, "frls_long": 31125, "fr45": 6860},
}

# Long-coil length differs by size — 4.0 and 6.0 sq mm ship as 200m, not 300m.
LONG_LEN = {"0.75": "300 m", "1.0": "300 m", "1.5": "300 m", "2.5": "300 m", "4.0": "200 m", "6.0": "200 m"}

PACKS = [
    ("silver",    "Finolex Silver FR",  "90 m"),
    ("gold",      "Finolex Gold FR",    "90 m"),
    ("ultra",     "Finolex Finoultra",  "90 m"),
    ("fr45",      "Finolex FR",         "45 m"),
    ("fr180",     "Finolex FR",         "180 m"),
    ("long",      "Finolex FR",         None),      # length from LONG_LEN
    ("frls90",    "Finolex FR-LSH",     "90 m"),
    ("frls180",   "Finolex FR-LSH",     "180 m"),
    ("frls_long", "Finolex FR-LSH",     None),
]

# ---------------------------------------------------------------- flexible
# size -> (1 core FR, FRLS 1 core, 2 core, 3 core, 4 core); None where not listed
# Single core per 100 m coil; multicore per 100 m coil (FR list price).
FLEXIBLE = {
    "0.5":  (1465, 1500, 3685, 5110, 6545),
    "0.75": (2115, 2170, 5125, 7075, 9100),
    "1.0":  (2700, 2765, 6410, 8975, 11585),
    "1.5":  (3995, 4095, 8830, 12545, 16535),
    "2.5":  (6570, 6735, 14360, 20245, 26985),
    "4.0":  (10010, 10260, 22495, 32160, 42355),
    "6.0":  (15215, 15595, None, None, None),
    "10.0": (26245, 26900, None, None, None),
    "16.0": (40865, 41885, None, None, None),
    "25.0": (63890, 65485, None, None, None),
    "35.0": (89225, 91455, None, None, None),
    "50.0": (126520, 129685, None, None, None),
    "70.0": (184395, 189005, None, None, None),
}
FLEX_COLS = ["1 core", "FRLSH 1 core", "2 core", "3 core", "4 core"]

# FRLS multicore list price per 100 m (2 core, 3 core, 4 core)
FLEXIBLE_FRLS_MULTI = {
    "0.5":  (3850, 5315, 6775),
    "0.75": (5355, 7325, 9375),
    "1.0":  (6665, 9245, 11875),
    "1.5":  (9095, 12860, 16950),
    "2.5":  (14790, 20750, 27660),
    "4.0":  (23170, 32965, 43415),
}

# ---------------------------------------------------------------- other ranges
# Telephone cable, list price per 90 m coil: pairs -> (0.4 mm, 0.5 mm)
TELEPHONE = {"1 pair": (850, 1280), "2 pair": (1585, 2290), "3 pair": (2300, 3355), "4 pair": (2975, 4435),
             "5 pair": (3675, 5530), "10 pair": (7810, 11380), "20 pair": (14665, 21580),
             "50 pair": (36550, 53505), "100 pair": (68955, 104025)}
TELEPHONE_COLS = ["0.4 mm", "0.5 mm"]

# CCTV Gen-Z, per 90 m coil
CCTV = {"3+1": 2565, "4+1": 2895}
CCTV_FULL = [
    ("CCTV cable Gen Z (3+1)", "90 m", 2565), ("CCTV cable Gen Z (3+1)", "180 m", 5050),
    ("CCTV cable Gen Z (4+1)", "90 m", 2895), ("CCTV cable Gen Z (4+1)", "180 m", 5730),
    ("CCTV cable (3+1)", "90 m", 2930), ("CCTV cable (3+1)", "180 m", 5795),
    ("CCTV cable (4+1)", "90 m", 3305), ("CCTV cable (4+1)", "180 m", 6550),
    ("RG59 JF x1 + 3x0.15 sq mm CCTV, white", "90 m", 4510), ("RG59 JF x1 + 3x0.15 sq mm CCTV, white", "305 m", 15284),
    ("RG59 JF x1 + 4x0.15 sq mm CCTV, white", "90 m", 4965), ("RG59 JF x1 + 4x0.15 sq mm CCTV, white", "305 m", 16826),
    ("RG59 JF x1 + 6x0.15 sq mm CCTV, white", "90 m", 5615), ("RG59 JF x1 + 6x0.15 sq mm CCTV, white", "305 m", 19029),
]

# Co-axial (jelly filled), per 100 m coil unless stated
COAXIAL = {"RG-6 CCS": 1760, "RG-6 CU": 3270, "RG-6 CCS Eco Lite (90 m)": 1390}
COAXIAL_FULL = [
    ("RG 59 CU", "100 m", 2345), ("RG 59 CU", "305 m drum", 7152),
    ("RG 6 CU", "100 m", 3270), ("RG 6 CU", "305 m drum", 9974),
    ("RG 11 CU", "100 m", 7630), ("RG 11 CU", "305 m drum", 23272),
    ("RG 6 CCS", "100 m", 1760), ("RG 6 CCS", "305 m drum", 5368),
    ("RG 11 CCS", "100 m", 3440), ("RG 11 CCS", "305 m drum", 10492),
    ("RG 6 CCS Eco Lite", "90 m", 1390),
    ("RG 11 CCA", "100 m", 3950), ("RG 11 CCA", "305 m drum", 12048),
]

# Speaker cable (transparent), per 100 m
SPEAKER_100M = {"0.5": 2745, "0.75": 4005, "1.0": 4900, "1.5": 7355, "2.0": 11490, "2.5": 12245}
SPEAKER_25M = {"0.5": 685, "0.75": 1000, "1.0": 1225, "1.5": 1840}

# Solar DC cable (e-beam, tinned copper), list price per 100 m
SOLAR_DC = {"2.5 sq mm (per 100 m)": 6185, "4.0 sq mm (per 100 m)": 9605, "6.0 sq mm (per 100 m)": 14010}
SOLAR_NOVA = {"2.5 sq mm (per 100 m)": 5945, "4.0 sq mm (per 100 m)": 9245, "6.0 sq mm (per 100 m)": 13625, "10 sq mm (per 100 m)": 23735}

# LAN cable, per box
LAN = {"Cat-6": 17905, "Cat-6 Lite": 16945}
LAN_FULL = [
    ("Cat 5e UTP 4 pair", "305 m", 13900),
    ("Cat 6 UTP 0.5 x 4 pair (yellow / grey / blue / green)", "305 m", 17905),
    ("Cat 6 UTP 0.5 x 4 pair, grey", "100 m x 2", 5555),
    ("Cat 6 Lite UTP 4 pair (grey / yellow / green / blue)", "305 m x 2", 16945),
    ("Cat 6 UTP CCA 0.5 x 4 pair", "305 m", 9130),
    ("Cat 6 UTP 0.5 x 4 pair, DOSTH", "305 m", 19770),
    ("Cat 5e UTP 0.5 x 2 pair", "250 m", 5445),
    ("Cat 6A UTP 4 pair 23 AWG, grey", "305 m", 23105),
    ("Cat 6 PE ECCS armoured 4 pair 23 AWG", "305 m", 25655),
]

# 3-core flat submersible (PVC), list price per 100 m
FLAT_SUBMERSIBLE = {"1.5": 12640, "2.5": 19975, "4.0": 28670, "6.0": 42540, "10": 77930, "16": 122870, "25": 192180, "35": 266630}
FLAT_SUBMERSIBLE_XLPE = {"1.5": 12980, "2.5": 21175, "4.0": 30390, "6.0": 45090, "10": 82605, "16": 130240, "25": 201790, "35": 279960}


def house_wire_rows(size):
    """[(pack label, length, list price, offer price)] for one conductor size."""
    d = HOUSE_WIRE[size]
    out = []
    for key, label, length in PACKS:
        mrp = d.get(key)
        if not mrp:
            continue
        out.append((label, length or LONG_LEN[size], mrp, offer(mrp, key)))
    return out
