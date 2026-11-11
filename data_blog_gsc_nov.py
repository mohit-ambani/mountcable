# -*- coding: utf-8 -*-
"""Posts written for queries Search Console showed mountcable.com reaching but
not owning (six months to Nov 2026): pairwise wire-brand comparisons that were
only covered inside the four-brand post, Anchor Roma vs Penta, and the
"how many metres in one coil" question.

Framing, as in data_blog_compare.py: fair comment. Nothing here asserts a defect
in a named brand. Prices appear only where a list is on file (Finolex net,
Polycab list, Anchor MRP); other brands are described by positioning only.
"""
from data_finolex_mrp import HOUSE_WIRE, LONG_LEN, offer, EFFECTIVE_FROM
from data_blog_compare import POLY_ETIRA, POLY_MAXIMA
from data_brand_prices import ANCHOR_ROMA_CLASSIC, ANCHOR_ROMA_URBAN, ANCHOR_PENTA_MOD, ANCHOR_PENTA_PIANO

D = ("2026-11-11", "November 11, 2026")
W = "https://wa.me/918867676700"
PH = "88676 76700"


def _rs(n):
    return "₹" + format(int(round(n)), ",d")


CTA = (f'<p class="muted"><strong>Want both brands priced for your list?</strong> Send it to <a href="{W}">WhatsApp {PH}</a> '
       'and Mount Cable India will quote each brand line by line within 60 minutes, so you compare real figures. '
       'No obligation to buy from us.</p>')

SAME = ("<h2>What is the same in both</h2>"
        "<p>Both make ISI-marked copper house wire to IS 694, in FR and FR-LSH grades, in the usual 90 m coil and in "
        "the sizes a house needs: 1.0, 1.5, 2.5, 4.0 and 6.0 sq mm. A genuine coil of the right size from either "
        "brand will carry its rated current for the life of the house. The differences are in range naming, "
        "availability, price on the day and how easily you can check that the coil is genuine.</p>")

GENUINE = ("<h2>The check that matters more than the brand</h2>"
           "<p>In Bangalore the larger risk is not choosing the wrong one of two good brands. It is receiving a "
           "duplicate or refilled coil of either. Buy sealed cartons from an authorised dealer, take a GST invoice "
           "naming the brand, range and size, check the printing along the insulation, and be wary of any price "
           "far below what other authorised sellers quote. Brand-by-brand checks: "
           "<a href=\"how-to-identify-duplicate-polycab-wire.html\">Polycab</a>, "
           "<a href=\"how-to-identify-duplicate-rr-kabel-wire.html\">RR Kabel</a>, "
           "<a href=\"how-to-identify-duplicate-kei-wire.html\">KEI</a>, "
           "<a href=\"how-to-identify-original-finolex-wire.html\">Finolex</a>.</p>")

MORE = ("<h2>Related comparisons</h2><ul>"
        "<li><a href=\"finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html\">Finolex vs Polycab vs RR Kabel vs KEI</a></li>"
        "<li><a href=\"../finolex-vs-polycab-wire.html\">Finolex vs Polycab</a></li>"
        "<li><a href=\"polycab-vs-rr-kabel-wire-which-is-better.html\">Polycab vs RR Kabel</a></li>"
        "<li><a href=\"polycab-vs-kei-wire-which-is-better.html\">Polycab vs KEI</a></li>"
        "<li><a href=\"kei-vs-rr-kabel-wire-which-is-better.html\">KEI vs RR Kabel</a></li>"
        "<li><a href=\"kei-vs-finolex-wire-which-is-better.html\">KEI vs Finolex</a></li>"
        "<li><a href=\"rr-kabel-vs-finolex-wire-which-is-better.html\">RR Kabel vs Finolex</a></li></ul>")

POLYCAB = ("<p><strong>Polycab</strong> is India's largest wire and cable manufacturer by sales. Its house-wire "
           "ranges include Etira (FR) and Maxima (HR-FR), with FR-LSH and halogen-free options above them, and it "
           "sells a wide catalogue of switchgear, fans and lighting alongside. Because of its scale, Polycab is "
           "stocked by a very large number of retailers and most sizes and colours are available on the day.</p>")
RRKABEL = ("<p><strong>RR Kabel</strong>, part of the RR Global group, is one of India's large house-wire makers and "
           "a significant exporter. Its house-wire ranges run from FR wire up to low-smoke halogen-free wire, and "
           "the brand leans on its international product certifications in its marketing. In Bangalore it is "
           "stocked by fewer retailers than Polycab, so one colour or size may need a day's notice.</p>")
KEI = ("<p><strong>KEI Industries</strong>, based in Delhi, built its reputation on LT and HT power cable, control "
       "and instrumentation cable, and added house wire later. Its residential lines (Homecab and Conflame) sit "
       "beside a much larger industrial catalogue. KEI house wire is stocked by fewer retailers and is more often "
       "ordered against a requirement, but it is a natural choice when the same order includes power cable.</p>")


def _poly_table():
    rows = "".join(f"<tr><td>{s} sq mm</td><td>{_rs(POLY_ETIRA[s])}</td><td>{_rs(POLY_MAXIMA[s])}</td></tr>" for s in POLY_ETIRA)
    return ('<div class="ptable-wrap"><table class="ptable"><thead><tr><th>Size (90 m coil)</th><th>Polycab Etira FR, list</th>'
            '<th>Polycab Maxima HR-FR, list</th></tr></thead><tbody>' + rows + '</tbody></table></div>'
            '<p class="ptable-note">Polycab list prices from the distributor lists of June to August 2026, before trade '
            'discount and tax. The price you pay is lower; ask for a quote.</p>')


def _vs(a, b, a_html, b_html, lead, choose_a, choose_b, price_html):
    return (f"<p><strong>{lead}</strong></p>"
            f"<h2>The two brands</h2>{a_html}{b_html}"
            + SAME +
            f"<h2>Price: {a} vs {b}</h2>{price_html}"
            f"<h2>Choose {a} if</h2><ul>{''.join(f'<li>{x}</li>' for x in choose_a)}</ul>"
            f"<h2>Choose {b} if</h2><ul>{''.join(f'<li>{x}</li>' for x in choose_b)}</ul>"
            + GENUINE + MORE + CTA)


_PRICE_NOTE_NO_LIST = ("<p>On the same grade the two are priced within a few percent of each other, and the order "
                       "changes from month to month as each company revises its list for copper. Compare like with "
                       "like: FR against FR, FR-LSH against FR-LSH, the same size and the same coil length. We do not "
                       "publish a figure for a brand whose current list we do not hold; send the list and we will "
                       "quote both.</p>")

# One coil: lengths by size, from the Finolex list.
_coil_rows = "".join(
    f"<tr><td>{s} sq mm</td><td>90 m</td><td>180 m</td><td>{LONG_LEN[s]}</td></tr>" for s in ("1.0", "1.5", "2.5", "4.0", "6.0"))
_per_m = {s: offer(HOUSE_WIRE[s]["silver"], "silver") / 90 for s in ("1.0", "1.5", "2.5", "4.0")}

# Anchor: comparable items across the three ranges.
_rc = dict((d, p) for _c, d, p in ANCHOR_ROMA_CLASSIC)
_ru = dict((d, p) for _c, d, p in ANCHOR_ROMA_URBAN)
_pm = dict((d, p) for _c, d, p in ANCHOR_PENTA_MOD)
_pp = dict((d, p) for _c, d, p in ANCHOR_PENTA_PIANO)
_anchor_table = (
    '<div class="ptable-wrap"><table class="ptable"><thead><tr><th>Item</th><th>Penta Modular</th><th>Roma Classic</th>'
    '<th>Roma Urban</th></tr></thead><tbody>'
    f"<tr><td>One-way switch</td><td>{_rs(_pm['6AX one-way switch, 1 module'])} (6AX)</td><td>{_rs(_rc['10AX one-way switch'])} (10AX)</td><td>{_rs(_ru['10AX one-way switch, 1 module'])} (10AX)</td></tr>"
    f"<tr><td>Two-way switch</td><td>{_rs(_pm['6AX two-way switch, 1 module'])} (6AX)</td><td>{_rs(_rc['10AX two-way switch'])} (10AX)</td><td>{_rs(_ru['10AX two-way switch, 1 module'])} (10AX)</td></tr>"
    f"<tr><td>6A 3-pin socket</td><td>{_rs(_pm['6A 3-pin socket with shutter, 2 module'])}</td><td>{_rs(_rc['6A 3-pin socket'])}</td><td>{_rs(_ru['6A 3-pin socket with shutter, 2 module'])}</td></tr>"
    f"<tr><td>16A 3-pin socket</td><td>{_rs(_pm['16A 3-pin socket, 2 module'])}</td><td>{_rs(_rc['16A 3-pin socket'])}</td><td>{_rs(_ru['16A 3-pin socket with shutter, 2 module'])}</td></tr>"
    f"<tr><td>Blank plate</td><td>{_rs(_pm['Blank plate, 1 module'])}</td><td>{_rs(_rc['Blank plate single'])}</td><td>{_rs(_ru['Blank plate, 1 module'])}</td></tr>"
    '</tbody></table></div><p class="ptable-note">MRP per piece from the Anchor by Panasonic pricelist of April 2026. '
    'Cover plates are priced separately. The price you pay is below MRP; ask for a quote.</p>')

BLOG_GSC_NOV = [

("polycab-vs-rr-kabel-wire-which-is-better",
 "Polycab vs RR Kabel Wire: Which Is Better for a House?",
 "Polycab and RR Kabel both make ISI copper house wire. Where each is strong, how the ranges and prices compare, and which one a Bangalore home should choose.",
 "Comparison",
 _vs("Polycab", "RR Kabel", POLYCAB, RRKABEL,
     "Polycab and RR Kabel are both sound choices for house wiring: both are ISI-marked copper wire in FR and FR-LSH "
     "grades. Polycab wins on availability, because almost every shop stocks every size and colour. RR Kabel is the "
     "one to pick if you want its halogen-free range or your electrician already works with it. On a genuine coil of "
     "the same grade and size, neither is the weaker wire.",
     ["you want every size and colour available the same day from almost any shop",
      "you are also buying Polycab switchgear, fans or lighting and want one brand on the bill",
      "your electrician is used to it and has leftover coils in the same colours"],
     ["you specifically want a low-smoke halogen-free wire and RR Kabel's is the one quoted to you",
      "the RR Kabel quote for the same grade is lower on the day",
      "you are happy to order a day ahead for a size or colour that is not on the shelf"],
     _poly_table() + _PRICE_NOTE_NO_LIST),
 D,
 [("Which is better, Polycab or RR Kabel?",
   "Both are ISI-marked copper house wire and both are sound for a home. Polycab is easier to find in every size and colour; RR Kabel is a good pick for its halogen-free range or if it is priced lower on the day. The grade, the size and a genuine coil matter more than which of the two you choose."),
  ("Is RR Kabel cheaper than Polycab?",
   "On the same grade they are usually within a few percent of each other and the order changes as each brand revises its list for copper. Compare the same grade, size and coil length, and ask for both to be quoted on your actual list."),
  ("Is RR Kabel a good brand for house wiring?",
   "Yes. RR Kabel is one of India's large house-wire makers, with FR, FR-LSH and halogen-free ranges. Buy sealed coils from an authorised dealer with a GST invoice."),
  ("Can I mix Polycab and RR Kabel wire in one house?",
   "There is no technical problem if the sizes and grades are right, but one brand through the house keeps colours matched for later extensions and keeps the warranty in one place."),
  ("How do I check a Polycab or RR Kabel coil is original?",
   "Buy sealed cartons from an authorised dealer, check the printing along the insulation and the label details, take a GST invoice naming the brand, range and size, and be wary of a price far below other authorised sellers.")],
 ("wire-coils-warehouse-electrical-distributor.jpg", "Polycab and RR Kabel house wire coils at an electrical distributor in Bangalore")),

("polycab-vs-kei-wire-which-is-better",
 "Polycab vs KEI Wire: Which Is Better for House Wiring?",
 "Polycab and KEI compared for house wiring: ranges, availability, price and which suits a home or a project in Bangalore. Also answers whether KEI wire is good.",
 "Comparison",
 _vs("Polycab", "KEI", POLYCAB, KEI,
     "For house wiring, Polycab is the easier choice because every size and colour is on the shelf in most shops. KEI "
     "is a good wire and the better choice when the same order includes power or control cable, which is where KEI's "
     "depth is. Both are ISI-marked copper wire, and a genuine coil of either will last the life of the house.",
     ["the job is a house or flat and you want stock available the same day",
      "you want one brand across wire, switchgear and lighting",
      "you may need one more coil in a particular colour at short notice"],
     ["the order also has armoured power cable, control cable or a long sub-main",
      "it is a project or commercial job where KEI is already specified",
      "the KEI quote for the same grade is lower and you can wait for stock"],
     _poly_table() + _PRICE_NOTE_NO_LIST),
 D,
 [("Which is better, Polycab or KEI wire?",
   "For a house, Polycab is easier because every size and colour is widely stocked. KEI is equally sound wire and suits orders that also include power or control cable. Both are ISI-marked copper wire."),
  ("Is KEI wire good for house wiring?",
   "Yes. KEI makes ISI-marked copper house wire in its Homecab and Conflame lines. Its reputation was built on industrial power and control cable, and its house wire is stocked by fewer retailers, so it is more often ordered against a requirement."),
  ("Is KEI cheaper than Polycab?",
   "On the same grade the two are close, and the order changes as each brand revises its list. Ask for both to be quoted on the same sizes, grade and coil length."),
  ("Which brand is better for a commercial project, Polycab or KEI?",
   "Both are used widely on projects. KEI is often specified where the package is heavy on power and control cable; Polycab where the package also includes switchgear and lighting. Follow the consultant's specification where there is one."),
  ("How do I avoid duplicate Polycab or KEI wire?",
   "Buy sealed cartons from an authorised dealer with a GST invoice, check the label and the printing on the insulation, and question any price far below other authorised sellers.")],
 ("contractor-bulk-order-loading-warehouse.jpg", "Polycab and KEI cable being loaded for a project order in Bangalore")),

("kei-vs-rr-kabel-wire-which-is-better",
 "KEI vs RR Kabel Wire: Which Is Better?",
 "KEI and RR Kabel compared for house wiring and projects: what each brand is known for, availability in Bangalore, price and how to choose.",
 "Comparison",
 _vs("KEI", "RR Kabel", KEI, RRKABEL,
     "KEI and RR Kabel are both ISI-marked copper house wire and either is a sound choice. RR Kabel is the more "
     "house-wire-focused of the two, with a halogen-free range; KEI is the stronger name in power and control cable. "
     "For a home, pick whichever is quoted lower in the grade you want and is in stock; for a job with power cable in "
     "it, KEI is the natural fit.",
     ["the same order has power cable, control cable or a long sub-main",
      "KEI is specified by the consultant or the builder",
      "the KEI price for the same grade is lower on the day"],
     ["the job is purely house wiring and you want a house-wire-focused range",
      "you want a low-smoke halogen-free wire",
      "your electrician already uses RR Kabel and has matching colours"],
     _PRICE_NOTE_NO_LIST),
 D,
 [("Which is better, KEI or RR Kabel?",
   "Both are sound ISI-marked copper wire. RR Kabel is more focused on house wire and has a halogen-free range; KEI is stronger in power and control cable. For a home, choose on grade, stock and the quote on the day."),
  ("Is KEI or RR Kabel cheaper?",
   "They are close on the same grade, and the order shifts with each list revision. Get both quoted on the same sizes, grade and coil length."),
  ("Is RR Kabel better than KEI for a house?",
   "For a house the two are comparable. RR Kabel's range is built around house wire; KEI's house wire sits beside a large industrial catalogue. The right size, an FR-LSH grade and a genuine coil matter more."),
  ("Are KEI and RR Kabel wires ISI marked?",
   "Yes. Both brands sell ISI-marked copper house wire to IS 694. Check the mark and the printing on the insulation of the coil you receive."),
  ("Where can I buy KEI or RR Kabel wire in Bangalore?",
   "Mount Cable India stocks both, alongside Finolex and Polycab, with free next-day delivery across Bangalore. WhatsApp 88676 76700 for a quote within 60 minutes.")],
 ("electrician-hands-stripping-wire-closeup.jpg", "Electrician stripping copper house wire during a wiring job")),

("anchor-roma-vs-penta-switches",
 "Anchor Roma vs Penta: Which Switch Range to Buy (2026 Prices)",
 "Anchor Roma Classic, Roma Urban and Penta compared: what each range is, the 2026 MRP of the same switch in each, and which suits a new home, a rental or a wooden board.",
 "Comparison",
 "<p><strong>Roma is Anchor's mainstream modular switch range and the right choice for a new home; Penta is the "
 "economy range, sold both as Penta Modular and as the older non-modular Penta piano switch for wooden boards. A "
 f"one-way switch is {_rs(_pm['6AX one-way switch, 1 module'])} MRP in Penta Modular (6AX), {_rs(_rc['10AX one-way switch'])} "
 f"in Roma Classic (10AX) and {_rs(_ru['10AX one-way switch, 1 module'])} in Roma Urban (10AX).</strong></p>"
 "<h2>What each range is</h2>"
 "<ul><li><strong>Penta piano</strong> is the non-modular switch that screws on to a wooden or sheet board. It is "
 f"the cheapest option (a 6A one-way switch is {_rs(_pp['Penta Deluxe 6A one-way switch'])} MRP) and is used for "
 "rentals, utility areas and repairs to old boards.</li>"
 "<li><strong>Penta Modular</strong> is the economy modular range: modules clip into a plate over a concealed box.</li>"
 "<li><strong>Roma Classic</strong> is the long-running modular range most Bangalore electricians know, with the "
 "widest spares availability.</li>"
 "<li><strong>Roma Urban</strong> is the current design-led Roma range, with a slimmer plate and a higher price.</li></ul>"
 "<h2>Price of the same item in each range</h2>" + _anchor_table +
 "<p>Full lists: <a href=\"../price-lists/anchor-panasonic-price-list.html\">Anchor Panasonic price list 2026</a>.</p>"
 "<h2>Which to choose</h2>"
 "<ul><li><strong>New home you will live in:</strong> Roma Classic for value, Roma Urban if the look matters and the "
 "budget allows.</li><li><strong>Rental flat or tight budget:</strong> Penta Modular.</li>"
 "<li><strong>Old wooden board, shed, utility area:</strong> Penta piano.</li></ul>"
 "<p>Choose before the conduit stage. Box sizes and module widths are fixed once the boxes are in the wall, and "
 "Roma and Penta plates are not interchangeable.</p>"
 "<h2>Check it is genuine</h2>"
 "<p>Roma Classic is the most widely fitted modular switch in India and the most copied. See "
 "<a href=\"how-to-identify-duplicate-anchor-switches.html\">how to identify duplicate Anchor switches</a>, and "
 "compare with <a href=\"greatwhite-vs-anchor-switches.html\">Greatwhite vs Anchor</a> and "
 "<a href=\"../legrand-vs-anchor-switches.html\">Legrand vs Anchor</a>.</p>" + CTA,
 D,
 [("What is the difference between Anchor Roma and Penta?",
   "Roma is Anchor's mainstream modular range (Roma Classic, Roma Urban, Roma Plus). Penta is the economy range, sold as Penta Modular and as the non-modular Penta piano switch for wooden boards. Roma costs more and has the wider choice of modules and plates."),
  ("Which is better, Roma or Penta?",
   "For a new home, Roma: it is the mainstream range with the widest spares. Penta Modular suits rentals and tight budgets, and Penta piano suits old wooden boards and utility areas."),
  ("What is the price of an Anchor Roma switch in 2026?",
   f"On the April 2026 Anchor pricelist a 10AX one-way switch is Rs {_rc['10AX one-way switch']} MRP in Roma Classic and Rs {_ru['10AX one-way switch, 1 module']} in Roma Urban. Cover plates are priced separately, and the selling price is below MRP."),
  ("What is the price of an Anchor Penta switch in 2026?",
   f"On the April 2026 Anchor pricelist a 6AX one-way switch is Rs {_pm['6AX one-way switch, 1 module']} MRP in Penta Modular, and a Penta Deluxe 6A piano switch is Rs {_pp['Penta Deluxe 6A one-way switch']} MRP."),
  ("Can I fit Roma switches in a Penta plate?",
   "No. Roma and Penta use different plates and frames, so decide the range before the boxes are fixed in the wall.")],
 ("woman-homeowner-choosing-modular-switches.jpg", "Homeowner comparing Anchor Roma and Penta switch ranges at a Bangalore showroom")),

("how-many-metres-in-one-coil-of-wire",
 "How Many Metres Is One Coil of Wire? 90 m, 180 m, 300 m Explained",
 "One coil of house wire in India is normally 90 metres. Coil lengths by size, how to price wire per metre, and how many coils a house needs.",
 "Buying Guide",
 "<p><strong>One coil of house wire in India is normally 90 metres. Finolex also sells 45 m, 180 m and long coils of "
 "300 m (1.0 to 2.5 sq mm) or 200 m (4.0 and 6.0 sq mm). Always check the length printed on the carton, because a "
 "price quoted 'per coil' means nothing until you know the metres.</strong></p>"
 "<h2>Coil lengths by size</h2>"
 '<div class="ptable-wrap"><table class="ptable"><thead><tr><th>Size</th><th>Standard coil</th><th>Double coil</th>'
 f'<th>Long coil</th></tr></thead><tbody>{_coil_rows}</tbody></table></div>'
 '<p class="ptable-note">Finolex house wire. Other brands also sell 90 m as the standard coil; project lengths vary by brand.</p>'
 "<h2>How to work out the price per metre</h2>"
 "<p>Divide the coil price by the metres in the coil. At Mount Cable India's current Finolex Silver FR prices that is "
 f"about {_rs(_per_m['1.0'])} a metre for 1.0 sq mm, {_rs(_per_m['1.5'])} for 1.5 sq mm, {_rs(_per_m['2.5'])} for "
 f"2.5 sq mm and {_rs(_per_m['4.0'])} for 4.0 sq mm, taxes extra, on the list effective {EFFECTIVE_FROM}. "
 "Longer coils cost less per metre and leave fewer joints. Per-size prices: "
 "<a href=\"finolex-1-mm-wire-price.html\">1.0</a>, <a href=\"finolex-1-5-mm-wire-price.html\">1.5</a>, "
 "<a href=\"finolex-2-5-mm-wire-price.html\">2.5</a>, <a href=\"finolex-4-mm-wire-price.html\">4.0</a>, "
 "<a href=\"finolex-6-mm-wire-price.html\">6.0 sq mm</a>.</p>"
 "<h2>Why 90 metres</h2>"
 "<p>The 90 m coil is the long-standing trade standard for house wire in India; it replaced the older 100-yard "
 "coil, which is about 91 metres. Wire is sold by the coil, not cut to length, because a sealed carton is what "
 "carries the batch number, the QR codes and the warranty.</p>"
 "<h2>How many coils a house needs</h2>"
 "<p>A 2BHK typically needs 3 to 4 coils of 1.0 sq mm, 4 to 6 of 1.5 sq mm, 3 to 5 of 2.5 sq mm and 1 to 2 of "
 "4.0 sq mm, depending on the number of points and the run from the distribution board. Work out your own figure "
 "with the <a href=\"../tools/wire-quantity-calculator.html\">wire quantity calculator</a> or read "
 "<a href=\"how-much-wire-required-2bhk-3bhk-house.html\">how much wire a 2BHK or 3BHK needs</a>.</p>"
 "<h2>Check the length you were sold</h2>"
 "<p>Genuine wire has the running length printed along the insulation at every metre, so the first and last "
 "markings on a coil tell you its length. A coil sold as 90 m that measures short is a standard trick with loose "
 "or re-wound wire. Buy sealed cartons.</p>" + CTA.replace("both brands", "your list"),
 D,
 [("How many metres are there in one coil of wire?",
   "One coil of house wire in India is normally 90 metres. Finolex also sells 45 m and 180 m coils, and long coils of 300 m in 1.0 to 2.5 sq mm and 200 m in 4.0 and 6.0 sq mm. The length is printed on the carton."),
  ("How many metres is one coil of 2.5 sq mm wire?",
   "The standard coil is 90 metres. In Finolex, 2.5 sq mm is also sold in 180 m and 300 m coils."),
  ("How do I calculate the wire price per metre?",
   "Divide the coil price by the number of metres in the coil. Compare brands and coil lengths per metre, not per coil, because a 180 m or 300 m coil costs less per metre than a 90 m coil."),
  ("Is a 300 metre coil cheaper than 90 metre coils?",
   "Per metre, yes. A long coil works out cheaper than the same length bought as 90 m coils and leaves fewer joints. It suits a full house or a project; for a small job the 90 m coil avoids leftover wire."),
  ("How can I check a coil really has 90 metres?",
   "Genuine wire carries a running metre marking printed along the insulation. Read the marking at the two ends of the coil; the difference is the length. Buy sealed cartons, not loose or re-wound wire.")],
 ("wire-coils-warehouse-electrical-distributor.jpg", "Coils of house wire in 90 metre, 180 metre and 300 metre lengths at a distributor")),
]


# ---------------------------------------------------------------------------
# Finolex coil-length and per-metre price posts. Search Console (Nov 2026)
# shows hundreds of impressions a month at positions 10 to 12 for
# "finolex 2.5 mm 300 meter price", "... 180 meter", "... 1 coil price" and
# "... price per meter", with almost no clicks, because no page answered them
# directly. Every figure is computed from data_finolex_mrp.py (net only).
# ---------------------------------------------------------------------------
from data_finolex_mrp import TAX_NOTE
from data_blog_price_nov import PER_METRE_EXTRA, PER_METRE_FAQS

_SZ = ["0.75", "1.0", "1.5", "2.5", "4.0", "6.0"]
_P = lambda s, k: (offer(HOUSE_WIRE[s][k], k) if HOUSE_WIRE[s].get(k) else None)
_c = lambda v: _rs(v) if v else "—"
_m = lambda v, metres: ("₹" + format(v / metres, ".1f")) if v else "—"
_long_m = lambda s: int(LONG_LEN[s].split()[0])
_NOTE = (f'<p class="ptable-note">Mount Cable India selling prices per coil on the Finolex list effective {EFFECTIVE_FROM}. '
         f'{TAX_NOTE} Prices move with copper; larger quantities are priced better.</p>')
_BUY = ("<h2>Before you pay</h2><p>Buy sealed cartons, scan the outer QR on the label and the inner QR inside the box "
        "(<a href=\"../finolex-wire-scanner.html\">Finolex wire scanner</a>), and take a GST invoice naming the range, "
        "size and coil length. A long coil sold loose or re-wound has no batch number and no way to verify it.</p>")
_CTA2 = (f'<p class="muted"><strong>Want today\'s confirmed rate?</strong> Send your list to <a href="{W}">WhatsApp {PH}</a> '
         'for an itemised quote within 60 minutes. Free next-day delivery across Bangalore, pay after delivery.</p>')
_SIZE_LINKS = ("<p>Per-size pages: <a href=\"finolex-0-75-mm-wire-price.html\">0.75</a>, <a href=\"finolex-1-mm-wire-price.html\">1.0</a>, "
               "<a href=\"finolex-1-5-mm-wire-price.html\">1.5</a>, <a href=\"finolex-2-5-mm-wire-price.html\">2.5</a>, "
               "<a href=\"finolex-4-mm-wire-price.html\">4.0</a>, <a href=\"finolex-6-mm-wire-price.html\">6.0 sq mm</a>. "
               "Coil lengths: <a href=\"finolex-300-meter-wire-price.html\">300 m</a>, <a href=\"finolex-180-meter-wire-price.html\">180 m</a>, "
               "<a href=\"finolex-wire-price-per-meter.html\">price per metre</a>. Full list: "
               "<a href=\"../price-lists/finolex-price-list.html\">Finolex price list</a>.</p>")


def _tbl(cols, rows):
    return ('<div class="ptable-wrap"><table class="ptable"><thead><tr>' + "".join(f"<th>{c}</th>" for c in cols)
            + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
            + "</tbody></table></div>")


# --- 300 m (long coil)
_long_rows = [[f"{s} sq mm", LONG_LEN[s], f"<strong>{_c(_P(s, 'long'))}</strong>", _m(_P(s, 'long'), _long_m(s)),
               f"<strong>{_c(_P(s, 'frls_long'))}</strong>", _m(_P(s, 'frls_long'), _long_m(s))] for s in _SZ]
_p25l, _p15l, _p10l = _P("2.5", "long"), _P("1.5", "long"), _P("1.0", "long")
_POST_300 = (
 "finolex-300-meter-wire-price",
 "Finolex 300 Metre Wire Price 2026: 1.0, 1.5 and 2.5 sq mm Coil",
 f"Finolex 300 metre coil price: 2.5 sq mm is {_rs(_p25l)}, 1.5 sq mm {_rs(_p15l)} and 1.0 sq mm {_rs(_p10l)} in FR at Mount Cable India. Every size, FR and FR-LSH, with the price per metre.",
 "Pricing",
 f"<p><strong>A Finolex 300 metre coil costs {_rs(_p25l)} in 2.5 sq mm, {_rs(_p15l)} in 1.5 sq mm and {_rs(_p10l)} in "
 f"1.0 sq mm (FR grade) at Mount Cable India, on the Finolex list effective {EFFECTIVE_FROM}. {TAX_NOTE} The long coil "
 "is 300 m for 0.75 to 2.5 sq mm and 200 m for 4.0 and 6.0 sq mm.</strong></p>"
 "<h2>Finolex long coil price, every size</h2>"
 + _tbl(["Size", "Coil", "FR price", "FR per metre", "FR-LSH price", "FR-LSH per metre"], _long_rows) + _NOTE +
 "<h2>300 m coil or 90 m coils: which is cheaper?</h2>"
 f"<p>Per metre, the long coil. In 2.5 sq mm the 300 m FR coil works out to {_m(_p25l, 300)} a metre, against "
 f"{_m(_P('2.5', 'silver'), 90)} a metre for the 90 m Silver FR coil. The long coil also means fewer joints. "
 "It suits a whole house or a project where you know the quantity; for a small job the 90 m coil avoids leftover wire.</p>"
 "<h2>Is there a 300 m coil in 4 and 6 sq mm?</h2>"
 f"<p>No. In 4.0 and 6.0 sq mm the long coil is 200 m: {_c(_P('4.0', 'long'))} for 4.0 sq mm and "
 f"{_c(_P('6.0', 'long'))} for 6.0 sq mm in FR.</p>"
 + _BUY + _SIZE_LINKS + _CTA2,
 D,
 [("What is the price of Finolex 2.5 mm 300 metre wire?",
   f"At Mount Cable India a Finolex 2.5 sq mm 300 m coil is Rs {_p25l:,} in FR and Rs {_P('2.5','frls_long'):,} in FR-LSH, on the Finolex list effective {EFFECTIVE_FROM}. Taxes extra. That is about Rs {_p25l/300:.1f} a metre in FR."),
  ("What is the price of Finolex 1.5 mm 300 metre wire?",
   f"A Finolex 1.5 sq mm 300 m coil is Rs {_p15l:,} in FR and Rs {_P('1.5','frls_long'):,} in FR-LSH at Mount Cable India, taxes extra, on the list effective {EFFECTIVE_FROM}."),
  ("What is the price of Finolex 1 mm 300 metre wire?",
   f"A Finolex 1.0 sq mm 300 m coil is Rs {_p10l:,} in FR and Rs {_P('1.0','frls_long'):,} in FR-LSH at Mount Cable India, taxes extra, on the list effective {EFFECTIVE_FROM}."),
  ("Is a 300 metre coil cheaper than 90 metre coils?",
   "Per metre, yes. The long coil costs less per metre than the same length bought as 90 m coils and leaves fewer joints. It suits a full house or project where the quantity is known."),
  ("Does Finolex make a 300 m coil in 4 sq mm and 6 sq mm?",
   "No. In 4.0 and 6.0 sq mm the long coil is 200 metres. The 300 m coil is made in 0.75, 1.0, 1.5 and 2.5 sq mm.")],
 ("contractor-bulk-order-loading-warehouse.jpg", "Finolex 300 metre long coils being loaded for a house wiring order in Bangalore"))

# --- 180 m
_180_rows = [[f"{s} sq mm", f"<strong>{_c(_P(s, 'fr180'))}</strong>", _m(_P(s, 'fr180'), 180),
              f"<strong>{_c(_P(s, 'frls180'))}</strong>", _m(_P(s, 'frls180'), 180)] for s in _SZ]
_POST_180 = (
 "finolex-180-meter-wire-price",
 "Finolex 180 Metre Wire Price 2026: Every Size, FR and FR-LSH",
 f"Finolex 180 metre coil price: 2.5 sq mm is {_c(_P('2.5','fr180'))} and 1.5 sq mm {_c(_P('1.5','fr180'))} in FR at Mount Cable India. Every size in FR and FR-LSH, with price per metre.",
 "Pricing",
 f"<p><strong>A Finolex 180 metre coil costs {_c(_P('2.5','fr180'))} in 2.5 sq mm, {_c(_P('1.5','fr180'))} in 1.5 sq mm and "
 f"{_c(_P('1.0','fr180'))} in 1.0 sq mm (FR grade) at Mount Cable India, on the Finolex list effective {EFFECTIVE_FROM}. "
 f"{TAX_NOTE}</strong></p>"
 "<h2>Finolex 180 m coil price, every size</h2>"
 + _tbl(["Size", "FR 180 m", "FR per metre", "FR-LSH 180 m", "FR-LSH per metre"], _180_rows) + _NOTE +
 "<h2>When the 180 m coil makes sense</h2>"
 "<p>The 180 m coil is two standard coils in one length. It is the practical choice for a 2BHK or 3BHK where a "
 "size is needed in more than one coil: fewer joints than two 90 m coils, and easier to handle on site than a "
 "300 m coil. It is made in FR and FR-LSH; the Silver and Gold packs are 90 m only.</p>"
 + _BUY + _SIZE_LINKS + _CTA2,
 D,
 [("What is the price of Finolex 2.5 mm 180 metre wire?",
   f"At Mount Cable India a Finolex 2.5 sq mm 180 m coil is Rs {_P('2.5','fr180'):,} in FR and Rs {_P('2.5','frls180'):,} in FR-LSH, taxes extra, on the Finolex list effective {EFFECTIVE_FROM}."),
  ("What is the price of Finolex 1.5 mm 180 metre wire?",
   f"A Finolex 1.5 sq mm 180 m coil is Rs {_P('1.5','fr180'):,} in FR and Rs {_P('1.5','frls180'):,} in FR-LSH at Mount Cable India, taxes extra."),
  ("Is Finolex Gold available in a 180 metre coil?",
   "No. Finolex Silver and Gold packs are 90 m coils. The 180 m coil is made in FR and FR-LSH."),
  ("Is the 180 m coil cheaper per metre than the 90 m coil?",
   "Compare per metre on the day: divide each coil price by its length. The 180 m coil also saves a joint, which is the main practical reason to choose it.")],
 ("wire-coils-warehouse-electrical-distributor.jpg", "Finolex 180 metre house wire coils in stock at a Bangalore distributor"))

# --- per metre
_pm_rows = [[f"{s} sq mm", _m(_P(s, 'silver'), 90), _m(_P(s, 'gold'), 90), _m(_P(s, 'frls90'), 90),
             _m(_P(s, 'fr180'), 180), _m(_P(s, 'long'), _long_m(s))] for s in _SZ]
_coil_rows2 = [[f"{s} sq mm", f"<strong>{_c(_P(s, 'silver'))}</strong>", f"<strong>{_c(_P(s, 'gold'))}</strong>",
                f"<strong>{_c(_P(s, 'frls90'))}</strong>"] for s in _SZ]
_POST_PM = (
 "finolex-wire-price-per-meter",
 "Finolex Wire Price Per Metre and Per Coil (Bundle) 2026",
 f"Finolex wire price per metre: about {_m(_P('1.5','silver'),90)} for 1.5 sq mm and {_m(_P('2.5','silver'),90)} for 2.5 sq mm in Silver FR. Per-metre and 1-coil prices for every size and grade.",
 "Pricing",
 f"<p><strong>Finolex house wire works out to about {_m(_P('1.0','silver'),90)} a metre in 1.0 sq mm, "
 f"{_m(_P('1.5','silver'),90)} in 1.5 sq mm, {_m(_P('2.5','silver'),90)} in 2.5 sq mm, {_m(_P('4.0','silver'),90)} in "
 f"4.0 sq mm and {_m(_P('6.0','silver'),90)} in 6.0 sq mm (Silver FR, 90 m coil) at Mount Cable India, on the Finolex "
 f"list effective {EFFECTIVE_FROM}. {TAX_NOTE} Wire is sold by the sealed coil, not cut by the metre.</strong></p>"
 "<h2>Finolex price per metre, by size and coil</h2>"
 + _tbl(["Size", "Silver FR 90 m", "Gold FR 90 m", "FR-LSH 90 m", "FR 180 m", "FR long coil"], _pm_rows) +
 '<p class="ptable-note">Coil price divided by coil length. The long coil is 300 m up to 2.5 sq mm and 200 m in 4.0 and 6.0 sq mm.</p>'
 "<h2>Finolex 1 coil price (90 m)</h2>"
 + _tbl(["Size", "Silver FR", "Gold FR", "FR-LSH (Flamegard)"], _coil_rows2) + _NOTE + PER_METRE_EXTRA +
 "<h2>Why wire is not sold by the metre</h2>"
 "<p>A sealed carton is what carries the batch number, both QR codes and the warranty. Wire cut loose from a coil "
 "has none of them, and cut wire is the easiest way for duplicate material to reach a site. Use the per-metre "
 "figure to compare brands and coil lengths, then buy whole sealed coils. If you are unsure how many, the "
 "<a href=\"../tools/wire-quantity-calculator.html\">wire quantity calculator</a> gives the coil count, and "
 "<a href=\"how-many-metres-in-one-coil-of-wire.html\">this guide</a> explains coil lengths.</p>"
 + _BUY + _SIZE_LINKS + _CTA2,
 D,
 [("What is the price of Finolex wire per metre?",
   f"At Mount Cable India's current prices, Finolex Silver FR works out to about Rs {_P('1.0','silver')/90:.1f} a metre in 1.0 sq mm, Rs {_P('1.5','silver')/90:.1f} in 1.5 sq mm, Rs {_P('2.5','silver')/90:.1f} in 2.5 sq mm and Rs {_P('4.0','silver')/90:.1f} in 4.0 sq mm, taxes extra. Wire is sold by the sealed coil."),
  ("What is the price of Finolex 2.5 mm wire per metre?",
   f"About Rs {_P('2.5','silver')/90:.1f} a metre in Silver FR (90 m coil at Rs {_P('2.5','silver'):,}) and about Rs {_P('2.5','long')/300:.1f} a metre in the 300 m FR coil, taxes extra, on the list effective {EFFECTIVE_FROM}."),
  ("What is the price of one coil of Finolex 2.5 mm wire?",
   f"A 90 m coil of Finolex 2.5 sq mm is Rs {_P('2.5','silver'):,} in Silver FR, Rs {_P('2.5','gold'):,} in Gold FR and Rs {_P('2.5','frls90'):,} in FR-LSH at Mount Cable India, taxes extra."),
  ("What is the price of one coil of Finolex 6 mm wire?",
   f"A 90 m coil of Finolex 6.0 sq mm is Rs {_P('6.0','silver'):,} in Silver FR, Rs {_P('6.0','gold'):,} in Gold FR and Rs {_P('6.0','frls90'):,} in FR-LSH at Mount Cable India, taxes extra."),
  *PER_METRE_FAQS,
  ("Can I buy Finolex wire by the metre?",
   "House wire is sold by the sealed coil, because the carton carries the batch number, the QR codes and the warranty. Loose cut wire cannot be verified. Buy the nearest whole coil; surplus sealed coils are easy to return or resell.")],
 ("electrician-hands-stripping-wire-closeup.jpg", "Finolex copper house wire measured out during a wiring job"))

# Owner direction (11 Nov 2026): publish only Finolex and Legrand content. The
# Polycab / RR Kabel / KEI pairings and Anchor Roma vs Penta above are held back.
BLOG_GSC_NOV = [p for p in BLOG_GSC_NOV if p[0] == "how-many-metres-in-one-coil-of-wire"] + [_POST_300, _POST_180, _POST_PM]
