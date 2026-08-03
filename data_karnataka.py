# -*- coding: utf-8 -*-
"""Karnataka city coverage for Finolex supply.

Mount Cable India is a Bengaluru business with two showrooms (Chickpete /
BVK Iyengar Road and Jayanagar) and free next-day delivery inside Bangalore.
Outside Bengaluru we supply by road transport against a quotation — we do NOT
have branches, showrooms or godowns in any other Karnataka city, and nothing
on these pages may imply that we do.

Each entry is a dict consumed by build_city() in build.py:

  slug     URL slug -> karnataka/<slug>.html
  name     display name (current official spelling)
  alt      older / alternate spelling people still search for ("" if none)
  district revenue district
  region   broad region of Karnataka, used in prose
  km       approximate road distance from Bengaluru in km
  route    honest road description, no highway numbers (they get renumbered)
  nearby   towns in the same catchment that the same consignment can cover
  context  one bespoke sentence about construction/wiring demand in that city
  demand   one bespoke paragraph about who orders Finolex there and why
  img      hero photograph from assets/img/people
  faqs     two city-specific FAQs; build_city adds three standard ones
"""

KARNATAKA_CITIES = [

 {"slug": "mysuru", "name": "Mysuru", "alt": "Mysore",
  "district": "Mysuru district", "region": "southern Karnataka", "km": 145,
  "route": "via Ramanagara and Mandya",
  "nearby": "Nanjangud, Srirangapatna, T Narasipura, Hunsur and Bannur",
  "context": "Mysuru's independent-house culture means most wiring decisions are still made by the family building the house rather than by a large contractor.",
  "demand": "Most Finolex enquiries from Mysuru come from people building a single house on their own site — typically a full 2BHK or 3BHK wiring list of 90-metre coils in 1.0, 1.5 and 2.5 sq mm, with a few 4.0 sq mm coils for the air-conditioner and geyser points. Because the same buyer is paying for the wire and living behind it, Mysuru customers ask more questions about originality than almost anywhere else in Karnataka, and we would rather they did.",
  "img": "happy-homeowner-couple-new-house-wiring.jpg",
  "faqs": [
    ("Do you have a shop in Mysuru?", "No. Mount Cable India has two showrooms, both in Bengaluru — Chickpete (BVK Iyengar Road, 560053) and Jayanagar (560011). We supply Finolex wires to Mysuru by road transport against a written quotation, with the freight shown separately so you can see exactly what you are paying for."),
    ("Is it worth ordering Finolex from Bengaluru instead of buying in Mysuru?", "It depends on the size of your list. For a full house of wiring the distributor rate on twenty or thirty coils usually more than covers the transport from Bengaluru, which is roughly 145 km away. For two or three coils it rarely does, and we will tell you so — message the list to 88676 76700 and we will give you the honest comparison."),
  ]},

 {"slug": "hubballi-dharwad", "name": "Hubballi-Dharwad", "alt": "Hubli-Dharwad",
  "district": "Dharwad district", "region": "north Karnataka", "km": 410,
  "route": "via Chitradurga, Davanagere and Haveri",
  "nearby": "Navanagar, Gokul Road, Kalghatgi, Kundgol, Navalgund and Annigeri",
  "context": "Hubballi-Dharwad is the commercial hub of north Karnataka, so orders from here are often larger and mix house wiring with small-commercial work.",
  "demand": "Enquiries from Hubballi and Dharwad tend to be split between residential builders in Navanagar and Gokul Road and small contractors wiring shops, clinics and offices. Those jobs usually need a mix of 90-metre coils for the light and fan circuits and 180-metre or 300-metre coils for the longer runs, which is exactly where ordering a consolidated consignment from a distributor starts to make financial sense.",
  "img": "contractor-bulk-order-loading-warehouse.jpg",
  "faqs": [
    ("Can you supply Finolex wire to Hubballi and Dharwad together in one consignment?", "Yes. Hubballi and Dharwad are close enough that a single consignment usually covers both, and combining them keeps the freight per coil down. Send both lists together on WhatsApp at 88676 76700 and we will quote them as one dispatch."),
    ("How long does delivery to Hubballi take?", "Hubballi is roughly 410 km from our Bengaluru godown by road, via Chitradurga, Davanagere and Haveri. Transit time depends on the transporter and the size of the consignment, and we confirm the expected date in writing before you pay anything — we do not give a date we cannot hold."),
  ]},

 {"slug": "mangaluru", "name": "Mangaluru", "alt": "Mangalore",
  "district": "Dakshina Kannada district", "region": "coastal Karnataka", "km": 350,
  "route": "via Hassan and Sakleshpur",
  "nearby": "Ullal, Bantwal, Moodbidri, Surathkal, Puttur and Mulki",
  "context": "The coastal climate makes insulation quality a practical concern in Mangaluru rather than a theoretical one, because humidity and salt air are unforgiving on poor PVC.",
  "demand": "Mangaluru buyers ask about grades more than most. Humid coastal conditions and long service life expectations push a lot of enquiries towards FR-LSH (Flamegard) and Finolex Ultra rather than plain FR, particularly for bedrooms and enclosed spaces. We stock all of them, and we will say plainly when the cheaper grade is genuinely enough for the circuit you are describing.",
  "img": "happy-family-new-home-lights-on.jpg",
  "faqs": [
    ("Which Finolex grade is best for a house in Mangaluru?", "For coastal humidity, the grade matters less than people assume — genuine Finolex FR insulation is rated for the same conditions everywhere in India. The reason to move up to FR-LSH (Flamegard) or Finolex Ultra is smoke and halogen behaviour in a fire, not humidity. Message your room-by-room list to 88676 76700 and we will suggest a grade mix rather than upselling the whole house."),
    ("Do you deliver to Udupi and Manipal as well as Mangaluru?", "Yes, and the same consignment usually covers both, since Udupi is a short run up the coast from Mangaluru. If you have material going to two coastal addresses, tell us at quotation stage so the freight is calculated once instead of twice."),
  ]},

 {"slug": "belagavi", "name": "Belagavi", "alt": "Belgaum",
  "district": "Belagavi district", "region": "north-west Karnataka", "km": 500,
  "route": "via Hubballi and Dharwad",
  "nearby": "Gokak, Bailhongal, Chikodi, Khanapur, Nippani and Saundatti",
  "context": "Belagavi sits near the Maharashtra and Goa borders, which means buyers there are comparing prices across three states and quotes vary wildly.",
  "demand": "Because Belagavi buyers can shop across state lines, they see a wider spread of quoted prices than anyone else in Karnataka — and a wide spread is exactly the condition in which counterfeit wire moves. If one of your quotes is far below the others, that gap is not negotiating skill. Genuine branded wire runs on a 3 to 5 per cent dealer margin, so there is no honest way to be 15 per cent cheaper than the market.",
  "img": "shop-owner-explaining-wire-quality.jpg",
  "faqs": [
    ("Why do Finolex quotes in Belagavi vary so much?", "Belagavi buyers collect quotes from Karnataka, Maharashtra and sometimes Goa, and each market prices freight and margin differently. A spread of a few per cent is normal. A spread of 15 per cent or more is not, because genuine branded wire runs on a 3 to 5 per cent dealer margin — a quote that far below the others is usually a short coil, an under-weight conductor or a counterfeit."),
    ("Is Belagavi too far to order Finolex wire from Bengaluru?", "Belagavi is roughly 500 km from our godown, so freight is a real cost and we will not pretend otherwise. For a full-house or project-sized list the distributor rate generally absorbs it; for a handful of coils it does not. Send the list to 88676 76700 and we will tell you honestly which side of that line you are on."),
  ]},

 {"slug": "kalaburagi", "name": "Kalaburagi", "alt": "Gulbarga",
  "district": "Kalaburagi district", "region": "north-east Karnataka", "km": 615,
  "route": "via Ballari and Raichur",
  "nearby": "Sedam, Aland, Chittapur, Jewargi, Afzalpur and Shahabad",
  "context": "Kalaburagi's summer heat is a genuine engineering input — conductor sizing that is marginal in a cooler district can run hot here.",
  "demand": "Ambient temperature de-rates a cable's safe current-carrying capacity, and Kalaburagi's summers are among the hottest in Karnataka. That is a good reason to size air-conditioner and geyser circuits generously in 4.0 sq mm rather than stretching 2.5 sq mm, and an even better reason not to accept a coil whose copper is thinner than the sq mm printed on it. Under-specification and heat is the combination that actually causes failures.",
  "img": "electrician-installing-mcb-distribution-board.jpg",
  "faqs": [
    ("Does the heat in Kalaburagi affect what wire size I should use?", "Yes. High ambient temperature reduces the current a cable can safely carry, so circuits that would be adequate elsewhere can run hot here. For air-conditioner and geyser points we would rather see 4.0 sq mm than a stretched 2.5 sq mm. Our free wire size calculator gives you a starting point, and you can send the load list to 88676 76700 for a second opinion."),
    ("Can you supply Finolex wire to Kalaburagi?", "Yes, by road transport from Bengaluru — roughly 615 km via Ballari and Raichur. We do not have a branch or godown in Kalaburagi and will not claim one. The quotation shows material and freight separately, and payment terms are agreed in writing before anything is despatched."),
  ]},

 {"slug": "davanagere", "name": "Davanagere", "alt": "",
  "district": "Davanagere district", "region": "central Karnataka", "km": 265,
  "route": "via Chitradurga and Harihar",
  "nearby": "Harihar, Channagiri, Honnali, Jagalur and Nyamati",
  "context": "Davanagere sits on the main Bengaluru–Hubballi corridor, which makes it one of the easier north-Karnataka runs for a part-load consignment.",
  "demand": "Davanagere and Harihar orders are usually residential — independent houses and small apartment blocks — and the lists are the classic house-wiring mix of 1.0, 1.5, 2.5 and 4.0 sq mm coils. Because the city is on a well-served transport corridor, part-load freight from Bengaluru is more economical here than the distance alone would suggest.",
  "img": "house-under-construction-conduit-wiring.jpg",
  "faqs": [
    ("How much does transport to Davanagere add to the wire cost?", "It depends on the weight of the consignment, and copper is heavy. We show freight as a separate line in the quotation rather than burying it in the rate, so you can compare our landed cost against a local quote honestly. Send your list to 88676 76700 for the figure."),
    ("Can you supply both Davanagere and Harihar in one order?", "Yes. Harihar is close enough to share a consignment with Davanagere, and combining them means the freight is worked out once. Mention both addresses when you send the list."),
  ]},

 {"slug": "ballari", "name": "Ballari", "alt": "Bellary",
  "district": "Ballari district", "region": "north-east Karnataka", "km": 310,
  "route": "via Chitradurga and Hosapete",
  "nearby": "Hosapete, Sandur, Siruguppa, Kampli, Kudligi and Toranagallu",
  "context": "Ballari's mix of residential building and industrial activity means enquiries here range from a single house to sizeable project quantities.",
  "demand": "Orders from Ballari and Hosapete swing between two extremes — a family wiring one house, and a contractor asking for project quantities with a delivery schedule. Both get the same two answers from us: an itemised quotation within 60 minutes, and an open invitation to have every coil scanned before it leaves the godown.",
  "img": "happy-electrical-contractor-site-team.jpg",
  "faqs": [
    ("Do you supply Finolex wire for projects in Ballari and Hosapete?", "Yes. Project quantities are quoted with a delivery schedule rather than as a single dump, so material arrives as each phase needs it. Send the bill of quantities to 88676 76700 and we will come back with an itemised quotation and a proposed dispatch plan."),
    ("Can I get the coils checked before they are sent to Ballari?", "Yes, and we encourage it. Ask us to scan the outer QR codes on your consignment before dispatch and we will share the record on WhatsApp. You then scan the outer and inner codes again yourself when the material reaches your site — the second scan is the one that proves the contents were not swapped in transit."),
  ]},

 {"slug": "tumakuru", "name": "Tumakuru", "alt": "Tumkur",
  "district": "Tumakuru district", "region": "southern Karnataka", "km": 70,
  "route": "via Nelamangala and Dobbaspet",
  "nearby": "Sira, Tiptur, Kunigal, Gubbi, Madhugiri and Dobbaspet",
  "context": "At roughly 70 km, Tumakuru is close enough to Bengaluru that delivery is straightforward and the distributor rate is worth having on almost any list.",
  "demand": "Tumakuru is one of the easiest runs we do outside Bengaluru. The industrial corridor along the Bengaluru road has pulled in a lot of residential building, and because the distance is short, the freight rarely eats into the saving. Several Tumakuru customers simply collect from Chickpete themselves when they are in Bengaluru anyway.",
  "img": "delivery-van-electrical-materials.jpg",
  "faqs": [
    ("Is Tumakuru covered by your free Bangalore delivery?", "Free next-day delivery applies inside Bengaluru. Tumakuru is roughly 70 km beyond it, so it is quoted with transport — but because the distance is short the freight is modest, and on a full house-wiring list the distributor rate comfortably covers it."),
    ("Can I collect the material from your Bengaluru showroom instead?", "Yes. Plenty of Tumakuru customers do exactly that, since Chickpete is an easy run down the Bengaluru road. Confirm the list on WhatsApp first so the coils are picked and ready, and scan every carton at the counter before you load it."),
  ]},

 {"slug": "shivamogga", "name": "Shivamogga", "alt": "Shimoga",
  "district": "Shivamogga district", "region": "the Malnad region", "km": 275,
  "route": "via Tumakuru, Tiptur and Arsikere",
  "nearby": "Bhadravathi, Sagara, Shikaripura, Thirthahalli, Hosanagara and Soraba",
  "context": "Malnad building means heavy rainfall, plenty of independent houses and a lot of concealed conduit work where the wire has to last without ever being touched again.",
  "demand": "In and around Shivamogga most of what we supply goes into concealed conduit in independent houses. That is precisely the situation where buying an unverified coil is expensive — once the wire is behind plaster, replacing it costs many times what the coil cost. Scan every carton before the electrician starts pulling.",
  "img": "electricians-installing-conduit-ceiling.jpg",
  "faqs": [
    ("What wire should I use for concealed conduit wiring in Shivamogga?", "Standard genuine Finolex FR house wire is designed for concealed conduit, and the size matters more than the grade — 1.0 or 1.5 sq mm for lights and fans, 2.5 sq mm for sockets, 4.0 sq mm for air-conditioner and geyser points. Upgrade to FR-LSH in bedrooms if you want lower smoke in a fire. Send the room list to 88676 76700 for a sizing check."),
    ("Do you deliver to Bhadravathi and Sagara as well?", "Yes — those towns share a consignment with Shivamogga. Give us all the delivery addresses when you send the list so the freight is worked out once rather than per address."),
  ]},

 {"slug": "vijayapura", "name": "Vijayapura", "alt": "Bijapur",
  "district": "Vijayapura district", "region": "north Karnataka", "km": 520,
  "route": "via Hubballi and Bagalkote",
  "nearby": "Indi, Basavana Bagewadi, Sindagi, Muddebihal, Talikote and Almatti",
  "context": "Vijayapura is a long run from Bengaluru, so orders here make sense at full-house or project scale rather than for a few coils.",
  "demand": "We are honest with Vijayapura buyers about the arithmetic: at roughly 520 km, freight is a real number. On a full house of wiring or a project bill of quantities the distributor rate absorbs it comfortably. On five coils it does not, and we will say so rather than take the order.",
  "img": "contractor-checking-price-list-phone.jpg",
  "faqs": [
    ("Is it economical to order Finolex wire to Vijayapura from Bengaluru?", "For a full house of wiring or a project quantity, generally yes — the distributor rate on twenty-plus coils absorbs the freight. For a handful of coils, generally no. Send us the list on 88676 76700 and we will give you the landed cost so you can compare it against a local quote yourself."),
    ("How do I verify Finolex wire bought locally in Vijayapura?", "The same way anywhere: scan the outer QR code printed on the carton label and confirm it opens Finolex's own verification portal at check.finolex.com with details matching the box, then open the carton and scan the inner QR code as well. The inner code is the one a repacker cannot pass. If either fails, do not pay."),
  ]},

 {"slug": "udupi", "name": "Udupi", "alt": "",
  "district": "Udupi district", "region": "coastal Karnataka", "km": 400,
  "route": "via Hassan and Mangaluru",
  "nearby": "Manipal, Kundapura, Karkala, Brahmavara, Kaup and Hebri",
  "context": "Udupi and Manipal have a steady stream of residential and rented-accommodation building, which produces a lot of repeat wiring work.",
  "demand": "A fair share of Udupi and Manipal enquiries are for buildings that will be let out rather than lived in by the owner — and that is where the temptation to save on wire is strongest, and worst. Wire is the one item in a rented building that the owner will never inspect again and the tenant can never see. Get it right once.",
  "img": "senior-electrician-teaching-apprentice.jpg",
  "faqs": [
    ("Do you supply Finolex wire to Manipal and Kundapura?", "Yes — both share a consignment with Udupi, and generally with Mangaluru too. List all the delivery points when you send the requirement so the transport is quoted once."),
    ("Should I use a cheaper wire in a building I am renting out?", "No. Wire in a let-out building is the one item nobody will ever inspect again — the owner does not live behind it and the tenant cannot see it. That is exactly why counterfeit wire ends up there, and exactly why it should not. Buy genuine, scan every carton, and it is a decision you never revisit."),
  ]},

 {"slug": "hassan", "name": "Hassan", "alt": "",
  "district": "Hassan district", "region": "southern Karnataka", "km": 185,
  "route": "via Nelamangala, Kunigal and Channarayapatna",
  "nearby": "Arsikere, Channarayapatna, Sakleshpur, Holenarasipura, Belur and Halebidu",
  "context": "Hassan is on the main road to the coast, which makes it a convenient stop for consignments already heading towards Mangaluru.",
  "demand": "Hassan sits on the Bengaluru–Mangaluru road, so material heading to the coast passes through anyway and part-load freight here is reasonable. Most orders are independent houses in and around the town, with the occasional small commercial job in Sakleshpur and Belur.",
  "img": "happy-house-builder-electrical-delivery.jpg",
  "faqs": [
    ("How far is Hassan from your Bengaluru godown?", "Roughly 185 km, via Nelamangala, Kunigal and Channarayapatna. It is on the main road to Mangaluru, so transport options are good and part-load freight is reasonable for a house-wiring quantity."),
    ("Do you cover Sakleshpur and Belur?", "Yes, both fall in the same catchment as Hassan and can share a consignment. Send all the addresses together when you ask for the quotation."),
  ]},

 {"slug": "bidar", "name": "Bidar", "alt": "",
  "district": "Bidar district", "region": "the far north-east of Karnataka", "km": 700,
  "route": "via Kalaburagi and Humnabad",
  "nearby": "Basavakalyan, Humnabad, Bhalki, Aurad and Chitguppa",
  "context": "Bidar is the furthest district headquarters from Bengaluru in Karnataka, so we quote it strictly at project or full-house scale.",
  "demand": "At roughly 700 km, Bidar is the longest run in the state and we will not pretend the freight is trivial. What we can do is quote it transparently — material rate, freight and transit time shown separately — so you can compare our landed cost against your local options and decide with real numbers rather than a sales pitch.",
  "img": "builder-architect-site-electrical-planning.jpg",
  "faqs": [
    ("Do you actually supply as far as Bidar?", "Yes, but only where the quantity justifies it. Bidar is roughly 700 km from Bengaluru — the longest run in Karnataka — so we quote material and freight separately and let you judge whether the landed cost beats what you can get locally. We would rather lose the order than talk you into an uneconomical one."),
    ("What if I only need a few coils in Bidar?", "Then buying locally will almost certainly cost less than freight from Bengaluru, and we will tell you that. What we will still do free of charge is look at photographs of whatever you are offered locally — the carton label, the QR codes and the wire markings — and give you a second opinion before you pay."),
  ]},

 {"slug": "raichur", "name": "Raichur", "alt": "",
  "district": "Raichur district", "region": "north-east Karnataka", "km": 410,
  "route": "via Ballari and Sindhanur",
  "nearby": "Sindhanur, Manvi, Devadurga, Lingsugur and Maski",
  "context": "Raichur is another hot district where conductor sizing and copper honesty matter more than the marketing on the box.",
  "demand": "Raichur summers put real thermal stress on domestic circuits. That makes two things worth insisting on: sizes chosen with some headroom, and copper that actually matches the sq mm printed on the insulation. A coil that is 10 per cent light on copper is a coil that runs 10 per cent hotter, every day, for thirty years.",
  "img": "electrician-hands-stripping-wire-closeup.jpg",
  "faqs": [
    ("How can I tell if a coil has less copper than it should?", "Cut a clean end and look at the conductor. Count the strands and look at the overall bundle thickness against the sq mm printed on the insulation — a short-weight coil usually shows fewer or thinner strands. Weight is the other tell: a genuine 90-metre coil has a predictable weight for its size. Send us a photograph of the cut end on 88676 76700 and we will give you an opinion."),
    ("Do you supply Finolex wire to Sindhanur and Manvi?", "Yes, both share a consignment with Raichur. Give us every delivery address at quotation stage so the freight is calculated once for the whole consignment."),
  ]},

 {"slug": "chitradurga", "name": "Chitradurga", "alt": "",
  "district": "Chitradurga district", "region": "central Karnataka", "km": 200,
  "route": "via Tumakuru and Sira",
  "nearby": "Hiriyur, Challakere, Hosadurga, Holalkere and Molakalmuru",
  "context": "Chitradurga is on the main northern corridor out of Bengaluru, so transport is frequent and part-load freight is inexpensive.",
  "demand": "Chitradurga is a straightforward run — roughly 200 km on a well-served corridor. Most orders are independent houses, and the freight on a full house-wiring list is small enough that the distributor rate is clearly worth having.",
  "img": "wire-coils-warehouse-electrical-distributor.jpg",
  "faqs": [
    ("How long does it take to get Finolex wire to Chitradurga?", "Chitradurga is roughly 200 km from Bengaluru via Tumakuru and Sira, on a corridor with frequent transport. We confirm the expected delivery date in writing with the quotation, and we would rather give you a date we can hold than an optimistic one."),
    ("Can you supply Hiriyur and Challakere too?", "Yes, both are in the same catchment and can travel with a Chitradurga consignment. Mention them when you send the list so the freight is worked out for the whole load."),
  ]},

 {"slug": "mandya", "name": "Mandya", "alt": "",
  "district": "Mandya district", "region": "southern Karnataka", "km": 100,
  "route": "via Ramanagara and Channapatna",
  "nearby": "Maddur, Malavalli, Pandavapura, Srirangapatna, Nagamangala and K R Pet",
  "context": "At about 100 km on the Mysuru road, Mandya is one of the shortest and cheapest runs outside Bengaluru.",
  "demand": "Mandya is close enough that transport barely moves the landed cost, so the distributor rate shows up almost entirely as saving. Most orders are independent houses in the town and the surrounding taluks, and material heading to Mysuru passes through anyway.",
  "img": "happy-customer-receiving-electrical-order.jpg",
  "faqs": [
    ("Is Mandya close enough for economical delivery?", "Yes. At roughly 100 km on the Mysuru road, freight is modest and the distributor rate on a house-wiring list comfortably covers it. Material heading further to Mysuru passes through Mandya anyway."),
    ("Do you cover Maddur, Malavalli and Srirangapatna?", "Yes, all of them sit in the same catchment as Mandya. Give us the delivery address with the list and we will include it in the quotation."),
  ]},

 {"slug": "chikkamagaluru", "name": "Chikkamagaluru", "alt": "Chikmagalur",
  "district": "Chikkamagaluru district", "region": "the Malnad region", "km": 245,
  "route": "via Hassan and Belur, or via Kadur",
  "nearby": "Kadur, Tarikere, Mudigere, Sringeri, Koppa and Birur",
  "context": "Estate bungalows and homestays around Chikkamagaluru often need longer cable runs than a town house, which changes the coil lengths that make sense.",
  "demand": "A lot of Chikkamagaluru wiring is spread out — estate houses, outbuildings, homestay blocks — so runs are longer and joints are the enemy. That is where 180-metre and 300-metre coils earn their keep over 90-metre ones: fewer joints, less wastage, and a cleaner installation. Voltage drop over long runs is worth checking too.",
  "img": "warm-led-lighting-living-room-family.jpg",
  "faqs": [
    ("Should I use 180M or 300M coils for a spread-out property?", "Usually yes. Longer coils mean fewer joints across long runs between a main house and outbuildings, which is both safer and less wasteful. On very long runs also check voltage drop — our free voltage drop calculator will tell you whether the size you planned is still adequate at that distance."),
    ("Do you supply Kadur, Tarikere and Mudigere?", "Yes, they share the Chikkamagaluru catchment. Send all the delivery points with your list so the transport is quoted once for the whole consignment."),
  ]},

 {"slug": "kolar", "name": "Kolar", "alt": "",
  "district": "Kolar district", "region": "eastern Karnataka", "km": 70,
  "route": "via Hoskote and Malur",
  "nearby": "Kolar Gold Fields (KGF), Bangarpet, Malur, Srinivaspur and Mulbagal",
  "context": "Kolar is barely an hour beyond Bengaluru's eastern edge, so it behaves much like an extension of our regular delivery area.",
  "demand": "Kolar, Malur and KGF are close enough to Bengaluru that the run is simple and the freight is small. The industrial belt along the Bengaluru road has brought steady residential building with it, and most of what we send that way is standard house-wiring quantities.",
  "img": "electrician-testing-socket-multimeter.jpg",
  "faqs": [
    ("Do you deliver Finolex wire to Kolar and KGF?", "Yes. Kolar is roughly 70 km east of Bengaluru via Hoskote and Malur, so it is a short and inexpensive run. KGF, Bangarpet and Malur are covered by the same consignment."),
    ("Is Kolar included in free delivery?", "Free next-day delivery applies within Bengaluru. Kolar sits outside it, so a transport charge applies — but at 70 km it is small, and on a full house-wiring list the distributor rate more than covers it."),
  ]},

 {"slug": "bagalkote", "name": "Bagalkote", "alt": "Bagalkot",
  "district": "Bagalkote district", "region": "north Karnataka", "km": 480,
  "route": "via Davanagere and Gadag",
  "nearby": "Badami, Jamkhandi, Mudhol, Ilkal, Rabkavi-Banhatti and Guledgudda",
  "context": "Bagalkote district covers a lot of small towns, so consignments here often serve several delivery points from one dispatch.",
  "demand": "Orders towards Bagalkote frequently have more than one destination — Badami, Jamkhandi, Mudhol or Ilkal on the same run. Consolidating them into a single consignment is what makes the freight sensible at this distance, so tell us every delivery point before we quote rather than after.",
  "img": "homeowner-electrician-discussing-switchboard.jpg",
  "faqs": [
    ("Can one consignment cover several towns in Bagalkote district?", "Usually yes, and at this distance that is what makes the economics work. Badami, Jamkhandi, Mudhol and Ilkal can often share a dispatch with Bagalkote. Give us every delivery point before we quote so the freight is split properly."),
    ("How do I know the wire that arrives is the wire you quoted?", "Two ways. Ask us to scan the outer QR codes before dispatch and we will send you the record. Then, when it arrives, scan the outer code on every carton yourself and open at least a sample of boxes to scan the inner codes as well. The inner code is what proves the contents were not swapped."),
  ]},

 {"slug": "ramanagara", "name": "Ramanagara", "alt": "",
  "district": "Ramanagara district", "region": "southern Karnataka", "km": 50,
  "route": "via Bidadi",
  "nearby": "Channapatna, Kanakapura, Magadi, Bidadi and Harohalli",
  "context": "Ramanagara is the closest district to Bengaluru on the Mysuru road, and in practice deliveries there work almost like a Bengaluru run.",
  "demand": "Ramanagara, Bidadi, Channapatna and Kanakapura sit within an hour of our godown, and a lot of Bengaluru families building weekend or retirement houses out that way order through us. The run is short enough that transport barely registers against the distributor rate.",
  "img": "happy-electrician-smiling-portrait.jpg",
  "faqs": [
    ("Do you deliver to Ramanagara, Bidadi and Kanakapura?", "Yes, and these are among the easiest runs we do outside Bengaluru — all within about an hour of the godown on the Mysuru road. Transport is quoted separately from free Bangalore delivery, but at this distance it is a small figure."),
    ("Can I still pay after checking the material?", "Payment terms outside Bengaluru are agreed in writing before dispatch, and for short runs like Ramanagara we can usually arrange for you to inspect and scan the cartons at your site first. Ask when you request the quotation, so the terms are settled before anything moves."),
  ]},

]
