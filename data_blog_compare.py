# -*- coding: utf-8 -*-
"""Brand comparison posts written for the queries Search Console shows landing
on mountcable.com (Sep 2026): kei vs finolex, rr kabel vs finolex,
rr kabel vs polycab vs finolex, greatwhite vs anchor.

Framing: fair comment. Nothing here asserts a defect in a named brand. Where a
price is quoted it comes from the lists held in the quote builder (Finolex list
wef 4 Sep 2026, Polycab distributor list Jun/Aug 2026, Anchor pricelist Apr 2026).
Brands without a list on file are described by positioning only.
"""
from data_finolex_mrp import HOUSE_WIRE, offer, EFFECTIVE_FROM

D = ("2026-09-08", "September 8, 2026")
W = "https://wa.me/918867676700"
PH = "88676 76700"


def _rs(n):
    return "₹" + format(int(round(n)), ",d")


CTA = (f'<p class="muted"><strong>Want both brands priced for your list?</strong> Send it to <a href="{W}">WhatsApp {PH}</a> '
       'and Mount Cable India will quote each brand line by line within 60 minutes, so the comparison is made on real figures '
       'rather than list prices. No obligation to buy from us.</p>')

FIN_SILVER = {s: offer(HOUSE_WIRE[s]["silver"], "silver") for s in ("1.0", "1.5", "2.5", "4.0", "6.0")}
FIN_LIST = {s: HOUSE_WIRE[s]["silver"] for s in ("1.0", "1.5", "2.5", "4.0", "6.0")}
POLY_ETIRA = {"1.0": 2590, "1.5": 3820, "2.5": 6095, "4.0": 9115, "6.0": 14015}
POLY_MAXIMA = {"1.0": 3100, "1.5": 4525, "2.5": 7100, "4.0": 10360, "6.0": 15550}


def _list_table():
    rows = "".join(
        f"<tr><td>{s} sq mm</td><td>{_rs(FIN_LIST[s])}</td><td>{_rs(POLY_ETIRA[s])}</td><td>{_rs(POLY_MAXIMA[s])}</td></tr>"
        for s in FIN_LIST)
    return ('<div class="ptable-wrap"><table class="ptable"><thead><tr><th>Size (90 m coil)</th><th>Finolex Silver FR list</th>'
            '<th>Polycab Etira FR list</th><th>Polycab Maxima HR-FR list</th></tr></thead><tbody>' + rows + '</tbody></table></div>')


BLOG_COMPARE = [

# ---------------------------------------------------------------- 1
("kei-vs-finolex-wire-which-is-better",
 "KEI vs Finolex Wires: Which Is Better for House Wiring?",
 "KEI and Finolex both make ISI copper house wire. Where each brand is strong, how their FR and FR-LSH ranges compare, what the price gap really is, and which one a Bangalore home should choose.",
 "Comparison",
 f"""<p><strong>For house wiring in Bangalore, Finolex is the safer choice on availability, verification and resale of
leftover coils; KEI is a strong choice where the same order includes power or control cable, because KEI's depth is in
the industrial range. On the wire inside the insulation, both are ISI 694 electrolytic copper and both will last the
life of the house if the coil is genuine and the size is right.</strong></p>

<h2>Who makes what</h2>
<p>Finolex Cables has made house wire in Pune since 1958 and is, by volume, the name most Indian electricians default
to for a residential job. Its residential ranges are the Silver Pack and Gold Pack FR wire, the Flamegard FR-LSH grade
and Finoultra, the halogen-free e-beam range. KEI Industries, based in Delhi, built its reputation on LT and HT power
cable, control and instrumentation cable and stainless-steel wire, and added house wire later. Its residential lines
(Homecab and Conflame) sit alongside a much larger industrial catalogue.</p>
<p>That history shows in the shops. In Bangalore, Finolex is stocked in almost every electrical retailer and every size
and colour is available on the day; KEI house wire is stocked by fewer retailers and more often ordered against a
requirement. For a homeowner that matters when the electrician runs short of one colour on a Sunday.</p>

<h2>Specification, side by side</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Point</th><th>Finolex</th><th>KEI</th></tr></thead>
<tbody>
<tr><td>Standard</td><td>IS 694, ISI marked, 1100 V</td><td>IS 694, ISI marked, 1100 V</td></tr>
<tr><td>Conductor</td><td>Multistrand bare electrolytic copper</td><td>Multistrand bare electrolytic copper</td></tr>
<tr><td>Residential grades</td><td>FR (Silver, Gold), FR-LSH (Flamegard), HFFR (Finoultra)</td><td>FR, FR-LSH, HFFR / LS0H</td></tr>
<tr><td>Coil lengths</td><td>45, 90, 180, 300 / 200 m</td><td>90 and 180 m typical</td></tr>
<tr><td>Verification</td><td>Outer and inner QR checked on Finolex's server</td><td>Hologram and batch printing; brand app where offered</td></tr>
<tr><td>Where the brand is deepest</td><td>House wire, flexible, telecom and coaxial cable</td><td>Power, control and instrumentation cable</td></tr>
</tbody></table></div>
<p>On paper the two are equivalent for a house. Both carry the ISI mark on the same standard; both offer an FR-LSH grade
for flats and stairwells. The differences that matter are practical: coil lengths, how you verify a coil, and who
stocks it.</p>

<h2>Price: what the gap actually is</h2>
<p>KEI does not publish a residential list we can reproduce here, so we will not invent a figure. In our own trade, KEI
house wire quotes land close to Finolex Silver for the same size, and both brands are sold by dealers at a large
discount to list. Mount Cable India's Finolex Silver Pack prices, current to {EFFECTIVE_FROM}, are
{_rs(FIN_SILVER['1.5'])} for 1.5 sq mm, {_rs(FIN_SILVER['2.5'])} for 2.5 sq mm and {_rs(FIN_SILVER['4.0'])} for
4.0 sq mm per 90 m coil, taxes extra; the full table is on the
<a href="../price-lists/finolex-price-list.html">Finolex price list</a>. If a KEI quote comes in far below those
figures, or a Finolex quote does, the coil deserves a scan before payment.</p>

<h2>Where KEI is the better buy</h2>
<ul>
<li><strong>Mixed orders.</strong> If the same site needs armoured power cable from the meter, control cable for a pump
and house wire inside, a single KEI order simplifies the paperwork and often the price.</li>
<li><strong>Specified projects.</strong> Builders and consultants who already use KEI power cable frequently specify
KEI house wire for consistency.</li>
<li><strong>Industrial and commercial premises</strong>, where KEI's control and flexible ranges are the natural
fit.</li>
</ul>

<h2>Where Finolex is the better buy</h2>
<ul>
<li><strong>A house or flat</strong> in Bangalore, where every retailer and every electrician knows the ranges and
leftover coils are easy to return or sell.</li>
<li><strong>Verification.</strong> The two-QR check on Finolex's own server is the most complete counterfeit check on
any Indian wire brand. The <a href="../finolex-wire-scanner.html">Finolex wire scanner</a> does it in ten seconds.</li>
<li><strong>Long coils.</strong> The 300 m and 200 m coils cut the per-metre cost on apartment projects.</li>
</ul>

<h2>Our recommendation</h2>
<p>For a home: Finolex Silver or Gold for the wiring, Flamegard FR-LSH in a flat. For a factory, a warehouse or a site
with power cable on the same order: KEI across the board. Either way, size the circuits correctly with the
<a href="../tools/wire-size-calculator.html">wire size calculator</a>, because a genuine coil of the wrong size fails
sooner than a genuine coil of the right size in either brand. The four-brand view, with Polycab and RR Kabel included,
is in <a href="finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html">Finolex vs Polycab vs RR Kabel vs KEI</a>.</p>
{CTA}""",
 D,
 [("Is KEI wire better than Finolex?",
   "Neither is better on the copper: both are ISI 694 multistrand electrolytic copper house wire. Finolex is stronger on residential availability, coil options and QR verification; KEI is stronger where power, control and house wire are bought together for one site."),
  ("Which is cheaper, KEI or Finolex wire?",
   "Dealer prices for the same size land close together. Mount Cable India's Finolex Silver 1.5 sq mm 90 m coil is " + _rs(FIN_SILVER['1.5']) + " taxes extra; a KEI quote for the same size is usually within a few percent. A quote far below either figure is the warning sign, not the bargain."),
  ("Does KEI make FR-LSH house wire?",
   "Yes. Like Finolex's Flamegard, KEI offers flame-retardant low-smoke and halogen-free grades for flats, stairwells and enclosed spaces."),
  ("Can I verify a KEI wire coil like a Finolex coil?",
   "KEI coils carry batch printing and packaging security features. Finolex's two-QR check on its own server is the most complete verification available on Indian house wire, which is one reason Finolex is preferred for residential buyers who cannot inspect the copper."),
  ("Which brand does Mount Cable recommend for a house in Bangalore?",
   "Finolex for a home, because of availability, the QR check and the range of coil lengths. KEI where the order also includes power or control cable. We stock and quote both."),
  ("Where can I buy KEI or Finolex wire in Bangalore?",
   f"Mount Cable India, Jayanagar and Chickpete, stocks both brands with free next-day delivery across Bangalore. WhatsApp {PH} with your sizes and quantities for an itemised quote.")],
 ("wire-coils-warehouse-electrical-distributor.jpg", "Finolex and KEI wire coils stacked in Mount Cable India's Bangalore warehouse"),
 None),

# ---------------------------------------------------------------- 2
("rr-kabel-vs-finolex-wire-which-is-better",
 "RR Kabel vs Finolex Wires: Which Is Better, and What You Pay for the Difference",
 "RR Kabel positions itself above Finolex on price with its Firex LS0H and Unilay conductor ranges. What that premium buys, where Finolex matches it, and which brand a Bangalore home should wire with.",
 "Comparison",
 f"""<p><strong>RR Kabel is the premium-priced brand of the two and earns part of that premium with its Firex LS0H
low-smoke range and its Unilay conductor; Finolex matches it on the ISI copper inside, offers an equivalent FR-LSH and
halogen-free grade at a lower price, and is easier to verify and to buy in Bangalore. For most homes Finolex is the
better value; RR Kabel is the choice when the specification names it or when the buyer wants the top-of-market brand.</strong></p>

<h2>The two brands</h2>
<p>RR Kabel, from Mumbai, sells on the strength of international certifications and its Unilay conductor, a
compacted bundle of strands that gives a rounder, more uniform core. Its residential ranges include Superex FR, Firex
LS0H and the HR-FR heat-resistant grade, all in 90 m coils. Finolex, from Pune, is the older and larger house-wire
brand with the Silver Pack and Gold Pack FR ranges, Flamegard FR-LSH and Finoultra HFFR, in coils from 45 m to 300 m.</p>

<h2>Where RR Kabel is ahead</h2>
<ul>
<li><strong>Low-smoke, zero-halogen positioning.</strong> Firex LS0H is RR Kabel's headline product and the brand has
marketed the fire-safety case harder than anyone in the category.</li>
<li><strong>Conductor uniformity.</strong> Unilay strands lie in a regular pattern, which RR Kabel argues gives a more
consistent cross-section. Finolex's multistrand conductor meets the same IS 694 resistance limit.</li>
<li><strong>Brand perception</strong> in premium apartments and villas, where architects specify it by name.</li>
</ul>

<h2>Where Finolex is ahead</h2>
<ul>
<li><strong>Price.</strong> RR Kabel list prices sit above Finolex for the same size and grade, and dealer prices
follow. Mount Cable India's Finolex Silver Pack coils are {_rs(FIN_SILVER['1.5'])} in 1.5 sq mm and
{_rs(FIN_SILVER['2.5'])} in 2.5 sq mm, current to {EFFECTIVE_FROM}, taxes extra. See the
<a href="../price-lists/finolex-price-list.html">Finolex price list</a>.</li>
<li><strong>An equivalent grade for every RR Kabel grade.</strong> Flamegard FR-LSH answers Firex LS0H for flats
and stairwells; Finoultra is the halogen-free e-beam range. <a href="fr-vs-frls-vs-finolex-ultra.html">FR vs FR-LSH
vs Finoultra</a> explains which to use where.</li>
<li><strong>Verification.</strong> Two QR codes checked against Finolex's own server, in ten seconds with the
<a href="../finolex-wire-scanner.html">Finolex wire scanner</a>.</li>
<li><strong>Availability and coil options.</strong> Finolex is in every Bangalore shop and offers 45, 90, 180, 300
and 200 m coils; RR Kabel is largely a 90 m coil brand stocked by fewer retailers.</li>
</ul>

<h2>Grade for grade</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Use</th><th>RR Kabel</th><th>Finolex</th></tr></thead>
<tbody>
<tr><td>Standard house wiring</td><td>Superex FR</td><td>Silver Pack / Gold Pack FR</td></tr>
<tr><td>Flats, stairwells, low smoke</td><td>Firex LS0H</td><td>Flamegard FR-LSH</td></tr>
<tr><td>Halogen-free specification</td><td>Firex LS0H</td><td>Finoultra HFFR</td></tr>
<tr><td>Heat-resistant (kitchen, geyser, long AC runs)</td><td>HR-FR</td><td>Gold Pack FR sized one step up</td></tr>
<tr><td>Project coils</td><td>90 m</td><td>180 m, 300 m / 200 m</td></tr>
</tbody></table></div>

<h2>What the premium buys, honestly</h2>
<p>Both brands make wire that meets IS 694 and both, correctly sized, will outlast the house. The extra you pay for RR
Kabel buys the LS0H positioning, the Unilay conductor and the brand. Whether that is worth it depends on the building:
in a high-rise flat with long shared corridors, a low-smoke grade is worth specifying, and either brand's LS0H or
FR-LSH does it. In an independent house, standard FR from either brand is the sensible spend, and the money saved goes
further on a better MCB board.</p>

<h2>Our recommendation</h2>
<p>Finolex Gold Pack or Silver Pack for an independent house; Flamegard FR-LSH for a flat; RR Kabel Firex where the
architect's specification names it or the client wants the premium brand. We stock and quote both, and the wider view
with Polycab in the picture is in <a href="rr-kabel-vs-polycab-vs-finolex-wire.html">RR Kabel vs Polycab vs
Finolex</a>.</p>
{CTA}""",
 D,
 [("Is RR Kabel better than Finolex?",
   "RR Kabel is positioned as the premium brand with its Firex LS0H range and Unilay conductor; Finolex offers equivalent FR-LSH and halogen-free grades at a lower price with stronger verification and availability. For most homes Finolex is the better value; RR Kabel is chosen when specified or for the brand."),
  ("Is RR Kabel more expensive than Finolex?",
   "Yes, size for size RR Kabel lists above Finolex and dealer prices follow. Mount Cable India's Finolex Silver 2.5 sq mm 90 m coil is " + _rs(FIN_SILVER['2.5']) + " taxes extra; the equivalent RR Kabel coil quotes higher."),
  ("What is RR Kabel Firex LS0H?",
   "It is RR Kabel's low-smoke zero-halogen house wire, meant for flats, stairwells and enclosed spaces where smoke in a fire is the main hazard. Finolex's Flamegard FR-LSH and Finoultra serve the same purpose."),
  ("What is the Unilay conductor?",
   "RR Kabel's conductor construction in which the copper strands are laid in a regular compacted pattern for a rounder, more uniform core. Finolex uses a conventional multistrand conductor that meets the same IS 694 resistance requirement."),
  ("Which should I use for a flat in Bangalore?",
   "A low-smoke grade: Finolex Flamegard FR-LSH or RR Kabel Firex LS0H. Between the two, Finolex costs less and is easier to verify; RR Kabel is the choice if the builder's specification names it."),
  ("Where can I buy RR Kabel and Finolex in Bangalore?",
   f"Mount Cable India stocks both at Jayanagar and Chickpete with free next-day delivery across Bangalore. WhatsApp {PH} for a line-by-line quote in both brands.")],
 ("shop-owner-explaining-wire-quality.jpg", "Comparing RR Kabel and Finolex wire coils at Mount Cable India's counter in Bangalore"),
 None),

# ---------------------------------------------------------------- 3
("rr-kabel-vs-polycab-vs-finolex-wire",
 "RR Kabel vs Polycab vs Finolex: Which Wire Brand to Buy in 2026",
 "The three brands Bangalore homes actually choose between, compared on ranges, list prices from the current Finolex and Polycab lists, verification, availability and what each is best at.",
 "Comparison",
 f"""<p><strong>Finolex is the value-and-verification choice, Polycab the widest range with the most grades, and RR
Kabel the premium brand. On the copper all three are ISI 694 and any of them wires a house for life. Choose Finolex
for a home where price and a clean QR check matter, Polycab when you want FRLF or HR-FR grades or are buying the whole
electrical package from one brand, and RR Kabel when the specification or the client asks for the top of the
market.</strong></p>

<h2>The three brands in one table</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Point</th><th>Finolex</th><th>Polycab</th><th>RR Kabel</th></tr></thead>
<tbody>
<tr><td>Base</td><td>Pune, since 1958</td><td>Mumbai, India's largest wire maker</td><td>Mumbai, premium positioning</td></tr>
<tr><td>House-wire ranges</td><td>Silver FR, Gold FR, Flamegard FR-LSH, Finoultra HFFR</td><td>Etira FR, Primma FRLF, Optima FRLF, Maxima HR-FR, FRLS-H, HFFR</td><td>Superex FR, Firex LS0H, HR-FR</td></tr>
<tr><td>Coil lengths</td><td>45, 90, 180, 300 / 200 m</td><td>90, 200 / 300 m</td><td>90 m</td></tr>
<tr><td>Verification</td><td>Outer and inner QR on Finolex's server</td><td>Hologram and code on carton</td><td>Hologram and app</td></tr>
<tr><td>Price position</td><td>Value</td><td>Value to mid</td><td>Premium</td></tr>
<tr><td>Also makes</td><td>Flexible, telecom, coaxial, LAN, solar</td><td>Everything: fans, lights, switches, pipes, power cable</td><td>Fans, lights, switches</td></tr>
</tbody></table></div>

<h2>List prices, Finolex and Polycab</h2>
<p>We hold the current lists for both brands, so here is the same 90 m coil in each. Finolex is the list effective
{EFFECTIVE_FROM}; Polycab is the distributor list effective 8 June 2026. Both are list prices before the dealer
discount and before GST; dealer prices on both are well below.</p>
{_list_table()}
<p>Two things stand out. Polycab Etira lists slightly above Finolex Silver on every size, and Polycab Maxima HR-FR
carries a clear premium for the heat-resistant grade. RR Kabel does not publish a list we can reproduce; in our trade
its Superex and Firex coils quote above both. Mount Cable India's own Finolex selling prices are on the
<a href="../price-lists/finolex-price-list.html">Finolex price list</a> and the Polycab list is on the
<a href="../price-lists/polycab-price-list.html">Polycab price list</a>.</p>

<h2>Grades: what each brand calls the same thing</h2>
<ul>
<li><strong>Standard FR house wire:</strong> Finolex Silver or Gold, Polycab Etira, RR Kabel Superex.</li>
<li><strong>Low smoke for flats and stairwells:</strong> Finolex Flamegard FR-LSH, Polycab FRLS-H or Primma/Optima
FRLF, RR Kabel Firex LS0H.</li>
<li><strong>Halogen-free:</strong> Finolex Finoultra, Polycab HFFR, RR Kabel Firex LS0H.</li>
<li><strong>Heat resistant:</strong> Polycab Maxima HR-FR, RR Kabel HR-FR; Finolex covers the same points by sizing
up one step in Gold Pack.</li>
</ul>
<p>The grade matters more than the brand. A flat above the fourth floor should be wired in a low-smoke grade from any
of the three; an independent house is fine in standard FR from any of the three.
<a href="fr-vs-frls-vs-finolex-ultra.html">FR vs FR-LSH vs HFFR</a> explains the difference.</p>

<h2>Verification and duplicates</h2>
<p>All three brands are copied, Finolex and Polycab most because they sell most. Finolex's two-QR check on its own
server is the strongest defence: the <a href="../finolex-wire-scanner.html">Finolex wire scanner</a> answers in ten
seconds. Polycab and RR Kabel rely on holograms, batch printing and, for RR Kabel, a brand app. Whichever brand you
buy, the printing along the wire must match the carton, and a coil offered far below the list prices above is the
usual sign of a problem. See <a href="how-to-identify-duplicate-polycab-wire.html">duplicate Polycab wire</a> and
<a href="how-to-identify-duplicate-rr-kabel-wire.html">duplicate RR Kabel wire</a>.</p>

<h2>Which to choose</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Situation</th><th>Pick</th></tr></thead>
<tbody>
<tr><td>Independent house, value matters</td><td>Finolex Silver or Gold</td></tr>
<tr><td>Flat, low smoke needed, value matters</td><td>Finolex Flamegard FR-LSH</td></tr>
<tr><td>Kitchen and geyser points on long runs</td><td>Polycab Maxima HR-FR, or Finolex Gold one size up</td></tr>
<tr><td>Whole electrical package from one brand</td><td>Polycab</td></tr>
<tr><td>Architect specifies premium brand</td><td>RR Kabel Firex</td></tr>
<tr><td>Apartment project, bulk coils</td><td>Finolex 300 / 200 m or Polycab 300 / 200 m</td></tr>
</tbody></table></div>
<p>Pairwise detail: <a href="rr-kabel-vs-finolex-wire-which-is-better.html">RR Kabel vs Finolex</a>,
<a href="kei-vs-finolex-wire-which-is-better.html">KEI vs Finolex</a>, and the four-brand
<a href="finolex-vs-polycab-vs-rr-kabel-vs-kei-wire-comparison.html">Finolex vs Polycab vs RR Kabel vs KEI</a>.</p>
{CTA}""",
 D,
 [("Which is the best wire brand: RR Kabel, Polycab or Finolex?",
   "All three are ISI 694 copper house wire. Finolex is the value-and-verification choice, Polycab has the widest range of grades, RR Kabel is the premium brand. For most Bangalore homes Finolex; for a one-brand package Polycab; for a specified premium build RR Kabel."),
  ("Which is cheaper, Polycab or Finolex?",
   f"Coil for coil the lists are close: a 1.5 sq mm 90 m coil lists at {_rs(FIN_LIST['1.5'])} for Finolex Silver against {_rs(POLY_ETIRA['1.5'])} for Polycab Etira. Dealer prices on both are well below list. Mount Cable India's Finolex Silver 1.5 sq mm is {_rs(FIN_SILVER['1.5'])} taxes extra."),
  ("Is RR Kabel more expensive than Polycab and Finolex?",
   "Yes. RR Kabel is positioned and priced as the premium brand, above both Polycab and Finolex for the same size and grade."),
  ("Which brand is best for a flat?",
   "Any low-smoke grade: Finolex Flamegard FR-LSH, Polycab FRLS-H or FRLF, or RR Kabel Firex LS0H. The grade matters more than the brand."),
  ("Which brand is easiest to verify?",
   "Finolex, with two QR codes checked live against Finolex's own server. Polycab and RR Kabel rely on holograms, batch printing and, for RR Kabel, a brand app."),
  ("Does Mount Cable stock all three?",
   f"Yes, at Jayanagar and Chickpete with free next-day delivery across Bangalore. WhatsApp {PH} for the same list quoted in each brand.")],
 ("electrician-hands-stripping-wire-closeup.jpg", "Electrician stripping house wire while comparing RR Kabel, Polycab and Finolex coils"),
 None),

# ---------------------------------------------------------------- 4
("greatwhite-vs-anchor-switches",
 "Greatwhite vs Anchor Switches: Which Modular Switch Brand Is Better?",
 "Greatwhite's Fiana and Myrah ranges against Anchor by Panasonic's Roma Urban, Roma Classic and Penta. Design, price from the current Anchor list, availability, spares and which to choose for a Bangalore home.",
 "Comparison",
 f"""<p><strong>Anchor by Panasonic is the safer choice for most homes: the widest range, the deepest spares
availability, every electrician knows it, and the April 2026 pricelist puts a Roma Classic 10AX switch at ₹77 MRP.
Greatwhite is the design-led choice: its Fiana and Myrah ranges look more contemporary at a similar mid-range price,
and it suits a homeowner choosing switches for how the wall looks. Both are ISI-marked and both work reliably when
genuine.</strong></p>

<h2>The two brands</h2>
<p>Anchor was founded in 1963 and became part of Panasonic in 2007; it is India's largest-selling switch brand, with
the Roma family (Classic, Urban, Plus), Penta Modular, Rider, Ziva and Tiona in modular switches and the Penta piano
range for non-modular boards. Greatwhite is a younger Mumbai brand that built its name on the Fiana range, with a slim
plate and a flat rocker, and followed it with Myrah and a home-automation line. Greatwhite also makes wires, fans and
lighting, so a whole-house package is possible in both brands.</p>

<h2>Design and feel</h2>
<p>This is where Greatwhite wins most arguments. Fiana's plate is thin, the rocker is wide and flat, and the finishes
run to matte black and metallics that photograph well. Anchor's answer is Roma Urban, with its curved-edge plate and
1-module and 2-module switch options in white, black, graphite and silver, and it holds up in a modern interior. Roma
Classic, which most Bangalore electricians reach for by default, looks dated next to either, and Penta Modular is
plainer still. If the interior designer is choosing, expect Greatwhite Fiana or Anchor Roma Urban on the shortlist.</p>

<h2>Price</h2>
<p>We hold Anchor's April 2026 pricelist. MRP per piece: Roma Classic 10AX one-way switch ₹77, Roma Urban 10AX
one-way ₹160, Penta Modular 6AX one-way ₹46; Roma Urban 6/16A twin socket ₹504, Roma Classic ₹319; Roma Urban 4-module
white plate ₹343, Penta Modular ₹168. Full tables are on the
<a href="../price-lists/anchor-panasonic-price-list.html">Anchor Panasonic price list</a>. Greatwhite does not
publish a list we can reproduce, so we will not quote figures; in our trade, Fiana mechanisms and plates land in the
same band as Roma Urban, above Roma Classic and well above Penta. Both brands sell below MRP through dealers.</p>

<h2>Availability and spares</h2>
<p>Anchor is in every electrical shop in Karnataka. A Roma Classic switch that fails in ten years is replaced from
stock the same afternoon, and the plate sizes have not changed in a generation. Greatwhite is stocked by fewer
retailers, mostly the larger ones, and a matching plate or a specific finish may need to be ordered. For a homeowner
that is the practical difference: Anchor is the brand you can fix on a Sunday.</p>

<h2>Reliability and duplicates</h2>
<p>Both brands are ISI-marked and both, genuine, give a long service life on a 10AX or 16AX switch. Anchor's problem
is that its popularity makes it the most copied switch in India; Roma Classic duplicates are common in Bangalore.
Greatwhite is copied less because it sells less, though Fiana copies do exist. Check the moulding, the ISI mark and
the packaging using <a href="how-to-identify-duplicate-anchor-switches.html">identifying duplicate Anchor
switches</a> and <a href="how-to-identify-duplicate-greatwhite-switches.html">identifying duplicate Greatwhite
switches</a>, and buy from an authorised dealer for either.</p>

<h2>Which to choose</h2>
<div class="ptable-wrap"><table class="ptable">
<thead><tr><th>Situation</th><th>Pick</th></tr></thead>
<tbody>
<tr><td>Budget build, rental flat, utility areas</td><td>Anchor Penta Modular or Roma Classic</td></tr>
<tr><td>Family home, balance of looks and cost</td><td>Anchor Roma Urban</td></tr>
<tr><td>Designer interior, matte and metallic finishes</td><td>Greatwhite Fiana or Myrah</td></tr>
<tr><td>Long-term spares certainty</td><td>Anchor</td></tr>
<tr><td>Whole-house package with fans and lights</td><td>Either; Anchor has the wider catalogue</td></tr>
</tbody></table></div>
<p>The broader field, including Legrand and Schneider, is compared in
<a href="best-modular-switch-brands-india-2026.html">best modular switch brands in India 2026</a> and
<a href="which-switch-brand-should-you-buy.html">which switch brand should you buy</a>. Legrand's MRP for the same
items is on the <a href="../price-lists/legrand-switches-price-list.html">Legrand switches price list</a>.</p>
{CTA}""",
 D,
 [("Is Greatwhite better than Anchor?",
   "Greatwhite wins on contemporary design with its Fiana and Myrah ranges; Anchor wins on range, spares availability and the number of electricians who know it. Both are ISI-marked and reliable when genuine. For most homes Anchor Roma Urban; for a designer interior Greatwhite Fiana."),
  ("Which is cheaper, Greatwhite or Anchor?",
   "Anchor's April 2026 MRP: Roma Classic 10AX switch ₹77, Roma Urban ₹160, Penta Modular ₹46. Greatwhite Fiana prices in our trade land in the Roma Urban band. Anchor Roma Classic and Penta are cheaper than anything in the Greatwhite modular range."),
  ("Is Greatwhite Fiana a good switch?",
   "Yes. Fiana is Greatwhite's flagship modular range with a slim plate and flat rocker, ISI-marked, and popular with interior designers for its finishes. Its practical drawbacks are narrower retail availability and spares compared with Anchor."),
  ("Which Anchor range competes with Greatwhite Fiana?",
   "Roma Urban, Anchor's current design range with a curved-edge plate, 1-module and 2-module switches and white, black, graphite and silver plates at ₹226 to ₹866 MRP."),
  ("Are Anchor switches copied more than Greatwhite?",
   "Yes. Anchor Roma Classic is the most copied switch in India because it is the largest-selling. Buy from an authorised dealer and check the ISI mark, moulding and packaging."),
  ("Where can I buy Greatwhite and Anchor switches in Bangalore?",
   f"Mount Cable India stocks both at Jayanagar and Chickpete with free next-day delivery across Bangalore. WhatsApp {PH} with your board count for a quote in each brand.")],
 ("woman-homeowner-choosing-modular-switches.jpg", "Homeowner comparing Greatwhite Fiana and Anchor Roma Urban modular switch samples"),
 None),
]
