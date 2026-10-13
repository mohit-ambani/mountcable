# -*- coding: utf-8 -*-
"""Best-price pillar for Finolex in Bangalore (Oct 2026, owner brief: Mount Cable
must rank first for "best price / best pricing for Finolex" in Bangalore; the
Legrand twin is legrand-best-price-bangalore in data_seo_legrand).

Finolex rule unchanged: NET selling prices only, never the list price, never a
discount percentage. Every figure renders from data_finolex_mrp.
"""
import json
from data_finolex_mrp import HOUSE_WIRE, PACKS, LONG_LEN, offer, EFFECTIVE_FROM, TAX_NOTE

W = "https://wa.me/918867676700"
PH = "88676 76700"
SIZES = ["0.75", "1.0", "1.5", "2.5", "4.0", "6.0"]


def rs(n):
    return "₹" + format(int(round(n)), ",d")


def _hw(size, key):
    v = HOUSE_WIRE[size].get(key)
    return rs(offer(v, key)) if v else "—"


def _tbl(cols, rows):
    head = "".join(f"<th>{c}</th>" for c in cols)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="ptable-wrap"><table class="ptable"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


NOTE = (f'<p class="ptable-note">Mount Cable India selling prices per coil, current to the Finolex list effective '
        f'{EFFECTIVE_FROM}. {TAX_NOTE} Bulk and project quantities are priced lower still.</p>')

_all = [offer(v, k) for s in SIZES for k, v in HOUSE_WIRE[s].items()]
FINOLEX_OFFER_LD = ('<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org", "@type": "Product",
    "name": "Finolex house wire (Silver, Gold, Flamegard FR-LSH, Finoultra), 0.75 to 6.0 sq mm",
    "brand": {"@type": "Brand", "name": "Finolex"},
    "offers": {"@type": "AggregateOffer", "priceCurrency": "INR", "lowPrice": min(_all), "highPrice": max(_all),
               "offerCount": len(_all), "availability": "https://schema.org/InStock",
               "areaServed": {"@type": "City", "name": "Bengaluru"},
               "seller": {"@type": "Organization", "name": "Mount Cable India"}},
}, ensure_ascii=False) + "</script>")

FINOLEX_BEST_PRICE = {
 "slug": "finolex-best-price-bangalore", "cluster": "best", "jsonld": FINOLEX_OFFER_LD,
 "title": "Best Price for Finolex Wires in Bangalore (2026) | Best Finolex Pricing — Mount Cable India",
 "desc": f"Best price for Finolex wires in Bangalore from one of India's largest Finolex distributors. Net prices for every size of Silver, Gold, Flamegard FR-LSH and Finoultra, current to {EFFECTIVE_FROM}, free next-day delivery, pay at site after scanning both QR codes. Quote in 60 minutes on WhatsApp {PH}.",
 "h1": "Best price for Finolex wires in Bangalore",
 "badge": f"Distributor net prices · Finolex list wef {EFFECTIVE_FROM} · Quote in 60 minutes",
 "intro": "Every electrical shop in Bangalore sells Finolex, so the only question that matters is who gives the best price on genuine Finolex. A shop buys Finolex from a distributor and adds its margin. Mount Cable India is the distributor, one of the largest Finolex distributors in India, in Bangalore for 35 years, so our price starts one step closer to the factory.",
 "answer": f"Mount Cable India gives the best pricing for Finolex in Bangalore because it sells at distributor rates: a 90 m coil of Finolex 1.5 sq mm is {_hw('1.5','silver')} in Silver Pack, {_hw('1.5','frls90')} in Flamegard FR-LSH and {_hw('1.5','gold')} in Gold, and 2.5 sq mm is {_hw('2.5','silver')}, {_hw('2.5','frls90')} and {_hw('2.5','gold')}, taxes extra. Delivery is free the next day across Bangalore and you pay at site after scanning every coil. WhatsApp {PH} for an exact quote in 60 minutes.",
 "hero": ("wire-coils-warehouse-electrical-distributor.jpg", "Genuine Finolex wire coils in Mount Cable India's Bangalore godown, sold at the best distributor price"),
 "sections": [
  ("Finolex best price list, every size, 90 m coils",
   _tbl(["Size", "Silver Pack FR", "Gold Pack FR", "Flamegard FR-LSH", "Finoultra (HFFR)"],
        [(f"{s} sq mm", _hw(s, "silver"), _hw(s, "gold"), _hw(s, "frls90"), _hw(s, "ultra")) for s in SIZES]) + NOTE
   + "<p>Flamegard FR-LSH, the low-smoke safety grade, costs less than Gold and only a little more than Silver, which is why it is the grade we recommend for most homes.</p>"),
  ("Lowest price per metre: 180 m and long coils",
   _tbl(["Size", "FR 180 m", "FR-LSH 180 m", "FR long coil", "FR-LSH long coil", "Long coil"],
        [(f"{s} sq mm", _hw(s, "fr180"), _hw(s, "frls180"), _hw(s, "long"), _hw(s, "frls_long"), LONG_LEN[s]) for s in SIZES]) + NOTE
   + "<p>For apartments, row houses and builders, the 180 m project pack and the 300 m / 200 m long coils are the cheapest way to buy Finolex per metre. See <a href=\"bulk-finolex-wire-supplier-karnataka.html\">bulk Finolex supply</a>.</p>"),
  ("Why our Finolex price is the best in Bangalore",
   "<ul><li><strong>We are the distributor.</strong> A shop's price includes the distributor's margin and its own. Ours includes one.</li>"
   "<li><strong>Volume.</strong> We buy Finolex by the truckload and turn the stock fast, so we can price every coil tightly.</li>"
   "<li><strong>No hidden costs.</strong> Free next-day delivery across Bangalore, no loading charge, pay at your site.</li>"
   "<li><strong>Every range in stock.</strong> No substitution with a costlier grade because the one you asked for is out.</li></ul>"),
  ("How to compare Finolex quotes fairly",
   "<ol><li><strong>Same grade.</strong> Silver, Gold, Flamegard and Finoultra are different prices; make sure every quote names the grade.</li>"
   "<li><strong>Same coil length.</strong> 90 m, 180 m and 300 m coils differ; compare per coil of the same length.</li>"
   "<li><strong>Taxes.</strong> Our prices are before GST. Ask whether the other quote includes it.</li>"
   "<li><strong>Delivery and payment.</strong> Free delivery and pay-at-site are worth money; a cheap quote with transport extra often is not cheaper.</li></ol>"),
  ("Too cheap is not the best price",
   "<p>Wire is a 3 to 5 percent margin trade. A distributor's price is close to the floor for genuine Finolex, so a quote far below it means a short coil, thin copper or a counterfeit carton. The best price is the lowest price on a coil that is genuinely Finolex. Finolex cartons carry two QR codes, an outer one on the label and an inner one inside the box; scan both before you pay, with our <a href=\"finolex-wire-scanner.html\">Finolex wire scanner</a>. More in <a href=\"blog/original-finolex-wire-price-check.html\">why cheap Finolex is not Finolex</a>.</p>"),
  ("Best Finolex price, delivered across Bangalore",
   "<p>The same price applies wherever you are building in Bengaluru, with free next-day delivery from our Jayanagar and Chickpete showrooms:</p>{areas}"),
  ("Get the best Finolex price in 60 minutes",
   f"<ol><li>WhatsApp your list, or a photo of the electrician's memo, to <a href=\"{W}\">{PH}</a>.</li>"
   "<li>Receive an itemised Finolex quote within 60 minutes.</li>"
   "<li>Use it as a reference anywhere. No obligation to buy from us.</li></ol>"
   "<p>Or order line by line on the <a href=\"buy-finolex-wires.html\">buy Finolex wires</a> page. Every Finolex range: <a href=\"price-lists/finolex-price-list.html\">Finolex price list 2026</a>.</p>"),
 ],
 "faqs": [
  ("Who gives the best price for Finolex wires in Bangalore?", f"Mount Cable India, one of India's largest Finolex distributors, sells at distributor rates: a 1.5 sq mm 90 m coil is {_hw('1.5','silver')} in Silver Pack and {_hw('1.5','frls90')} in Flamegard FR-LSH, taxes extra, with free next-day delivery across Bangalore."),
  ("What is the best price for Finolex 1.5 sq mm wire?", f"{_hw('1.5','silver')} for a Silver Pack 90 m coil, {_hw('1.5','frls90')} for Flamegard FR-LSH, {_hw('1.5','gold')} for Gold and {_hw('1.5','ultra')} for Finoultra at Mount Cable India, current to {EFFECTIVE_FROM}, taxes extra."),
  ("What is the best price for Finolex 2.5 sq mm wire?", f"{_hw('2.5','silver')} for a Silver Pack 90 m coil, {_hw('2.5','frls90')} for Flamegard FR-LSH and {_hw('2.5','gold')} for Gold, taxes extra."),
  ("What is the best price for Finolex 4 sq mm and 6 sq mm wire?", f"4.0 sq mm: {_hw('4.0','silver')} Silver, {_hw('4.0','frls90')} FR-LSH. 6.0 sq mm: {_hw('6.0','silver')} Silver, {_hw('6.0','frls90')} FR-LSH, per 90 m coil, taxes extra."),
  ("Why is Mount Cable's Finolex price lower than my local shop?", "We are the distributor; the shop buys from a distributor and adds its own margin. Our price includes one margin, not two, plus free delivery."),
  ("Is a much cheaper Finolex quote a better deal?", "No. A distributor's price is close to the floor for genuine Finolex. Far below it means a short coil, thin copper or a fake carton. Scan both QR codes before paying."),
  ("Do you give a better Finolex price for bulk orders?", "Yes. 180 m and 300 m / 200 m coils cost less per metre, and project quantities are quoted lower still. Send the list for a quote."),
  ("How fast can I get a Finolex quote?", f"Within 60 minutes on WhatsApp {PH} during working hours, itemised per coil."),
 ],
}
