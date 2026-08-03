# -*- coding: utf-8 -*-
"""Finolex MRP price list — transcribed from the owner's printed list.

Source: Mount Cable India MRP sheet, EFFECTIVE FROM 21/05/2026 (photographs
IMG_1962 / IMG_1963). All figures are MANUFACTURER MRP in rupees, per pack.

⚠ CRITICAL FRAMING — do not break this anywhere on the site.
The rest of mountcable.com argues, correctly, that a discount of 15%+ off the
*market* rate signals copper shortfall, a short coil or counterfeit stock. Our
own offer is 35%+ off *MRP*, which is a different baseline entirely: Indian wire
MRP is set well above the transacted trade price. Cross-checked against the
market bands already published in data_price_lists.py, 35% off MRP lands at or
just above the top of those bands on every size. So the offer is genuine and
consistent — but ONLY if every price is labelled "off MRP". Never write
"35% below market price"; that would contradict the site's own trust argument
and read exactly like the sellers we warn buyers about.

Coil lengths: SILVER / GOLD / FRLS-90 are 90m. FR-180 / FRLS-180 are 180m.
The long-coil column is 300m for 1.0-2.5 sq mm and 200m for 4.0 and 6.0 sq mm.
"""

EFFECTIVE_FROM = "21 May 2026"
# Per-range discount off MRP, set by the owner (3 Aug 2026). The site publishes
# the NET price only — never the percentage, never the MRP-vs-price comparison.
DISCOUNT = {
    "silver":    38,
    "gold":      37,
    "ultra":     35,
    "long":      45,   # the 300 m / 200 m long coil
    "frls90":    38,
    "frls180":   38,
    "frls_long": 44,   # FRLS 300 m / 200 m long coil
    "fr180":     38,
}
DEFAULT_DISCOUNT = 35      # anything not in the map above
TAX_NOTE = "Taxes extra as applicable."
MRP_IMAGES = [
    ("finolex-mrp-list-1.jpg", "Finolex MRP price list held by Mount Cable India, effective 21 May 2026 — house wire ranges"),
    ("finolex-mrp-list-2.jpg", "Finolex MRP price list — flexible, telephone, coaxial, LAN, submersible and speaker cable"),
]


def offer(mrp, pack=None, pct=None):
    """Net selling price for a pack, rounded to the nearest rupee.

    Always call with the pack key so the correct per-range discount applies.
    """
    if pct is None:
        pct = DISCOUNT.get(pack, DEFAULT_DISCOUNT)
    return int(round(mrp * (100 - pct) / 100))


# ---------------------------------------------------------------- house wire
# size -> dict of pack -> MRP
HOUSE_WIRE = {
    "1.0":  {"silver": 2365,  "gold": 2640,  "ultra": 2625,  "fr180": 4760,  "long": 7970,  "frls90": 2425,  "frls180": 4880,  "frls_long": 8170},
    "1.5":  {"silver": 3495,  "gold": 3865,  "ultra": 3820,  "fr180": 6890,  "long": 11530, "frls90": 3580,  "frls180": 7060,  "frls_long": 11820},
    "2.5":  {"silver": 5580,  "gold": 6015,  "ultra": 6155,  "fr180": 11365, "long": 19020, "frls90": 5720,  "frls180": 11650, "frls_long": 19495},
    "4.0":  {"silver": 8475,  "gold": 8820,  "ultra": 9545,  "fr180": 17710, "long": 19760, "frls90": 8685,  "frls180": 18155, "frls_long": 20255},
    "6.0":  {"silver": 12855, "gold": 13215, "ultra": 14140, "fr180": 26600, "long": 29685, "frls90": 13175, "frls180": 27265, "frls_long": 30425},
}

# Long-coil length differs by size — 4.0 and 6.0 sq mm ship as 200m, not 300m.
LONG_LEN = {"1.0": "300 m", "1.5": "300 m", "2.5": "300 m", "4.0": "200 m", "6.0": "200 m"}

PACKS = [
    ("silver",    "Finolex Silver FR",  "90 m"),
    ("gold",      "Finolex Gold FR",    "90 m"),
    ("ultra",     "Finolex Ultra",      "90 m"),
    ("fr180",     "Finolex FR",         "180 m"),
    ("long",      "Finolex FR",         None),      # length from LONG_LEN
    ("frls90",    "Finolex FR-LSH",     "90 m"),
    ("frls180",   "Finolex FR-LSH",     "180 m"),
    ("frls_long", "Finolex FR-LSH",     None),
]

# ---------------------------------------------------------------- flexible
# size -> (1 core, FRLSH 1 core, 2 core, 3 core, 4 core); None where not listed
FLEXIBLE = {
    "0.5":  (1390, 1425, 3605, 4985, 6375),
    "0.75": (2005, 2055, 4995, 6880, 8845),
    "1.0":  (2570, 2635, 6240, 8720, 11240),
    "1.5":  (3845, 3940, 8580, 12160, 16020),
    "2.5":  (6165, 6320, 13935, 19610, 26115),
    "4.0":  (9400, 9635, 21815, 31115, 40945),
    "6.0":  (14270, 14625, None, 46270, 60500),
    "10.0": (24980, 25605, None, 78775, 103460),
    "16.0": (39345, 40330, None, 122885, 160510),
}
FLEX_COLS = ["1 core", "FRLSH 1 core", "2 core", "3 core", "4 core"]

# ---------------------------------------------------------------- other ranges
TELEPHONE = {"2 pair": (1535, 2220), "3 pair": (2230, 3245), "4 pair": (2880, 4290),
             "5 pair": (3555, 5350), "10 pair": (7575, 11010), "20 pair": (14185, 20850)}
TELEPHONE_COLS = ["0.4 mm", "0.5 mm"]

CCTV = {"3+1": 2615, "4+1": 2950}
COAXIAL = {"RG-6 CCS": 1865, "RG-6 CU": 3460, "RG-6 Lite": 1410}
SPEAKER_100M = {"0.5": 2845, "0.75": 4150, "1.0": 5075, "1.5": 7615, "2.5": 12655}
SOLAR_DC = {"4.0 sq mm (per metre)": 90.45}
LAN = {"Cat-6": 17710, "Cat-6 Lite": 16760}
FLAT_SUBMERSIBLE = {"1.5": 12200, "2.5": 19290, "4.0": 27640, "6.0": 41005}


def house_wire_rows(size):
    """[(pack label, length, MRP, offer price)] for one conductor size."""
    d = HOUSE_WIRE[size]
    out = []
    for key, label, length in PACKS:
        mrp = d.get(key)
        if not mrp:
            continue
        out.append((label, length or LONG_LEN[size], mrp, offer(mrp, key)))
    return out
