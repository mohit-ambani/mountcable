# -*- coding: utf-8 -*-
"""Pricing posts (Nov 2026). Price searches are the highest-intent searches the
site receives, and autocomplete plus Search Console show several that had no
page answering them directly: "finolex wire price today", "fr vs frls price",
"finolex wire online price", telephone and speaker cable prices, and Legrand
MCB price by ampere rating.

Rules, as everywhere on the site:
  * Finolex: NET price only. Never the list price, never a discount percentage.
  * Legrand: MRP and the net price at the published 65% off, side by side.
  * Every figure is computed from the data modules, so nothing can drift.
"""
from data_finolex_mrp import (HOUSE_WIRE, LONG_LEN, EFFECTIVE_FROM, TAX_NOTE, offer,
                              TELEPHONE, SPEAKER_100M, SPEAKER_25M, FLEXIBLE, FLAT_SUBMERSIBLE)
from data_brand_prices import LEGRAND_MCB_C, LEGRAND_MCB_D, LEGRAND_MCB_HI, LEGRAND_DISCOUNT, lnet

D = ("2026-11-11", "November 11, 2026")
W = "https://wa.me/918867676700"
PH = "88676 76700"
SZ = ["0.75", "1.0", "1.5", "2.5", "4.0", "6.0"]


def rs(n):
    return "₹" + format(int(round(n)), ",d")


def P(s, k):
    v = HOUSE_WIRE[s].get(k)
    return offer(v, k) if v else None


def c(v):
    return rs(v) if v else "—"


def tbl(cols, rows):
    return ('<div class="ptable-wrap"><table class="ptable"><thead><tr>' + "".join(f"<th>{x}</th>" for x in cols)
            + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>" for r in rows)
            + "</tbody></table></div>")


NOTE = (f'<p class="ptable-note">Mount Cable India selling prices on the Finolex list effective {EFFECTIVE_FROM}. '
        f'{TAX_NOTE} Prices move with copper; larger quantities are priced better.</p>')
CTA = (f'<p class="muted"><strong>Want the confirmed rate for your list?</strong> Send it to <a href="{W}">WhatsApp {PH}</a> '
       'for an itemised quote within 60 minutes. Free next-day delivery across Bangalore, pay after delivery, and every '
       'Finolex coil can be QR-checked at your site. No obligation to buy.</p>')
VERIFY = ("<h2>Check the coil before you pay</h2><p>A low price only helps if the wire is genuine. Buy sealed cartons, "
          "scan the outer QR on the label and the inner QR inside the box with the "
          "<a href=\"../finolex-wire-scanner.html\">Finolex wire scanner</a>, and take a GST invoice naming the range, "
          "size and coil length. A price far below the figures here is the usual sign of duplicate or refilled wire.</p>")
LINKS = ("<p>More prices: <a href=\"finolex-wire-price-per-meter.html\">per metre and per coil</a>, "
         "<a href=\"finolex-300-meter-wire-price.html\">300 m coil</a>, <a href=\"finolex-180-meter-wire-price.html\">180 m coil</a>, "
         "<a href=\"../price-lists/finolex-gold-wire-price-list.html\">Gold</a>, "
         "<a href=\"../price-lists/finolex-silver-wire-price-list.html\">Silver</a>, "
         "<a href=\"../price-lists/finolex-frls-wire-price-list.html\">FR-LSH</a>, "
         "<a href=\"../price-lists/finolex-ultra-wire-price-list.html\">Ultra</a>, "
         "<a href=\"../price-lists/finolex-price-list.html\">full Finolex price list</a>.</p>")

_all = tbl(["Size", "Silver FR", "Gold FR", "FR-LSH (Flamegard)", "Finoultra"],
           [[f"{s} sq mm", f"<strong>{c(P(s,'silver'))}</strong>", f"<strong>{c(P(s,'gold'))}</strong>",
             f"<strong>{c(P(s,'frls90'))}</strong>", f"<strong>{c(P(s,'ultra'))}</strong>"] for s in SZ])

# ------------------------------------------------------------------ 1. today
POST_TODAY = (
 "finolex-wire-price-today",
 "Finolex Wire Price Today: Current Rate for Every Size (2026)",
 f"Finolex wire price today at Mount Cable India: 1.5 sq mm {rs(P('1.5','silver'))}, 2.5 sq mm {rs(P('2.5','silver'))} per 90 m Silver coil, on the Finolex list effective {EFFECTIVE_FROM}. Every size and grade.",
 "Pricing",
 f"<p><strong>Today a 90 m coil of Finolex wire costs {rs(P('1.0','silver'))} in 1.0 sq mm, {rs(P('1.5','silver'))} in "
 f"1.5 sq mm, {rs(P('2.5','silver'))} in 2.5 sq mm and {rs(P('4.0','silver'))} in 4.0 sq mm (Silver FR) at Mount Cable "
 f"India. These are our current selling prices, on the Finolex list effective {EFFECTIVE_FROM}, which is the latest "
 f"list we hold. {TAX_NOTE}</strong></p>"
 "<h2>Finolex price today, 90 m coil, every size and grade</h2>" + _all + NOTE +
 "<h2>Has the Finolex price gone up?</h2>"
 "<p>Finolex revises its price list whenever copper and the rupee move far enough, upward or downward. A coil of "
 f"house wire is mostly copper, so the list follows the metal. The list in force here took effect on {EFFECTIVE_FROM}. "
 "When Finolex issues a new list, the figures on this page change with it; the reasoning is in "
 "<a href=\"copper-price-and-wire-rates-explained.html\">why wire prices keep changing</a>.</p>"
 "<h2>How to get today's confirmed rate</h2>"
 f"<p>Send your list on <a href=\"{W}\">WhatsApp {PH}</a>. The quote that comes back within 60 minutes is the rate "
 "for that day and holds for the order. Use it as a reference even if you buy elsewhere in Bangalore.</p>"
 "<h2>Is a much lower price a good deal?</h2>"
 "<p>Usually not. Wire is a low-margin product, so genuine prices from different authorised sellers sit close "
 "together. A coil offered far below the day's price is far more likely to be duplicate or refilled than a bargain.</p>"
 + VERIFY + LINKS + CTA,
 D,
 [("What is the Finolex wire price today?",
   f"At Mount Cable India today a 90 m Silver FR coil is Rs {P('1.0','silver'):,} in 1.0 sq mm, Rs {P('1.5','silver'):,} in 1.5 sq mm, Rs {P('2.5','silver'):,} in 2.5 sq mm and Rs {P('4.0','silver'):,} in 4.0 sq mm, taxes extra, on the Finolex list effective {EFFECTIVE_FROM}."),
  ("What is the price of Finolex 1.5 sq mm wire today?",
   f"A 90 m coil of Finolex 1.5 sq mm is Rs {P('1.5','silver'):,} in Silver FR, Rs {P('1.5','gold'):,} in Gold FR and Rs {P('1.5','frls90'):,} in FR-LSH at Mount Cable India, taxes extra."),
  ("What is the price of Finolex 2.5 sq mm wire today?",
   f"A 90 m coil of Finolex 2.5 sq mm is Rs {P('2.5','silver'):,} in Silver FR, Rs {P('2.5','gold'):,} in Gold FR and Rs {P('2.5','frls90'):,} in FR-LSH at Mount Cable India, taxes extra."),
  ("Has Finolex increased its wire price?",
   f"Finolex revises its list when copper and the rupee move. The list in force at Mount Cable India took effect on {EFFECTIVE_FROM}. Send your list on WhatsApp 88676 76700 for the rate confirmed for the day."),
  ("Why does the Finolex wire price change?",
   "A wire coil is mostly copper, an internationally traded metal priced in dollars. When copper or the rupee moves, Finolex issues a new list, so no honest seller can promise one fixed rate for the year.")],
 ("contractor-checking-price-list-phone.jpg", "Contractor checking today's Finolex wire price on a phone"))

# ------------------------------------------------------------ 2. FR vs FRLS
_fr_rows = [[f"{s} sq mm", f"<strong>{c(P(s,'silver'))}</strong>", f"<strong>{c(P(s,'frls90'))}</strong>",
             rs(P(s, 'frls90') - P(s, 'silver')), f"<strong>{c(P(s,'gold'))}</strong>"] for s in SZ]
_d15 = P("1.5", "frls90") - P("1.5", "silver")
_d25 = P("2.5", "frls90") - P("2.5", "silver")
POST_FRLS = (
 "finolex-fr-vs-frls-price",
 "Finolex FR vs FRLS Price: How Much More Does FR-LSH Cost?",
 f"Finolex FR vs FRLS price by size: FR-LSH (Flamegard) costs only {rs(_d15)} more than Silver FR on a 1.5 sq mm coil and {rs(_d25)} more on 2.5 sq mm. Full table and which to buy.",
 "Pricing",
 f"<p><strong>Finolex FR-LSH (sold as Flamegard, often called FRLS) costs only a little more than FR. On a 90 m coil "
 f"of 1.5 sq mm it is {rs(P('1.5','frls90'))} against {rs(P('1.5','silver'))} for Silver FR, a gap of {rs(_d15)}; on "
 f"2.5 sq mm the gap is {rs(_d25)}. FR-LSH is also priced below the Gold pack. For a house, the low-smoke grade is "
 "worth the difference.</strong></p>"
 "<h2>FR vs FR-LSH price, 90 m coil</h2>"
 + tbl(["Size", "Silver FR", "FR-LSH (Flamegard)", "FR-LSH costs more by", "Gold FR"], _fr_rows) + NOTE +
 "<h2>What you get for the difference</h2>"
 "<p>Both grades resist flame. FR-LSH insulation also gives off less smoke and less corrosive gas when it burns. "
 "In a house fire it is smoke, not flame, that stops people getting out, so the low-smoke grade matters most in "
 "flats, stairwells, bedrooms and any enclosed route. More in "
 "<a href=\"fr-vs-frls-vs-finolex-ultra.html\">FR vs FR-LSH vs Finolex Ultra</a>.</p>"
 "<h2>What it adds to a whole house</h2>"
 "<p>A 2BHK uses roughly 12 to 18 coils across all sizes. At the per-coil gaps in the table, choosing FR-LSH "
 "throughout adds well under a thousand rupees to a wire bill that runs to tens of thousands. Work out your own count with "
 "the <a href=\"../tools/wire-quantity-calculator.html\">wire quantity calculator</a>.</p>"
 "<h2>FR-LSH in 180 m and long coils</h2>"
 + tbl(["Size", "FR 180 m", "FR-LSH 180 m", "FR long coil", "FR-LSH long coil"],
       [[f"{s} sq mm", c(P(s, 'fr180')), c(P(s, 'frls180')), f"{c(P(s,'long'))} ({LONG_LEN[s]})",
         f"{c(P(s,'frls_long'))} ({LONG_LEN[s]})"] for s in SZ]) + NOTE
 + VERIFY + LINKS + CTA,
 D,
 [("What is the price difference between Finolex FR and FRLS wire?",
   f"On a 90 m coil, Finolex FR-LSH costs Rs {_d15} more than Silver FR in 1.5 sq mm (Rs {P('1.5','frls90'):,} against Rs {P('1.5','silver'):,}) and Rs {_d25} more in 2.5 sq mm at Mount Cable India, taxes extra."),
  ("What is the Finolex FRLS wire price?",
   f"A 90 m coil of Finolex FR-LSH (Flamegard) is Rs {P('1.0','frls90'):,} in 1.0 sq mm, Rs {P('1.5','frls90'):,} in 1.5 sq mm, Rs {P('2.5','frls90'):,} in 2.5 sq mm, Rs {P('4.0','frls90'):,} in 4.0 sq mm and Rs {P('6.0','frls90'):,} in 6.0 sq mm at Mount Cable India, taxes extra."),
  ("Is FRLS wire worth the extra cost?",
   "For a house, yes. The gap per coil is small, and FR-LSH gives off less smoke and gas in a fire, which matters most in enclosed rooms and stairwells."),
  ("Is Finolex FRLS cheaper than Finolex Gold?",
   f"Yes. A 1.5 sq mm 90 m coil is Rs {P('1.5','frls90'):,} in FR-LSH and Rs {P('1.5','gold'):,} in Gold FR at Mount Cable India."),
  ("Is Flamegard the same as FRLS?",
   "Flamegard is Finolex's name for its FR-LSH wire, flame retardant with low smoke and halogen. In the trade it is usually called FRLS.")],
 ("house-under-construction-conduit-wiring.jpg", "House wiring in progress where FR-LSH wire is being pulled through conduit"))

# --------------------------------------------------------------- 3. online
POST_ONLINE = (
 "finolex-wire-online-price",
 "Finolex Wire Online Price 2026: Order Online, Pay After Delivery",
 f"Finolex wire online price: 1.5 sq mm {rs(P('1.5','silver'))}, 2.5 sq mm {rs(P('2.5','silver'))} per 90 m coil from an authorised distributor. How to order online in Bangalore and what to check on any online seller.",
 "Pricing",
 f"<p><strong>You can order Finolex wire online from Mount Cable India, an authorised Finolex distributor in Bangalore: "
 f"a 90 m coil is {rs(P('1.5','silver'))} in 1.5 sq mm and {rs(P('2.5','silver'))} in 2.5 sq mm (Silver FR). You order "
 "on WhatsApp or the website, the wire is delivered free across Bangalore by the next day, and you pay only after "
 f"it reaches your site. {TAX_NOTE}</strong></p>"
 "<h2>Finolex online price, 90 m coil</h2>" + _all + NOTE +
 "<h2>How ordering online works</h2>"
 f"<ol><li>Send your list on <a href=\"{W}\">WhatsApp {PH}</a>, or use the <a href=\"../buy-finolex-wires.html\">buy "
 "Finolex wires page</a> or the <a href=\"../quote.html\">quote form</a>. A photo of the electrician's list is enough.</li>"
 "<li>An itemised quote comes back within 60 minutes.</li>"
 "<li>Confirm, and the order is delivered to your site in Bangalore by the next day, often the same day.</li>"
 "<li>Scan the QR codes on the cartons, then pay in any mode. Nothing is paid in advance.</li></ol>"
 "<p>Karnataka towns outside Bangalore are supplied by transport, with freight shown on the quote.</p>"
 "<h2>What to check on any online seller</h2>"
 "<ul><li><strong>Who the seller is.</strong> On a marketplace the listing may be from any reseller. Look for an "
 "authorised dealer or distributor and a GST invoice in your name.</li>"
 "<li><strong>Sealed carton.</strong> Wire sold loose, cut or re-wound has no batch number and no QR codes.</li>"
 "<li><strong>Coil length.</strong> Compare per metre; a 'coil' may be 45 m, 90 m or 180 m.</li>"
 "<li><strong>Both QR codes</strong> on delivery, before the return window closes.</li>"
 "<li><strong>A price far below the rest</strong> is the usual sign of duplicate wire.</li></ul>"
 + VERIFY + LINKS + CTA,
 D,
 [("What is the Finolex wire price online?",
   f"From Mount Cable India, ordered online, a 90 m Silver FR coil is Rs {P('1.0','silver'):,} in 1.0 sq mm, Rs {P('1.5','silver'):,} in 1.5 sq mm and Rs {P('2.5','silver'):,} in 2.5 sq mm, taxes extra, with free next-day delivery in Bangalore."),
  ("Can I buy Finolex wire online in Bangalore?",
   "Yes. Order on WhatsApp 88676 76700 or on mountcable.com from Mount Cable India, an authorised Finolex distributor. Delivery is free across Bangalore by the next day and you pay after delivery."),
  ("Is it safe to buy Finolex wire online?",
   "It is safe when the seller is an authorised dealer, the carton arrives sealed, both QR codes verify and you get a GST invoice. Be careful with marketplace listings from unknown resellers and with prices far below the rest."),
  ("Do I have to pay in advance for an online order?",
   "Not at Mount Cable India. Payment is taken after the material reaches your site and you have checked the cartons."),
  ("What is the online price of Finolex Gold wire?",
   f"A 90 m coil of Finolex Gold FR is Rs {P('1.5','gold'):,} in 1.5 sq mm and Rs {P('2.5','gold'):,} in 2.5 sq mm at Mount Cable India, taxes extra.")],
 ("happy-customer-receiving-electrical-order.jpg", "Customer receiving a Finolex wire order placed online in Bangalore"))

# --------------------------------------------- 4. telephone and speaker cable
_n = lambda v: offer(v)
POST_TEL = (
 "finolex-telephone-speaker-cable-price",
 "Finolex Telephone Cable and Speaker Wire Price 2026",
 f"Finolex telephone cable price: 2 pair {rs(_n(TELEPHONE['2 pair'][1]))} per 90 m coil (0.5 mm). Every pair count from 1 to 100, plus Finolex speaker wire prices by size.",
 "Pricing",
 f"<p><strong>Finolex 2 pair telephone cable is {rs(_n(TELEPHONE['2 pair'][0]))} per 90 m coil in 0.4 mm and "
 f"{rs(_n(TELEPHONE['2 pair'][1]))} in 0.5 mm at Mount Cable India. Finolex speaker wire is "
 f"{rs(_n(SPEAKER_100M['1.5']))} per 100 m in 1.5 sq mm. Prices are on the Finolex list effective {EFFECTIVE_FROM}. "
 f"{TAX_NOTE}</strong></p>"
 "<h2>Finolex telephone cable price, 90 m coil</h2>"
 + tbl(["Pairs", "0.4 mm conductor", "0.5 mm conductor"],
       [[k, f"<strong>{rs(_n(a))}</strong>", f"<strong>{rs(_n(b))}</strong>"] for k, (a, b) in TELEPHONE.items()]) + NOTE +
 "<p>Use 2 pair for a single line or intercom point and 4 or 5 pair where the same run carries several extensions. "
 "The 0.5 mm conductor is the better choice for longer runs. For internet and Wi-Fi points use LAN cable instead: "
 "<a href=\"../price-lists/finolex-lan-cable-price-list.html\">Finolex Cat 6 and LAN cable prices</a>.</p>"
 "<h2>Finolex speaker wire price</h2>"
 + tbl(["Size", "25 m coil", "100 m coil"],
       [[f"{s} sq mm", f"<strong>{rs(_n(SPEAKER_25M[s]))}</strong>" if s in SPEAKER_25M else "—",
         f"<strong>{rs(_n(v))}</strong>"] for s, v in SPEAKER_100M.items()]) + NOTE +
 "<p>For a home theatre, 1.5 sq mm suits most runs; go to 2.5 sq mm for long runs to rear speakers. CCTV and "
 "co-axial cable: <a href=\"../price-lists/finolex-cctv-cable-price-list.html\">Finolex CCTV and co-axial prices</a>.</p>"
 + LINKS + CTA,
 D,
 [("What is the price of Finolex 2 pair telephone cable?",
   f"A 90 m coil of Finolex 2 pair telephone cable is Rs {_n(TELEPHONE['2 pair'][0]):,} in 0.4 mm and Rs {_n(TELEPHONE['2 pair'][1]):,} in 0.5 mm at Mount Cable India, taxes extra."),
  ("What is the price of Finolex 20 pair telephone cable?",
   f"A 90 m coil of Finolex 20 pair telephone cable is Rs {_n(TELEPHONE['20 pair'][0]):,} in 0.4 mm and Rs {_n(TELEPHONE['20 pair'][1]):,} in 0.5 mm at Mount Cable India, taxes extra."),
  ("What is the price of Finolex speaker wire 1.5 mm?",
   f"Finolex 1.5 sq mm speaker wire is Rs {_n(SPEAKER_25M['1.5']):,} for a 25 m coil and Rs {_n(SPEAKER_100M['1.5']):,} for 100 m at Mount Cable India, taxes extra."),
  ("Should I use telephone cable or LAN cable for internet?",
   "Use LAN cable (Cat 6) for internet and Wi-Fi points. Telephone cable is for voice lines and intercoms.")],
 ("networking-cable-installation-home-office.jpg", "Telephone and data cable being installed in a home office"))

# ----------------------------------------------------- 5. Legrand MCB by amp
_band = {r: d for r, d in LEGRAND_MCB_C}
_lo, _mid, _hi = _band["0.5 to 4 A"], _band["6 to 32 A"], _band["40 to 63 A"]


def _lp(mrp):
    return f"<s>{rs(mrp)}</s> <strong>{rs(lnet(mrp))}</strong>" if mrp else "—"


_amp_rows = []
for amp in ("6 A", "10 A", "16 A", "20 A", "25 A", "32 A"):
    _amp_rows.append([amp, _lp(_mid["SP"]), _lp(_mid["DP"]), _lp(_mid["TP"]), _lp(_mid["FP"])])
for amp in ("40 A", "50 A", "63 A"):
    _amp_rows.append([amp, _lp(_hi["SP"]), _lp(_hi["DP"]), _lp(_hi["TP"]), _lp(_hi["FP"])])
for amp, d in LEGRAND_MCB_HI:
    _amp_rows.append([amp, _lp(d.get("SP")), _lp(d.get("DP")), _lp(d.get("TP")), _lp(d.get("FP"))])
_dmid = dict(LEGRAND_MCB_D)["6 to 32 A"]
POST_LEGRAND_MCB = (
 "legrand-mcb-price-by-ampere",
 "Legrand MCB Price by Ampere: 6A, 16A, 32A, 63A (2026, 65% Off)",
 f"Legrand DX3 MCB price by rating: a 6A to 32A single pole MCB is {rs(lnet(_mid['SP']))} net (MRP {rs(_mid['SP'])}), 40A to 63A is {rs(lnet(_hi['SP']))}. SP, DP, TP and FP for every ampere rating.",
 "Pricing",
 f"<p><strong>A Legrand DX3 single pole MCB costs {rs(lnet(_mid['SP']))} at Mount Cable India in any rating from 6A to "
 f"32A (MRP {rs(_mid['SP'])}, less {LEGRAND_DISCOUNT}%), and {rs(lnet(_hi['SP']))} in 40A, 50A or 63A (MRP "
 f"{rs(_hi['SP'])}). Legrand prices MCBs in bands, so a 6A, 16A and 32A MCB of the same pole count cost the same. "
 "Prices are for C curve, the curve used in homes.</strong></p>"
 "<h2>Legrand DX3 MCB price by ampere rating, C curve</h2>"
 + tbl(["Rating", "Single pole (SP)", "Double pole (DP)", "Triple pole (TP)", "Four pole (FP)"], _amp_rows) +
 f'<p class="ptable-note">Struck-through figure is Legrand India MRP per unit including GST, from the Legrand Corp MPL 2026. '
 f'Bold figure is the Mount Cable India price at {LEGRAND_DISCOUNT}% off MRP.</p>'
 "<h2>Which rating goes where in a house</h2>"
 "<ul><li><strong>6A or 10A SP:</strong> lighting and fan circuits.</li>"
 "<li><strong>16A SP:</strong> socket circuits, kitchen points, geyser.</li>"
 "<li><strong>20A or 25A SP:</strong> air conditioner on its own circuit.</li>"
 "<li><strong>32A, 40A or 63A DP:</strong> the incomer at the distribution board, sized to the sanctioned load.</li></ul>"
 "<p>Match the MCB to the wire, not just the appliance: see <a href=\"../wire-and-mcb-for-ac-geyser.html\">wire and MCB "
 "for AC and geyser</a> and the <a href=\"../tools/mcb-selector.html\">MCB selector</a>.</p>"
 "<h2>C curve or D curve</h2>"
 f"<p>Homes use C curve. D curve is for motors and other loads with a high starting current; a D curve 6A to 32A "
 f"single pole MCB is {rs(lnet(_dmid['SP']))} (MRP {rs(_dmid['SP'])}). Full tables with SPN and TPN: "
 "<a href=\"../price-lists/legrand-mcb-price-list.html\">Legrand MCB price list</a>, "
 "<a href=\"../price-lists/legrand-rccb-price-list.html\">RCCB</a>, "
 "<a href=\"../price-lists/legrand-distribution-board-price-list.html\">distribution boards</a>, "
 "<a href=\"../legrand-mcb-best-price.html\">best price on Legrand MCBs</a>.</p>"
 "<h2>Check it is a genuine Legrand MCB</h2>"
 "<p>Buy in the sealed Legrand box with a GST invoice, and run the checks in "
 "<a href=\"../original-legrand-mcb.html\">original Legrand MCB: seven checks</a>. A price well below a stockist's net "
 "price is the warning sign.</p>"
 f'<p class="muted"><strong>Need a full distribution board priced?</strong> Send the list to <a href="{W}">WhatsApp {PH}</a> '
 'for an itemised quote within 60 minutes. Free next-day delivery across Bangalore, pay after delivery.</p>',
 D,
 [("What is the price of a Legrand 16A MCB?",
   f"A Legrand DX3 16A single pole C curve MCB is Rs {lnet(_mid['SP'])} at Mount Cable India (MRP Rs {_mid['SP']}, less {LEGRAND_DISCOUNT}%). The double pole is Rs {lnet(_mid['DP'])}."),
  ("What is the price of a Legrand 32A MCB?",
   f"A Legrand DX3 32A C curve MCB is Rs {lnet(_mid['SP'])} in single pole and Rs {lnet(_mid['DP'])} in double pole at Mount Cable India, against MRP of Rs {_mid['SP']} and Rs {_mid['DP']}."),
  ("What is the price of a Legrand 63A MCB?",
   f"A Legrand DX3 63A C curve MCB is Rs {lnet(_hi['SP']):,} in single pole, Rs {lnet(_hi['DP']):,} in double pole, Rs {lnet(_hi['TP']):,} in triple pole and Rs {lnet(_hi['FP']):,} in four pole at Mount Cable India, at {LEGRAND_DISCOUNT}% off MRP."),
  ("What is the price of a Legrand 6A MCB?",
   f"A Legrand DX3 6A single pole C curve MCB is Rs {lnet(_mid['SP'])} at Mount Cable India (MRP Rs {_mid['SP']}). Ratings from 6A to 32A are priced the same."),
  ("Why do Legrand 6A and 32A MCBs cost the same?",
   "Legrand prices the DX3 range in rating bands: 0.5 to 4A, 6 to 32A and 40 to 63A. Within a band every rating of the same pole count has the same MRP."),
  ("What discount do you give on Legrand MCBs?",
   f"Mount Cable India sells Legrand at {LEGRAND_DISCOUNT}% off MRP, with the MRP and the net price shown side by side on every Legrand price page.")],
 ("electrician-installing-mcb-distribution-board.jpg", "Electrician fitting Legrand MCBs into a distribution board"))

BLOG_PRICE_NOV = [POST_TODAY, POST_FRLS, POST_ONLINE, POST_TEL, POST_LEGRAND_MCB]


# FAQs appended to the per-grade price-list pages: one answer per size, so a
# search for "finolex gold 2.5 mm wire price" lands on a page that states it.
def grade_size_faqs(label, key, have=()):
    out = []
    for s in SZ:
        if s in have or not P(s, key):
            continue
        out.append((f"What is the Finolex {label} wire price for {s} sq mm?",
                    f"A 90 m coil of Finolex {label} {s} sq mm is Rs {P(s, key):,} at Mount Cable India, taxes extra, on the Finolex list effective {EFFECTIVE_FROM}."))
    return out


GRADE_FAQS = {
    "finolex-gold-wire": grade_size_faqs("Gold", "gold", have=("1.5",)),
    "finolex-silver-wire": grade_size_faqs("Silver", "silver", have=("1.5", "2.5")),
    "finolex-frls-wire": grade_size_faqs("FRLS", "frls90", have=("1.5", "2.5")),
    "finolex-ultra-wire": grade_size_faqs("Ultra", "ultra", have=("1.5", "2.5")),
}

# Per-metre prices for flexible and submersible cable, added to the per-metre post.
PER_METRE_EXTRA = (
    "<h2>Finolex flexible and submersible cable price per metre</h2>"
    + tbl(["Size", "Flexible 1 core", "Flexible 3 core", "Flat submersible 3 core"],
          [[f"{s} sq mm",
            ("₹" + format(offer(FLEXIBLE[s][0]) / 100, ".1f")) if s in FLEXIBLE and FLEXIBLE[s][0] else "—",
            ("₹" + format(offer(FLEXIBLE[s][3]) / 100, ".1f")) if s in FLEXIBLE and len(FLEXIBLE[s]) > 3 and FLEXIBLE[s][3] else "—",
            ("₹" + format(offer(FLAT_SUBMERSIBLE[s]) / 100, ".1f")) if s in FLAT_SUBMERSIBLE else "—"]
           for s in ("1.5", "2.5", "4.0", "6.0")])
    + '<p class="ptable-note">Price of the 100 m coil divided by 100. Full tables: '
      '<a href="../price-lists/finolex-flexible-cable-price-list.html">flexible cable</a>, '
      '<a href="../price-lists/finolex-submersible-cable-price-list.html">submersible cable</a>. Taxes extra.</p>'
    "<h2>Coil, bundle, roll or box</h2>"
    "<p>They are the same thing. A Finolex wire 'bundle', 'roll' or 'box' is one sealed coil, normally 90 metres, "
    "so the bundle price is the coil price in the table above.</p>")
PER_METRE_FAQS = [
    ("What is the Finolex wire bundle price?",
     f"A bundle is one sealed coil, normally 90 metres. At Mount Cable India a Finolex Silver FR bundle is Rs {P('1.0','silver'):,} in 1.0 sq mm, Rs {P('1.5','silver'):,} in 1.5 sq mm and Rs {P('2.5','silver'):,} in 2.5 sq mm, taxes extra."),
    ("What is the price of Finolex 6 sq mm submersible cable per metre?",
     f"About Rs {offer(FLAT_SUBMERSIBLE['6.0']) / 100:.1f} a metre for Finolex 3-core flat submersible cable in 6 sq mm (Rs {offer(FLAT_SUBMERSIBLE['6.0']):,} per 100 m) at Mount Cable India, taxes extra."),
]
