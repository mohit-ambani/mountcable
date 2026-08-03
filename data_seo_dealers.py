# -*- coding: utf-8 -*-
"""Finolex dealer / distributor landing pages (Karnataka + range-specific).

These are appended to SEO_PAGES in build.py and rendered by build_seo_page().
In addition to the original SEO page keys (slug, title, h1, desc, badge, intro,
sections, faqs) they use three optional keys that build_seo_page understands:

  answer   a self-contained, quotable answer rendered bolded as the first
           paragraph of the body. This is the paragraph an answer engine lifts,
           so it has to be true and complete standing on its own.
  hero     (filename in assets/img/people, alt text)
  cities   set True to render the Karnataka city grid where {cities} appears

House rules honoured here: no showrooms are claimed outside Bengaluru; prices
are approximate ranges only; free next-day delivery is a Bangalore promise and
is never extended to the rest of Karnataka in the copy.
"""

W = "https://wa.me/918867676700"
PH = "88676 76700"

# The two-code rule, worded identically to the rest of the site.
TWO_QR = ("""<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Code</th><th>Where it is</th><th>What it proves</th></tr></thead>
<tbody>
<tr><td><strong>Outer QR</strong></td><td>Printed on the carton label with the size, grade, coil length and batch</td><td>That the carton itself was produced by Finolex and is registered with them</td></tr>
<tr><td><strong>Inner QR</strong></td><td>Inside the box, reachable only after the carton is opened</td><td>That the contents are what Finolex packed — the check a repacker cannot pass</td></tr>
</tbody></table></div>
<p>Both codes matter, and the reason is specific: a genuine carton can be emptied and refilled with duplicate wire. In that case the outer code still verifies perfectly and only the inner code fails. Scanning the outer code alone is an incomplete check, and the people who refill cartons are counting on you stopping there.</p>""")

DEALER_CTA = (f'<p class="muted"><strong>Send the list, get the number.</strong> WhatsApp your sizes and quantities to '
              f'<a href="{W}">{PH}</a> and you will have an itemised quotation within 60 minutes. '
              f'There is no obligation to buy — plenty of people use our quote purely as a reference price to check '
              f'what someone else has offered them, and we are glad to be used that way.</p>')


DEALER_SEO_PAGES = [

# ------------------------------------------------------------------ 1
{"slug": "finolex-dealers-karnataka",
 "title": "Dealers of Finolex Wires in Karnataka | Mount Cable India, Bengaluru",
 "h1": "Dealers of Finolex wires in Karnataka",
 "desc": "Mount Cable India is one of the largest dealers and distributors of Finolex cables, supplying 100% original Finolex wires across Karnataka from two Bengaluru showrooms in Chickpete and Jayanagar. Every range in stock, best pricing in Bangalore, and you may scan any coil — or the entire stock — before you buy. WhatsApp 88676 76700.",
 "badge": "Finolex Dealer &amp; Distributor · Serving All of Karnataka",
 "intro": "Mount Cable India has sold Finolex wire in Bengaluru for 35 years and is one of the largest dealers and distributors of Finolex cables in the country. This page explains what we hold, what we supply across Karnataka, and the one check that separates a real Finolex dealer from a firm that merely says it is one.",
 "answer": "Mount Cable India is one of the largest dealers and distributors of Finolex wires and cables, operating from two showrooms in Bengaluru — Chickpete (BVK Iyengar Road) and Jayanagar — and supplying 100% original Finolex wire across Karnataka. Every range is in stock, pricing is the best in Bangalore, and you may scan any coil, or the entire stock, before you buy.",
 "hero": ("wire-coils-warehouse-electrical-distributor.jpg",
          "Finolex wire coils in stock at Mount Cable India, a Finolex dealer and distributor serving Karnataka from Bengaluru"),
 "sections": [
   ("Who is Mount Cable India?",
    "<p>We have been selling electrical material in Bengaluru for 35 years, from a main showroom at 10/3 Sri Complex, BVK Iyengar Road in Chickpete (560053) and a second showroom in Jayanagar (560011). Finolex is the line we are best known for, and we are one of the largest dealers and distributors of Finolex cables in India.</p>"
    "<p>What that means in practice is stock. Every Finolex range we list is physically held — not indented against your order, not promised for next week. If you need thirty coils of 2.5 sq mm on a Tuesday, they exist before you ask.</p>"),

   ("Careful: many firms claim to be Finolex dealers",
    "<p>This is the part of the page that matters most, and we would rather say it plainly than dress it up.</p>"
    "<p><strong>A great many firms — including large, impressive showrooms — will tell you they are Finolex dealers.</strong> Some are. Some are buying from whoever offers the best price that week. Some are selling repacked cartons. A showroom's size proves its marketing budget and nothing else, and confusing buyers on this point is a business model, not an accident.</p>"
    "<p>You cannot resolve this by judging the shop, the signage or the salesman. There is exactly one defence and it is absolute:</p>"
    "<p><strong>Scan every single QR code on every single coil — the outer code on the carton and the inner code inside it — and confirm 100% original material before you pay.</strong> Not a sample. Not the top box. Every coil, both codes. It takes twenty seconds each and it is the only check that cannot be talked around.</p>"
    + TWO_QR +
    "<p>Finolex's own verification portal is at check.finolex.com, and Finolex customer care is 1800-209-0166 if you want the company's word rather than ours. We tell every customer this, including the ones who then go and check our stock with it. That is the point.</p>"),

   ("What we hold in stock",
    "<p>All of it, all the time:</p>"
    "<div class=\"ptable-wrap\"><table class=\"ptable\"><thead><tr><th>Range</th><th>Coil</th><th>Grade</th><th>Common sizes</th></tr></thead><tbody>"
    "<tr><td><a href=\"finolex/90m-silver.html\">90M Silver</a></td><td>90 m</td><td>FR</td><td>0.75 to 6.0 sq mm</td></tr>"
    "<tr><td><a href=\"finolex/90m-gold.html\">90M Gold</a></td><td>90 m</td><td>FR, premium tier</td><td>0.75 to 6.0 sq mm</td></tr>"
    "<tr><td><a href=\"finolex/90m-frls.html\">90M FRLS (Flamegard)</a></td><td>90 m</td><td>FR-LSH</td><td>0.75 to 6.0 sq mm</td></tr>"
    "<tr><td><a href=\"finolex/180m.html\">180M</a></td><td>180 m</td><td>FR</td><td>0.75 to 6.0 sq mm</td></tr>"
    "<tr><td><a href=\"finolex/300m.html\">300M</a></td><td>300 m</td><td>FR</td><td>0.75 to 6.0 sq mm</td></tr>"
    "<tr><td><a href=\"finolex/300m-frls.html\">300M FRLS</a></td><td>300 m</td><td>FR-LSH</td><td>0.75 to 6.0 sq mm</td></tr>"
    "<tr><td><a href=\"finolex/ultra.html\">Finolex Ultra</a></td><td>90 / 180 m</td><td>LSZH, E-Beam</td><td>0.75 to 6.0 sq mm</td></tr>"
    "<tr><td><a href=\"finolex/co-axial-cables.html\">Co-axial</a></td><td>Various</td><td>RG series</td><td>RG-6, RG-11, RG-59</td></tr>"
    "<tr><td><a href=\"finolex/telephone-cables.html\">Telephone</a></td><td>Various</td><td>Multi-pair</td><td>1 to 10 pair</td></tr>"
    "<tr><td><a href=\"finolex/internet-lan-cables.html\">Internet / LAN</a></td><td>Box / reel</td><td>Cat5e, Cat6</td><td>UTP, outdoor</td></tr>"
    "</tbody></table></div>"
    "<p>Project packing is available on the house-wire sizes as well — see <a href=\"finolex-project-packing-dealers.html\">Finolex project packing</a> for what that means and when it is worth asking for.</p>"),

   ("Verify any coil, or the entire stock, before you buy",
    "<p>This is a standing offer and not a figure of speech. Before you commit to anything, you may:</p>"
    "<ul>"
    "<li><strong>Scan any coil in our showroom</strong> — pick the boxes yourself, we will open them.</li>"
    "<li><strong>Scan your entire consignment</strong> before it is despatched, with the verification record sent to you on WhatsApp.</li>"
    "<li><strong>Scan again at your own site</strong> when the material arrives, outer code and inner code, before any money changes hands.</li>"
    "</ul>"
    "<p>Inside Bangalore we deliver free by the next day and collect payment at your site precisely so that this sequence is possible. A seller who is reluctant to let you scan cartons before paying has already answered the only question that mattered.</p>"),

   ("Pricing: best in Bangalore, and why nobody can beat it by 15%",
    "<p>We give the best pricing and the highest discounts you will find in Bangalore on Finolex, because volume is what a distributor's economics are built on. But there is a floor under any honest price, and it is worth understanding.</p>"
    "<p>Genuine branded wire runs on a <strong>3 to 5 per cent dealer margin</strong>. The copper inside a coil has a market cost that every honest seller in India pays. So the entire space available for discounting is a few per cent — and a shop offering 15 or 20 per cent off a premium wire brand is not funding it out of generosity. It is funded by what is missing from the product: copper purity, conductor thickness, insulation quality, coil length, or the brand itself.</p>"
    "<p>Use that as a test. Our quote is the reference; if someone is far below it, the difference is inside the coil. Approximate ranges are on our <a href=\"price-lists/finolex-price-list.html\">Finolex price list page</a>, and the exact figure for your list comes back on WhatsApp within 60 minutes. Copper is a traded commodity, so we quote the day's rate rather than publishing a rate card that would be wrong by the time you read it.</p>"),

   ("Where we supply in Karnataka",
    "<p>Two things, stated separately so there is no confusion.</p>"
    "<p><strong>Inside Bengaluru:</strong> free next-day delivery to your site — often same day — with payment collected at the site after you have inspected and scanned the material. Two showrooms you can walk into.</p>"
    "<p><strong>Everywhere else in Karnataka:</strong> we supply against a written quotation, despatched by road transport from Bengaluru, with material and freight shown as separate lines so you can judge the landed cost honestly. <strong>We have no showrooms, branches or godowns outside Bengaluru and we will not pretend otherwise.</strong> For a full house of wiring or a project quantity, the distributor rate generally absorbs the freight comfortably; for three coils to a far district it does not, and we will tell you so rather than take the order.</p>"
    "{cities}"),

   ("Read what customers say",
    f"<p>We would rather you did not take our word for any of this. Mount Cable India's Google listing carries reviews from Bengaluru home builders, electricians and contractors who have bought Finolex from us — <a href=\"{{review}}\" target=\"_blank\" rel=\"noopener\">read the Google reviews about our Finolex wires</a> and judge for yourself.</p>"
    + DEALER_CTA),
 ],
 "faqs": [
   ("Who are the dealers of Finolex wires in Karnataka?", "Mount Cable India is one of the largest dealers and distributors of Finolex cables, operating from two showrooms in Bengaluru — Chickpete on BVK Iyengar Road and Jayanagar — and supplying 100% original Finolex wire across Karnataka. Every Finolex range is held in stock, and any coil or the entire consignment may be scanned and verified before you buy."),
   ("How do I know a Finolex dealer is genuine?", "Do not judge the showroom — judge the stock. Many firms, including large showrooms, claim to be Finolex dealers. The only reliable check is to scan every QR code on every coil: the outer code printed on the carton label, and the inner code found only after the carton is opened. Both must verify against Finolex's own portal at check.finolex.com. A genuine carton can be refilled with duplicate wire, in which case only the inner code fails."),
   ("Do you have a Finolex showroom outside Bengaluru?", "No. Mount Cable India has two showrooms, both in Bengaluru — Chickpete (BVK Iyengar Road, 560053) and Jayanagar (560011). We supply the rest of Karnataka by road transport against a written quotation, with freight shown as a separate line. We do not have branches or godowns in any other city and do not claim to."),
   ("Which Finolex ranges do you keep in stock?", "All of them: 90M Silver, 90M Gold, 90M FRLS, 180M, 300M, 300M FRLS and Finolex Ultra in every common house-wiring size from 0.75 to 6.0 sq mm, plus co-axial, telephone and Cat5e/Cat6 internet cables. Project packing is available on the house-wire sizes as well."),
   ("Can I check the wire before paying for it?", "Yes, and we encourage it. In the showroom you may pick cartons yourself and scan them. On a delivery inside Bangalore you scan at your own site and pay afterwards. On an outstation consignment we can scan the stock before dispatch and send you the record, and you scan again on arrival. Scan the outer code and the inner code on every coil, not a sample."),
   ("How much cheaper can a genuine Finolex dealer be?", "A few per cent, not fifteen. Genuine branded wire runs on a 3 to 5 per cent dealer margin because the copper inside has a market cost every honest seller pays. We give the best pricing and the highest discounts in Bangalore within that reality. Anyone quoting 15 to 20 per cent below the market is funding the gap with missing copper, a short coil or a counterfeit."),
   ("How do I get an exact Finolex price?", "WhatsApp your sizes and quantities to 88676 76700 and you will have an itemised quotation within 60 minutes. Published figures are approximate ranges only, because copper is a traded commodity and a fixed rate card goes stale within days. There is no obligation to buy — using our quote as a reference price to check another seller is a perfectly good reason to ask."),
 ]},

# ------------------------------------------------------------------ 2
{"slug": "finolex-silver-90m-dealers",
 "title": "Finolex Silver 90M Dealers | 100% Original, Distributor Price — Bengaluru & Karnataka",
 "h1": "Finolex Silver 90M dealers",
 "desc": "Finolex 90M Silver dealers in Bengaluru and across Karnataka. Mount Cable India holds every size from 0.75 to 6.0 sq mm in stock, at the best pricing in Bangalore, with every carton open to QR verification before you pay. WhatsApp 88676 76700 for today's rate.",
 "badge": "Finolex 90M Silver · Every Size In Stock",
 "intro": "Finolex 90M Silver is the FR-grade house wire most Indian homes are actually wired with. Here is what it is, which sizes go where, what it should cost, and how to make sure the coil you are handed is the real thing.",
 "answer": "Mount Cable India is a Finolex 90M Silver dealer and distributor in Bengaluru, holding every size from 0.75 to 6.0 sq mm in stock at distributor pricing and supplying across Karnataka. Finolex 90M Silver is FR-grade PVC house wire in a 90-metre coil — the standard choice for domestic lighting, fan and socket circuits.",
 "hero": ("electrician-scanning-qr-code-wire-coil.jpg",
          "Scanning the QR code on a Finolex 90M Silver wire carton to verify it is 100% original before paying"),
 "sections": [
   ("What is Finolex 90M Silver?",
    "<p>Finolex 90M Silver is flame-retardant (FR) grade PVC-insulated house wire supplied in a 90-metre coil, with an electrolytic-grade bare copper conductor. It is the everyday domestic range — the wire that goes into the great majority of independent houses and flats in Karnataka — and it is available across the full house-wiring span from 0.75 to 6.0 sq mm. Full specifications are on the <a href=\"finolex/90m-silver.html\">90M Silver product page</a>.</p>"
    "<p>Ninety metres is the coil size domestic wiring is planned around. It is enough for a typical circuit run without leaving expensive offcuts, and it keeps the carton small enough to handle, count and verify one box at a time.</p>"),

   ("Which size for which circuit?",
    "<div class=\"ptable-wrap\"><table class=\"ptable\"><thead><tr><th>Size</th><th>Typical use</th><th>Rough coils for a 2BHK</th></tr></thead><tbody>"
    "<tr><td>0.75 sq mm</td><td>Light points, bulbs, tube lights</td><td>1 to 2</td></tr>"
    "<tr><td>1.0 sq mm</td><td>Light and fan points, 5A circuits</td><td>3 to 5</td></tr>"
    "<tr><td>1.5 sq mm</td><td>Fan and light circuits, utility points</td><td>3 to 5</td></tr>"
    "<tr><td>2.5 sq mm</td><td>6A and 16A sockets, fridge, TV, kitchen</td><td>4 to 6</td></tr>"
    "<tr><td>4.0 sq mm</td><td>Air-conditioners, geysers, heavy 16A loads</td><td>2 to 3</td></tr>"
    "<tr><td>6.0 sq mm</td><td>Sub-mains and long heavy runs</td><td>1 to 2</td></tr>"
    "</tbody></table></div>"
    "<p class=\"ptable-note\">Coil counts are indicative for a compact 2BHK and vary a great deal with layout, point count and run lengths. Work yours out with the free <a href=\"tools/wire-quantity-calculator.html\">wire quantity calculator</a>, or send us the point list and we will do it.</p>"),

   ("Silver or Gold?",
    "<p>Both 90M Silver and <a href=\"finolex-gold-90m-dealers.html\">90M Gold</a> are FR-grade Finolex house wire in 90-metre coils; Gold is the premium tier of the two. For ordinary domestic lighting, fan and socket circuits, Silver is the range most houses are wired with and is entirely adequate for the job.</p>"
    "<p>The decision that actually changes fire behaviour is not Silver versus Gold — it is FR versus FR-LSH versus Ultra, which is about smoke and halogen emission rather than tier. That comparison is set out in <a href=\"blog/fr-vs-frls-vs-finolex-ultra.html\">FR vs FRLS vs Finolex Ultra</a>, and side by side in <a href=\"blog/finolex-silver-vs-gold-90m.html\">Finolex Silver vs Gold 90M</a>.</p>"),

   ("What should Finolex 90M Silver cost?",
    "<p>Approximate ranges for 90-metre coils sit on our <a href=\"price-lists/finolex-price-list.html\">Finolex price list page</a>. We publish ranges rather than exact figures deliberately: the price of a coil is mostly the price of the copper inside it, copper is a traded commodity, and a fixed rate card would be wrong within days.</p>"
    "<p>For today's exact number, WhatsApp your list to <a href=\"" + W + "\">" + PH + "</a>. We give the best pricing and the highest discounts in Bangalore on Finolex — but note the shape of that claim. Genuine wire runs on a 3 to 5 per cent dealer margin, so a real discount is a few per cent. If a seller is 15 or 20 per cent below everyone else, the money is coming out of the copper, the coil length or the brand.</p>"),

   ("Confirming a Silver coil is genuine",
    "<p>Do not rely on the shop's word, ours included. Every 90M Silver carton carries an outer QR code on the printed label and a second, inner code inside the box.</p>"
    + TWO_QR +
    "<p>Scan both, on every coil, before you pay. Then look at the wire itself: the repeating markings printed along the insulation should be crisp and evenly spaced, and the copper at a cut end should look right for the sq mm on the label. The step-by-step versions are in <a href=\"blog/original-finolex-wire-outer-qr-code.html\">scanning the outer code</a>, <a href=\"blog/original-finolex-wire-inner-qr-code.html\">scanning the inner code</a> and the <a href=\"blog/original-finolex-wire-checklist-before-paying.html\">12-point checklist before paying</a>.</p>"
    "<p>Come to our Chickpete or Jayanagar showroom and pick the cartons yourself — we will open them for you. Ordering to a site in Bangalore, you scan at your own site and pay afterwards. Ordering outstation in Karnataka, we will scan the consignment before dispatch and send you the record.</p>"
    + DEALER_CTA),
 ],
 "faqs": [
   ("Who are the Finolex 90M Silver dealers in Bengaluru?", "Mount Cable India is a Finolex Silver 90M dealer and distributor with showrooms in Chickpete (BVK Iyengar Road) and Jayanagar, holding every size from 0.75 to 6.0 sq mm in stock. Material is supplied at distributor pricing across Bengaluru with free next-day delivery, and across the rest of Karnataka against a written quotation."),
   ("What is Finolex 90M Silver wire?", "Finolex 90M Silver is flame-retardant (FR) grade PVC-insulated house wire on a 90-metre coil with an electrolytic-grade bare copper conductor. It is the everyday domestic range used for lighting, fan and socket circuits, available from 0.75 to 6.0 sq mm."),
   ("What is the difference between Finolex Silver and Gold 90M?", "Both are FR-grade Finolex house wire in 90-metre coils; Gold is the premium tier of the two. For ordinary domestic circuits, Silver is what most houses are wired with and is adequate for the job. The choice that genuinely changes fire behaviour is FR versus FR-LSH versus Ultra, which concerns smoke and halogen emission rather than tier."),
   ("How many coils of 90M Silver do I need for a 2BHK?", "Indicatively around fifteen to twenty 90-metre coils across the sizes — roughly 3 to 5 of 1.0 sq mm, 3 to 5 of 1.5 sq mm, 4 to 6 of 2.5 sq mm and 2 to 3 of 4.0 sq mm — but this varies a great deal with layout and point count. Use our free wire quantity calculator, or send the point list to 88676 76700 and we will work it out."),
   ("What is the price of Finolex 90M Silver today?", "Approximate ranges are published on our Finolex price list page. Exact prices are not published because a coil's cost is mostly the copper inside it and copper is a traded commodity, so a fixed rate card goes stale within days. WhatsApp your sizes to 88676 76700 for today's exact figure within 60 minutes, with no obligation to buy."),
   ("How do I verify a Finolex Silver coil is original?", "Scan the outer QR code printed on the carton label and confirm it opens Finolex's own verification portal with details matching the box, then open the carton and scan the inner QR code as well. Do this on every coil rather than a sample. A genuine carton can be emptied and refilled, in which case the outer code still passes and only the inner code fails."),
 ]},

# ------------------------------------------------------------------ 3
{"slug": "finolex-gold-90m-dealers",
 "title": "Finolex Gold 90M Dealers | Premium FR House Wire, Distributor Price — Karnataka",
 "h1": "Finolex Gold 90M dealers",
 "desc": "Finolex 90M Gold dealers in Bengaluru and across Karnataka. Mount Cable India stocks the premium FR house wire in every size from 0.75 to 6.0 sq mm, at the best pricing in Bangalore, with QR verification on every carton before you pay. WhatsApp 88676 76700.",
 "badge": "Finolex 90M Gold · Premium FR House Wire",
 "intro": "Finolex 90M Gold is the premium tier of Finolex's 90-metre FR house wire. This page covers what you are paying the premium for, when it is worth paying, and how to be certain the carton in front of you is genuinely Gold and genuinely Finolex.",
 "answer": "Mount Cable India is a Finolex 90M Gold dealer and distributor in Bengaluru, stocking every size from 0.75 to 6.0 sq mm at distributor pricing and supplying across Karnataka. Finolex 90M Gold is the premium tier of Finolex's flame-retardant 90-metre house wire, used for the same domestic lighting, fan and socket circuits as the Silver range.",
 "hero": ("happy-electrician-installing-modular-switch.jpg",
          "Electrician wiring a modular switch with genuine Finolex 90M Gold house wire in Bengaluru"),
 "sections": [
   ("What is Finolex 90M Gold?",
    "<p>Finolex 90M Gold is FR-grade PVC-insulated house wire on a 90-metre coil, positioned as the premium tier alongside <a href=\"finolex-silver-90m-dealers.html\">90M Silver</a>. It is built on the same New Improved FR platform with high-grade copper and robust insulation, and it covers the full domestic range from 0.75 to 6.0 sq mm. Details are on the <a href=\"finolex/90m-gold.html\">90M Gold product page</a>.</p>"
    "<p>It is used for exactly the circuits Silver is used for — lights, fans, sockets, air-conditioner and geyser points. The choice between them is a choice of tier within the same flame-retardant grade, not a choice between two different kinds of wire.</p>"),

   ("Gold, Silver, FRLS or Ultra — how to actually decide",
    "<div class=\"ptable-wrap\"><table class=\"ptable\"><thead><tr><th>Range</th><th>Grade</th><th>What changes</th><th>Sensible for</th></tr></thead><tbody>"
    "<tr><td>90M Silver</td><td>FR</td><td>The standard domestic FR house wire</td><td>Most rooms in most houses</td></tr>"
    "<tr><td>90M Gold</td><td>FR, premium tier</td><td>Premium tier of the same FR grade</td><td>Buyers who want the top of the FR range throughout</td></tr>"
    "<tr><td>90M FRLS</td><td>FR-LSH</td><td>Lower smoke and reduced halogen gases in a fire</td><td>Bedrooms, children's rooms, enclosed spaces</td></tr>"
    "<tr><td>Finolex Ultra</td><td>LSZH, E-Beam</td><td>Highest heat resistance, lowest smoke and halogen</td><td>Whole-house fire safety at the top of the range</td></tr>"
    "</tbody></table></div>"
    "<p>The honest guidance: if you are choosing between Silver and Gold, you are choosing a tier. If you want the choice that materially changes what happens in a fire, that is the step up to FR-LSH or Ultra, because smoke and halogen kill more people in house fires than flame does. Many buyers mix — FR-LSH or Ultra in bedrooms and enclosed rooms, FR elsewhere — and that is usually a better use of the same budget than upgrading tier everywhere. <a href=\"blog/fr-vs-frls-vs-finolex-ultra.html\">Full comparison here.</a></p>"),

   ("Price, and the limit of any honest discount",
    "<p>Gold sits above Silver in price and both track the copper market, so we quote the day's rate rather than publishing a rate card. Approximate bands are on the <a href=\"price-lists/finolex-price-list.html\">Finolex price list page</a>; the exact figure comes back on WhatsApp within 60 minutes.</p>"
    "<p>We give the highest discounts in Bangalore on Finolex, and it is worth being precise about what that can mean. Genuine branded wire is a 3 to 5 per cent margin business. The room to discount is measured in single digits. A quote 15 or 20 per cent below the rest of the market is not a better dealer — it is a different product, and the difference is inside the coil.</p>"),

   ("Making sure Gold is actually Gold",
    "<p>Premium tiers attract counterfeiting for an obvious reason: the packaging change is cheap and the price difference is not. So the verification matters more here, not less.</p>"
    + TWO_QR +
    "<p>Scan the outer code, open the carton, scan the inner code, and check that what the verification reports — range, size, grade, batch — matches what is printed in front of you. A verification that says genuine while describing a different range is not a pass. Then check the printing along the insulation itself, which is covered in <a href=\"blog/finolex-wire-insulation-markings.html\">reading Finolex insulation markings</a>.</p>"
    "<p>Do this on every coil. Not the top box, not a sample. This is the check that no amount of showroom polish can substitute for, and it is why we hand customers the cartons and let them scan before anything is paid.</p>"
    + DEALER_CTA),
 ],
 "faqs": [
   ("Who are the Finolex 90M Gold dealers in Karnataka?", "Mount Cable India is a Finolex Gold 90M dealer and distributor with two showrooms in Bengaluru — Chickpete on BVK Iyengar Road and Jayanagar — stocking every size from 0.75 to 6.0 sq mm. We deliver free across Bangalore by the next day and supply the rest of Karnataka against a written quotation."),
   ("What is Finolex 90M Gold wire?", "Finolex 90M Gold is flame-retardant (FR) grade PVC-insulated house wire on a 90-metre coil, positioned as the premium tier alongside 90M Silver. It is built on the same New Improved FR platform with high-grade copper and robust insulation, and covers the domestic range from 0.75 to 6.0 sq mm."),
   ("Is Finolex Gold worth the extra over Silver?", "It buys you the premium tier of the same flame-retardant grade. If your goal is a materially different fire performance rather than a higher tier, the step that actually changes smoke and halogen emission is FR-LSH (Flamegard) or Finolex Ultra. Many buyers get better value by putting FR-LSH in bedrooms and enclosed rooms and keeping standard FR elsewhere."),
   ("How do I know a Finolex Gold carton is genuine?", "Scan the outer QR code on the carton label, confirm it opens Finolex's own verification portal and that the range, size, grade and batch it reports match the printing in front of you, then open the box and scan the inner QR code as well. Premium tiers are counterfeited more often precisely because the packaging is cheap to copy and the price gap is not."),
   ("What is the price difference between Finolex Silver and Gold?", "Gold sits above Silver, and both move with the copper market, so we quote the day's rate instead of publishing a fixed figure that would be stale within days. Approximate bands are on our Finolex price list page; WhatsApp your sizes to 88676 76700 for the exact difference on your list, with no obligation to buy."),
   ("Can I mix Finolex Gold and FRLS in the same house?", "Yes, and it is common. Grades and ranges are compatible within a house as long as each circuit is correctly sized and terminated. A frequent arrangement is FR-LSH or Ultra in bedrooms, children's rooms and enclosed spaces where smoke matters most, with standard FR in utility areas."),
 ]},

# ------------------------------------------------------------------ 4
{"slug": "finolex-project-packing-dealers",
 "title": "Finolex Project Packing Dealers | Bulk Coils for Builders — Bengaluru & Karnataka",
 "h1": "Finolex project packing dealers",
 "desc": "Finolex project packing dealers in Bengaluru and Karnataka. Mount Cable India supplies project-quantity Finolex wire to builders and contractors with phased dispatch, itemised quotations and QR verification of every carton before payment. WhatsApp 88676 76700.",
 "badge": "Project Packing · Builders &amp; Contractors",
 "intro": "Project packing is the trade term for Finolex wire supplied in project quantities and longer coil lengths, rather than in the retail 90-metre boxes a household buys. This page explains what it is, when it saves real money, and what a builder should insist on before accepting a consignment.",
 "answer": "Finolex project packing is wire supplied in project quantities and longer coil lengths — typically 180-metre and 300-metre coils — for construction projects rather than in the 90-metre retail boxes households buy. Mount Cable India supplies project packing to builders and contractors in Bengaluru and across Karnataka, with itemised quotations, phased dispatch and QR verification of every carton before payment.",
 "hero": ("builder-architect-site-electrical-planning.jpg",
          "Builder and architect planning electrical requirements for a project supplied with Finolex project packing wire"),
 "sections": [
   ("What project packing actually means",
    "<p>Retail house wire comes in 90-metre cartons because that is the unit a household can carry, count and pay for. A project has a different problem: hundreds of coils, long runs, and a store that has to issue material floor by floor without losing track of it.</p>"
    "<p>Project packing addresses that by moving to longer coil lengths — commonly <a href=\"finolex/180m.html\">180-metre</a> and <a href=\"finolex/300m.html\">300-metre</a> coils — and to project-quantity ordering and dispatch. Two consequences follow, and both are money:</p>"
    "<ul>"
    "<li><strong>Fewer joints.</strong> A long run served from a 300-metre coil needs no mid-run joint. Joints are where installations lose reliability and where inspection time goes.</li>"
    "<li><strong>Less offcut wastage.</strong> Ninety-metre coils leave short tail ends that are too short to use and too long to ignore. Across a project, those tails add up to real quantity.</li>"
    "</ul>"
    "<p>The exact packing available depends on the size and grade you need, so we confirm it against your bill of quantities at quotation stage rather than promising a format in the abstract.</p>"),

   ("When project packing saves money and when it does not",
    "<div class=\"ptable-wrap\"><table class=\"ptable\"><thead><tr><th>Situation</th><th>Better choice</th><th>Why</th></tr></thead><tbody>"
    "<tr><td>One independent house, ordinary room sizes</td><td>90-metre coils</td><td>Runs are short; long coils create handling problems, not savings</td></tr>"
    "<tr><td>Large house or duplex, long runs</td><td>Mix of 90 m and 180 m</td><td>Long circuits from 180 m, short ones from 90 m</td></tr>"
    "<tr><td>Apartment block or multiple units</td><td>180 m and 300 m</td><td>Repeating circuit lengths, fewer joints, less tail wastage</td></tr>"
    "<tr><td>Commercial floor plate or long horizontal runs</td><td>300 m</td><td>Continuous runs without mid-run joints</td></tr>"
    "</tbody></table></div>"
    "<p class=\"ptable-note\">If your project is a single house, we will usually tell you to stay on 90-metre coils. Project packing is a genuine saving on project-shaped work and an inconvenience on domestic work, and there is no reason to pretend otherwise.</p>"),

   ("How we quote and dispatch a project",
    "<ol>"
    "<li><strong>Send the bill of quantities</strong> — sizes, grades, quantities, and the phase each is needed in. A drawing set or an estimate photograph works just as well.</li>"
    "<li><strong>Itemised quotation within 60 minutes</strong>, line by line, with freight shown separately where the site is outside Bengaluru. Approximate ranges are on the <a href=\"price-lists/finolex-price-list.html\">Finolex price list page</a>; the quotation carries the day's actual rate.</li>"
    "<li><strong>Phased dispatch.</strong> Material arrives as each phase needs it rather than in one delivery that has to be stored and guarded for months.</li>"
    "<li><strong>Verification before payment.</strong> We will scan the outer codes on the consignment before it leaves the godown and send you the record, and your site team scans outer and inner codes on arrival.</li>"
    "</ol>"),

   ("What a builder should insist on",
    "<p>Project quantities are where counterfeit wire does the most damage, because nobody scans four hundred cartons unless it is somebody's stated job. Make it somebody's stated job.</p>"
    + TWO_QR +
    "<p>Four conditions worth writing into any material supply arrangement, ours included:</p>"
    "<ul>"
    "<li>Cartons delivered sealed, and opened at site rather than before arrival.</li>"
    "<li><strong>Every carton scanned — outer code and inner code — before payment is released.</strong> Not a sample of the consignment. Every carton.</li>"
    "<li>A GST invoice naming the brand, the range, the size and the coil length on each line.</li>"
    "<li>Your right to cross-check the rate against another distributor before releasing payment.</li>"
    "</ul>"
    "<p>Any honest supplier will accept all four without argument. If a supplier resists the second one in particular, that resistance is the answer. More on the mechanics of this in <a href=\"blog/bulk-finolex-wire-orders-builders-karnataka.html\">bulk Finolex orders for builders in Karnataka</a> and <a href=\"blog/verify-finolex-dealer-stock-before-ordering.html\">verifying a dealer's stock before ordering</a>.</p>"
    + DEALER_CTA),
 ],
 "faqs": [
   ("What is Finolex project packing?", "Project packing is the trade term for Finolex wire supplied in project quantities and longer coil lengths — commonly 180-metre and 300-metre coils — for construction projects, rather than the 90-metre retail cartons households buy. It reduces mid-run joints and offcut wastage on project-shaped work. The exact packing available depends on the size and grade, and is confirmed against the bill of quantities at quotation."),
   ("Who supplies Finolex project packing in Karnataka?", "Mount Cable India, one of the largest dealers and distributors of Finolex cables, supplies project quantities to builders and contractors from Bengaluru — free next-day delivery within Bangalore, and road transport against a written quotation elsewhere in Karnataka, with freight shown as a separate line."),
   ("Is project packing cheaper than 90M coils?", "On project-shaped work, usually yes, because longer coils mean fewer joints and less offcut wastage across repeating circuit lengths. On a single independent house it generally is not — runs are short and long coils create handling problems rather than savings. We will say which applies to your job rather than pushing the larger format."),
   ("What is the minimum quantity for a project order?", "There is no fixed minimum. What determines whether project packing makes sense is the shape of the work, not a number of coils — repeating circuit lengths and long runs favour 180-metre and 300-metre coils, while a single house with ordinary room sizes does not. Send the bill of quantities to 88676 76700 and we will advise."),
   ("Can you deliver a project in phases?", "Yes. Material is dispatched as each phase needs it rather than in one delivery that has to be stored and guarded for months, which also reduces site pilferage and damage. The dispatch schedule is agreed with the quotation."),
   ("How should a builder verify a large Finolex consignment?", "Make verification an assigned job, not an intention. Every carton should be scanned on both codes — the outer QR on the label and the inner QR inside the box — before payment is released, with cartons opened at site rather than beforehand. Counterfeit wire does the most damage in project quantities precisely because nobody scans four hundred cartons unless someone is responsible for it."),
 ]},

# ------------------------------------------------------------------ 5
{"slug": "bulk-finolex-wire-supplier-karnataka",
 "title": "Bulk Finolex Wire Supplier in Karnataka | Builders & Contractors — Mount Cable India",
 "h1": "Bulk Finolex wire supplier for Karnataka",
 "desc": "Bulk Finolex wire supply for builders, contractors and electrical contractors across Karnataka. Mount Cable India quotes project quantities within 60 minutes, dispatches in phases from Bengaluru, and lets you verify every coil or the entire stock before you buy. WhatsApp 88676 76700.",
 "badge": "Bulk Supply · Builders, Contractors, Electrical Contractors",
 "intro": "Buying Finolex wire in quantity is a different exercise from buying five coils. The rate matters, but so do dispatch phasing, verification at scale and knowing that what arrives on the tenth delivery is the same material as the first. This page is about all four.",
 "answer": "Mount Cable India supplies bulk Finolex wire to builders, contractors and electrical contractors across Karnataka from its Bengaluru godown. Project quantities are quoted itemised within 60 minutes, dispatched in phases as each stage needs them, and every coil — or the entire consignment — may be scanned and verified before you buy.",
 "hero": ("contractor-bulk-order-loading-warehouse.jpg",
          "Bulk Finolex wire coils being loaded for a contractor's project order in Karnataka"),
 "sections": [
   ("Why bulk buyers get targeted",
    "<p>Counterfeit wire is not distributed evenly. It concentrates where three conditions hold at once: large quantities, nobody personally attached to the outcome, and material that disappears into a wall within days of arriving. A construction project is all three.</p>"
    "<p>A homeowner buying twenty coils will open a box. A site store receiving four hundred cartons across six months will not, unless it is written into someone's job. That gap is the whole opportunity, and it is why the single most valuable thing a builder can do is make verification a named responsibility rather than a good intention.</p>"),

   ("What bulk supply from us looks like",
    "<ul>"
    "<li><strong>Itemised quotation within 60 minutes</strong> of receiving your bill of quantities — line by line, with freight shown separately for sites outside Bengaluru so the landed cost is visible rather than buried in the rate.</li>"
    "<li><strong>Stock actually held.</strong> Every Finolex range is physically in our godown, so a schedule is a schedule rather than an indent against a factory queue.</li>"
    "<li><strong>Phased dispatch</strong> against your programme, so material arrives when the floor needs it instead of sitting on site for months collecting damage and shrinkage.</li>"
    "<li><strong>Verification at scale.</strong> We will scan the outer codes on a consignment before dispatch and send you the record on WhatsApp; your site team scans outer and inner codes on arrival.</li>"
    "<li><strong>Best pricing in Bangalore</strong> — within the 3 to 5 per cent margin that genuine branded wire actually runs on. We will not pretend to a number that does not exist.</li>"
    "</ul>"),

   ("Verifying a large consignment without stopping the site",
    "<p>The objection to scanning every carton is time. In practice a scan takes about twenty seconds, so a hundred-carton delivery is roughly thirty-five minutes of one person's day — against a rewiring bill if it goes wrong. Build it into the receiving routine:</p>"
    "<ol>"
    "<li><strong>At the gate:</strong> count cartons against the challan and check seals before anything is unloaded into the store.</li>"
    "<li><strong>Outer code on every carton.</strong> One person, one phone, scanning as cartons come off the vehicle. Confirm the size, grade and batch reported match the label.</li>"
    "<li><strong>Inner code on every carton that gets opened for issue.</strong> Wire is issued from the store anyway; scan the inner code at the moment of issue and the check costs no extra handling.</li>"
    "<li><strong>Log it.</strong> Carton, batch, result, date, initials. If a dispute ever arises, this log is the difference between a claim and an argument.</li>"
    "</ol>"
    + TWO_QR),

   ("A note on with-material contracts",
    "<p>If you are a homeowner or a developer letting electrical work on a with-material basis, understand the incentive you have created: every rupee the contractor saves on material is his profit, and you will never see the boxes. That is not an accusation, it is arithmetic.</p>"
    "<p>The fix is not distrust, it is specification. Require sealed cartons opened at site, QR verification on both codes in your presence or your engineer's, brand-named GST invoices, and your right to cross-check rates against a reference distributor. An honest contractor agrees to all four immediately, because none of them cost him anything. Full detail in our <a href=\"original-vs-duplicate-electrical-products.html\">original vs duplicate buyer's guide</a>.</p>"),

   ("Send the bill of quantities",
    "<p>Sizes, grades, quantities and the phase each is needed in — or simply a photograph of the estimate. WhatsApp it to <a href=\"" + W + "\">" + PH + "</a> and the itemised quotation comes back within 60 minutes.</p>"
    "<p>There is no obligation whatsoever. If you want our number purely to check what someone else has quoted you, ask for it on that basis and we will still send it inside the hour. A market where buyers know the real price is a market we do better in. Read the <a href=\"{review}\" target=\"_blank\" rel=\"noopener\">Google reviews about our Finolex wires</a> if you want to know how that works out for the people who try it.</p>"),
 ],
 "faqs": [
   ("Who supplies bulk Finolex wire in Karnataka?", "Mount Cable India, one of the largest dealers and distributors of Finolex cables, supplies bulk and project quantities to builders, contractors and electrical contractors across Karnataka from its Bengaluru godown — free next-day delivery inside Bangalore, and road transport against a written quotation elsewhere in the state with freight itemised separately."),
   ("How quickly can I get a quotation for a project quantity?", "Within 60 minutes of sending the bill of quantities to 88676 76700 on WhatsApp. A photograph of the estimate works as well as a spreadsheet. The quotation is itemised line by line, with freight as a separate line for sites outside Bengaluru, and there is no obligation to buy."),
   ("Can bulk deliveries be phased across a project programme?", "Yes. Material is dispatched against your programme so it arrives as each stage needs it, rather than in one delivery that sits on site for months collecting damage and shrinkage. Because every Finolex range is physically held in stock, a dispatch schedule is a commitment rather than an indent against a factory queue."),
   ("How do you verify a large consignment without delaying the site?", "A scan takes about twenty seconds, so a hundred-carton delivery is roughly thirty-five minutes of one person's time. Scan the outer QR on every carton as it comes off the vehicle, scan the inner QR at the moment each carton is opened for issue from the store, and log carton, batch, result and date. Built into the receiving routine, it costs almost no extra handling."),
   ("Why are bulk buyers more exposed to counterfeit wire?", "Because counterfeit concentrates where large quantities meet nobody personally attached to the outcome and material that disappears into a wall within days. A homeowner buying twenty coils opens a box; a site store receiving four hundred cartons over six months does not, unless verification is written into someone's job. Making it a named responsibility closes the gap."),
   ("Can I use your quotation just to check another supplier's price?", "Yes, and people do it regularly. Ask on that basis and the itemised quotation still comes back within the hour. Genuine branded wire runs on a 3 to 5 per cent dealer margin, so if another quote sits 15 or 20 per cent below ours the gap is not commercial skill — it is inside the coil."),
 ]},

]
