# -*- coding: utf-8 -*-
"""Free calculators for Mount Cable India.

Each tool is a dict: slug, name, tagline, title, h1, desc, intro, body (HTML+JS),
faqs, hero. Rendered by build_tool() in build.py at /tools/<slug>.html
"""

W = "https://wa.me/918867676700"
PH = "88676 76700"

# Shared reference data, kept in one place so every calculator agrees.
# Current ratings: PVC-insulated copper single-core, 3 loaded conductors in
# conduit, ~40 C ambient — the realistic Indian domestic case.
# Volt drop: mV per amp per metre, single-phase (two conductors).
CABLE_JS = """
const CABLE = [
  {size:1.0,  amps:11, mvam:44.0},
  {size:1.5,  amps:14, mvam:29.0},
  {size:2.5,  amps:19, mvam:18.0},
  {size:4.0,  amps:26, mvam:11.0},
  {size:6.0,  amps:33, mvam:7.3},
  {size:10.0, amps:45, mvam:4.4},
  {size:16.0, amps:61, mvam:2.8},
  {size:25.0, amps:80, mvam:1.75}
];
const MCB_RATINGS = [6,10,16,20,25,32,40,50,63];
function fmt(n, d){ return Number(n).toFixed(d===undefined?1:d); }
function inr(n){ return '\\u20B9' + Math.round(n).toLocaleString('en-IN'); }
"""

TOOLS = [

# ------------------------------------------------------------------ 1
{
 "slug": "wire-size-calculator",
 "name": "Wire Size Calculator",
 "tagline": "Find the correct sq mm for any circuit from its load and run length.",
 "title": "Wire Size Calculator (sq mm) for House Wiring | Mount Cable India",
 "h1": "Wire Size Calculator",
 "desc": "Free wire size calculator for Indian house wiring. Enter load in watts or amps, run length and phase to get the correct sq mm cable size, with voltage drop checked.",
 "intro": "Enter the load, the run length from your distribution board and the supply type. The calculator sizes the cable on current capacity and then re-checks it against voltage drop, which is what catches out long runs to an outbuilding, a pump or a top-floor air conditioner.",
 "hero": ("electrician-hands-stripping-wire-closeup.jpg", "Copper house wire being prepared for a circuit"),
 "body": """
<div class="calc">
  <div class="calc-grid">
    <label>Load type
      <select id="ltype">
        <option value="w">Watts</option>
        <option value="a">Amps</option>
      </select>
    </label>
    <label>Load value <input type="number" id="lval" value="1600" min="1" step="any"></label>
    <label>Supply
      <select id="phase">
        <option value="1">Single phase (230V)</option>
        <option value="3">Three phase (415V)</option>
      </select>
    </label>
    <label>Run length from DB (metres) <input type="number" id="len" value="18" min="1" step="any"></label>
    <label>Power factor <input type="number" id="pf" value="0.9" min="0.5" max="1" step="0.05"></label>
    <label>Max voltage drop
      <select id="vd">
        <option value="3">3% (recommended)</option>
        <option value="5">5% (permitted maximum)</option>
      </select>
    </label>
  </div>
  <button class="btn btn-gold calc-go" onclick="calcWire()">Calculate wire size</button>
  <div id="out" class="calc-out"></div>
</div>
<script>
""" + CABLE_JS + """
function calcWire(){
  const type = document.getElementById('ltype').value;
  const val  = parseFloat(document.getElementById('lval').value);
  const ph   = document.getElementById('phase').value;
  const len  = parseFloat(document.getElementById('len').value);
  const pf   = parseFloat(document.getElementById('pf').value) || 0.9;
  const vdp  = parseFloat(document.getElementById('vd').value);
  const out  = document.getElementById('out');
  if(!(val>0) || !(len>0)){ out.innerHTML = '<p class="calc-warn">Enter a load and a run length.</p>'; return; }

  const volts = ph === '3' ? 415 : 230;
  let amps;
  if(type === 'a'){ amps = val; }
  else { amps = ph === '3' ? val / (1.732 * volts * pf) : val / (volts * pf); }

  const vdLimit = volts * vdp / 100;
  const factor  = ph === '3' ? 0.866 : 1;   // 3-phase drop is line-to-line

  const design = amps * 1.25;            // margin for sustained load
  const MIN_SIZE = 1.5;                  // practical floor outside lighting
  let byAmp = null, byDrop = null;
  for(const c of CABLE){
    if(c.size < MIN_SIZE) continue;
    if(byAmp === null && c.amps >= design) byAmp = c;
    const drop = c.mvam * amps * len * factor / 1000;
    if(byDrop === null && drop <= vdLimit) byDrop = c;
  }
  if(!byAmp || !byDrop){
    out.innerHTML = '<p class="calc-warn">This load is beyond the domestic range covered here. WhatsApp 88676 76700 and we will size it for you.</p>';
    return;
  }
  const pick = byDrop.size > byAmp.size ? byDrop : byAmp;
  const drop = pick.mvam * amps * len * factor / 1000;
  const dropPct = drop / volts * 100;
  const governed = byDrop.size > byAmp.size ? 'voltage drop over the run length' : 'current-carrying capacity';

  let mcb = null;
  for(const r of MCB_RATINGS){ if(r >= amps * 1.15 && r <= pick.amps){ mcb = r; break; } }

  out.innerHTML =
    '<div class="calc-result"><span class="calc-big">' + fmt(pick.size,1) + ' sq mm</span>' +
    '<p>Recommended copper cable size for this circuit.</p></div>' +
    '<div class="ptable-wrap"><table class="ptable"><tbody>' +
    '<tr><td>Load current</td><td>' + fmt(amps,1) + ' A</td></tr>' +
    '<tr><td>Design current (with 25% margin)</td><td>' + fmt(design,1) + ' A</td></tr>' +
    '<tr><td>Minimum size on current capacity</td><td>' + fmt(byAmp.size,1) + ' sq mm (' + byAmp.amps + ' A)</td></tr>' +
    '<tr><td>Minimum size on voltage drop</td><td>' + fmt(byDrop.size,1) + ' sq mm</td></tr>' +
    '<tr><td>Voltage drop at ' + fmt(pick.size,1) + ' sq mm</td><td>' + fmt(drop,2) + ' V (' + fmt(dropPct,2) + '%)</td></tr>' +
    (mcb ? '<tr><td>Suggested MCB</td><td>' + mcb + 'A, Curve C</td></tr>' : '') +
    '</tbody></table></div>' +
    '<p class="calc-note">Size is governed here by <strong>' + governed + '</strong>. Ratings assume PVC-insulated copper conductors in conduit at around 40&deg;C with three loaded cores. Bunched cables, hot roof voids or buried runs need derating — send us the details and we will check it. For a geyser, air conditioner or pump that runs for hours at a stretch, most electricians go one size above the calculated minimum.</p>';
}
calcWire();
</script>
""",
 "faqs": [
  ("How do I calculate the wire size for a circuit?", "Convert the load to amperes, choose the smallest cable whose current rating exceeds that figure, then check voltage drop over the actual run length and step up a size if the drop exceeds 3%. Long runs are frequently governed by voltage drop rather than current, which is why a short 16A circuit and a 30-metre 16A circuit can need different cable."),
  ("What wire size is needed for a 1.5 ton AC?", "Typically 4.0 sq mm with a 20A Curve C MCB for a normal run length. If the distribution board is more than about 20 metres away, run the calculator with your actual distance, because voltage drop may push the requirement to 6.0 sq mm."),
  ("What is an acceptable voltage drop in house wiring?", "3% is the recommended design limit for a domestic circuit and 5% is generally treated as the permitted maximum from the supply point to the furthest outlet. Excessive drop causes dim lighting, poor motor starting and, in pumps, overheating."),
  ("Does cable in a hot roof space need a larger size?", "Yes. The current ratings used here assume around 40°C ambient with three loaded conductors in conduit. Cables bunched together, run through hot roof voids or buried directly need derating, which usually means going up one size. Send us the layout and we will check it."),
  ("Can I use this calculator for a three-phase circuit?", "Yes — select three phase and the calculator uses 415V, divides by the square root of three for current and applies the line-to-line factor for voltage drop. It covers domestic and light commercial sizes up to 25 sq mm."),
 ],
},

# ------------------------------------------------------------------ 2
{
 "slug": "wire-quantity-calculator",
 "name": "Wire Quantity Calculator",
 "tagline": "Work out how many 90m coils your house actually needs.",
 "title": "House Wire Quantity Calculator — How Many Coils Do You Need | Mount Cable India",
 "h1": "Wire Quantity Calculator",
 "desc": "Calculate how many 90m coils of 1.0, 1.5, 2.5, 4.0 and 6.0 sq mm wire your house needs, from point counts. Free calculator from Mount Cable India, Bangalore.",
 "intro": "Contractors quote coils generously because leftover wire stays with them. Enter your actual point counts and this gives you an independent estimate, including the earth wire that is so often under-ordered.",
 "hero": ("wire-coils-warehouse-electrical-distributor.jpg", "Coils of house wire stacked at a distributor warehouse"),
 "body": """
<div class="calc">
  <div class="calc-grid">
    <label>Light &amp; fan points <input type="number" id="p_light" value="34" min="0"></label>
    <label>6A socket points <input type="number" id="p_6a" value="22" min="0"></label>
    <label>16A power sockets <input type="number" id="p_16a" value="10" min="0"></label>
    <label>AC / geyser points <input type="number" id="p_ac" value="4" min="0"></label>
    <label>Average run per point (m) <input type="number" id="runlen" value="11" min="4" step="0.5"></label>
    <label>Meter to DB distance (m) <input type="number" id="mains" value="14" min="1" step="0.5"></label>
    <label>Wastage allowance
      <select id="waste">
        <option value="10">10% — tight site</option>
        <option value="15" selected>15% — normal</option>
        <option value="20">20% — complex layout</option>
      </select>
    </label>
    <label>Coil length
      <select id="coil">
        <option value="90">90 m (standard)</option>
        <option value="180">180 m</option>
        <option value="300">300 m</option>
      </select>
    </label>
  </div>
  <button class="btn btn-gold calc-go" onclick="calcQty()">Calculate coils</button>
  <div id="out" class="calc-out"></div>
</div>
<script>
""" + CABLE_JS + """
function calcQty(){
  const g = id => parseFloat(document.getElementById(id).value) || 0;
  const light = g('p_light'), s6 = g('p_6a'), s16 = g('p_16a'), ac = g('p_ac');
  const run = g('runlen'), mains = g('mains');
  const waste = 1 + g('waste')/100;
  const coil = g('coil');
  const out = document.getElementById('out');
  if(light + s6 + s16 + ac === 0){ out.innerHTML = '<p class="calc-warn">Enter at least one point count.</p>'; return; }

  // Two current-carrying conductors per point (phase + neutral); earth counted
  // separately because it is ordered as its own green coil.
  const need = {
    '1.0': light * run * 2 * 0.45,
    '1.5': (light * run * 2 * 0.55) + (s6 * run * 2),
    '2.5': s16 * run * 2,
    '4.0': ac * run * 2,
    '6.0': mains * 2
  };
  const earth = (light + s6 + s16 + ac) * run * 0.9;

  let rows = '', totalCoils = 0;
  for(const size in need){
    const metres = need[size] * waste;
    if(metres < 5) continue;
    const coils = Math.ceil(metres / coil);
    totalCoils += coils;
    rows += '<tr><td>' + size + ' sq mm</td><td>' + Math.round(metres) + ' m</td><td><strong>' + coils + '</strong></td></tr>';
  }
  const eMetres = earth * waste, eCoils = Math.ceil(eMetres / coil);
  totalCoils += eCoils;
  rows += '<tr><td>Earth wire (green, 1.5 / 2.5 sq mm)</td><td>' + Math.round(eMetres) + ' m</td><td><strong>' + eCoils + '</strong></td></tr>';

  out.innerHTML =
    '<div class="calc-result"><span class="calc-big">' + totalCoils + ' coils</span>' +
    '<p>of ' + coil + ' m, across all sizes.</p></div>' +
    '<div class="ptable-wrap"><table class="ptable">' +
    '<thead><tr><th>Size</th><th>Approx length</th><th>Coils</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
    '<p class="calc-note">An estimate for planning, not a substitute for the electrician measuring your actual layout. Order about 90% of this and top up after the first floor is pulled — we deliver next day across Bangalore, so there is no reason to carry spare coils.</p>' +
    '<p><a class="btn btn-outline" href="https://wa.me/918867676700">Send this list on WhatsApp for a quote</a></p>';
}
calcQty();
</script>
""",
 "faqs": [
  ("How many wire coils are needed for a 2BHK house?", "Usually 12 to 20 coils of 90m across all sizes for about 70 points, including earth wire. The number depends on your point count, the average run length from the distribution board, and the distance from the meter to the board, which alone can consume a full coil of 6.0 sq mm."),
  ("How is house wire quantity calculated?", "Count the points on each circuit type, multiply by the average run length and by two conductors for phase and neutral, add earth wire separately, add 10 to 20% for bends, loops and wastage, then divide by the coil length. This calculator does exactly that from your point counts."),
  ("Should I buy 90m, 180m or 300m coils?", "90m is the standard pack and the easiest to verify, return and account for. If a single size needs four or more coils, 180m or 300m works out cheaper per metre and reduces joint wastage, so it is worth asking for on larger houses."),
  ("Why does the calculator ask for the meter to DB distance separately?", "Because the mains run from the energy meter to the distribution board uses heavier cable, usually 6.0 or 10.0 sq mm, and is often the single longest run in the house. Estimates that ignore it routinely fall a full coil short of the largest size."),
  ("How much extra wire should I order?", "Order about 90% of the estimate and top up once the first floor has been pulled. Wire is available next day across Bangalore, and surplus coils tie up money and tend to disappear from site."),
 ],
},

# ------------------------------------------------------------------ 3
{
 "slug": "house-wiring-cost-calculator",
 "name": "House Wiring Cost Calculator",
 "tagline": "Estimate the full electrical material budget for your house.",
 "title": "House Wiring Cost Calculator — Bangalore 2026 | Mount Cable India",
 "h1": "House Wiring Cost Calculator",
 "desc": "Estimate the electrical material cost for a house in Bangalore — wire, conduit, switches, MCBs, DB, earthing, fans and lights — by size and specification level. Free calculator.",
 "intro": "Enter your built-up area, point count and the specification level you have in mind. The result is an approximate <strong>material</strong> budget in current Bangalore bands, broken down so you can see where the money actually goes — and which line to adjust if the total is too high.",
 "hero": ("happy-homeowner-couple-new-house-wiring.jpg", "A couple planning the wiring of their newly built house"),
 "body": """
<div class="calc">
  <div class="calc-grid">
    <label>Built-up area (sq ft) <input type="number" id="area" value="1250" min="200" step="10"></label>
    <label>Total switch points <input type="number" id="pts" value="95" min="10"></label>
    <label>Air conditioners planned <input type="number" id="acs" value="3" min="0"></label>
    <label>Wire grade
      <select id="grade">
        <option value="1">FR — standard</option>
        <option value="1.12">FRLS — low smoke</option>
      </select>
    </label>
    <label>Switch range
      <select id="sw">
        <option value="260">Entry (approx &#8377;260/point)</option>
        <option value="500" selected>Mid (approx &#8377;500/point)</option>
        <option value="1000">Premium (approx &#8377;1,000/point)</option>
        <option value="2200">Designer / touch (approx &#8377;2,200/point)</option>
      </select>
    </label>
    <label>Include fans &amp; lights
      <select id="fl">
        <option value="1">Yes</option>
        <option value="0">No</option>
      </select>
    </label>
  </div>
  <button class="btn btn-gold calc-go" onclick="calcCost()">Estimate material cost</button>
  <div id="out" class="calc-out"></div>
</div>
<script>
""" + CABLE_JS + """
function calcCost(){
  const g = id => parseFloat(document.getElementById(id).value) || 0;
  const area = g('area'), pts = g('pts'), acs = g('acs');
  const grade = g('grade'), swRate = g('sw'), fl = g('fl');
  const out = document.getElementById('out');
  if(!(area>0) || !(pts>0)){ out.innerHTML = '<p class="calc-warn">Enter a built-up area and a point count.</p>'; return; }

  // Per-unit bands are approximate Bangalore 2026 material rates.
  const wire    = pts * 470 * grade;            // all sizes incl. earth
  const conduit = area * 26;                    // pipe, boxes, bends, accessories
  const switches= pts * swRate;
  const mcbs    = (Math.ceil(pts/7) + acs + 2) * 340;
  const db      = pts < 70 ? 2400 : (pts < 120 ? 4200 : 7200);
  const rccb    = (pts < 120 ? 1 : 2) * 3200;
  const earth   = (area > 1600 ? 3 : 2) * 8500;
  const fans    = fl ? Math.max(2, Math.round(area/280)) * 3200 : 0;
  const lights  = fl ? area * 42 : 0;
  const misc    = (wire + conduit + switches) * 0.06;

  const rows = [
    ['House wire (all sizes incl. earth)', wire],
    ['Conduit, boxes and accessories', conduit],
    ['Modular switches, sockets and plates', switches],
    ['MCBs', mcbs],
    ['Distribution board', db],
    ['RCCB', rccb],
    ['Earthing (electrode, strip, compound)', earth],
    ['Fans', fans],
    ['Lights', lights],
    ['Sundries (tape, clips, lugs, ties)', misc]
  ].filter(r => r[1] > 0);

  const total = rows.reduce((s,r) => s + r[1], 0);
  const low = total * 0.85, high = total * 1.18;

  out.innerHTML =
    '<div class="calc-result"><span class="calc-big">' + inr(low) + ' &ndash; ' + inr(high) + '</span>' +
    '<p>Approximate electrical <strong>material</strong> budget. Labour is charged separately.</p></div>' +
    '<div class="ptable-wrap"><table class="ptable"><thead><tr><th>Line</th><th>Approx</th><th>Share</th></tr></thead><tbody>' +
    rows.map(r => '<tr><td>' + r[0] + '</td><td>' + inr(r[1]) + '</td><td>' + fmt(r[1]/total*100,0) + '%</td></tr>').join('') +
    '<tr><td><strong>Total (mid estimate)</strong></td><td><strong>' + inr(total) + '</strong></td><td>100%</td></tr>' +
    '</tbody></table></div>' +
    '<p class="calc-note">Wiring labour in Bangalore is typically quoted per point or as a percentage of material and is <strong>not</strong> included above. The biggest lever on this total is the switch range — moving between entry and premium can change the figure by more than a lakh on a large house.</p>' +
    '<p><a class="btn btn-outline" href="https://wa.me/918867676700">Get an exact itemised quote on WhatsApp</a></p>';
}
calcCost();
</script>
""",
 "faqs": [
  ("How much does electrical material cost for a house in Bangalore?", "Approximately ₹90,000 to ₹1,30,000 for a 2BHK at economy specification, ₹1,30,000 to ₹1,90,000 at standard specification, and ₹2,00,000 upwards at premium. A 3BHK typically runs ₹1,50,000 to ₹3,00,000 depending on the switch range chosen. These are material costs only."),
  ("Does this include wiring labour?", "No. The calculator estimates material only. Wiring labour in Bangalore is usually quoted per point or as a percentage of material value, and varies with the number of floors, whether the work is concealed, and the contractor. Ask for labour as a separate line so you can compare quotes properly."),
  ("What is the biggest cost in house wiring?", "Usually the modular switches and sockets, followed by the wire. The switch range is also the single biggest lever on the total — the same house can take ₹35,000 or ₹1,60,000 of switches depending on the series, which is why the calculator asks for it separately."),
  ("How accurate is this estimate?", "It is a planning band, not a quotation. Real cost depends on layout, floor count, run lengths, brand choice and how much of the range is premium. For a firm figure, send your list or drawing on WhatsApp and you will receive an exact itemised quote within 60 minutes."),
  ("Why is FRLS wire more expensive than FR?", "FRLS uses a different insulation compound that emits far less smoke during a fire, which matters in enclosed apartments and stairwells. It typically costs around 8 to 12% more per coil, which the calculator applies when you select it."),
 ],
},

# ------------------------------------------------------------------ 4
{
 "slug": "voltage-drop-calculator",
 "name": "Voltage Drop Calculator",
 "tagline": "Check whether a long cable run is losing too much voltage.",
 "title": "Voltage Drop Calculator for Copper Cable | Mount Cable India",
 "h1": "Voltage Drop Calculator",
 "desc": "Calculate voltage drop over a copper cable run — enter size, length, current and phase to see the drop in volts and percent, with a pass or fail against the 3% design limit.",
 "intro": "Voltage drop is what makes a borewell pump run hot, a top-floor air conditioner underperform and lights dim when a motor starts. It grows with distance, so a cable that is perfectly adequate at 10 metres can be undersized at 40.",
 "hero": ("house-under-construction-conduit-wiring.jpg", "Conduit runs laid through a house under construction"),
 "body": """
<div class="calc">
  <div class="calc-grid">
    <label>Cable size
      <select id="size">
        <option>1.0</option><option>1.5</option><option selected>2.5</option><option>4.0</option>
        <option>6.0</option><option>10.0</option><option>16.0</option><option>25.0</option>
      </select>
    </label>
    <label>Run length one way (m) <input type="number" id="len" value="35" min="1" step="any"></label>
    <label>Current (A) <input type="number" id="amps" value="16" min="0.1" step="any"></label>
    <label>Supply
      <select id="phase">
        <option value="1">Single phase (230V)</option>
        <option value="3">Three phase (415V)</option>
      </select>
    </label>
  </div>
  <button class="btn btn-gold calc-go" onclick="calcVD()">Calculate voltage drop</button>
  <div id="out" class="calc-out"></div>
</div>
<script>
""" + CABLE_JS + """
function calcVD(){
  const size = parseFloat(document.getElementById('size').value);
  const len  = parseFloat(document.getElementById('len').value);
  const amps = parseFloat(document.getElementById('amps').value);
  const ph   = document.getElementById('phase').value;
  const out  = document.getElementById('out');
  if(!(len>0) || !(amps>0)){ out.innerHTML = '<p class="calc-warn">Enter a run length and a current.</p>'; return; }

  const c = CABLE.find(x => x.size === size);
  const volts  = ph === '3' ? 415 : 230;
  const factor = ph === '3' ? 0.866 : 1;
  const drop = c.mvam * amps * len * factor / 1000;
  const pct  = drop / volts * 100;
  const ok3 = pct <= 3, ok5 = pct <= 5;

  // Smallest size that would pass 3% at this current and length.
  let fix = null;
  for(const x of CABLE){
    if((x.mvam * amps * len * factor / 1000) / volts * 100 <= 3 && x.amps >= amps){ fix = x; break; }
  }

  const verdict = ok3
    ? '<span class="calc-pass">Within the 3% design limit</span>'
    : (ok5 ? '<span class="calc-warnbadge">Over 3% — acceptable but not ideal</span>'
           : '<span class="calc-fail">Exceeds 5% — this cable is undersized for the run</span>');

  out.innerHTML =
    '<div class="calc-result"><span class="calc-big">' + fmt(drop,2) + ' V (' + fmt(pct,2) + '%)</span><p>' + verdict + '</p></div>' +
    '<div class="ptable-wrap"><table class="ptable"><tbody>' +
    '<tr><td>Cable</td><td>' + fmt(size,1) + ' sq mm copper</td></tr>' +
    '<tr><td>Voltage at the far end</td><td>approx ' + fmt(volts - drop,1) + ' V</td></tr>' +
    '<tr><td>3% limit</td><td>' + fmt(volts*0.03,1) + ' V</td></tr>' +
    '<tr><td>Cable current rating</td><td>' + c.amps + ' A</td></tr>' +
    (fix && fix.size !== size ? '<tr><td>Smallest size that passes 3%</td><td><strong>' + fmt(fix.size,1) + ' sq mm</strong></td></tr>' : '') +
    '</tbody></table></div>' +
    '<p class="calc-note">Based on PVC-insulated copper conductors. Voltage drop is the usual reason a long run needs a larger cable than its current alone suggests — borewell pumps, outbuildings, gate motors and top-floor air conditioners are the common cases.</p>';
}
calcVD();
</script>
""",
 "faqs": [
  ("What is an acceptable voltage drop in house wiring?", "3% is the recommended design limit for a domestic circuit, and 5% is generally treated as the maximum permitted from the supply point to the furthest outlet. Beyond that you get dim lighting, poor motor starting and, in pumps and compressors, overheating."),
  ("Why does a long cable run need a thicker wire?", "Because voltage drop is proportional to length. The same current over four times the distance produces four times the drop, so a cable sized purely on current capacity can be well within its rating and still deliver unusable voltage at the far end."),
  ("What causes a borewell pump to burn out?", "Frequently voltage drop over the cable down the borewell. Low voltage at the motor increases current draw and heat, which degrades the winding. Sizing the submersible cable for depth, not just for motor rating, is the single most effective preventative measure."),
  ("How do I reduce voltage drop?", "Increase the cable size, shorten the run, or move the distribution point closer to the load. Increasing the size is usually the practical option — this calculator shows the smallest size that brings the run within 3%."),
  ("Does three phase have less voltage drop?", "For the same power, yes. Three-phase current is lower for a given load and the line-to-line drop calculation carries a factor of about 0.866, so three-phase runs generally tolerate longer distances at the same cable size."),
 ],
},

# ------------------------------------------------------------------ 5
{
 "slug": "mcb-selector",
 "name": "MCB Selector",
 "tagline": "Get the right MCB rating and trip curve for each circuit.",
 "title": "MCB Rating and Curve Selector for Home Circuits | Mount Cable India",
 "h1": "MCB Selector",
 "desc": "Select the correct MCB rating and trip curve for any home circuit — lights, sockets, geyser, air conditioner, pump — checked against the cable size so protection is correct.",
 "intro": "An MCB protects the <em>cable</em>, not the appliance, so its rating must never exceed what the wire can safely carry. Choose the circuit type and cable size and this will give you a rating and a curve, and warn you if the combination is unsafe.",
 "hero": ("electrician-installing-mcb-distribution-board.jpg", "MCBs being installed in a home distribution board"),
 "body": """
<div class="calc">
  <div class="calc-grid">
    <label>Circuit type
      <select id="ctype">
        <option value="light|B|0.5">Lights and fans</option>
        <option value="socket6|B|1.2">6A socket circuit</option>
        <option value="socket16|C|2.5">16A power sockets / kitchen</option>
        <option value="geyser|C|3.0">Geyser</option>
        <option value="ac|C|1.8">Air conditioner</option>
        <option value="pump|C|1.5">Water pump / motor</option>
        <option value="main|C|0">Main incomer</option>
      </select>
    </label>
    <label>Connected load (watts) <input type="number" id="watts" value="1800" min="50" step="50"></label>
    <label>Cable size installed
      <select id="size">
        <option>1.0</option><option>1.5</option><option>2.5</option><option selected>4.0</option>
        <option>6.0</option><option>10.0</option><option>16.0</option>
      </select>
    </label>
    <label>Supply
      <select id="phase">
        <option value="1">Single phase (230V)</option>
        <option value="3">Three phase (415V)</option>
      </select>
    </label>
  </div>
  <button class="btn btn-gold calc-go" onclick="calcMCB()">Select MCB</button>
  <div id="out" class="calc-out"></div>
</div>
<script>
""" + CABLE_JS + """
function calcMCB(){
  const parts = document.getElementById('ctype').value.split('|');
  const kind = parts[0], curve = parts[1];
  const watts = parseFloat(document.getElementById('watts').value) || 0;
  const size  = parseFloat(document.getElementById('size').value);
  const ph    = document.getElementById('phase').value;
  const out   = document.getElementById('out');

  const volts = ph === '3' ? 415 : 230;
  const pf = (kind === 'ac' || kind === 'pump') ? 0.85 : 1;
  const amps = ph === '3' ? watts / (1.732 * volts * pf) : watts / (volts * pf);
  const c = CABLE.find(x => x.size === size);

  // Rating must be at least the design current and never above cable capacity.
  let pick = null;
  for(const r of MCB_RATINGS){ if(r >= amps * 1.15 && r <= c.amps){ pick = r; break; } }

  let warn = '';
  if(!pick){
    const needed = CABLE.find(x => x.amps >= amps * 1.15);
    warn = '<p class="calc-warn"><strong>This cable is too small for this load.</strong> ' + fmt(amps,1) +
           ' A on ' + fmt(size,1) + ' sq mm (rated ' + c.amps + ' A) cannot be protected correctly. ' +
           (needed ? 'Use at least <strong>' + fmt(needed.size,1) + ' sq mm</strong>.' : 'WhatsApp us and we will size it.') +
           ' Fitting a larger MCB on an undersized cable removes the protection instead of solving the tripping.</p>';
    for(const r of MCB_RATINGS){ if(r <= c.amps){ pick = r; } }
  }

  const rcbo = (kind === 'geyser' || kind === 'pump');
  out.innerHTML =
    '<div class="calc-result"><span class="calc-big">' + (pick ? pick + 'A, Curve ' + curve : 'Check cable size') + '</span>' +
    '<p>' + (rcbo ? 'An RCBO is recommended on this circuit rather than a plain MCB.' : 'Recommended protection for this circuit.') + '</p></div>' +
    warn +
    '<div class="ptable-wrap"><table class="ptable"><tbody>' +
    '<tr><td>Design current</td><td>' + fmt(amps,1) + ' A</td></tr>' +
    '<tr><td>Cable capacity at ' + fmt(size,1) + ' sq mm</td><td>' + c.amps + ' A</td></tr>' +
    '<tr><td>Trip curve</td><td>Curve ' + curve + (curve === 'C' ? ' — tolerates motor and compressor inrush' : ' — faster trip, suits resistive loads') + '</td></tr>' +
    '<tr><td>Whole-house RCCB</td><td>40A or 63A, 30mA</td></tr>' +
    '</tbody></table></div>' +
    '<p class="calc-note">The MCB rating must match the <strong>cable</strong>, not the appliance. If a breaker trips repeatedly, the correct fix is a larger cable or a separate circuit — never a larger breaker on the same wire.</p>';
}
calcMCB();
</script>
""",
 "faqs": [
  ("What MCB rating do I need for a geyser?", "A 2000W storage geyser on 2.5 sq mm cable takes a 16A Curve C MCB, and a 3000W unit on 4.0 sq mm takes 20A. An instant geyser around 4500W needs 4.0 sq mm with a 25A breaker. On all of them an RCBO is preferable to a plain MCB, because a geyser element is the highest shock-risk item in a house."),
  ("What is the difference between MCB Curve B and Curve C?", "Curve B trips faster and suits resistive loads such as lights, heaters and general sockets. Curve C tolerates the brief inrush current drawn by motors and compressors, which is why air conditioners, pumps and refrigerators belong on Curve C. Nuisance tripping when a motor starts is usually a curve problem."),
  ("Can I fit a bigger MCB to stop nuisance tripping?", "No. The MCB protects the cable, so its rating must not exceed what the wire can carry. Fitting a larger breaker means the cable will overheat before the breaker reacts. If a circuit trips repeatedly, the correct fix is a larger cable or a separate dedicated circuit."),
  ("What MCB does an air conditioner need?", "A 1.5 ton unit on 4.0 sq mm cable takes a 20A Curve C MCB, and a 2 ton unit takes 20A or 25A depending on the rated input. Each air conditioner should be on its own dedicated circuit from the distribution board rather than sharing a room socket circuit."),
  ("Do I need an RCCB as well as MCBs?", "Yes. MCBs protect the wiring against overload and short circuit; an RCCB protects people by tripping on earth leakage. A 40A or 63A, 30mA RCCB is standard for a home, and splitting the house across two RCCBs makes faults easier to isolate."),
 ],
},

# ------------------------------------------------------------------ 6
{
 "slug": "load-calculator",
 "name": "Electrical Load Calculator",
 "tagline": "Total your connected load and size the main incomer.",
 "title": "Home Electrical Load Calculator — Connected Load and Incomer Size | Mount Cable India",
 "h1": "Electrical Load Calculator",
 "desc": "Calculate your home's connected load and diversified demand from appliance counts, and get the recommended main MCB rating, mains cable size and sanctioned load to apply for.",
 "intro": "Add up what you actually plan to run. The calculator applies a realistic diversity factor — no house runs everything at once — and gives you the connected load, the likely maximum demand, the mains cable size and the sanctioned load worth applying for.",
 "hero": ("builder-architect-site-electrical-planning.jpg", "A builder and architect planning the electrical layout of a house"),
 "body": """
<div class="calc">
  <div class="calc-grid" id="loadgrid"></div>
  <button class="btn btn-gold calc-go" onclick="calcLoad()">Calculate load</button>
  <div id="out" class="calc-out"></div>
</div>
<script>
""" + CABLE_JS + """
const ITEMS = [
  ['LED lights',            10, 12],
  ['Ceiling fans',           5, 70],
  ['Air conditioners (1.5T)',3, 1600],
  ['Geyser (storage)',       2, 2000],
  ['Refrigerator',           1, 250],
  ['Washing machine',        1, 800],
  ['Microwave / oven',       1, 1400],
  ['Television',             2, 120],
  ['Water pump (1 HP)',      1, 750],
  ['Mixer / kitchen small',  2, 600],
  ['Computers',              2, 200],
  ['Iron',                   1, 1000]
];
document.getElementById('loadgrid').innerHTML = ITEMS.map((it,i) =>
  '<label>' + it[0] + ' <span class="calc-sub">' + it[2] + 'W each</span>' +
  '<input type="number" id="q' + i + '" value="' + it[1] + '" min="0"></label>').join('');

function calcLoad(){
  let connected = 0, rows = '';
  ITEMS.forEach((it,i) => {
    const q = parseFloat(document.getElementById('q'+i).value) || 0;
    if(!q) return;
    const w = q * it[2];
    connected += w;
    rows += '<tr><td>' + it[0] + '</td><td>' + q + '</td><td>' + w + ' W</td></tr>';
  });
  const out = document.getElementById('out');
  if(connected === 0){ out.innerHTML = '<p class="calc-warn">Enter at least one appliance.</p>'; return; }

  // Diversity: larger installations run a smaller share simultaneously.
  const div = connected < 3000 ? 0.9 : connected < 8000 ? 0.7 : connected < 15000 ? 0.55 : 0.45;
  const demand = connected * div;
  const amps = demand / (230 * 0.9);
  const threePhase = demand > 7000;

  let main = null;
  for(const r of MCB_RATINGS){ if(r >= amps * 1.15){ main = r; break; } }
  let mains = null;
  for(const c of CABLE){ if(c.amps >= amps * 1.15){ mains = c; break; } }
  const sanctioned = Math.ceil(demand / 1000 * 1.15);

  out.innerHTML =
    '<div class="calc-result"><span class="calc-big">' + fmt(connected/1000,2) + ' kW connected</span>' +
    '<p>Likely maximum demand approx <strong>' + fmt(demand/1000,2) + ' kW</strong> after diversity.</p></div>' +
    '<div class="ptable-wrap"><table class="ptable"><thead><tr><th>Appliance</th><th>Qty</th><th>Load</th></tr></thead><tbody>' +
    rows + '<tr><td><strong>Total connected</strong></td><td></td><td><strong>' + connected + ' W</strong></td></tr>' +
    '</tbody></table></div>' +
    '<div class="ptable-wrap"><table class="ptable"><tbody>' +
    '<tr><td>Diversity factor applied</td><td>' + fmt(div*100,0) + '%</td></tr>' +
    '<tr><td>Design current</td><td>' + fmt(amps,1) + ' A</td></tr>' +
    (main  ? '<tr><td>Suggested main MCB</td><td>' + main + 'A, Curve C</td></tr>' : '') +
    (mains ? '<tr><td>Suggested mains cable</td><td>' + fmt(mains.size,1) + ' sq mm</td></tr>' : '') +
    '<tr><td>Supply type</td><td>' + (threePhase ? 'Three phase recommended' : 'Single phase is adequate') + '</td></tr>' +
    '<tr><td>Sanctioned load to apply for</td><td>approx ' + sanctioned + ' kW</td></tr>' +
    '</tbody></table></div>' +
    '<p class="calc-note">Diversity reflects the fact that a household never runs everything simultaneously. Utilities apply their own rules to sanctioned load, so treat the figure above as a planning guide and confirm with your BESCOM application.</p>';
}
calcLoad();
</script>
""",
 "faqs": [
  ("What is connected load and maximum demand?", "Connected load is the total wattage of everything installed if it all ran at once. Maximum demand is what the house realistically draws, because no household runs every appliance simultaneously. A diversity factor of roughly 45 to 90% is applied depending on installation size, and the mains and incomer are sized on demand, not connected load."),
  ("How much sanctioned load do I need for a 3BHK house?", "Commonly 5 to 8 kW for a 3BHK with two or three air conditioners and a geyser, and more for larger homes with additional cooling or an EV charger. This calculator gives an indicative figure from your appliance list, but the utility applies its own rules, so confirm at the application stage."),
  ("When do I need a three-phase connection?", "Generally once maximum demand exceeds about 7 kW, which typically means three or more air conditioners plus a geyser and a pump. Three phase also balances the load across phases, which reduces voltage fluctuation and allows smaller mains cable for the same power."),
  ("What size cable is needed from the meter to the distribution board?", "It depends on the design current, typically 6.0 sq mm for smaller homes and 10.0 or 16.0 sq mm for larger ones. The run is often the longest in the house, so check it for voltage drop as well as current — the voltage drop calculator handles that."),
  ("Should I plan for an EV charger in the load?", "Yes if there is any chance of one. A home charger adds roughly 3.3 to 7.4 kW of continuous load, which frequently pushes a house into three phase and changes the mains cable and incomer. Adding a spare way and a suitably sized cable route during construction costs very little; retrofitting it does not."),
 ],
},

# ------------------------------------------------------------------ 7
{
 "slug": "material-list-builder",
 "name": "Material List Builder",
 "tagline": "Build your full electrical list and send it to us for an exact quote.",
 "title": "Electrical Material List Builder — Build and Send Your List | Mount Cable India",
 "h1": "Material List Builder",
 "desc": "Build a complete electrical material list for your house — wires, conduit, switches, MCBs, DB, earthing, fans and lights — and send it on WhatsApp for an exact quote within 60 minutes.",
 "intro": "Add the items you need, adjust quantities and send the finished list to us on WhatsApp. You will have an exact, itemised quote within 60 minutes — free next-day delivery across Bangalore, pay on delivery, every product QR-verifiable at your site. Use the quote as your reference price anywhere; there is no obligation to buy from us.",
 "hero": ("contractor-bulk-order-loading-warehouse.jpg", "An order of electrical material being loaded for delivery in Bangalore"),
 "body": """
<div class="calc">
  <div class="mlb" id="mlb"></div>
  <div class="mlb-actions">
    <button class="btn btn-outline" onclick="mlbClear()">Clear all</button>
    <button class="btn btn-gold" onclick="mlbSend()">Send list on WhatsApp</button>
  </div>
  <div id="out" class="calc-out"></div>
</div>
<script>
const GROUPS = [
  ['Wires &amp; Cables', [
    'House wire 1.0 sq mm (90m coil)', 'House wire 1.5 sq mm (90m coil)',
    'House wire 2.5 sq mm (90m coil)', 'House wire 4.0 sq mm (90m coil)',
    'House wire 6.0 sq mm (90m coil)', 'Earth wire green 2.5 sq mm (90m coil)',
    '3 core flexible cable 1.5 sq mm (per m)', 'Submersible flat cable 3x2.5 sq mm (per m)'
  ]],
  ['Conduit &amp; Accessories', [
    'PVC conduit 20mm (per length)', 'PVC conduit 25mm (per length)',
    'Modular box 2 module', 'Modular box 4 module', 'Modular box 8 module',
    'Bends, couplers and clips (lot)'
  ]],
  ['Switches &amp; Sockets', [
    'Switch 6A one way', 'Switch 16A', 'Socket 6A', 'Socket 16A',
    'Fan regulator', 'Plate 4 module', 'Plate 8 module', 'USB module'
  ]],
  ['Switchgear', [
    'MCB 6A SP', 'MCB 16A SP', 'MCB 20A SP', 'MCB 32A DP',
    'RCCB 40A 30mA', 'RCBO 20A 30mA', 'Distribution board 8 way', 'Distribution board 12 way'
  ]],
  ['Earthing', [
    'Chemical earthing electrode', 'GI earth strip (per m)', 'Earthing backfill compound (bag)', 'Earth pit chamber'
  ]],
  ['Lighting &amp; Fans', [
    'LED panel light 12W', 'LED panel light 18W', 'COB spotlight 7W',
    'LED strip (per m)', 'Ceiling fan 1200mm', 'BLDC ceiling fan 1200mm', 'Exhaust fan'
  ]],
  ['Networking', [
    'Cat6 LAN cable (305m box)', 'RG-6 coaxial cable (per m)', 'RJ45 keystone jack', 'Telephone cable (per m)'
  ]]
];

document.getElementById('mlb').innerHTML = GROUPS.map((g, gi) =>
  '<div class="mlb-group"><h3>' + g[0] + '</h3>' +
  g[1].map((item, ii) =>
    '<div class="mlb-row"><span>' + item + '</span>' +
    '<input type="number" min="0" value="0" id="m' + gi + '_' + ii + '" oninput="mlbCount()"></div>'
  ).join('') + '</div>').join('');

function mlbLines(){
  const lines = [];
  GROUPS.forEach((g, gi) => g[1].forEach((item, ii) => {
    const q = parseFloat(document.getElementById('m' + gi + '_' + ii).value) || 0;
    if(q > 0) lines.push(item.replace(/&amp;/g, '&') + ' \\u2014 ' + q);
  }));
  return lines;
}
function mlbCount(){
  const n = mlbLines().length;
  document.getElementById('out').innerHTML = n
    ? '<p class="calc-note"><strong>' + n + ' item' + (n>1?'s':'') + '</strong> in your list. Send it across and we will price it exactly.</p>'
    : '';
}
function mlbClear(){
  GROUPS.forEach((g, gi) => g[1].forEach((item, ii) => { document.getElementById('m' + gi + '_' + ii).value = 0; }));
  mlbCount();
}
function mlbSend(){
  const lines = mlbLines();
  if(!lines.length){
    document.getElementById('out').innerHTML = '<p class="calc-warn">Add a quantity against at least one item first.</p>';
    return;
  }
  const msg = 'Hi Mount Cable, please quote for this electrical list:\\n\\n' + lines.join('\\n') +
              '\\n\\nDelivery area: \\nSite / building: ';
  window.open('https://wa.me/918867676700?text=' + encodeURIComponent(msg), '_blank');
}
mlbCount();
</script>
""",
 "faqs": [
  ("How do I get an exact price for my electrical list?", "Build the list here and send it on WhatsApp, or message it directly to 88676 76700. You will receive an exact, itemised quote within 60 minutes, with free next-day delivery across Bangalore and payment on delivery."),
  ("Do I have to buy from Mount Cable to get a quote?", "No. Use our quote as your reference price anywhere. Genuine electrical is a 3 to 5% margin business, so if another seller is far below our figure you are almost certainly being offered duplicate material — which is exactly what a reference price is for."),
  ("Can I send a photo of a handwritten list instead?", "Yes. WhatsApp a photo of your contractor's estimate, a handwritten list or an architect's drawing to 88676 76700 and we will read it and quote against it. Many customers find that easier than typing the list out."),
  ("What if I do not know the quantities yet?", "Send approximate figures, or use the wire quantity and cost calculators first to produce a planning estimate. We will flag anything that looks under or over-ordered when we quote, which often saves more than the price difference."),
  ("Do you deliver across Bangalore?", "Yes, free next-day delivery across Bangalore and often the same day, with no minimum order. You inspect and QR-verify the material at your site before paying, in cash, UPI, card or bank transfer."),
 ],
},
]
