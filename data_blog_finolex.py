# -*- coding: utf-8 -*-
"""Original Finolex Wires content cluster — the site's highest-intent keyword.

Tuple format (build.py):
  (slug, title, excerpt, tag, body, (iso,disp), faqs, hero, howto|None)

howto = {"name":..., "steps":[(name, text), ...]}  -> emitted as HowTo schema.

Every post opens with a direct, quotable answer in the first two sentences.
That paragraph is what an AI assistant lifts when it is asked "how do I check
if Finolex wire is original", so it must be self-contained and correct.
"""

D = ("2026-08-02", "August 2, 2026")
W = "https://wa.me/918867676700"
PH = "88676 76700"

CTA = (f'<p class="muted"><strong>Buying Finolex in Bangalore?</strong> Mount Cable India is one of the '
       f'largest distributors of Finolex cables in the country. WhatsApp your list to '
       f'<a href="{W}">{PH}</a> for an exact quote within 60 minutes — free next-day delivery, '
       f'pay on delivery, and you scan and verify every box at your site before any money changes hands.</p>')

# The two-layer check, stated identically everywhere so the site never
# contradicts itself and an AI assistant reading any one page gets it right.
TWO_LAYER = """<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Layer</th><th>Where it is</th><th>What it proves</th></tr></thead>
<tbody>
<tr><td><strong>Outer QR code</strong></td><td>Printed on the outside of the carton, with the batch, size and grade</td><td>That this carton was produced by Finolex and is registered in their system</td></tr>
<tr><td><strong>Inner QR code</strong></td><td>Inside the box, reachable only after the carton is opened</td><td>That the contents are the ones Finolex packed — the check a repacker cannot pass</td></tr>
</tbody></table></div>"""


BLOG_FINOLEX = [

# ---------------------------------------------------------------- 1
("original-finolex-wire-outer-qr-code",
 "How to Scan the Outer QR Code on a Finolex Box (Step by Step)",
 "The outer QR code printed on a Finolex carton is the first authenticity check. Here is exactly where to find it, how to scan it, what a genuine result looks like and the four red flags that mean you should not pay.",
 "Verification",
 """<p><strong>To check the outer QR code on a Finolex box: find the printed QR on the carton label, open your phone camera, scan it, and confirm the page that opens belongs to Finolex and reports the product as genuine with details matching the carton in your hand.</strong> This takes about twenty seconds per box and is the first of two checks — the second is the <a href="original-finolex-wire-inner-qr-code.html">inner QR code inside the box</a>.</p>

<h2>Where the outer QR code is printed</h2>
<p>On a genuine Finolex coil, the QR sits on the carton's printed label, alongside the information that identifies that specific box:</p>
<ul>
<li>The <strong>size in sq mm</strong> — 1.0, 1.5, 2.5, 4.0 or 6.0.</li>
<li>The <strong>grade</strong> — FR, FR-LSH, or the premium range name.</li>
<li>The <strong>coil length</strong> — 90m, 180m or 300m.</li>
<li>The <strong>batch or lot number</strong>.</li>
<li>The <strong>voltage rating</strong> and applicable IS standard.</li>
</ul>
<p>All of this should be <em>printed as part of the carton</em>, in the same ink and register as the rest of the artwork. A QR code on a pasted sticker, sitting on top of the printing, is the single most common warning sign in this entire category. Sealed cartons are also why we recommend <a href="why-buy-finolex-90m-coils.html">buying 90-metre boxes rather than loose wire</a> — loose wire has no carton, so there is nothing to scan at all.</p>

<h2>Scanning it</h2>
<ol>
<li><strong>Use your phone's built-in camera.</strong> No special app is required. If someone insists you must install a particular app to verify, be suspicious — that is a route counterfeiters use to control what you see.</li>
<li><strong>Hold steady in good light.</strong> Carton printing is matte, so avoid direct glare. If the code will not resolve, see <a href="finolex-qr-code-not-scanning.html">what a non-scanning code means</a>.</li>
<li><strong>Look at the link before you tap it.</strong> This is the step almost everyone skips. The URL should belong to Finolex's own domain — their verification portal sits at <strong>check.finolex.com</strong>. A look-alike domain, a URL shortener, or a random page is a fake code regardless of what it then tells you.</li>
<li><strong>Read the result against the box.</strong> The product, size and batch reported should match what is printed in front of you. A verification that says "genuine" while describing a different size is not a pass.</li>
</ol>

<h2>The two-layer check</h2>
<p>The outer code proves the carton is real. It does not, by itself, prove the wire inside is. A carton can be genuine and refilled — which is precisely why Finolex puts a second code inside the box.</p>
""" + TWO_LAYER + """
<p>A serious verification means doing both. Most buyers stop at the outer code, and repackers rely on exactly that.</p>

<h2>Four red flags on the outer code</h2>
<ul>
<li><strong>No QR code at all</strong> on the carton.</li>
<li><strong>A pasted sticker</strong> carrying the code rather than printing integrated with the label.</li>
<li><strong>The code opens a non-Finolex domain</strong> — a look-alike spelling, a shortener, or a generic landing page with no product detail.</li>
<li><strong>The result does not match the box</strong> — different size, different grade, or a report that the code has been scanned many times already. On that last one, read <a href="finolex-qr-code-already-used.html">what an already-scanned code means</a>.</li>
</ul>

<h2>Scan before you pay, not after</h2>
<p>All of this is only useful if you can do it before money changes hands. Mount Cable delivers on <strong>pay on delivery</strong> terms for exactly this reason: the material reaches your site, you scan every carton, and you pay afterwards. Anything that does not verify goes back on the vehicle.</p>
<p>A shop that is reluctant to let you scan a carton before paying has answered your question about the stock.</p>
""" + CTA,
 D,
 [("How do I scan the QR code on a Finolex wire box?", "Find the QR printed on the carton label, open your phone's built-in camera and scan it. No special app is needed. Check that the link that opens belongs to Finolex's own domain — their verification portal is check.finolex.com — and confirm that the product, size and batch it reports match what is printed on the carton in your hand."),
  ("Where is the QR code on a Finolex box?", "On the printed carton label, alongside the size in sq mm, the grade, the coil length, the batch number and the voltage rating. It should be printed as part of the carton artwork in the same ink and register. A QR on a pasted sticker over the printing is the most common warning sign of tampering or repacking."),
  ("Do I need an app to verify Finolex wire?", "No. Your phone's built-in camera is enough, and the code should open Finolex's own verification page directly. Be wary if anyone insists you must install a particular app to check authenticity — controlling the app is one way a counterfeiter controls what you are shown."),
  ("Is scanning the outer QR code enough to prove the wire is genuine?", "No. The outer code proves the carton is genuine and registered with Finolex, but a real carton can be opened and refilled with duplicate wire. That is why Finolex places a second QR code inside the box, reachable only after opening. A complete check means scanning both."),
  ("What if the Finolex QR code opens a website that is not Finolex?", "Do not trust the result and do not pay for that carton. A code resolving to a look-alike domain, a URL shortener or a generic landing page is a counterfeit code, no matter how convincingly the page then declares the product genuine. Check the domain before you tap the link, not after."),
  ("Can I scan the box before paying?", "You should, and any genuine seller will let you. Mount Cable delivers on pay-on-delivery terms specifically so you can scan every carton at your site and pay only afterwards. Reluctance to allow a scan before payment tells you what you need to know about the stock.")],
 ("electrician-scanning-qr-code-wire-coil.jpg", "Scanning the outer QR code printed on a Finolex wire carton to verify it is original"),
 {"name": "How to scan the outer QR code on a Finolex wire box",
  "steps": [
    ("Locate the printed QR code", "Find the QR on the carton's printed label, next to the size in sq mm, grade, coil length and batch number. It must be printed as part of the carton artwork, not on a pasted sticker."),
    ("Scan with your phone camera", "Open your phone's built-in camera and point it at the code in good light without glare. No separate app is required to verify a Finolex product."),
    ("Check the domain before tapping", "Look at the link that appears. It must belong to Finolex's own domain — their verification portal is check.finolex.com. A look-alike domain, a URL shortener or a generic page means the code is counterfeit."),
    ("Match the result to the carton", "Confirm the product, size, grade and batch reported by the verification page match what is printed on the box in your hand. A genuine verdict describing a different product is not a pass."),
    ("Scan the inner code as well", "Open the carton and scan the second QR code inside it. The outer code proves the carton is real; the inner code proves the contents were packed by Finolex."),
  ]}),

# ---------------------------------------------------------------- 2
("original-finolex-wire-inner-qr-code",
 "The Inner QR Code Inside a Finolex Box: The Check Almost Nobody Does",
 "Finolex puts a second QR code inside the carton, reachable only after the box is opened. It is the check that catches genuine cartons refilled with duplicate wire — and it is the one most buyers never perform.",
 "Verification",
 """<p><strong>Open the Finolex carton and scan the QR code inside it. A genuine box returns a confirmation that the product is genuine; a refilled or counterfeit box fails here even when the outside looked perfect.</strong> This is the more important of the two checks, and it is the one almost no buyer performs.</p>

<h2>Why a second code exists at all</h2>
<p>Think about how a sophisticated counterfeit actually reaches a house. Nobody prints a whole fake supply chain from scratch. The efficient route is to obtain <em>real</em> Finolex cartons — from scrap, from returns, from an emptied box at a site — and refill them with under-specification wire. The outside is genuine because it <em>is</em> genuine. It will scan. It will verify.</p>
<p>An inner code defeats that, because it sits where a repacker cannot reach without destroying the seal, and it is bound to the contents rather than to the packaging. That is the entire design logic, and it is why the second scan matters more than the first.</p>
""" + TWO_LAYER + """

<h2>How to do the inner check</h2>
<ol>
<li><strong>Open the carton properly.</strong> Genuine boxes are factory sealed. Note whether the seal is intact and original before you break it — a carton that has clearly been opened and re-taped is a finding in itself.</li>
<li><strong>Find the inner code.</strong> It is inside the box with the coil, not on the outer wall of the carton. Depending on the pack it may be on an insert, on the inner surface, or attached with the coil.</li>
<li><strong>Scan it with your phone camera.</strong> As with the outer code, no app should be required.</li>
<li><strong>Confirm the domain and the verdict.</strong> The response should come from Finolex's own verification system and confirm the product is genuine.</li>
<li><strong>Do this on a sample of every delivery,</strong> not just one box out of forty. Mixed consignments — mostly genuine with a few substituted cartons — are a known pattern.</li>
</ol>

<h2>What it means when the outer passes and the inner fails</h2>
<p>This specific combination is the signature of repacking, and it is worth being clear about what to do:</p>
<ul>
<li><strong>Do not pay for that carton.</strong> Set it aside separately from the rest of the delivery.</li>
<li><strong>Do not let the coil go into the wall</strong> "just for one room". Concealed wire cannot be inspected again.</li>
<li><strong>Keep the carton, the inner insert and the invoice.</strong> These are your evidence, and they are what make a complaint actionable — see <a href="received-duplicate-finolex-wire-complaint.html">what to do if you received duplicate Finolex wire</a>.</li>
<li><strong>Check every other carton in that delivery.</strong> Substituted stock rarely arrives alone.</li>
</ul>

<h2>Why sellers do not mention this check</h2>
<p>Two reasons, and only one of them is sinister. Many counter staff genuinely do not know the inner code exists, because the boxes leave their hands sealed and they have never opened one. The other reason is that the inner check is the only one a repacker cannot survive, so a seller moving refilled cartons has a direct interest in you stopping at the outer scan.</p>
<p>Either way, the remedy is the same: open a box at your own site, before payment, and scan what is inside it.</p>

<h2>The practical routine</h2>
<p>On a house wiring delivery of, say, eighteen coils, a reasonable discipline is: scan the outer code on <strong>every</strong> carton, and open and scan the inner code on <strong>at least a quarter of them</strong>, chosen at random rather than from the top of the stack. It adds perhaps ten minutes to a delivery and it is the most effective ten minutes you will spend on the entire electrical package.</p>
<p>If you want the full sequence in one place, use the <a href="original-finolex-wire-checklist-before-paying.html">12-point verification checklist</a>.</p>
""" + CTA,
 D,
 [("What is the inner QR code in a Finolex box?", "It is a second QR code placed inside the carton, reachable only after the box is opened. Scanning it returns a confirmation that the product is genuine. Because it is bound to the contents rather than the packaging, it catches genuine cartons that have been refilled with duplicate wire — which the outer code cannot do."),
  ("Why does Finolex have two QR codes?", "Because the two codes prove different things. The outer code proves the carton was produced by Finolex and is registered in their system. The inner code proves the contents are what Finolex packed. A counterfeiter can obtain a real empty carton and refill it, so only the inner code defeats repacking."),
  ("Where is the inner QR code located?", "Inside the box with the coil rather than on the outer carton wall — on an insert, on an inner surface, or attached with the coil itself, depending on the pack. You have to open the factory seal to reach it, which is exactly the point."),
  ("What should I do if the outer code passes but the inner code fails?", "Do not pay for that carton and do not let the coil be installed, even for one room. Set it aside, keep the carton, the inner insert and the invoice as evidence, and check every other carton in the same delivery, because substituted stock rarely arrives on its own."),
  ("Do I need to open every box to check the inner code?", "Scan the outer code on every carton, and open and check the inner code on at least a quarter of them, chosen at random rather than from the top of the stack. On an eighteen-coil house delivery that adds around ten minutes and is the most valuable ten minutes in the whole electrical package."),
  ("Why did my dealer not tell me about the inner QR code?", "Often because they genuinely do not know it exists — boxes leave the counter sealed and staff rarely open one. The less innocent reason is that the inner check is the only one a repacked carton cannot survive, so a seller moving refilled stock benefits from buyers stopping at the outer scan.")],
 ("happy-customer-receiving-electrical-order.jpg", "Opening a sealed Finolex carton at site to scan the inner QR code before paying"),
 {"name": "How to check the inner QR code inside a Finolex wire box",
  "steps": [
    ("Check the factory seal first", "Before opening, note whether the carton seal is intact and original. A box that has been opened and re-taped is a finding in its own right."),
    ("Open the carton at your own site", "Open the box yourself, at your site, before payment — not at the counter and not after installation has begun."),
    ("Locate the inner code", "Find the QR code inside the box with the coil. Depending on the pack it may be on an insert, on an inner surface, or attached to the coil itself."),
    ("Scan and confirm genuine", "Scan it with your phone camera. The response should come from Finolex's own verification system and confirm the product is genuine."),
    ("Repeat on a random sample", "Check the inner code on at least a quarter of the cartons in the delivery, chosen at random rather than from the top of the stack, since substituted cartons are usually mixed into genuine stock."),
  ]}),

# ---------------------------------------------------------------- 3
("finolex-genuine-product-message-meaning",
 "What the \"Genuine Product\" Reply Actually Proves (and What It Does Not)",
 "A genuine confirmation from a Finolex QR scan is strong evidence, but it answers a narrower question than most buyers assume. Here is precisely what it verifies, what it cannot verify, and how to read the result properly.",
 "Verification",
 """<p><strong>A "genuine product" reply from a Finolex QR scan confirms that the code you scanned is a real code issued by Finolex and registered in their system. It does not, on its own, confirm that the wire inside the carton is the wire Finolex packed.</strong> Understanding that distinction is what separates a real verification from a comforting one.</p>

<h2>What the reply does prove</h2>
<ul>
<li><strong>The code is authentic.</strong> It exists in Finolex's database. It was not invented, guessed or generated.</li>
<li><strong>The product identity is known.</strong> The system can state which size, grade and batch that code belongs to.</li>
<li><strong>It came from the real supply chain</strong> at the point the code was issued.</li>
</ul>
<p>That is genuinely valuable, and it is more than most brands in this category offer.</p>

<h2>What it does not prove by itself</h2>
<ul>
<li><strong>That the carton still contains its original wire.</strong> A real carton can be emptied and refilled. The outer code will still verify, because the code is real — the contents are not. This is exactly why the <a href="original-finolex-wire-inner-qr-code.html">inner QR code inside the box</a> exists, and why scanning only the outside is an incomplete check.</li>
<li><strong>That the code is unique to your box.</strong> A photographed code can be reprinted onto many cartons. Each will verify. This is why a result reporting repeated prior scans matters — see <a href="finolex-qr-code-already-used.html">already-scanned codes</a>.</li>
<li><strong>That the details match your carton.</strong> The system reports what the code says it is; you have to compare that against what is printed in front of you.</li>
</ul>

<h2>How to read the result properly</h2>
<p>Treat the verification screen as a statement to be checked, not a verdict to be accepted. Three comparisons, every time:</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Check</th><th>What you are comparing</th><th>Fail condition</th></tr></thead>
<tbody>
<tr><td>Domain</td><td>The URL that opened against Finolex's own domain</td><td>Look-alike spelling, URL shortener, generic landing page</td></tr>
<tr><td>Product identity</td><td>Size, grade and batch on screen against the carton in your hand</td><td>Any mismatch, however small</td></tr>
<tr><td>Scan history</td><td>Whether the system indicates the code has been used before</td><td>Repeated prior scans on a box you are buying new</td></tr>
</tbody></table></div>

<h2>The pattern that should worry you most</h2>
<p>Not a failed scan. A <strong>passing outer scan on a carton whose contents are wrong</strong> is the dangerous case, because it produces confidence rather than suspicion. A failed scan makes people cautious; a false pass makes them relax. That asymmetry is the whole reason the two-layer system exists.</p>
""" + TWO_LAYER + """

<h2>Verification is one signal among several</h2>
<p>A complete assessment of a Finolex coil uses the QR result alongside three independent checks that a counterfeiter has to defeat separately:</p>
<ol>
<li><strong>The printed markings along the insulation</strong> — see <a href="finolex-wire-insulation-markings.html">reading the markings on the wire itself</a>.</li>
<li><strong>The copper</strong> — strand count, strand thickness and colour at a cut end.</li>
<li><strong>The price.</strong> Genuine wire runs on 3–5% margin, so a deep discount is a specification claim, not a commercial one. See <a href="original-finolex-wire-price-check.html">why cheap Finolex is not Finolex</a>.</li>
</ol>
<p>A carton that passes both QR layers, carries correct insulation markings, shows full-specification copper and is priced within the market band is genuine to any practical standard. A carton failing any one of those deserves a question before it goes into a wall.</p>
""" + CTA,
 D,
 [("What does a genuine product message from a Finolex QR scan mean?", "It confirms that the code you scanned is a real code issued by Finolex and registered in their system, and it identifies which size, grade and batch that code belongs to. It confirms the code's authenticity, which is a narrower claim than confirming the wire inside the carton."),
  ("Does a genuine QR result guarantee the wire inside is original?", "Not on its own. A real carton can be emptied and refilled with duplicate wire, and the outer code will still verify because the code itself is genuine. That is why Finolex places a second code inside the box, and why a complete check means scanning both layers."),
  ("Can a fake product show a genuine QR result?", "Yes, in two ways. A genuine carton refilled with duplicate wire will pass the outer scan, and a code photographed from a real box can be reprinted onto many cartons, each of which will verify. The defences are the inner code and paying attention to whether the system reports repeated prior scans."),
  ("What should I compare when the verification page opens?", "Three things: that the domain belongs to Finolex rather than a look-alike or a shortener, that the size, grade and batch on screen match what is printed on your carton, and whether the system indicates the code has been scanned before. A genuine verdict describing a different product is a failure, not a pass."),
  ("Which is more dangerous, a failed scan or a false pass?", "A false pass. A failed scan makes a buyer cautious, whereas a passing outer scan on a carton with substituted contents produces confidence and the wire goes into the wall. That asymmetry is precisely why the two-layer inner and outer system exists."),
  ("What other checks should I do besides the QR code?", "Read the repeating markings printed along the insulation, examine the copper at a cut end for strand count and uniformity, and compare the price against the market band. Genuine wire runs on 3 to 5% dealer margin, so a deep discount is a claim about specification rather than a bargain.")],
 ("electrician-scanning-qr-code-wire-coil.jpg", "Reading the genuine product verification result after scanning a Finolex wire carton"),
 None),

# ---------------------------------------------------------------- 4
("finolex-qr-code-not-scanning",
 "Finolex QR Code Not Scanning: What It Means and What To Do",
 "A Finolex QR code that will not scan is not always a fake, but it is always a stop. Here are the six reasons a code fails to read, how to tell an innocent cause from a counterfeit, and what to do before you pay.",
 "Verification",
 """<p><strong>If a Finolex QR code will not scan, do not pay for that carton until you know why. Clean the surface, improve the light and try a second phone — and if it still will not read, treat the carton as unverified and ask for a replacement.</strong> Around half of non-scanning codes have an innocent explanation and half do not, and you cannot tell which from the outside.</p>

<h2>The six reasons a code will not read</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Cause</th><th>How to tell</th><th>Innocent?</th></tr></thead>
<tbody>
<tr><td>Glare or poor light</td><td>Code reads at a different angle or in shade</td><td>Yes</td></tr>
<tr><td>Dust, grease or storage marking</td><td>Reads after gentle cleaning</td><td>Yes</td></tr>
<tr><td>Physical damage in transit</td><td>Visible crease, tear or abrasion across the code</td><td>Usually</td></tr>
<tr><td>Old or slow phone camera</td><td>A second phone reads it immediately</td><td>Yes</td></tr>
<tr><td>Reprinted or copied code</td><td>Printing is soft, blurred or lower resolution than the surrounding label</td><td>No</td></tr>
<tr><td>Fabricated pattern</td><td>Looks like a QR but carries no valid data at all; no phone reads it</td><td>No</td></tr>
</tbody></table></div>

<h2>Work through it in this order</h2>
<ol>
<li><strong>Change the angle and the light.</strong> Carton printing is matte and glare defeats more scans than counterfeiting does. Step into shade; do not use the flash.</li>
<li><strong>Wipe the surface gently.</strong> Warehouse dust and marker lines across a code are common.</li>
<li><strong>Try a second phone.</strong> Older cameras struggle with dense codes. This single step resolves a large share of failures.</li>
<li><strong>Look at the print quality with your eye.</strong> Compare the QR's sharpness against the small text printed beside it. A code noticeably softer or blurrier than the surrounding label has been reprinted — which is the counterfeit signature.</li>
<li><strong>Check whether it is a sticker.</strong> A QR on a pasted label over the printed carton is a red flag independent of whether it scans.</li>
<li><strong>Check the other cartons.</strong> If one code in forty fails, that is probably damage. If several fail across the same delivery, that is a pattern.</li>
</ol>

<h2>The distinction that matters</h2>
<p>A damaged genuine code and a fabricated fake code both fail to scan, but they look different under inspection. Damage is <em>localised</em> — a crease, a scuff, a tear across part of the pattern, with the rest of the label sharp. A counterfeit code is <em>uniformly soft</em>, because the whole label was reprinted from a photograph and lost definition in the process. Hold the carton at arm's length and compare the QR against the small print next to it; the difference is usually visible without magnification.</p>

<h2>What to do when it still will not scan</h2>
<ul>
<li><strong>Do not pay for that carton.</strong> An unverified box is an unverified box, whatever the explanation.</li>
<li><strong>Ask for a replacement carton</strong> from the same delivery and scan that one. A genuine seller will swap it without argument.</li>
<li><strong>Open it and try the <a href="original-finolex-wire-inner-qr-code.html">inner code</a>.</strong> An outer code damaged in transit will often sit alongside a perfectly readable inner one, which resolves the question immediately.</li>
<li><strong>Check the physical evidence.</strong> The <a href="finolex-wire-insulation-markings.html">printed markings along the insulation</a> and the copper at a cut end are independent of any code, and a counterfeiter has to get those right separately.</li>
<li><strong>Escalate if the seller resists.</strong> Reluctance to replace an unscannable carton is more informative than the failed scan itself.</li>
</ul>

<h2>Why this should never happen after installation</h2>
<p>Every one of these steps requires the carton to still be in your hands and the money to still be in your pocket. That is the argument for buying on <strong>pay on delivery</strong> terms and verifying at your own site: a failed scan becomes a five-minute inconvenience instead of a wall that has to be broken open.</p>
""" + CTA,
 D,
 [("What does it mean if a Finolex QR code will not scan?", "It means the carton is unverified, which is a reason to stop rather than a proof of counterfeiting. Roughly half of non-scanning codes have innocent causes such as glare, dust, transit damage or an old phone camera, and half indicate a reprinted or fabricated code. Work through the causes before paying."),
  ("How do I tell a damaged QR code from a fake one?", "Damage is localised — a crease, scuff or tear across part of the pattern with the rest of the label still sharp. A counterfeit code is uniformly soft or blurry, because the whole label was reprinted from a photograph and lost definition. Compare the QR's sharpness against the small text printed beside it."),
  ("What should I try before assuming a Finolex code is fake?", "Change the angle and move into shade since glare defeats more scans than counterfeiting does, wipe dust or marker lines off the surface, and try a second phone because older cameras struggle with dense codes. Then inspect print quality and check whether the code is on a pasted sticker."),
  ("Should I pay for a carton whose QR code does not scan?", "No. An unverified carton is unverified whatever the explanation. Ask for a replacement carton from the same delivery and scan that one instead — a genuine seller will swap it without argument, and reluctance to do so is more informative than the failed scan itself."),
  ("Can I check the wire another way if the code will not scan?", "Yes. Open the carton and try the inner QR code, which is often perfectly readable when an outer code has been damaged in transit. Beyond that, the repeating markings printed along the insulation and the copper at a cut end are independent checks a counterfeiter has to defeat separately."),
  ("What if several codes fail across the same delivery?", "That is a pattern rather than an accident. Transit damage affects isolated cartons; multiple failures in one consignment suggest reprinted labels. Set the delivery aside, do not pay, and ask the supplier to replace the whole lot from verified stock.")],
 ("electrician-scanning-qr-code-wire-coil.jpg", "Troubleshooting a Finolex wire carton QR code that will not scan at the delivery site"),
 None),

# ---------------------------------------------------------------- 5
("finolex-qr-code-already-used",
 "\"This Code Has Already Been Scanned\": What It Means on a Finolex Box",
 "A Finolex QR code reporting prior scans on a box you are buying new is one of the strongest counterfeit signals there is. Here is what causes it, the one innocent explanation, and exactly what to do.",
 "Verification",
 """<p><strong>If a Finolex code reports that it has already been scanned many times on a carton you are buying new, treat the carton as counterfeit and do not pay for it.</strong> The most likely explanation is that a code was photographed from a genuine box and reprinted onto many cartons — and every one of those will verify as genuine, which is precisely the trap.</p>

<h2>How code cloning works</h2>
<p>It is simple, cheap and effective. Someone buys one genuine Finolex coil, photographs the QR code on the carton, and reprints that same code onto hundreds of counterfeit cartons. Every one of them scans. Every one of them returns a genuine verdict, because the code <em>is</em> genuine — it is just not unique any more.</p>
<p>The only thing that distinguishes the fiftieth cloned carton from the original is the scan count. That is why verification systems track it and why the count is worth reading rather than skipping past.</p>

<h2>The one innocent explanation</h2>
<p>A small number of prior scans on a carton that has passed through a distributor and a counter is normal. Stock gets checked. Staff test codes. A customer scanned it last week and did not buy. Two or three prior scans on a box that has been sitting in a shop is not evidence of anything.</p>
<p>The signal is in the pattern, not the existence of prior scans:</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Scan history</th><th>Reading</th></tr></thead>
<tbody>
<tr><td>First scan, or 1–3 prior scans</td><td>Normal for stock that has moved through the channel</td></tr>
<tr><td>Many prior scans over a long period</td><td>Suspicious — a code in circulation longer than a coil should be</td></tr>
<tr><td>Many scans from widely separated locations</td><td>Cloning. One code cannot be in five districts at once</td></tr>
<tr><td>Scans dated before the carton could plausibly exist</td><td>Cloning, and the original coil was sold long ago</td></tr>
</tbody></table></div>

<h2>What to do, in order</h2>
<ol>
<li><strong>Do not pay for that carton.</strong> Separate it physically from the rest of the delivery so it does not get mixed back in.</li>
<li><strong>Scan the <a href="original-finolex-wire-inner-qr-code.html">inner code</a>.</strong> A cloned outer code on a counterfeit carton will almost always sit alongside a missing or failing inner code, which converts suspicion into certainty.</li>
<li><strong>Photograph everything</strong> — the carton, the label, the code, the verification screen showing the scan history, and the invoice. This is what makes a complaint actionable.</li>
<li><strong>Check every other carton in the delivery.</strong> Cloned codes are printed in quantity, so a second and third will usually show the same pattern.</li>
<li><strong>Raise it with the seller immediately,</strong> before installation and before payment. Then follow the escalation route in <a href="received-duplicate-finolex-wire-complaint.html">what to do if you received duplicate Finolex wire</a>.</li>
</ol>

<h2>Why this matters more than it sounds</h2>
<p>A cloned code is not a paperwork problem. It means the carton in front of you was produced by someone whose business is making counterfeit Finolex packaging convincing enough to survive a scan. The wire inside it was chosen by that same person, and the property they were economising on is copper — the one thing that determines whether the cable can carry its marked current without overheating inside your wall.</p>
<p>The scan count is the cheapest early warning you will ever get. Read it.</p>

<h2>Buy so that this is recoverable</h2>
<p>Every action above assumes the wire has not been installed and you have not yet paid. Buying on pay-on-delivery terms from an authorised distributor, and scanning at your own site, is what keeps a cloned code a five-minute problem rather than a wall that has to be broken open two years later.</p>
""" + CTA,
 D,
 [("What does it mean if a Finolex QR code says it has already been scanned?", "On a carton you are buying new, many prior scans usually means the code was photographed from a genuine box and reprinted onto counterfeit cartons. Every cloned carton verifies as genuine because the code itself is real — it is simply no longer unique. Treat it as counterfeit and do not pay."),
  ("Is one or two prior scans on a Finolex code a problem?", "No. A small number of prior scans is normal for stock that has moved through a distributor and a counter, where staff check codes and customers scan boxes they do not buy. The warning signs are many scans over a long period, scans from widely separated locations, or scans dated before the carton could exist."),
  ("How does Finolex QR code cloning work?", "Someone buys one genuine coil, photographs the QR code on its carton, and reprints that code onto hundreds of counterfeit cartons. All of them scan and all of them return a genuine verdict, because the code is authentic. The only thing distinguishing the fiftieth cloned carton is the scan count."),
  ("What should I do if a code shows many previous scans?", "Do not pay, separate that carton from the delivery, and scan the inner code inside the box — a cloned outer code almost always sits alongside a missing or failing inner one. Photograph the carton, label, code, verification screen and invoice, then check every other carton in the consignment."),
  ("Can a cloned code be detected before buying?", "Yes, and the scan history is how. It is the one property a counterfeiter cannot control, because reprinting a code does not reset the count in Finolex's system. Reading the scan history takes seconds and is the cheapest early warning available to a buyer."),
  ("Why is a cloned code more serious than a printing error?", "Because it means the carton was produced by an operation capable of making counterfeit Finolex packaging survive a scan. The wire inside was chosen by that same operation, and the property they economise on is copper — which is what determines whether the cable can carry its marked current without overheating in a wall.")],
 ("shop-owner-explaining-wire-quality.jpg", "Checking the scan history on a Finolex wire carton verification result before paying"),
 None),

# ---------------------------------------------------------------- 6
("original-vs-duplicate-finolex-wire-comparison",
 "Original vs Duplicate Finolex Wire: A Side-by-Side Comparison",
 "Eleven points of difference between genuine and counterfeit Finolex wire — carton, QR codes, insulation printing, copper, weight, feel, coil length and price — set out so you can check a coil in front of you.",
 "Comparison",
 """<p><strong>Original Finolex wire differs from duplicate on eleven checkable points, of which four cannot be faked cheaply: the inner QR code, the copper cross-section, the insulation marking quality, and the price.</strong> The rest can be imitated well enough to fool a buyer looking casually, which is why the four that matter deserve the attention.</p>

<h2>The comparison, point by point</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Check</th><th>Original</th><th>Duplicate</th></tr></thead>
<tbody>
<tr><td>Carton print</td><td>Sharp, correctly registered, consistent colour</td><td>Soft edges, slight colour drift, small text loses definition</td></tr>
<tr><td>Label integration</td><td>Details printed as part of the carton</td><td>Pasted sticker over or beside the printing</td></tr>
<tr><td>Outer QR</td><td>Scans to Finolex's own domain, details match the box</td><td>May scan, may be cloned, may open a look-alike site</td></tr>
<tr><td><strong>Inner QR</strong></td><td>Present inside the box, confirms genuine</td><td>Missing, unreadable, or fails verification</td></tr>
<tr><td>Factory seal</td><td>Intact and original</td><td>Re-taped, resealed, or opened and closed</td></tr>
<tr><td>Insulation printing</td><td>Even spacing, crisp characters, consistent along the length</td><td>Faint, smudged, irregular spacing, sometimes missing stretches</td></tr>
<tr><td><strong>Copper cross-section</strong></td><td>Full marked sq mm, uniform strand count and thickness</td><td>Under-specification: fewer or thinner strands</td></tr>
<tr><td>Copper colour</td><td>Bright, uniform electrolytic copper</td><td>Dull, reddish or varying along the length</td></tr>
<tr><td>Coil weight</td><td>Consistent with size and length</td><td>Noticeably light for its marking</td></tr>
<tr><td>Coil length</td><td>Full 90m, 180m or 300m</td><td>Short — the shortfall is invisible once installed</td></tr>
<tr><td><strong>Price</strong></td><td>Within a few percent of the market band</td><td>15% or more below, which is not a discount</td></tr>
</tbody></table></div>

<h2>The four that actually decide it</h2>
<h3>1. The inner QR code</h3>
<p>A counterfeiter can obtain real cartons and clone outer codes. What they cannot do is produce a valid inner code bound to contents they packed themselves. This is the single strongest check available to a buyer, and it is covered in full in <a href="original-finolex-wire-inner-qr-code.html">the inner QR code guide</a>.</p>

<h3>2. The copper</h3>
<p>Cut fifty millimetres off a coil and look at the conductor end. Count the strands, look at their thickness, and look at the colour. Copper is the expensive part of a wire, so it is the part a counterfeit economises on — a coil marked 1.5 sq mm carrying 1.2 sq mm of copper looks identical, weighs slightly less, and cannot carry its rated current. Under load it runs hot, its insulation ages a decade in two years, and the failure mode is a fire inside a wall.</p>

<h3>3. The insulation markings</h3>
<p>Genuine house wire carries repeating printed markings along its length. Counterfeits reproduce these, but rarely with the same consistency — spacing drifts, characters smudge, and stretches go missing. Unroll a metre and look. The detail is in <a href="finolex-wire-insulation-markings.html">reading the markings on the wire</a>.</p>

<h3>4. The price</h3>
<p>Genuine branded wire runs on 3–5% dealer margin. There is no mechanism by which an honest seller can go 15% below the market band. A price that looks like a steal is a statement about specification, and it is explained in <a href="original-finolex-wire-price-check.html">why cheap Finolex is not Finolex</a>.</p>

<h2>What a duplicate actually costs you</h2>
<p>This is not a quality debate about longevity. Under-specification copper cannot carry the current the marking claims, so a circuit that should run cool runs warm every summer. Insulation ages under heat. The cable is inside a wall, so nothing is inspected, nothing is noticed, and the fault presents years later as a burning smell or a tripped main at two in the morning. The saving on a whole house is a few thousand rupees against a risk nobody would accept if it were visible.</p>

<h2>Check in this order</h2>
<ol>
<li>Carton seal intact, printing sharp, no pasted stickers.</li>
<li>Outer QR scans to Finolex's own domain, details match, scan history reasonable.</li>
<li>Open the box, scan the inner QR, confirm genuine.</li>
<li>Unroll a metre and read the insulation markings.</li>
<li>Cut a short piece and look at the copper.</li>
<li>Compare the price against a reference quote.</li>
</ol>
<p>The full version is the <a href="original-finolex-wire-checklist-before-paying.html">12-point checklist</a>.</p>
""" + CTA,
 D,
 [("What is the difference between original and duplicate Finolex wire?", "They differ on eleven checkable points, but four decide it: the inner QR code inside the box, the copper cross-section at a cut end, the consistency of the printed markings along the insulation, and the price. The carton, outer code and general appearance can all be imitated well enough to fool a casual look."),
  ("How can I check Finolex wire copper is full specification?", "Cut about fifty millimetres off the coil and examine the conductor end. Count the strands and look at their thickness and colour. Genuine electrolytic copper is bright and uniform; a duplicate typically carries fewer or thinner strands than the marked cross-section, which is invisible once the wire is inside conduit."),
  ("Is duplicate wire only a quality problem or is it dangerous?", "Genuinely dangerous. Under-specification copper cannot carry the current its marking claims, so the circuit runs warm under normal household load and the insulation ages rapidly. Because the cable is concealed, nothing is inspected and the fault presents years later as a burning smell or a tripping main."),
  ("Can a duplicate Finolex carton pass the QR check?", "The outer check, often yes — counterfeiters obtain real cartons or clone codes photographed from genuine boxes. The inner code inside the box is what they cannot pass, because it is bound to contents they did not pack. That is why a complete verification uses both layers."),
  ("How much cheaper is duplicate Finolex wire?", "Typically 15% or more below the market band, which is the giveaway. Genuine branded wire runs on 3 to 5% dealer margin, so no honest seller has the room to discount that deeply. A price that looks like a steal is a statement about what is inside the carton."),
  ("What order should I check a Finolex coil in?", "Carton seal and print quality first, then the outer QR including its scan history, then open the box and scan the inner QR, then unroll a metre and read the insulation markings, then cut a short piece and inspect the copper, and finally compare the price against a reference quote.")],
 ("shop-owner-explaining-wire-quality.jpg", "Comparing original and duplicate house wire side by side at an electrical counter"),
 None),

# ---------------------------------------------------------------- 7
("finolex-wire-insulation-markings",
 "Reading the Markings Printed on Finolex Wire (What They Mean)",
 "Genuine house wire carries repeating printed markings along its insulation. Here is what each element means, what the printing quality tells you, and why this check works even when a carton has been thrown away.",
 "Verification",
 """<p><strong>Genuine Finolex wire carries repeating printed markings along the insulation identifying the brand, the conductor size, the voltage rating and the applicable IS standard. Duplicates reproduce these markings but rarely with the same spacing consistency and character definition.</strong> This check works on wire already unrolled, already cut, and even after the carton is gone — which makes it the one verification available when everything else has been discarded.</p>

<h2>What the markings say</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Element</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>Brand name</td><td>The manufacturer, printed at regular intervals along the length</td></tr>
<tr><td>Conductor size</td><td>The nominal cross-section in sq mm — 1.0, 1.5, 2.5, 4.0, 6.0</td></tr>
<tr><td>Voltage rating</td><td>Typically 1100V for domestic house wire</td></tr>
<tr><td>Standard reference</td><td>The Indian Standard the cable is manufactured to</td></tr>
<tr><td>Grade indication</td><td>FR, FR-LSH or the premium range designation</td></tr>
<tr><td>Sequential metre marking</td><td>Running length marking, where the range carries it — useful for checking coil length</td></tr>
</tbody></table></div>

<h2>What the printing quality tells you</h2>
<p>The content of the markings is easy to copy. The <em>quality</em> and <em>consistency</em> are not, because they come from production-line printing equipment running continuously at speed. Look for:</p>
<ul>
<li><strong>Even spacing.</strong> The interval between repeats should be regular along the whole length. Drifting or irregular intervals indicate a slower, cruder printing process.</li>
<li><strong>Crisp character edges.</strong> Letters should be sharply defined, not fuzzy or bleeding into the insulation.</li>
<li><strong>Consistent depth of colour.</strong> Printing that fades in and out along the run is a strong signal.</li>
<li><strong>No missing stretches.</strong> Long unmarked gaps are common on counterfeits and rare on genuine production.</li>
<li><strong>Legibility after handling.</strong> Genuine marking survives being pulled through conduit. Printing that rubs off between your fingers is a finding.</li>
</ul>
<p>Unroll a full metre, not fifty centimetres. Counterfeits often get the first few repeats right and deteriorate after that.</p>

<h2>Using the sequential metre marking</h2>
<p>Where the wire carries running length numbers, they answer a question the carton cannot: is the coil actually the length it claims? Short coils are one of the most profitable and least detectable tricks in this trade, because a homeowner never measures 90 metres and the shortfall disappears into the job. Note the number at the outer end of a fresh coil and again at the inner end — the difference should be close to the marked length.</p>
<p>This is a strong argument for buying sealed cartons in the first place, which is covered in <a href="why-buy-finolex-90m-coils.html">why 90-metre boxes are the safe default</a>. Loose or cut wire carries no carton, no QR code and no accountability for length.</p>

<h2>Why this check matters most after the fact</h2>
<p>Every other verification depends on having the packaging. The QR codes need a carton; the seal check needs a seal; the price check needs an invoice. Insulation markings are printed on the product itself, so they remain available when:</p>
<ul>
<li>Your contractor supplied the wire and discarded the boxes.</li>
<li>You are inspecting an existing house before buying it.</li>
<li>Wire is already pulled into conduit and only the tails are visible.</li>
<li>You are checking a partially used coil left on site.</li>
</ul>
<p>In those situations this is the check you have. Combine it with a look at the copper at a cut end, and you can form a reasonable judgement without any packaging at all.</p>

<h2>What to do if the markings look wrong</h2>
<ol>
<li><strong>Photograph a length of the wire</strong> showing several repeats of the marking, in good light.</li>
<li><strong>Cut a short sample</strong> and examine the copper — strand count, thickness and colour.</li>
<li><strong>Stop the installation</strong> before more of it goes into walls.</li>
<li><strong>Retrieve the cartons if they still exist,</strong> and check the QR codes.</li>
<li><strong>Raise it with whoever supplied it,</strong> following <a href="received-duplicate-finolex-wire-complaint.html">the complaint route</a>.</li>
</ol>
""" + CTA,
 D,
 [("What markings are printed on genuine Finolex wire?", "Repeating printed markings along the insulation identifying the brand, the conductor size in sq mm, the voltage rating which is typically 1100V for house wire, the applicable Indian Standard, and the grade such as FR or FR-LSH. Some ranges also carry sequential running-length numbers."),
  ("How do markings help identify duplicate wire?", "Counterfeits copy the content but rarely match the quality. Genuine production printing has even spacing, crisp character edges, consistent colour depth and no missing stretches, because it comes from line equipment running continuously. Unroll a full metre — duplicates often get the first few repeats right and deteriorate after that."),
  ("Can I check wire authenticity without the box?", "Yes, and the insulation markings are how. Every other check needs packaging — the QR codes need a carton, the seal check needs a seal — but the markings are printed on the product itself. Combined with an inspection of the copper at a cut end, they allow a reasonable judgement with no packaging at all."),
  ("What is the sequential metre marking used for?", "It shows the running length along the wire, which lets you check whether a coil is genuinely the length it claims. Note the number at the outer end of a fresh coil and again at the inner end; the difference should be close to the marked length. Short coils are a common and otherwise undetectable trick."),
  ("Should printed markings rub off the wire?", "No. Genuine marking survives being pulled through conduit and normal handling. Printing that rubs off between your fingers, fades along the run, or disappears for long stretches is a strong indication of a crude printing process rather than factory production."),
  ("What should I do if wire is already installed and the markings look wrong?", "Photograph a length showing several repeats of the marking in good light, cut a short sample and inspect the copper, and stop further installation before more of it goes into walls. Retrieve the cartons if they still exist to check the QR codes, then raise it with whoever supplied the material.")],
 ("electrician-hands-stripping-wire-closeup.jpg", "Examining the printed markings along the insulation of a house wire to verify it is genuine"),
 None),

# ---------------------------------------------------------------- 8
("original-finolex-wire-price-check",
 "Why Cheap Finolex Wire Is Not Finolex: The Price Test",
 "Genuine wire runs on a 3-5% dealer margin, which puts a hard floor under what any honest seller can quote. Here is how to use price as an authenticity test, and what a 15% discount actually means.",
 "Pricing",
 """<p><strong>Genuine branded house wire runs on roughly 3–5% dealer margin, so no authorised seller can discount 15% or more below the market band. A Finolex quote far below the going rate is not a better deal — it is a different product.</strong> Price is the fastest authenticity test available, and it works before you have even seen the carton.</p>

<h2>The arithmetic that makes this reliable</h2>
<p>Wire pricing is MRP-linked and the channel margin is thin, because copper dominates the cost and copper is a traded commodity with a visible market price. That leaves very little room between what a distributor pays and what he can sell for. Concretely:</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Discount off the market band</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>0–5%</td><td>Normal competitive pricing</td></tr>
<tr><td>5–8%</td><td>Aggressive, plausible on a large order or a stock clearance</td></tr>
<tr><td>8–15%</td><td>Beyond the margin available. Ask what is different</td></tr>
<tr><td>15%+</td><td>Not a discount. Copper shortfall, short coil, or counterfeit</td></tr>
</tbody></table></div>
<p>Reference bands for Finolex FR 90m coils in Bangalore in 2026 run approximately ₹1,950–₹2,250 for 1.5 sq mm, ₹3,150–₹3,650 for 2.5 sq mm and ₹4,700–₹5,400 for 4.0 sq mm. These move with copper — the full explanation is in <a href="copper-price-and-wire-rates-explained.html">why wire prices keep changing</a>, and current brand-wise bands are on our <a href="../price-lists/finolex-price-list.html">Finolex price list</a>.</p>

<h2>Where the "saving" actually comes from</h2>
<p>A counterfeit is not cheaper because someone is being generous. The money comes out of one of three places, all invisible at the counter:</p>
<ol>
<li><strong>Copper cross-section.</strong> A coil marked 1.5 sq mm carrying 1.2 sq mm of copper saves roughly a fifth of the expensive component. It looks identical. It cannot carry its rated current.</li>
<li><strong>Coil length.</strong> An 82-metre coil sold as 90 metres is an 9% saving that no homeowner will ever measure.</li>
<li><strong>Insulation quality.</strong> Cheaper compound, thinner wall, no genuine FR performance — which matters precisely once, during a fire.</li>
</ol>
<p>All three disappear inside a wall on the day of installation and none of them is discoverable afterwards without breaking plaster.</p>

<h2>Why a large showroom does not change the arithmetic</h2>
<p>Margins are thin regardless of premises. In fact an expensively fitted showroom has <em>more</em> pressure to find margin somewhere, which is part of why impressive shops are not automatically safer. The relevant question is not how the shop looks but whether it holds the brand's authorisation and will let you verify the stock — covered in <a href="authorised-finolex-dealer-check.html">asking for the dealer certificate</a>.</p>

<h2>How to use price as a test</h2>
<ol>
<li><strong>Get a reference quote first.</strong> Send your full list to <a href="{W}">{PH}</a> and you will have an itemised quote within 60 minutes. Use it as your reference band whether or not you buy from us.</li>
<li><strong>Compare like with like.</strong> FR against FR, not FR against FRLS. Per metre, not per coil, since 90m and 180m packs are not comparable line for line.</li>
<li><strong>Check the size mix.</strong> A cheaper total often means less 4.0 sq mm, which is a specification change rather than a saving.</li>
<li><strong>Treat outliers as questions, not opportunities.</strong> Ask the seller directly what is different about their stock, and watch how the question is received.</li>
<li><strong>Verify anyway.</strong> A correct price is not proof of genuineness; it just removes the loudest warning sign. Still scan both <a href="original-finolex-wire-outer-qr-code.html">outer</a> and <a href="original-finolex-wire-inner-qr-code.html">inner</a> codes.</li>
</ol>

<h2>Use our quote to check someone else</h2>
<p>We mean this literally and we say it on every price page: send us your list, take the quote, and use it as a reference price anywhere in Bangalore. There is no obligation to buy from us. A reference price is the cheapest protection a home builder has, and it costs us nothing to give.</p>
""".replace("{W}", W).replace("{PH}", PH) + CTA,
 D,
 [("Why is cheap Finolex wire usually fake?", "Because genuine branded wire runs on roughly 3 to 5% dealer margin, which puts a hard floor under what any authorised seller can quote. A discount of 15% or more is beyond the margin that exists in the channel, so the saving has to come from copper cross-section, coil length or insulation quality instead."),
  ("How much discount is realistic on Finolex wire?", "Zero to 5% is normal competitive pricing and 5 to 8% is aggressive but plausible on a large order. Between 8 and 15% you should ask what is different about the stock. Above 15% it is not a discount at all — it indicates copper shortfall, a short coil or a counterfeit."),
  ("What is the price of genuine Finolex wire in Bangalore?", "Approximately ₹1,950 to ₹2,250 for a 1.5 sq mm FR 90m coil, ₹3,150 to ₹3,650 for 2.5 sq mm and ₹4,700 to ₹5,400 for 4.0 sq mm in 2026. These bands move with copper prices, so ask for a current quote rather than relying on any published figure."),
  ("Where does the saving on duplicate wire actually come from?", "Three places, all invisible at the counter: reduced copper cross-section, where a coil marked 1.5 sq mm carries around 1.2 sq mm; short coil length, such as 82 metres sold as 90; and cheaper insulation with no genuine flame-retardant performance. All three disappear into a wall on installation day."),
  ("Is a large showroom safer to buy Finolex from?", "Not automatically. Margins are equally thin regardless of premises, and an expensively fitted showroom has more pressure to find margin somewhere. The relevant test is whether the shop holds the brand's authorisation and will let you scan and verify stock before you pay."),
  ("How do I compare two Finolex quotes fairly?", "Compare the same grade, FR against FR rather than FR against FRLS, compare per metre rather than per coil since 90m and 180m packs differ, and check that the size mix is identical. A cheaper total frequently means less 4.0 sq mm, which is a specification change rather than a saving.")],
 ("contractor-checking-price-list-phone.jpg", "Comparing a Finolex wire price quotation against the market reference band before buying"),
 None),

# ---------------------------------------------------------------- 9
("original-finolex-wire-checklist-before-paying",
 "The 12-Point Checklist Before You Pay for Finolex Wire",
 "A complete site verification sequence for a Finolex delivery — seal, carton, outer QR, inner QR, markings, copper, length, price and paperwork — in the order that catches problems earliest.",
 "Checklist",
 """<p><strong>Run these twelve checks at your own site, before payment and before installation. Together they take about fifteen minutes on a house delivery and they close every route by which duplicate wire reaches a wall.</strong> The order matters — each step is arranged to catch problems before you have invested more effort.</p>

<h2>Before the delivery arrives</h2>
<h3>1. Buy in your own name</h3>
<p>Order the wire and switchgear yourself with your own invoice rather than on a with-material contract. This single decision removes the substitution incentive entirely — the reasoning is in <a href="electrician-retailer-nexus-duplicate-wires.html">how duplicate wire reaches your home</a>.</p>

<h3>2. Confirm the seller is authorised</h3>
<p>Ask for the Finolex dealer certificate and check the name on it matches the billing entity. See <a href="authorised-finolex-dealer-check.html">asking for the certificate</a>.</p>

<h3>3. Get a reference price</h3>
<p>Have an independent quote in hand so you know the honest band before anyone quotes you. Ours takes 60 minutes on WhatsApp and carries no obligation.</p>

<h3>4. Insist on pay on delivery</h3>
<p>Every check below requires the material to be in front of you and the money still in your pocket.</p>

<h2>When the delivery arrives</h2>
<h3>5. Check the factory seals</h3>
<p>Every carton sealed and original. Re-taped or resealed boxes are set aside immediately, before anything else is checked.</p>

<h3>6. Inspect the carton printing</h3>
<p>Sharp, correctly registered print. Size in sq mm, grade, coil length, batch number and voltage rating all present and printed as part of the label — not on a pasted sticker.</p>

<h3>7. Scan the outer QR on every carton</h3>
<p>Confirm the link belongs to Finolex's own domain, the reported product matches the box, and the scan history is reasonable. Full detail in <a href="original-finolex-wire-outer-qr-code.html">the outer QR guide</a>; if a code will not read, see <a href="finolex-qr-code-not-scanning.html">non-scanning codes</a>; if it reports prior scans, see <a href="finolex-qr-code-already-used.html">already-scanned codes</a>.</p>

<h3>8. Open and scan the inner QR on a random sample</h3>
<p>At least a quarter of the cartons, picked at random rather than off the top of the stack. This is the check that catches refilled cartons and the one most buyers skip — <a href="original-finolex-wire-inner-qr-code.html">the inner QR guide</a> explains why it matters most.</p>

<h2>On the wire itself</h2>
<h3>9. Read the insulation markings</h3>
<p>Unroll a full metre. Even spacing, crisp characters, consistent colour, no missing stretches, brand and size correct. See <a href="finolex-wire-insulation-markings.html">reading the markings</a>.</p>

<h3>10. Inspect the copper</h3>
<p>Cut about fifty millimetres and look at the conductor end. Strand count, strand thickness, uniform bright colour. This is where a duplicate's saving actually lives.</p>

<h3>11. Sanity-check length and weight</h3>
<p>Where the wire carries sequential metre marking, compare the outer and inner ends. A coil noticeably light for its size and marking is worth questioning.</p>

<h2>Before you pay</h2>
<h3>12. Check the invoice line by line</h3>
<p>Your own name, GST details, and every item listed by brand, size, grade and quantity — 4.0 sq mm should appear if your house has air conditioners and a geyser. A vague invoice makes a warranty claim very difficult and makes it impossible to prove later what you were supplied.</p>

<h2>The whole thing on one page</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>#</th><th>Check</th><th>Fail action</th></tr></thead>
<tbody>
<tr><td>1</td><td>Bought in your own name</td><td>Change the contract terms before ordering</td></tr>
<tr><td>2</td><td>Seller authorised for the brand</td><td>Buy elsewhere</td></tr>
<tr><td>3</td><td>Reference price in hand</td><td>Get one before committing</td></tr>
<tr><td>4</td><td>Pay on delivery agreed</td><td>Do not pay in advance</td></tr>
<tr><td>5</td><td>Factory seals intact</td><td>Set carton aside, do not pay for it</td></tr>
<tr><td>6</td><td>Carton printing sharp, no stickers</td><td>Reject the carton</td></tr>
<tr><td>7</td><td>Outer QR verifies and matches</td><td>Replacement carton, rescan</td></tr>
<tr><td>8</td><td>Inner QR verifies on sample</td><td>Reject the delivery, keep evidence</td></tr>
<tr><td>9</td><td>Insulation markings consistent</td><td>Stop installation, photograph, escalate</td></tr>
<tr><td>10</td><td>Copper full specification</td><td>Reject, keep sample as evidence</td></tr>
<tr><td>11</td><td>Length and weight plausible</td><td>Question before accepting</td></tr>
<tr><td>12</td><td>Invoice complete and in your name</td><td>Do not pay until corrected</td></tr>
</tbody></table></div>
<p>If something fails, <a href="received-duplicate-finolex-wire-complaint.html">the complaint guide</a> covers what to do next.</p>
""" + CTA,
 D,
 [("What should I check before paying for Finolex wire?", "Twelve things, in order: that you bought in your own name, that the seller is authorised, that you have a reference price, that terms are pay on delivery, then factory seals, carton printing, the outer QR on every carton, the inner QR on a random sample, insulation markings, copper cross-section, coil length and weight, and finally the invoice."),
  ("How long does verifying a wire delivery take?", "About fifteen minutes for a full house delivery. Scanning outer codes on every carton takes most of it, opening and checking inner codes on a random quarter adds a few minutes, and the physical checks on markings and copper take two or three minutes on one sample coil."),
  ("How many boxes should I open to check the inner code?", "At least a quarter of the delivery, chosen at random rather than from the top of the stack. Substituted cartons are usually mixed into genuine stock rather than delivered as a complete consignment, so sampling from the top defeats the purpose."),
  ("What should a Finolex invoice contain?", "Your own name and GST details, and a line for every item stating brand, size in sq mm, grade and quantity. Check that 4.0 sq mm appears if your house has air conditioners and a geyser. A vague invoice makes warranty claims very difficult and makes it impossible to prove later what you were actually supplied."),
  ("Why does buying in my own name matter?", "Because on a with-material contract the contractor buys and any saving from substitution stays with him, and the wire disappears inside a wall before anyone inspects it. Buying the wire and switchgear yourself removes the incentive entirely, without anyone needing to have an awkward conversation."),
  ("What do I do if one carton fails a check?", "Set that carton aside physically so it does not get mixed back into the delivery, do not pay for it, and check every other carton in the same consignment — substituted stock rarely arrives alone. Keep the carton, any inner insert and the invoice as evidence before raising it with the seller.")],
 ("happy-customer-receiving-electrical-order.jpg", "Running the verification checklist on a Finolex wire delivery at site before paying"),
 {"name": "How to verify a Finolex wire delivery before paying",
  "steps": [
    ("Check the factory seals", "Confirm every carton is sealed and the seal is original. Set aside any box that has been re-taped or resealed before checking anything else."),
    ("Inspect the carton printing", "Confirm the print is sharp and correctly registered, and that size, grade, coil length, batch number and voltage rating are printed as part of the label rather than on a pasted sticker."),
    ("Scan the outer QR on every carton", "Confirm the link belongs to Finolex's own domain, the product reported matches the box, and the scan history is reasonable for stock being sold new."),
    ("Open and scan the inner QR on a sample", "Open at least a quarter of the cartons, chosen at random rather than from the top of the stack, and confirm the inner code verifies as genuine."),
    ("Read the insulation markings", "Unroll a full metre and check that the printed markings are evenly spaced, crisply defined, consistent in colour and correct for brand and size."),
    ("Inspect the copper", "Cut about fifty millimetres from a coil and examine the conductor end for strand count, strand thickness and uniform bright colour."),
    ("Check the invoice before paying", "Confirm the invoice is in your own name with GST details and lists every item by brand, size, grade and quantity, then pay only once every check has passed."),
  ]}),

# ---------------------------------------------------------------- 10
("received-duplicate-finolex-wire-complaint",
 "You Received Duplicate Finolex Wire: What To Do Now",
 "Practical steps if wire fails verification — what to preserve as evidence, how to raise it with the seller, how to escalate to Finolex, and what to do if some of it is already inside the wall.",
 "Guide",
 """<p><strong>Stop the installation immediately, do not pay for the suspect material, preserve the cartons, inner inserts, a cut sample and the invoice, photograph everything including the verification screen, and raise it with the seller in writing before anything else.</strong> What you can recover depends almost entirely on how much of it is still outside the wall.</p>

<h2>Step 1 — Stop, before anything else</h2>
<p>Every hour of continued installation reduces your options and increases the eventual cost. Concealed wire cannot be inspected, cannot be returned, and can only be replaced by breaking finished walls. If a coil has failed verification, no part of the delivery should go into a chase until the question is settled.</p>

<h2>Step 2 — Preserve the evidence</h2>
<p>This determines whether you have a claim or an argument. Keep:</p>
<ul>
<li>The <strong>cartons</strong>, including any that are already empty.</li>
<li>The <strong>inner inserts or codes</strong> from inside the boxes.</li>
<li>A <strong>cut sample</strong> of the wire itself, at least a foot, showing the insulation markings and the conductor end.</li>
<li>The <strong>invoice</strong> and any delivery challan.</li>
<li><strong>Photographs</strong> of the carton, the label, both QR codes, the verification screens including any scan history, the insulation markings and the cut copper end.</li>
<li>Any <strong>WhatsApp messages</strong> with the seller, especially the original quote.</li>
</ul>
<p>Photograph before you move anything. A carton that has been carried around a site for a week photographs badly and argues badly.</p>

<h2>Step 3 — Raise it with the seller, in writing</h2>
<p>Message rather than telephone, so there is a record. State plainly: which cartons, which check failed, what the verification screen said, and what you want — replacement with verified stock, or a refund. Attach the photographs.</p>
<p>Watch the response, because it is informative. A genuine seller who has been supplied bad stock himself will want the cartons back and will replace them, because his own supplier owes him the same remedy. Deflection, delay or an offer of a discount to keep the material are all answers to a different question than the one you asked.</p>

<h2>Step 4 — Escalate to Finolex</h2>
<p>Counterfeiting harms the brand more than it harms any single buyer, and manufacturers do act on specific, evidenced reports. Contact Finolex customer care on <strong>1800-209-0166</strong> with the batch number, the QR verification result, the seller's name and location, and your photographs. Ask them to confirm whether the code and batch are legitimate and where that batch was despatched.</p>
<p>Two things make a report actionable: the <strong>batch number</strong> and the <strong>seller's identity</strong>. Without those, a complaint cannot be traced to a source.</p>

<h2>Step 5 — If some is already installed</h2>
<p>Assess rather than panic. Not every situation requires rewiring:</p>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Situation</th><th>Reasonable action</th></tr></thead>
<tbody>
<tr><td>Wire pulled but not yet plastered over</td><td>Pull it out and replace. Cost is labour only</td></tr>
<tr><td>Concealed, on light and fan circuits</td><td>Have an electrician measure load and check temperature under load; replace at the next opportunity</td></tr>
<tr><td>Concealed, on AC, geyser or power circuits</td><td>Replace. These are the highest-load circuits and the ones where under-specification copper actually fails</td></tr>
<tr><td>Concealed, mains from meter to DB</td><td>Replace without debate. This carries the whole house</td></tr>
</tbody></table></div>
<p>Ask the electrician to check whether the installed sizes match the design as well — an undersized circuit and a duplicate coil produce the same failure and often travel together.</p>

<h2>Step 6 — Fix the process, not just the delivery</h2>
<p>Duplicate material almost always enters through a process gap rather than bad luck. Before replacing the stock, close the gap:</p>
<ul>
<li>Buy in your own name, not on a with-material contract.</li>
<li>Buy from an authorised dealer who will show the certificate.</li>
<li>Insist on pay on delivery.</li>
<li>Verify at your own site using the <a href="original-finolex-wire-checklist-before-paying.html">12-point checklist</a>, including the <a href="original-finolex-wire-inner-qr-code.html">inner QR code</a>.</li>
</ul>
<p>If you would like a second opinion on material already delivered, send photographs of the carton, the label and the wire markings to <a href="{W}">{PH}</a>. We will tell you what we see, whether or not you bought it from us — we have been doing this in Bengaluru for 35 years and we would rather a house was wired correctly than win an argument about where it was bought.</p>
""".replace("{W}", W).replace("{PH}", PH) + CTA,
 D,
 [("What should I do if I receive duplicate Finolex wire?", "Stop the installation immediately, do not pay for the suspect material, and preserve the cartons, any inner inserts, a cut sample of the wire and the invoice. Photograph everything including the verification screen, then raise it with the seller in writing before taking any other step."),
  ("What evidence do I need to make a complaint?", "The cartons including empty ones, the inner inserts or codes from inside the boxes, a cut sample of wire at least a foot long showing the markings and conductor end, the invoice and delivery challan, photographs of everything including verification screens, and any WhatsApp messages with the seller."),
  ("How do I report counterfeit Finolex wire to the company?", "Contact Finolex customer care on 1800-209-0166 with the batch number, the QR verification result, the seller's name and location and your photographs. The batch number and the seller's identity are what make a report actionable — without both, a complaint cannot be traced to a source."),
  ("What if the duplicate wire is already inside the wall?", "It depends on the circuit. Wire pulled but not yet plastered should be replaced at labour cost only. Concealed light and fan circuits can be assessed by an electrician measuring load and temperature. Concealed air conditioner, geyser, power and mains circuits should be replaced, because those are where under-specification copper actually fails."),
  ("How should I raise the issue with the seller?", "In writing rather than by phone, so there is a record. State which cartons, which check failed, what the verification screen said, and what remedy you want — replacement with verified stock or a refund — and attach photographs. A genuine seller will want the cartons back and will replace them."),
  ("Can I get a second opinion on wire I already bought?", "Yes. Send photographs of the carton, the label and the wire markings to Mount Cable on 88676 76700 and we will tell you what we see, whether or not the material was bought from us. We would rather a house was wired correctly than win an argument about where it was purchased.")],
 ("homeowner-electrician-discussing-switchboard.jpg", "A homeowner and electrician reviewing suspect wire and cartons before continuing installation"),
 None),

]
