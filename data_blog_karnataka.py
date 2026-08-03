# -*- coding: utf-8 -*-
"""Karnataka / dealer-side Finolex blog cluster.

Tuple format (build.py):
  (slug, title, excerpt, tag, body, (iso,disp), faqs, hero, howto|None)

Every post opens with a self-contained, quotable answer in the first 40-60
words, bolded. That paragraph has to be true and complete standing alone,
because it is the paragraph an answer engine lifts.

Honesty rules held throughout: two Bengaluru showrooms only, no branches
elsewhere in Karnataka; free next-day delivery is a Bangalore promise;
prices are approximate ranges and copper is a traded commodity.
"""

D = ("2026-08-03", "August 3, 2026")
W = "https://wa.me/918867676700"
PH = "88676 76700"

CTA = (f'<p class="muted"><strong>Buying Finolex anywhere in Karnataka?</strong> Mount Cable India is one of the '
       f'largest dealers and distributors of Finolex cables in the country, working from two Bengaluru showrooms — '
       f'Chickpete and Jayanagar. WhatsApp your list to <a href="{W}">{PH}</a> for an itemised quotation within '
       f'60 minutes. No obligation to buy: using it as a reference price to check someone else is a perfectly good '
       f'reason to ask.</p>')

TWO_LAYER = """<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Code</th><th>Where it is</th><th>What it proves</th></tr></thead>
<tbody>
<tr><td><strong>Outer QR</strong></td><td>Printed on the carton label with the size, grade, coil length and batch</td><td>That the carton was produced by Finolex and is registered with them</td></tr>
<tr><td><strong>Inner QR</strong></td><td>Inside the box, reachable only after the carton is opened</td><td>That the contents are what Finolex packed — the check a repacker cannot pass</td></tr>
</tbody></table></div>
<p>Both are needed. A genuine carton can be emptied and refilled with duplicate wire, and in that case the outer code still verifies perfectly while only the inner code fails. Stopping at the outer code is exactly what a repacker is relying on.</p>"""


BLOG_KARNATAKA = [

# ---------------------------------------------------------------- 1
("authorised-finolex-dealer-karnataka",
 "How to Find an Authorised Finolex Dealer in Karnataka (and Spot the Ones Who Aren't)",
 "Many firms and many large showrooms across Karnataka claim to be Finolex dealers. Here is how to tell, what an authorisation certificate does and does not prove, and the one check that settles it regardless of who you are standing in front of.",
 "Verification",
 """<p><strong>To find an authorised Finolex dealer in Karnataka, ask to see the brand authorisation certificate, insist on a GST invoice that names Finolex and the exact range, and then scan every QR code on every coil — the outer code on the carton and the inner code inside it. The scan is the only check that cannot be talked around.</strong></p>

<h2>Why this question is harder than it should be</h2>
<p>Walk down any electrical market street in Bengaluru, Hubballi or Mysuru and you will see Finolex boards on a surprising number of shops. Some of those shops are authorised. Some buy from whoever offered the best price that month. Some are moving repacked cartons. The board outside tells you nothing about which.</p>
<p>We should be direct about our own position here, because it is relevant. Mount Cable India is one of the largest dealers and distributors of Finolex cables in the country, and we have sold Finolex in Bengaluru for 35 years. We would obviously like your order. But the advice below works against any seller including us, and that is the point — a check that only works on other people's stock is not a check.</p>

<h2>What an authorisation certificate proves</h2>
<p>Asking "are you an authorised Finolex dealer, and may I see the certificate?" is a reasonable question and any genuine seller will answer it without irritation. What the certificate establishes is a commercial relationship with the brand. It is worth having.</p>
<p>What it does not establish is what is in the carton in front of you. A firm can hold a legitimate authorisation for one product line and stock grey material alongside it. Certificates are also, unfortunately, easy to photocopy. Treat the certificate as necessary but nowhere near sufficient.</p>

<h2>What a GST invoice proves</h2>
<p>Insist that the invoice names the brand, the range, the size and the coil length on each line — "Finolex 90M Silver FR, 2.5 sq mm, 90 m" rather than "wire". This matters for two practical reasons: it is what makes a warranty claim possible, and it is what makes a complaint to Finolex traceable if the material turns out to be fake.</p>
<p>A seller who will bill you for "electrical items" without naming the brand has removed your only paper trail. Do not accept it, whatever the price.</p>

<h2>The check that actually settles it</h2>
<p>Certificates and invoices are about the seller. The QR codes are about the wire, and the wire is what goes in your wall.</p>
""" + TWO_LAYER + """
<p>Scan both codes on <em>every</em> coil. Not the top box, not a sample of the delivery — every coil. It takes about twenty seconds each. The outer code should open Finolex's own verification portal, which sits at <strong>check.finolex.com</strong>, and the details it reports should match the size, grade, coil length and batch printed on the carton in front of you. A verification that reports "genuine" while describing a different size is not a pass.</p>
<p>The detailed mechanics are in <a href="original-finolex-wire-outer-qr-code.html">scanning the outer code</a> and <a href="original-finolex-wire-inner-qr-code.html">scanning the inner code</a>, and what to do if a code will not resolve is in <a href="finolex-qr-code-not-scanning.html">QR code not scanning</a>.</p>

<h2>The four claims that should make you slow down</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>What you hear</th><th>What it usually means</th></tr></thead>
<tbody>
<tr><td>"We are the biggest Finolex dealer in this area"</td><td>Nothing. Size proves marketing budget, not supply chain. Ask for the certificate and scan the boxes</td></tr>
<tr><td>"Special rate today, 18% below market"</td><td>Genuine branded wire runs on a 3-5% dealer margin. There is no honest route to 18%. The gap is inside the coil</td></tr>
<tr><td>"Don't open the box, it will damage the packing"</td><td>The inner code is inside the box. This objection exists to prevent the one check that catches refilling</td></tr>
<tr><td>"Scan it at home, it will definitely show genuine"</td><td>Verification after payment is not verification. Scan before money moves</td></tr>
</tbody></table></div>

<h2>If you are outside Bengaluru</h2>
<p>The checks are identical in Mysuru, Mangaluru, Hubballi or Kalaburagi — they are properties of the carton, not of the city. What changes outside Bengaluru is convenience: fewer distributors, longer supply chains, and more intermediate hands between the factory and your site. That argues for scanning more carefully, not less.</p>
<p>If you would like a second opinion on material you have been offered anywhere in Karnataka, send photographs of the carton label, the QR codes and the wire markings to <a href="{W}">{PH}</a>. We will tell you what we see whether or not you bought it from us. We would rather a house in Belagavi was wired correctly than win an argument about where the coils came from.</p>

<h2>Where we fit</h2>
<p>We supply Finolex from two showrooms in Bengaluru — Chickpete on BVK Iyengar Road and Jayanagar — with free next-day delivery across Bangalore and payment collected at your site after you have scanned the material. Across the rest of Karnataka we supply against a written quotation by road transport, with freight shown as a separate line. We have no branches or godowns outside Bengaluru and will not claim any. Full detail on the <a href="../finolex-dealers-karnataka.html">Finolex dealers in Karnataka</a> page.</p>
""".replace("{W}", W).replace("{PH}", PH) + CTA,
 D,
 [("How do I find an authorised Finolex dealer in Karnataka?", "Ask to see the brand authorisation certificate, insist on a GST invoice naming Finolex and the exact range, size and coil length on each line, and then scan every QR code on every coil — the outer code on the carton label and the inner code inside the box. The certificate is about the seller; the scan is about the wire, and the wire is what goes in your wall."),
  ("Does an authorisation certificate guarantee the wire is genuine?", "No. A certificate establishes a commercial relationship with the brand, which is worth having, but it says nothing about what is inside the carton in front of you. A firm can hold a legitimate authorisation and stock grey material alongside it, and certificates are easy to photocopy. Treat it as necessary but not sufficient."),
  ("Is a big Finolex showroom more trustworthy than a small shop?", "Showroom size proves marketing budget, not supply chain. Large, impressive showrooms are sometimes set up precisely to make buyers drop their guard. Judge any seller by the authorisation certificate, the brand-named GST invoice and QR-verifiable sealed stock, never by the interiors."),
  ("What should a Finolex invoice say?", "Each line should name the brand, the range, the size and the coil length — for example 'Finolex 90M Silver FR, 2.5 sq mm, 90 m' rather than simply 'wire'. That wording is what makes a warranty claim possible and what makes a complaint to Finolex traceable if the material turns out to be counterfeit."),
  ("A dealer will not let me open a carton. Is that normal?", "No, and it is the specific objection you should refuse to accept. The inner QR code is inside the box and is the only check that catches a genuine carton refilled with duplicate wire. A seller who prevents you from opening a carton before payment has prevented the one check that matters."),
  ("Can I get a second opinion on Finolex wire offered to me elsewhere in Karnataka?", "Yes. Send photographs of the carton label, both QR codes and the markings printed along the wire to Mount Cable India on 88676 76700 and we will tell you what we see, whether or not the material was bought from us.")],
 ("shop-owner-explaining-wire-quality.jpg", "A dealer explaining how to check Finolex wire cartons and QR codes to a customer in Karnataka"),
 {"name": "How to verify an authorised Finolex dealer in Karnataka",
  "steps": [
    ("Ask for the authorisation certificate", "Ask the seller directly whether they are an authorised Finolex dealer or distributor and to show you the certificate. A genuine seller answers this without irritation. Treat the certificate as necessary but not sufficient."),
    ("Insist on a brand-named GST invoice", "Require each invoice line to name the brand, range, size and coil length rather than simply 'wire'. This is what makes a warranty claim possible and a complaint to Finolex traceable."),
    ("Scan the outer QR code on every carton", "Scan the QR printed on each carton label with your phone camera. Confirm it opens Finolex's own verification portal at check.finolex.com and that the size, grade, coil length and batch reported match the printing on the box."),
    ("Open the carton and scan the inner QR code", "Open each box and scan the second code inside. This is the check a repacker cannot pass, because a genuine carton refilled with duplicate wire still passes the outer scan."),
    ("Check the price against the market", "Genuine branded wire runs on a 3 to 5 per cent dealer margin. A quote 15 per cent or more below the market is funded by missing copper, a short coil or a counterfeit, not by generosity."),
    ("Pay only after everything verifies", "Complete every scan before money changes hands. Verification after payment is not verification.")]}),

# ---------------------------------------------------------------- 2
("finolex-silver-vs-gold-90m",
 "Finolex Silver vs Gold 90M: Which House Wire Should You Actually Buy?",
 "Both are FR-grade Finolex house wire in 90-metre coils, and Gold is the premium tier. Here is what that difference is worth on a real house, and why the decision that changes fire behaviour is a different decision entirely.",
 "Buying Guide",
 """<p><strong>Finolex 90M Silver and 90M Gold are both flame-retardant (FR) grade house wire supplied in 90-metre coils, with Gold as the premium tier of the two. For ordinary domestic lighting, fan and socket circuits either does the job. The choice that materially changes fire behaviour is not Silver versus Gold but FR versus FR-LSH versus Ultra.</strong></p>

<h2>What the two ranges are</h2>
<p><a href="../finolex/90m-silver.html">Finolex 90M Silver</a> is the everyday FR house wire — PVC insulated, electrolytic-grade bare copper conductor, 90-metre coil, available from 0.75 to 6.0 sq mm. It is what the great majority of houses in Karnataka are actually wired with.</p>
<p><a href="../finolex/90m-gold.html">Finolex 90M Gold</a> sits above it as the premium tier, on the same New Improved FR platform, in the same coil length and the same size range. It is used for exactly the same circuits.</p>

<h2>Side by side</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th></th><th>90M Silver</th><th>90M Gold</th></tr></thead>
<tbody>
<tr><td>Grade</td><td>FR (flame retardant)</td><td>FR (flame retardant), premium tier</td></tr>
<tr><td>Coil length</td><td>90 metres</td><td>90 metres</td></tr>
<tr><td>Sizes</td><td>0.75 to 6.0 sq mm</td><td>0.75 to 6.0 sq mm</td></tr>
<tr><td>Conductor</td><td>Electrolytic-grade bare copper</td><td>Electrolytic-grade bare copper</td></tr>
<tr><td>Smoke and halogen behaviour</td><td>Standard FR</td><td>Standard FR</td></tr>
<tr><td>Typical use</td><td>Lights, fans, sockets, AC and geyser points</td><td>Lights, fans, sockets, AC and geyser points</td></tr>
<tr><td>Price</td><td>Lower</td><td>Higher</td></tr>
</tbody></table></div>
<p>Notice the row that does not change between the two columns: smoke and halogen behaviour. Both are FR. Moving from Silver to Gold moves you up a tier within the same grade — it does not change what the insulation does in a fire.</p>

<h2>The decision most people should actually be making</h2>
<p>In a house fire, smoke and toxic gas incapacitate people before flame reaches them. That is why the meaningful step up from standard FR is <strong>FR-LSH</strong> (Finolex's Flamegard range, sold as <a href="../finolex/90m-frls.html">90M FRLS</a>) which emits lower smoke and reduced halogen gases, or <strong>Finolex Ultra</strong>, the E-Beam irradiated LSZH range at the top of the line.</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Option</th><th>What you get for the extra money</th></tr></thead>
<tbody>
<tr><td>Silver to Gold</td><td>The premium tier of the same FR grade</td></tr>
<tr><td>FR to FR-LSH</td><td>Lower smoke and reduced halogen gases in a fire</td></tr>
<tr><td>FR to Ultra</td><td>Highest heat resistance, lowest smoke and halogen emission</td></tr>
</tbody></table></div>
<p>So if you have a fixed budget and you are asking us, the more useful spend is usually not upgrading every coil from Silver to Gold. It is putting <strong>FR-LSH or Ultra into the bedrooms, children's rooms and enclosed spaces</strong> — the rooms where people sleep and where smoke does its damage — and keeping standard FR in utility areas, store rooms and outdoor points. Grades mix perfectly well within one house. The full grade comparison is in <a href="fr-vs-frls-vs-finolex-ultra.html">FR vs FRLS vs Finolex Ultra</a>.</p>

<h2>What matters far more than the tier</h2>
<p>Here is the uncomfortable truth about this whole comparison. The difference between a genuine Silver coil and a genuine Gold coil is smaller than the difference between a genuine coil and a counterfeit one wearing either label.</p>
<p>A duplicate coil can be under-weight on copper by 10 or 15 per cent while looking identical on the shelf. That shortfall makes the wire run hotter for its entire thirty-year life, on every circuit, in every room — a far bigger safety difference than any tier upgrade you can buy. Which is why the tier question should come second and this should come first:</p>
""" + TWO_LAYER + """
<p>Scan both codes on every coil, whichever range you choose. <a href="original-finolex-wire-checklist-before-paying.html">The full 12-point checklist is here.</a></p>

<h2>Rough coil counts, either way</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Size</th><th>Circuit</th><th>Indicative 90 m coils, compact 2BHK</th></tr></thead>
<tbody>
<tr><td>1.0 sq mm</td><td>Lights and fans</td><td>3 to 5</td></tr>
<tr><td>1.5 sq mm</td><td>Fan, light and utility circuits</td><td>3 to 5</td></tr>
<tr><td>2.5 sq mm</td><td>6A and 16A sockets, kitchen, fridge</td><td>4 to 6</td></tr>
<tr><td>4.0 sq mm</td><td>Air-conditioner and geyser points</td><td>2 to 3</td></tr>
<tr><td>6.0 sq mm</td><td>Sub-mains, long heavy runs</td><td>1 to 2</td></tr>
</tbody></table></div>
<p class="ptable-note">Indicative only — layout, point count and run lengths move these figures a great deal. Work yours out with the free <a href="../tools/wire-quantity-calculator.html">wire quantity calculator</a>, or send us the point list.</p>

<h2>Price, honestly</h2>
<p>Gold costs more than Silver, and both move with the copper market, because most of what you are paying for in a coil is the copper inside it. That is why we publish approximate ranges on the <a href="../price-lists/finolex-price-list.html">Finolex price list page</a> rather than a rate card that would be wrong within days.</p>
<p>For today's exact difference on your specific list, message it across. And apply the standard test to whatever you are quoted anywhere: genuine branded wire runs on a 3 to 5 per cent dealer margin, so a seller 15 per cent below the market is not being generous — the money is coming out of the coil.</p>
""" + CTA,
 D,
 [("What is the difference between Finolex Silver and Gold 90M?", "Both are flame-retardant (FR) grade PVC-insulated house wire on 90-metre coils, in the same 0.75 to 6.0 sq mm size range, with electrolytic-grade bare copper conductors. Gold is the premium tier of the two. Crucially, both are standard FR, so moving from Silver to Gold does not change smoke or halogen behaviour in a fire."),
  ("Is Finolex Gold worth the extra cost over Silver?", "It buys the premium tier of the same FR grade. If your goal is materially better fire performance rather than a higher tier, the better use of the same money is usually putting FR-LSH (Flamegard) or Finolex Ultra into bedrooms and enclosed rooms where smoke does its damage, and keeping standard FR in utility areas."),
  ("Which Finolex wire is best for bedrooms?", "FR-LSH (Finolex Flamegard) or Finolex Ultra, rather than either Silver or Gold. In a house fire, smoke and toxic gas incapacitate people before flame reaches them, and those are the two ranges engineered for lower smoke and reduced halogen emission. Bedrooms and children's rooms are where that matters most."),
  ("Can I use Finolex Silver and Gold in the same house?", "Yes. Ranges and grades mix perfectly well within one house as long as each circuit is correctly sized and terminated. Many buyers mix deliberately — a higher grade in sleeping and enclosed areas, standard FR elsewhere — which is usually better value than upgrading tier uniformly."),
  ("How many 90M coils does a 2BHK need?", "Indicatively around fifteen to twenty coils across the sizes: roughly 3 to 5 of 1.0 sq mm, 3 to 5 of 1.5 sq mm, 4 to 6 of 2.5 sq mm, 2 to 3 of 4.0 sq mm and 1 to 2 of 6.0 sq mm. Layout, point count and run lengths move these numbers considerably, so use a wire quantity calculator or send the point list for a proper working."),
  ("Does the Silver versus Gold choice matter more than buying genuine?", "No, and not close. A counterfeit coil can be under-weight on copper by 10 to 15 per cent while looking identical on the shelf, which makes the wire run hotter for its entire life on every circuit. That is a far larger safety difference than any tier upgrade. Scan the outer and inner QR codes on every coil before deciding anything else.")],
 ("woman-homeowner-choosing-modular-switches.jpg", "A homeowner in Karnataka comparing Finolex 90M Silver and Gold house wire options before buying"),
 None),

# ---------------------------------------------------------------- 3
("what-is-finolex-project-packing",
 "What Is Finolex Project Packing? A Plain Explanation for Builders",
 "Project packing means longer coils and project-quantity supply rather than retail 90-metre boxes. Here is what actually changes, the arithmetic on joints and offcut wastage, and the jobs where it saves nothing at all.",
 "Projects",
 """<p><strong>Finolex project packing is wire supplied in project quantities and longer coil lengths — typically 180-metre and 300-metre coils — for construction projects, instead of the 90-metre retail cartons a household buys. The benefit is fewer mid-run joints and less offcut wastage across repeating circuit lengths. On a single independent house it usually saves nothing.</strong></p>

<h2>Why retail packing is 90 metres</h2>
<p>Ninety metres is a household unit. It is a carton one person can lift, count and pay for, it suits the run lengths in an ordinary house, and it keeps the quantity you have to verify down to something you can actually verify — one box at a time.</p>
<p>A project has none of those constraints and a completely different problem: hundreds of coils, long horizontal runs, repeating circuit lengths floor after floor, and a site store issuing material daily.</p>

<h2>What project packing changes</h2>
<p>Two things, and both are money.</p>
<h3>Fewer joints</h3>
<p>A 40-metre continuous run served from a 90-metre coil is fine. Served from the 25-metre tail left on a previous coil, it needs a joint. Joints are where installations lose reliability, where resistance and heat creep in, and where inspection time goes. Moving to <a href="../finolex/180m.html">180-metre</a> or <a href="../finolex/300m.html">300-metre</a> coils removes most mid-run joints from a project.</p>
<h3>Less offcut wastage</h3>
<p>Every coil ends in a tail too short for the next run and too long to throw away without noticing. On one house that is a few metres. On a hundred-flat project it is a quantity you paid copper prices for and then binned. Longer coils produce proportionally fewer tails.</p>

<h2>When it helps and when it does not</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Job</th><th>Sensible packing</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Single independent house, ordinary rooms</td><td>90 m</td><td>Runs are short; long coils are heavy and awkward with no offsetting saving</td></tr>
<tr><td>Large house or duplex with long runs</td><td>Mix of 90 m and 180 m</td><td>Long circuits from 180 m, short ones from 90 m</td></tr>
<tr><td>Apartment block, repeating unit layouts</td><td>180 m and 300 m</td><td>Repeating circuit lengths, far fewer joints, much less tail wastage</td></tr>
<tr><td>Commercial floor plate, long horizontal runs</td><td>300 m</td><td>Continuous runs without mid-run joints</td></tr>
</tbody></table></div>
<p class="ptable-note">If you are wiring one house, we will usually tell you to stay on 90-metre coils. Project packing is a real saving on project-shaped work and an inconvenience on domestic work.</p>

<h2>What we can and cannot promise about format</h2>
<p>The exact packing available depends on the size and grade you need — not every size exists in every coil length at every moment. Rather than promise a format in the abstract, we confirm it against your bill of quantities when we quote. If a size you need is not available in the length you want, we will say so and propose the nearest sensible alternative instead of substituting silently.</p>

<h2>The verification problem project packing creates</h2>
<p>Here is the part nobody puts in a brochure. Longer coils and larger consignments mean <em>fewer cartons per metre of wire</em>, which sounds like less to check. It is not, because the exposure per carton goes up correspondingly. A refilled 300-metre carton is three times the problem a refilled 90-metre carton is.</p>
""" + TWO_LAYER + """
<p>On project quantities, verification has to be somebody's assigned job rather than a good intention. The workable routine is: count cartons and check seals at the gate, scan the outer code on every carton as it comes off the vehicle, scan the inner code at the moment each carton is opened for issue from the store, and log carton, batch, result and date. At roughly twenty seconds a scan, a hundred-carton delivery is about thirty-five minutes of one person's day. Set against the cost of rewiring a floor, that is not a close call. More on this in <a href="bulk-finolex-wire-orders-builders-karnataka.html">bulk Finolex orders for builders</a>.</p>

<h2>How to ask for a project quotation</h2>
<p>Send the bill of quantities — sizes, grades, quantities and the phase each is needed in. A photograph of the estimate works as well as a spreadsheet. You get an itemised quotation within 60 minutes, with freight shown as a separate line for sites outside Bengaluru so the landed cost is visible rather than buried in the rate.</p>
<p>Dispatch is phased against your programme, so material arrives when the floor needs it rather than sitting on site for months collecting damage and shrinkage. Full detail on the <a href="../finolex-project-packing-dealers.html">Finolex project packing</a> page.</p>
""" + CTA,
 D,
 [("What is Finolex project packing?", "It is wire supplied in project quantities and longer coil lengths — typically 180-metre and 300-metre coils — for construction projects, rather than the 90-metre retail cartons households buy. The benefit is fewer mid-run joints and less offcut wastage across repeating circuit lengths."),
  ("Is project packing cheaper than 90M coils?", "On project-shaped work usually yes, because longer coils cut mid-run joints and reduce the short tail ends left at the end of every coil, which on a large project add up to a quantity you paid copper prices for and then binned. On a single independent house it generally is not, because runs are short and long coils are heavy and awkward with no offsetting saving."),
  ("What coil lengths does project packing use?", "Commonly 180-metre and 300-metre coils rather than the retail 90-metre carton. Which lengths are available depends on the size and grade, so the exact format should be confirmed against your bill of quantities at quotation stage rather than assumed."),
  ("Is there a minimum quantity for a Finolex project order?", "There is no fixed minimum. What decides whether project packing makes sense is the shape of the work rather than a coil count — repeating circuit lengths and long horizontal runs favour 180-metre and 300-metre coils, a single house with ordinary rooms does not. Send the bill of quantities to 88676 76700 for advice."),
  ("How do you verify a project-quantity consignment?", "Make it an assigned job. Count cartons and check seals at the gate, scan the outer QR on every carton as it is unloaded, scan the inner QR at the moment each carton is opened for issue from the store, and log carton, batch, result and date. At about twenty seconds a scan, a hundred-carton delivery is roughly thirty-five minutes of one person's time."),
  ("Can project material be delivered in phases?", "Yes. Dispatch is scheduled against the construction programme so material arrives as each stage needs it, instead of one large delivery that has to be stored and guarded for months while it collects damage and shrinkage.")],
 ("house-under-construction-conduit-wiring.jpg", "Concealed conduit wiring on a Karnataka construction project supplied with Finolex project packing coils"),
 None),

# ---------------------------------------------------------------- 4
("finolex-dealer-price-vs-retail-price",
 "Finolex Dealer Price vs Retail Price: What the Gap Really Is",
 "The gap between a distributor rate and a retail counter price is real but much smaller than most buyers imagine — and understanding its true size is the single best defence against counterfeit wire.",
 "Pricing",
 """<p><strong>The gap between a Finolex dealer or distributor price and a retail counter price is genuine but narrow, because branded wire runs on a 3 to 5 per cent dealer margin. A distributor sells nearer that floor and a retail counter nearer MRP. Any seller claiming 15 to 20 per cent below the market is not offering a better dealer price — that gap is funded from inside the coil.</strong></p>

<h2>Why the margin is so thin</h2>
<p>Most of what you pay for in a coil of house wire is the copper inside it. Copper is a globally traded commodity with a published daily price that every honest seller in India pays the same way. It is not a cost anyone negotiates their way around.</p>
<p>That single fact governs this entire subject. If the raw material is 70 to 80 per cent of the cost and its price is externally fixed, then the entire space available for discounting, distribution, storage, transport and profit is what remains. In practice, genuine branded wire moves on a <strong>3 to 5 per cent dealer margin</strong>. It is a volume business, not a margin business.</p>

<h2>What the price ladder actually looks like</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Level</th><th>Roughly where the price sits</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Printed MRP</td><td>The ceiling</td><td>A maximum, not a market price</td></tr>
<tr><td>Retail counter</td><td>At or near MRP</td><td>Small volumes, single-coil handling, shop overheads</td></tr>
<tr><td>Distributor rate</td><td>Meaningfully below MRP</td><td>Volume purchasing and direct sourcing, within a 3-5% margin</td></tr>
<tr><td>"Special" 15-20% below market</td><td>Below any honest floor</td><td>Not a discount. Short coil, light copper, or counterfeit</td></tr>
</tbody></table></div>
<p>We publish approximate ranges rather than exact figures on the <a href="../price-lists/finolex-price-list.html">Finolex price list page</a>, precisely because the copper component moves. Anyone showing you a fixed rate card that never changes is quoting stale numbers.</p>

<h2>Where the saving actually shows up</h2>
<p>On two coils, the difference between a distributor rate and a counter price is small enough that it may not be worth the trip. On a full house of wiring — fifteen to twenty-five coils across five sizes — the same percentage applied to a much larger number becomes worth having. That is the honest shape of it: the distributor advantage scales with quantity and is close to irrelevant below a certain size.</p>
<p>We tell customers this openly, including when it costs us the order. If you are in Bidar and you want four coils, freight from Bengaluru will beat any saving we can offer and we will say so.</p>

<h2>The three ways a quote gets to be too cheap</h2>
<p>When a price is far below the honest floor, the money has to come from somewhere. There are only three places:</p>
<ul>
<li><strong>Copper shortfall.</strong> The conductor carries less copper than the sq mm printed on the insulation. Looks identical, runs hotter for thirty years.</li>
<li><strong>Short coil.</strong> The carton says 90 metres and holds 82. You do not find out until you are three rooms short at the end of the job.</li>
<li><strong>Counterfeit.</strong> Not Finolex wire at all, in a Finolex-looking carton — sometimes in a genuine Finolex carton that has been emptied and refilled.</li>
</ul>
<p>That last case is exactly why the inner QR code exists:</p>
""" + TWO_LAYER + """

<h2>Using a quote as a reference price</h2>
<p>This is the practical takeaway, and it costs you nothing. Before buying wire anywhere in Karnataka, send your list to a distributor and get an itemised quotation. Then compare.</p>
<ul>
<li><strong>A few per cent either way:</strong> normal. Different sellers, different freight, different overheads.</li>
<li><strong>Far above:</strong> you are being overcharged. Negotiate or walk.</li>
<li><strong>Far below:</strong> the difference is inside the coil. Scan both QR codes on every carton before you pay, and if either fails, walk.</li>
</ul>
<p>Send your list to <a href="{W}">{PH}</a> and the itemised quotation comes back within 60 minutes. Ask for it purely as a reference price if you like — say so plainly and we will still send it inside the hour, with no follow-up pressure. A market where buyers know the real price is a market we do better in.</p>
<p>The related reads: <a href="original-finolex-wire-price-check.html">why cheap Finolex is not Finolex</a>, <a href="copper-price-and-wire-rates-explained.html">how copper prices drive wire rates</a>, and the full <a href="../original-vs-duplicate-electrical-products.html">original vs duplicate buyer's guide</a>.</p>
""".replace("{W}", W).replace("{PH}", PH) + CTA,
 D,
 [("What is the difference between Finolex dealer price and retail price?", "A distributor sells nearer the floor of the honest price band and a retail counter nearer MRP, but the whole band is narrow because genuine branded wire runs on a 3 to 5 per cent dealer margin. The gap is real and worth having on a full house of wiring, and close to irrelevant on two or three coils."),
  ("Why is the margin on wire so small?", "Because most of a coil's cost is the copper inside it, and copper is a globally traded commodity with a published daily price that every honest seller pays identically. When the raw material is 70 to 80 per cent of the cost and externally fixed, the space left for discount, distribution and profit is only a few per cent."),
  ("Is a 20% discount on Finolex wire possible?", "Not honestly. Genuine branded wire moves on a 3 to 5 per cent dealer margin, so there is no route to 20 per cent below the market that does not come out of the product. The three places that money comes from are copper shortfall in the conductor, a short coil, or an outright counterfeit — sometimes in a genuine carton that has been emptied and refilled."),
  ("How much can I save buying Finolex from a distributor?", "It scales with quantity. On a full house of wiring — typically fifteen to twenty-five coils across five sizes — a few per cent applied to a large total is worth having. On two or three coils it usually is not worth the trip, and if freight is involved it can be worse than buying locally. We will tell you which case you are in."),
  ("Why don't you publish exact Finolex prices?", "Because a coil's price is mostly the price of the copper inside it, and copper moves daily. A fixed rate card would be wrong within days and anyone showing you one that never changes is quoting stale numbers. We publish approximate ranges and give the day's exact figure on WhatsApp within 60 minutes."),
  ("Can I use a distributor quote just to check another shop's price?", "Yes, and it is one of the most useful things a buyer can do. Ask for the quotation on that basis and you will still get it inside the hour with no follow-up pressure. A few per cent either way is normal; far below the reference means the difference is inside the coil, and you should scan both QR codes on every carton before paying.")],
 ("contractor-checking-price-list-phone.jpg", "A contractor in Karnataka comparing a Finolex dealer quotation against a retail counter price on his phone"),
 None),

# ---------------------------------------------------------------- 5
("verify-finolex-dealer-stock-before-ordering",
 "How to Verify a Finolex Dealer's Stock Before You Order",
 "You can check a dealer's stock before committing a rupee — in the showroom, over WhatsApp, or before dispatch. Here is exactly what to ask for and what a straight answer looks like.",
 "Verification",
 """<p><strong>You can verify a Finolex dealer's stock before ordering: ask to scan cartons yourself in the showroom, ask for the outer QR codes on your consignment to be scanned and the record sent to you before dispatch, and then scan the outer and inner codes again at your own site before paying. A dealer who refuses any of these has answered your question.</strong></p>

<h2>Verification is not a favour you ask for</h2>
<p>Most buyers treat checking stock as slightly rude — as though asking to open a carton implies an accusation. It does not. It is ordinary commercial diligence on a product that will be sealed inside your walls for thirty years and that you cannot judge by looking at.</p>
<p>Our own position: we invite it. Come to Chickpete or Jayanagar, pick cartons off the stack yourself — not the ones we hand you — and we will open them for you to scan. Any coil, or the entire stock. If that offer makes a seller uncomfortable, that discomfort is information.</p>

<h2>Stage 1 — Before you place the order</h2>
<p>Three questions, asked plainly:</p>
<ol>
<li><strong>"Are you an authorised Finolex dealer or distributor, and may I see the certificate?"</strong> A genuine seller answers without irritation. The certificate is necessary but not sufficient — it proves a commercial relationship, not what is in this particular carton.</li>
<li><strong>"Is the material in stock, or are you indenting it?"</strong> This matters more than it sounds. Stock that exists can be scanned today. Stock that will be "arranged" is being bought from somewhere you cannot see, and that is where grey material enters.</li>
<li><strong>"May I scan cartons before I pay?"</strong> The only acceptable answer is yes.</li>
</ol>

<h2>Stage 2 — Checking stock you cannot visit</h2>
<p>If you are in Mysuru, Hubballi or Mangaluru and the dealer is in Bengaluru, you can still verify a good deal remotely:</p>
<ul>
<li><strong>Ask for photographs of the actual cartons</strong> allocated to your order — the printed label showing size, grade, coil length and batch, not a stock image.</li>
<li><strong>Ask for the outer QR codes to be scanned before dispatch</strong> and the verification record sent to you on WhatsApp.</li>
<li><strong>Ask for the batch numbers in writing.</strong> If a dispute ever arises, the batch number is what makes a complaint to Finolex traceable.</li>
<li><strong>Check the invoice wording before payment</strong> — brand, range, size and coil length on each line, not "wire".</li>
</ul>
<p>Remote verification narrows the risk considerably, but it does not close it, which brings us to the part that matters most.</p>

<h2>Stage 3 — At your own site, before money moves</h2>
<p>Nothing replaces scanning the material yourself once it is in front of you. Pre-dispatch checks confirm what left the godown; the site scan confirms what arrived.</p>
""" + TWO_LAYER + """
<p>Do this on every carton, not a sample. Twenty seconds each. Open at minimum every carton you intend to use that week and scan the inner code, and ideally open all of them. Then look at the wire itself — the markings printed along the insulation should be crisp and evenly spaced, and the copper at a cut end should look right for the sq mm on the label. Detail in <a href="finolex-wire-insulation-markings.html">reading insulation markings</a> and the <a href="original-finolex-wire-checklist-before-paying.html">12-point checklist</a>.</p>
<p>Inside Bangalore we deliver free by the next day and collect payment at your site after this sequence, which is the entire reason we work pay-on-delivery. Outside Bengaluru, payment terms are agreed in writing before dispatch — ask for the scan-before-dispatch record as part of those terms.</p>

<h2>Answers that should end the conversation</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>What you hear</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>"Opening the box will damage the packing"</td><td>Walk. The inner code is inside the box; this objection exists to block the one check that catches refilling</td></tr>
<tr><td>"Scan it at home, it will show genuine"</td><td>Walk. Verification after payment is not verification</td></tr>
<tr><td>"We don't have it in stock but we'll arrange it"</td><td>Ask where from, and insist on scanning whatever arrives before paying</td></tr>
<tr><td>"Bill will be for electrical items, brand rate is different"</td><td>Walk. No brand name on the invoice means no warranty and no traceable complaint</td></tr>
<tr><td>"Certificate is with the owner, he's out of station"</td><td>Wait for the certificate, or buy elsewhere. There is no hurry that justifies skipping this</td></tr>
</tbody></table></div>

<h2>If something fails</h2>
<p>Do not pay, do not let installation start, and keep everything — cartons, inserts, a cut sample of wire, the invoice and photographs of the verification screens. Then raise it with the seller in writing so there is a record, and escalate to Finolex customer care on <strong>1800-209-0166</strong> with the batch number and the seller's details. The full procedure is in <a href="received-duplicate-finolex-wire-complaint.html">what to do if you received duplicate Finolex wire</a>.</p>
<p>And if you simply want a second opinion on something you have been offered anywhere in Karnataka, send photographs of the carton label, both codes and the wire markings to <a href="{W}">{PH}</a>. We will tell you what we see, whether or not you bought it from us.</p>
""".replace("{W}", W).replace("{PH}", PH) + CTA,
 D,
 [("Can I check a Finolex dealer's stock before ordering?", "Yes, and you should. In a showroom, ask to pick cartons off the stack yourself and scan them. Remotely, ask for photographs of the actual cartons allocated to your order and for the outer QR codes to be scanned before dispatch with the record sent to you. Then scan the outer and inner codes again at your own site before paying."),
  ("What should I ask a Finolex dealer before placing an order?", "Three things: whether they are an authorised dealer or distributor and can show the certificate; whether the material is physically in stock or is being indented from elsewhere; and whether you may scan cartons before you pay. The only acceptable answer to the third question is yes."),
  ("How do I verify stock if the dealer is in another city?", "Ask for photographs of the actual cartons allocated to your order showing the printed label with size, grade, coil length and batch — not stock images. Ask for the outer QR codes to be scanned before dispatch and the record sent on WhatsApp. Get the batch numbers in writing, and check the invoice wording before paying. Then scan again yourself on arrival."),
  ("Is it rude to ask to open a Finolex carton before buying?", "No. It is ordinary diligence on a product that will be sealed inside your walls for thirty years and cannot be judged by looking at it. The inner QR code is inside the box, so opening a carton is the only way to run the check that catches a genuine carton refilled with duplicate wire."),
  ("What if the dealer says opening the box will damage the packing?", "Treat that as the end of the conversation. The objection exists precisely to prevent the inner-code check. A genuine seller expects cartons to be opened and scanned before payment, because material that verifies has nothing to lose from being verified."),
  ("What should I do if a QR code fails verification?", "Do not pay and do not let installation begin. Preserve the cartons, inner inserts, a cut sample of wire and the invoice, and photograph everything including the verification screen. Raise it with the seller in writing, then escalate to Finolex customer care on 1800-209-0166 with the batch number and the seller's name and location.")],
 ("electrician-scanning-qr-code-wire-coil.jpg", "Scanning the QR code on a Finolex carton to verify a dealer's stock before placing an order"),
 {"name": "How to verify a Finolex dealer's stock before ordering",
  "steps": [
    ("Ask for the authorisation certificate", "Ask whether the seller is an authorised Finolex dealer or distributor and to see the certificate. A genuine seller answers without irritation."),
    ("Confirm the material is physically in stock", "Ask whether the coils exist now or are being indented from elsewhere. Stock that exists can be scanned today; stock that will be arranged comes from a source you cannot see."),
    ("Scan cartons yourself in the showroom", "Pick cartons off the stack rather than accepting the ones handed to you, and scan the outer QR on each. Ask for boxes to be opened so you can scan the inner code too."),
    ("Get pre-dispatch verification for outstation orders", "Ask for photographs of the actual cartons allocated to your order and for the outer QR codes to be scanned before dispatch, with the record sent to you on WhatsApp along with the batch numbers in writing."),
    ("Check the invoice wording", "Each line should name the brand, range, size and coil length rather than simply 'wire'. Without the brand named there is no warranty and no traceable complaint."),
    ("Scan again at your own site before paying", "Scan the outer code on every carton and the inner code on every carton you open. Pre-dispatch checks confirm what left the godown; the site scan confirms what arrived."),
    ("Stop if anything fails", "Do not pay and do not begin installation. Preserve cartons, inserts, a cut wire sample and the invoice, photograph the verification screens, raise it in writing with the seller and escalate to Finolex customer care on 1800-209-0166.")]}),

# ---------------------------------------------------------------- 6
("bulk-finolex-wire-orders-builders-karnataka",
 "Bulk Finolex Wire Orders for Builders in Karnataka: A Practical Guide",
 "Ordering wire by the hundred coils is a different job from buying twenty. Quotation, phasing, receiving routine, verification at scale and the contract clauses that keep counterfeit material off your site.",
 "Projects",
 """<p><strong>For a bulk Finolex order in Karnataka, send an itemised bill of quantities with the phase each size is needed in, get a line-by-line quotation with freight shown separately, take delivery in phases against your programme, and make QR verification of every carton a named person's job before payment is released.</strong></p>

<h2>Why projects attract counterfeit wire</h2>
<p>Counterfeit material is not spread evenly across the market. It concentrates where three conditions occur together: large quantities, nobody personally attached to the outcome, and material that disappears into a wall within days of arriving. A construction project is all three at once.</p>
<p>A family buying twenty coils will open a box out of curiosity. A site store taking four hundred cartons across six months will not, unless checking is written into somebody's job description. That gap is the entire opportunity, and closing it costs about thirty-five minutes per hundred cartons.</p>

<h2>Stage 1 — The quotation</h2>
<p>Send sizes, grades, quantities and the phase each is needed in. A photograph of the estimate works as well as a spreadsheet. What you should get back, within 60 minutes:</p>
<ul>
<li><strong>Line-by-line pricing</strong> — brand, range, size, coil length, quantity, rate. Not a lump sum.</li>
<li><strong>Freight as a separate line</strong> for sites outside Bengaluru, so the landed cost is visible rather than buried in the rate.</li>
<li><strong>A dispatch schedule</strong> tied to your programme.</li>
<li><strong>Confirmation of what is physically in stock</strong> versus what would have to be arranged.</li>
</ul>
<p>That last point decides more than people realise. A distributor holding stock can commit to a schedule; a seller indenting against your order is buying from a source neither of you can see.</p>

<h2>Stage 2 — Phasing the deliveries</h2>
<p>Taking the whole order in one delivery looks efficient and rarely is. Material sits on site for months absorbing damage, damp and shrinkage, and a large stack of copper is the most attractive thing on any site. Phased dispatch against the construction programme means each floor's material arrives when that floor needs it.</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Phase</th><th>Typically needed</th></tr></thead>
<tbody>
<tr><td>Conduiting</td><td>Conduit, accessories, junction boxes — no wire yet</td></tr>
<tr><td>Wire pulling</td><td>The bulk of 1.0, 1.5 and 2.5 sq mm coils</td></tr>
<tr><td>Heavy circuits</td><td>4.0 and 6.0 sq mm for AC, geyser and sub-mains</td></tr>
<tr><td>Termination and fit-out</td><td>Switches, sockets, DB components, remaining short runs</td></tr>
</tbody></table></div>

<h2>Stage 3 — The receiving routine</h2>
<p>This is the part that actually protects the project. Write it down, assign it to a named person, and do not treat it as optional:</p>
<ol>
<li><strong>At the gate.</strong> Count cartons against the challan. Check seals before anything is unloaded into the store. A broken or re-taped seal is stopped there, not investigated later.</li>
<li><strong>Outer code on every carton.</strong> One person, one phone, scanning as cartons come off the vehicle. Confirm the reported size, grade and batch match the label.</li>
<li><strong>Inner code at issue.</strong> Cartons get opened when the store issues wire anyway. Scan the inner code at that moment and the check costs no extra handling.</li>
<li><strong>Log everything.</strong> Carton, batch, scan result, date, initials. If a dispute ever arises, this log is the difference between a claim and an argument.</li>
</ol>
""" + TWO_LAYER + """
<p>The time objection does not survive contact with the numbers: twenty seconds a scan means a hundred-carton delivery is about thirty-five minutes of one person's day. Rewiring one floor because a batch was light on copper is a different order of cost entirely.</p>

<h2>Stage 4 — The contract clauses</h2>
<p>If you are letting electrical work with material included, understand the incentive that creates: every rupee saved on material is the contractor's profit, and you will never see the boxes. That is arithmetic, not an accusation. Four clauses fix it, and none of them cost an honest contractor anything:</p>
<ul>
<li>Cartons delivered sealed and opened <strong>at site</strong>, not beforehand.</li>
<li><strong>Outer and inner QR verification on every carton</strong>, in the presence of your engineer, before payment is released.</li>
<li>GST invoices naming brand, range, size and coil length on each line.</li>
<li>Your right to cross-check rates against a reference distributor before releasing payment.</li>
</ul>
<p>A contractor who agrees to all four immediately is telling you something useful. So is one who does not. More on the tactics involved in the <a href="../original-vs-duplicate-electrical-products.html">original vs duplicate buyer's guide</a> and <a href="electrician-retailer-nexus-duplicate-wires.html">the electrician-retailer nexus</a>.</p>

<h2>Stage 5 — The rate sanity check</h2>
<p>Before releasing a large material payment, price the same bill of quantities with a second distributor. Genuine branded wire runs on a 3 to 5 per cent dealer margin, so honest quotes cluster. A quote sitting 15 or 20 per cent below the others on a project-sized order is not a commercial win — on that quantity, the shortfall it represents is measured in kilograms of copper. Detail in <a href="finolex-dealer-price-vs-retail-price.html">dealer price vs retail price</a>.</p>

<h2>Ordering from us</h2>
<p>We are one of the largest dealers and distributors of Finolex cables in the country, holding every range in stock at our Bengaluru godown. Inside Bangalore, delivery is free by the next day with payment collected at your site after verification. Across the rest of Karnataka we supply by road transport against a written quotation with freight itemised — we have no branches outside Bengaluru and will not claim any. See the <a href="../bulk-finolex-wire-supplier-karnataka.html">bulk supply page</a> or the <a href="../finolex-project-packing-dealers.html">project packing page</a>.</p>
<p>Send the bill of quantities to <a href="{W}">{PH}</a> and the itemised quotation comes back within 60 minutes. If you want it purely to benchmark another supplier, say so and you will still have it inside the hour.</p>
""".replace("{W}", W).replace("{PH}", PH) + CTA,
 D,
 [("How do I place a bulk Finolex wire order for a project in Karnataka?", "Send an itemised bill of quantities listing sizes, grades, quantities and the phase each is needed in — a photograph of the estimate is fine. You should get back a line-by-line quotation within 60 minutes with freight shown separately for sites outside Bengaluru, a dispatch schedule tied to your programme, and confirmation of what is physically in stock versus what would be arranged."),
  ("Why are construction projects more exposed to counterfeit wire?", "Because counterfeit concentrates where three conditions occur together: large quantities, nobody personally attached to the outcome, and material that disappears into a wall within days. A family buying twenty coils opens a box; a site store taking four hundred cartons over six months does not, unless checking is written into someone's job."),
  ("Should a bulk order be delivered all at once?", "Usually not. A single large delivery sits on site for months absorbing damage, damp and shrinkage, and a stack of copper is the most attractive thing on any site. Phase the dispatch against the construction programme so each stage's material arrives when it is needed."),
  ("How long does it take to QR-verify a large delivery?", "About twenty seconds a carton, so roughly thirty-five minutes of one person's time for a hundred-carton delivery. Scan the outer code as cartons come off the vehicle and the inner code at the moment each carton is opened for issue from the store, which adds no extra handling."),
  ("What clauses should a builder put in a with-material electrical contract?", "Four: cartons delivered sealed and opened at site rather than beforehand; outer and inner QR verification on every carton in your engineer's presence before payment is released; GST invoices naming brand, range, size and coil length on each line; and your right to cross-check rates against a reference distributor before releasing payment. None of these cost an honest contractor anything."),
  ("How do I sanity-check a bulk wire quotation?", "Price the same bill of quantities with a second distributor. Genuine branded wire runs on a 3 to 5 per cent dealer margin, so honest quotes cluster within a few per cent. A quote sitting 15 or 20 per cent below the others on a project-sized order represents a shortfall measured in kilograms of copper, not a commercial win.")],
 ("happy-electrical-contractor-site-team.jpg", "A contractor's site team receiving and verifying a bulk Finolex wire consignment in Karnataka"),
 {"name": "How to run a bulk Finolex wire order on a construction project",
  "steps": [
    ("Send an itemised bill of quantities", "List sizes, grades, quantities and the phase each is needed in. A photograph of the estimate works as well as a spreadsheet."),
    ("Get a line-by-line quotation", "Insist on brand, range, size, coil length, quantity and rate per line, with freight shown separately for sites outside Bengaluru, plus confirmation of what is physically in stock."),
    ("Agree a phased dispatch schedule", "Tie deliveries to the construction programme so each stage's material arrives when it is needed rather than sitting on site absorbing damage and shrinkage."),
    ("Check seals and count at the gate", "Count cartons against the challan and inspect seals before anything is unloaded. A broken or re-taped seal is stopped at the gate, not investigated later."),
    ("Scan the outer QR on every carton", "One person with one phone, scanning as cartons come off the vehicle. Confirm the reported size, grade and batch match the printed label."),
    ("Scan the inner QR at issue", "Cartons are opened when the store issues wire anyway. Scan the inner code at that moment so the check costs no extra handling."),
    ("Log every scan", "Record carton, batch, scan result, date and initials. This log is what turns a future dispute into a claim rather than an argument."),
    ("Benchmark the rate before releasing payment", "Price the same bill of quantities with a second distributor. Honest quotes cluster within a few per cent because branded wire runs on a 3 to 5 per cent margin.")]}),

]
